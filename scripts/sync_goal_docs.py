#!/usr/bin/env python3
"""Generate consolidated goal-library documents from canonical goal files."""

from __future__ import annotations

import argparse
import difflib
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
)


def demote_title(text: str) -> str:
    lines = text.strip().splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError("canonical goal file must begin with one H1 title")
    lines[0] = "#" + lines[0]
    return "\n".join(lines).rstrip()


def render_collection(title: str, intro: str, filenames: tuple[str, ...]) -> str:
    sections = [
        f"# {title}",
        (
            "> [!NOTE]\n"
            "> This file is generated from the canonical files under [`goals/`](goals/). "
            "Edit those files, then run `python3 scripts/sync_goal_docs.py --write`."
        ),
        intro,
    ]
    for filename in filenames:
        source = ROOT / "goals" / filename
        sections.append(demote_title(source.read_text(encoding="utf-8")))
    return "\n\n---\n\n".join(sections) + "\n"


def render_documents() -> dict[Path, str]:
    return {
        ROOT / "GOAL_LIBRARY.md": render_collection(
            "Core `/goal` Library",
            (
                "These seven profiles form the recommended permanent toolkit for "
                "long-running coding-agent work in mature repositories. Use "
                "[`shape-goal`](skills/shape-goal/SKILL.md) to approve the target, "
                "then run the selected profile through "
                "[`goal-engine`](skills/goal-engine/SKILL.md)."
            ),
            CORE_GOALS,
        ),
        ROOT / "SPECIALIST_LOOPS.md": render_collection(
            "Specialist `/goal` Extensions",
            (
                "Use these optional profiles when the work has a distinct risk model: "
                "incidents, ecosystem upgrades, data migrations, or divergent branches. "
                "The seven core profiles remain the default toolkit."
            ),
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
            actual.splitlines(),
            expected.splitlines(),
            fromfile=str(path.relative_to(ROOT)),
            tofile=f"{path.relative_to(ROOT)} (generated)",
            lineterm="",
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
        if args.check:
            return check_documents(documents)
        return write_documents(documents)
    except (OSError, ValueError) as error:
        print(f"Goal-doc sync failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
