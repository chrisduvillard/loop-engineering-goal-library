#!/usr/bin/env python3
"""Synchronize interactive-first launcher guidance across canonical goals."""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOALS_DIR = ROOT / "goals"
MAX_GOAL_CHARS = 4000

INTERACTIVE_HEADING = "## Recommended — interactive shaping"
ADVANCED_HEADING = "## Advanced — autonomous preflight"
FALLBACK_HEADING = "## Advanced — self-contained preflight"


def canonical_goal_paths() -> list[Path]:
    return sorted(path for path in GOALS_DIR.glob("[0-9][0-9]-*.md") if path.is_file())


def goal_title(text: str) -> str:
    first = text.splitlines()[0]
    if not first.startswith("# "):
        raise ValueError("goal file must begin with an H1")
    return first[2:].strip()


def interactive_block(title: str) -> str:
    return f"""{INTERACTIVE_HEADING}

`shape-goal` is the main command. Run it **outside an active `/goal`** so you can answer each question normally.

| Host | Command |
|---|---|
| Claude Code | `/shape-goal Use the {title} profile` |
| Codex CLI / IDE | `$shape-goal Use the {title} profile` |

`shape-goal` searches first, asks one material question, saves the answer, and ends the turn. After you approve the Goal Contract, paste the exact `/goal` command it returns.
"""


def insert_interactive_block(text: str, title: str) -> str:
    if INTERACTIVE_HEADING in text:
        return text
    match = re.search(r"^\*\*In simple terms:\*\* .+$", text, flags=re.MULTILINE)
    if not match:
        raise ValueError("In simple terms line was not found")
    insertion = "\n\n" + interactive_block(title).rstrip()
    return text[: match.end()] + insertion + text[match.end() :]


def relabel_sections(text: str) -> str:
    updated = text.replace("## Run unchanged — recommended", ADVANCED_HEADING)
    updated = updated.replace(
        "Copy this command exactly. It uses `shape-goal` to discover and approve the missing inputs, then `goal-engine` to execute the result.",
        "Use this only when an approved contract or authoritative artifact already resolves every owner decision. It must stop and return control instead of asking questions inside the active `/goal`.",
    )
    updated = updated.replace("## Run unchanged — self-contained fallback", FALLBACK_HEADING)
    updated = updated.replace(
        "Use this command when the skills are unavailable. It reproduces the same shape-then-execute gate without requiring placeholders.",
        "Use this only when the skills are unavailable and no owner interaction is expected. If a decision is missing, it must save one proposed question and stop instead of looping.",
    )
    return updated


def replace_commands(text: str) -> str:
    commands = re.findall(r"```text\n(/goal .*?)\n```", text, flags=re.DOTALL)
    if len(commands) != 2:
        raise ValueError(f"expected exactly two /goal commands, found {len(commands)}")

    recommended, fallback = commands

    recommended = re.sub(
        r"Resolve every material input from evidence where possible; ask only unresolved owner decisions, one at a time with a recommended answer, and do not make production changes until the user approves a Goal Contract\. .*? Then hand off",
        "Resolve every material input from evidence where possible. Continue inside this `/goal` only when an already-approved Goal Contract or authoritative artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to resume `shape-goal` outside `/goal`; do not ask the question or take another autonomous turn, and do not make production changes before approval. Then hand off",
        recommended,
        count=1,
        flags=re.DOTALL,
    )

    fallback = re.sub(
        r"Search before asking; when a material decision cannot be derived, ask the user one question at a time, include the evidence and a recommended answer, .*? Do not edit production before approval,",
        "Search before asking. Continue inside this `/goal` only when an existing approved artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to reply outside `/goal` and continue shaping from the saved state; do not ask the question or take another autonomous turn. Do not edit production before approval,",
        fallback,
        count=1,
        flags=re.DOTALL,
    )

    if "Approval required" not in recommended or "Approval required" not in fallback:
        raise ValueError("could not install interactive stop clauses")

    iterator = iter((recommended, fallback))
    return re.sub(
        r"```text\n/goal .*?\n```",
        lambda _: "```text\n" + next(iterator) + "\n```",
        text,
        count=2,
        flags=re.DOTALL,
    )


def normalize_sensitive_guards(text: str) -> str:
    updated = text.replace(
        "containing CONTRACT.md, final PROGRESS.md, and RESULT.md",
        "containing SHAPING.md, CONTRACT.md, final PROGRESS.md, and RESULT.md",
    )
    updated = updated.replace(
        "never archive secrets, private data, production dumps",
        "never archive secrets or private data, including personal, customer, or confidential business information, production dumps",
    )
    updated = updated.replace(
        "exclude secrets, private data, raw production dumps",
        "exclude secrets or private data, including personal, customer, or confidential business information, raw production dumps",
    )
    return updated


def transform(text: str) -> str:
    title = goal_title(text)
    updated = insert_interactive_block(text, title)
    updated = relabel_sections(updated)
    updated = replace_commands(updated)
    return normalize_sensitive_guards(updated)


def validate_goal(path: Path, text: str) -> None:
    title = goal_title(text)
    for fragment in (
        INTERACTIVE_HEADING,
        f"/shape-goal Use the {title} profile",
        f"$shape-goal Use the {title} profile",
        "outside an active `/goal`",
        ADVANCED_HEADING,
        FALLBACK_HEADING,
    ):
        if fragment not in text:
            raise ValueError(f"{path.name}: missing {fragment!r}")

    commands = re.findall(r"```text\n(/goal .*?)\n```", text, flags=re.DOTALL)
    if len(commands) != 2:
        raise ValueError(f"{path.name}: expected two /goal commands")
    for index, command in enumerate(commands, start=1):
        if len(command) > MAX_GOAL_CHARS:
            raise ValueError(
                f"{path.name}: command {index} is {len(command)} characters; maximum is {MAX_GOAL_CHARS}"
            )
        for fragment in (
            "SHAPING.md",
            "Approval required",
            "outside `/goal`",
            "do not ask the question",
            "do not make production changes" if index == 1 else "Do not edit production before approval",
        ):
            if fragment not in command:
                raise ValueError(f"{path.name}: command {index} is missing {fragment!r}")


def render() -> dict[Path, str]:
    documents: dict[Path, str] = {}
    for path in canonical_goal_paths():
        updated = transform(path.read_text(encoding="utf-8"))
        validate_goal(path, updated)
        documents[path] = updated
    return documents


def check(documents: dict[Path, str]) -> int:
    failed = False
    for path, expected in documents.items():
        actual = path.read_text(encoding="utf-8")
        if actual == expected:
            print(f"OK: {path.relative_to(ROOT)}")
            continue
        failed = True
        print(f"OUT OF DATE: {path.relative_to(ROOT)}", file=sys.stderr)
        diff = difflib.unified_diff(
            actual.splitlines(),
            expected.splitlines(),
            fromfile=str(path.relative_to(ROOT)),
            tofile=f"{path.relative_to(ROOT)} (synchronized)",
            lineterm="",
        )
        print("\n".join(diff), file=sys.stderr)
    return 1 if failed else 0


def write(documents: dict[Path, str]) -> int:
    for path, content in documents.items():
        path.write_text(content, encoding="utf-8")
        print(f"Wrote {path.relative_to(ROOT)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()
    try:
        documents = render()
        return check(documents) if args.check else write(documents)
    except (OSError, ValueError) as error:
        print(f"Launcher synchronization failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
