#!/usr/bin/env python3
"""Generate concise consolidated goal-library documents from canonical goal files."""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CORE_GOALS = (
    "01-brownfield-continue-finish.md",
    "02-prd-spec-compliance.md",
    "03-next-milestone.md",
    "04-deep-audit-remediation.md",
    "05-qa-regression-uat.md",
    "06-safe-refactor-modernization.md",
    "07-release-readiness.md",
)

SPECIALIST_GOALS = (
    "08-incident-recovery.md",
    "09-dependency-framework-upgrade.md",
    "10-data-migration-integrity.md",
    "11-branch-rescue-integration.md",
    "12-measured-optimization-benchmark.md",
    "13-technical-spike-feasibility.md",
)


def parse_goal(filename: str) -> tuple[str, str, str, str]:
    text = (ROOT / "goals" / filename).read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError(f"goals/{filename} must begin with one H1 title")
    title = lines[0][2:].strip()
    use_match = re.search(r"^\*\*Use when:\*\* (.+)$", text, flags=re.MULTILINE)
    commands = re.findall(r"```text\n(/goal .*?)\n```", text, flags=re.DOTALL)
    why_match = re.search(r"^\*\*Why it works:\*\* (.+)$", text, flags=re.MULTILINE)
    if not use_match or not commands or not why_match:
        raise ValueError(f"goals/{filename} is missing Use when, /goal, or Why it works")
    return title, use_match.group(1).strip(), commands[0].strip(), why_match.group(1).strip()


def render_collection(title: str, intro: str, filenames: tuple[str, ...]) -> str:
    header = "\n\n".join((
        f"# {title}",
        (
            "> [!NOTE]\n"
            "> Generated from the canonical files under [`goals/`](goals/). "
            "Edit those files, then run `python3 scripts/sync_goal_docs.py --write`."
        ),
        intro,
    ))
    sections: list[str] = []
    for filename in filenames:
        goal_title, use_when, command, why = parse_goal(filename)
        sections.append("\n".join((
            f"## [{goal_title}](goals/{filename})",
            "",
            f"**Use when:** {use_when}",
            "",
            "```text",
            command,
            "```",
            "",
            f"**Why it works:** {why}",
            "",
            f"**Standalone fallback:** [Open the complete profile](goals/{filename}).",
        )))
    return header + "\n\n---\n\n" + "\n\n---\n\n".join(sections) + "\n"


def render_documents() -> dict[Path, str]:
    return {
        ROOT / "GOAL_LIBRARY.md": render_collection(
            "Core `/goal` Library",
            "Seven copy-ready skill-backed commands for most long-running work in mature repositories. Each linked profile also contains a self-contained standalone fallback.",
            CORE_GOALS,
        ),
        ROOT / "SPECIALIST_LOOPS.md": render_collection(
            "Specialist `/goal` Extensions",
            "Six optional profiles for incidents, ecosystem upgrades, data migrations, divergent branches, measured optimization, and technical feasibility. The core library remains the default.",
            SPECIALIST_GOALS,
        ),
    }


def check_documents(documents: dict[Path, str]) -> int:
    failed = False
    for path, expected in documents.items():
        actual = path.read_text(encoding="utf-8") if path.exists() else ""
        if actual == expected:
            print(f"OK: {path.relative_to(ROOT)}")
            continue
        failed = True
        print(f"OUT OF DATE: {path.relative_to(ROOT)}", file=sys.stderr)
        diff = difflib.unified_diff(
            actual.splitlines(), expected.splitlines(),
            fromfile=str(path.relative_to(ROOT)),
            tofile=f"{path.relative_to(ROOT)} (generated)", lineterm="",
        )
        print("\n".join(diff), file=sys.stderr)
    return 1 if failed else 0


def write_documents(documents: dict[Path, str]) -> int:
    for path, content in documents.items():
        path.write_text(content, encoding="utf-8")
        print(f"Wrote {path.relative_to(ROOT)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Fail when generated docs differ")
    mode.add_argument("--write", action="store_true", help="Rewrite generated docs")
    args = parser.parse_args()
    try:
        documents = render_documents()
        return check_documents(documents) if args.check else write_documents(documents)
    except (OSError, ValueError) as error:
        print(f"Goal-doc sync failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
