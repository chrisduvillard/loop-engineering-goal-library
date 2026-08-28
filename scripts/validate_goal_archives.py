#!/usr/bin/env python3
"""Validate durable goal archives and their history index."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOALS_ROOT = ROOT / "docs" / "goals"
INDEX_PATH = GOALS_ROOT / "INDEX.md"
GOAL_ID = re.compile(r"\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*")
CLOSED = re.compile(r"^\*\*(?:Status|State):\*\*\s*Closed\b", re.MULTILINE | re.IGNORECASE)
OUTCOME = re.compile(r"^\*\*Outcome:\*\*\s*(.+)$", re.MULTILINE)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate(root: Path = GOALS_ROOT, index_path: Path = INDEX_PATH) -> list[str]:
    errors: list[str] = []
    if not root.is_dir():
        return [f"Missing goal archive root: {root}"]
    if index_path.is_symlink() or not index_path.is_file():
        return [f"Missing or unsafe goal history index: {index_path}"]
    index = read(index_path)

    seen: set[str] = set()
    for directory in sorted(path for path in root.iterdir() if path.is_dir()):
        goal_id = directory.name
        if directory.is_symlink():
            errors.append(f"{goal_id}: goal archive may not be a symlink")
            continue
        if not GOAL_ID.fullmatch(goal_id):
            errors.append(f"{goal_id}: unsafe goal archive directory name")
            continue
        if goal_id in seen:
            errors.append(f"{goal_id}: duplicate goal archive")
        seen.add(goal_id)

        contents: dict[str, str] = {}
        for name in ("SHAPING.md", "CONTRACT.md", "PROGRESS.md"):
            path = directory / name
            if path.is_symlink() or not path.is_file():
                errors.append(f"{goal_id}: missing or unsafe {name}")
                continue
            source = read(path)
            contents[name] = source
            if goal_id not in source:
                errors.append(f"{goal_id}/{name}: Goal ID is not recorded")

        result_path = directory / "RESULT.md"
        has_result = result_path.is_file() and not result_path.is_symlink()
        is_closed = any(CLOSED.search(source) for source in contents.values())
        indexed = f"`{goal_id}`" in index

        if result_path.exists() and not has_result:
            errors.append(f"{goal_id}: RESULT.md must be a regular file")
        if is_closed and not has_result:
            errors.append(f"{goal_id}: closed goal has no RESULT.md")
        if indexed and not has_result:
            errors.append(f"{goal_id}: indexed goal has no RESULT.md")

        if has_result:
            result = read(result_path)
            if goal_id not in result:
                errors.append(f"{goal_id}/RESULT.md: Goal ID is not recorded")
            outcome = OUTCOME.search(result)
            if not outcome or outcome.group(1).strip().lower() in {"", "pending", "—", "-"}:
                errors.append(f"{goal_id}/RESULT.md: terminal Outcome is missing")
            if not indexed:
                errors.append(f"{goal_id}: completed goal is missing from INDEX.md")
            for suffix in ("SHAPING.md", "RESULT.md"):
                if f"({goal_id}/{suffix})" not in index:
                    errors.append(f"{goal_id}: INDEX.md does not link {suffix}")
        elif indexed:
            errors.append(f"{goal_id}: active goal must not be listed as closed history")
    return errors


def self_test() -> None:
    import tempfile

    with tempfile.TemporaryDirectory() as raw:
        root = Path(raw) / "docs" / "goals"
        root.mkdir(parents=True)
        index = root / "INDEX.md"
        index.write_text("# Goal History\n", encoding="utf-8")
        goal_id = "2026-08-27-example"
        goal = root / goal_id
        goal.mkdir()
        for name in ("SHAPING.md", "CONTRACT.md", "PROGRESS.md"):
            (goal / name).write_text(f"# {name}\n\n**Goal ID:** {goal_id}\n", encoding="utf-8")
        assert not validate(root, index)
        (goal / "CONTRACT.md").write_text(
            f"# Contract\n\n**Goal ID:** {goal_id}\n**Status:** Closed\n",
            encoding="utf-8",
        )
        assert validate(root, index)
        (goal / "RESULT.md").write_text(
            f"# Result\n\n**Goal ID:** {goal_id}\n**Outcome:** Achieved\n",
            encoding="utf-8",
        )
        assert validate(root, index)
        index.write_text(
            "# Goal History\n\n"
            f"| `{goal_id}` | [shape]({goal_id}/SHAPING.md) | [result]({goal_id}/RESULT.md) |\n",
            encoding="utf-8",
        )
        assert not validate(root, index)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_test:
            self_test()
            print("Goal-archive self-test passed.")
        errors = validate()
    except (AssertionError, OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1
    if errors:
        print("Goal-archive validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Goal archives and history index are consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
