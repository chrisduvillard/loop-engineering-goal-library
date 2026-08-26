#!/usr/bin/env python3
"""Synchronize shared zero-friction launcher clauses across canonical goals."""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOALS_DIR = ROOT / "goals"
MAX_GOAL_CHARS = 4000

RECOMMENDED_ANCHOR = (
    "and do not make production changes until the user approves a Goal Contract. "
    "Then hand off"
)
RECOMMENDED_REPLACEMENT = (
    "and do not make production changes until the user approves a Goal Contract. "
    "Create or resume an append-only `SHAPING.md` under the resolved goal archive; "
    "after every answer, save the exact question, safe user answer, evidence, recommendation, "
    "normalized decision, and contract impact, and append corrections or supersessions instead "
    "of rewriting history. At each shaping-round close, let the user approve, request another "
    "deeper non-duplicate round, or pause; deeper rounds must read all prior rounds first. "
    "Then hand off"
)

FALLBACK_ANCHOR = (
    "record the decision, and continue until a concise Goal Contract is approved."
)
FALLBACK_REPLACEMENT = (
    "create or resume an append-only `SHAPING.md` under the resolved goal archive, save the exact "
    "question, safe user answer, evidence, recommendation, normalized decision, and contract impact "
    "after every answer, append corrections or supersessions instead of rewriting history, and "
    "continue until a concise Goal Contract is approved. At each shaping-round close, offer approval, "
    "another deeper non-duplicate round, or pause; deeper rounds must read all prior rounds first."
)


def canonical_goal_paths() -> list[Path]:
    return sorted(path for path in GOALS_DIR.glob("[0-9][0-9]-*.md") if path.is_file())


def transform(text: str) -> str:
    updated = text
    if "append-only `SHAPING.md`" not in updated:
        if RECOMMENDED_ANCHOR not in updated:
            raise ValueError("recommended launcher anchor was not found")
        updated = updated.replace(RECOMMENDED_ANCHOR, RECOMMENDED_REPLACEMENT, 1)

    commands = re.findall(r"```text\n(/goal .*?)\n```", updated, flags=re.DOTALL)
    if len(commands) != 2:
        raise ValueError(f"expected exactly two /goal commands, found {len(commands)}")

    if "At each shaping-round close" not in commands[1]:
        if FALLBACK_ANCHOR not in updated:
            raise ValueError("fallback launcher anchor was not found")
        updated = updated.replace(FALLBACK_ANCHOR, FALLBACK_REPLACEMENT, 1)

    updated = updated.replace(
        "containing CONTRACT.md, final PROGRESS.md, and RESULT.md",
        "containing SHAPING.md, CONTRACT.md, final PROGRESS.md, and RESULT.md",
    )
    updated = updated.replace(
        "never archive secrets, private data, production dumps",
        "never archive secrets, private personal or confidential business data, production dumps",
    )
    updated = updated.replace(
        "exclude secrets, private data, raw production dumps",
        "exclude secrets, private personal or confidential business data, raw production dumps",
    )
    return updated


def validate_commands(path: Path, text: str) -> None:
    commands = re.findall(r"```text\n(/goal .*?)\n```", text, flags=re.DOTALL)
    if len(commands) != 2:
        raise ValueError(f"{path.name}: expected two /goal commands")
    for index, command in enumerate(commands, start=1):
        if len(command) > MAX_GOAL_CHARS:
            raise ValueError(
                f"{path.name}: command {index} is {len(command)} characters; maximum is {MAX_GOAL_CHARS}"
            )
        required = (
            "SHAPING.md",
            "exact question",
            "safe user answer",
            "recommendation",
            "normalized decision",
            "deeper non-duplicate round",
        )
        for fragment in required:
            if fragment not in command:
                raise ValueError(f"{path.name}: command {index} is missing {fragment!r}")


def render() -> dict[Path, str]:
    documents: dict[Path, str] = {}
    for path in canonical_goal_paths():
        original = path.read_text(encoding="utf-8")
        updated = transform(original)
        validate_commands(path, updated)
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
