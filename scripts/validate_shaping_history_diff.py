#!/usr/bin/env python3
"""Reject destructive edits to previously committed shaping questions and answers."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION = re.compile(r"^#### (R\d+-Q\d+)\b.*$", flags=re.MULTILINE)
MUTABLE_LINES = re.compile(r"^- \*\*(?:Status|Supersedes):\*\*.*$", flags=re.MULTILINE)


def git(*args: str) -> str:
    completed = subprocess.run(
        ("git", *args),
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def shaping_paths(ref: str) -> list[str]:
    output = git("ls-tree", "-r", "--name-only", ref)
    return sorted(
        path
        for path in output.splitlines()
        if path.endswith("/SHAPING.md") or path == "SHAPING.md"
    )


def read_at(ref: str, path: str) -> str:
    return git("show", f"{ref}:{path}")


def question_blocks(text: str) -> dict[str, str]:
    matches = list(QUESTION.finditer(text))
    blocks: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[start:end]
        # Status and supersession pointers may change when a correction is appended.
        immutable = MUTABLE_LINES.sub("", block).strip()
        blocks[match.group(1)] = immutable
    return blocks


def validate(base_ref: str) -> list[str]:
    errors: list[str] = []
    for path in shaping_paths(base_ref):
        current = ROOT / path
        if not current.exists():
            errors.append(f"Deleted committed shaping history: {path}")
            continue

        before = question_blocks(read_at(base_ref, path))
        after = question_blocks(current.read_text(encoding="utf-8"))
        for question_id, immutable_block in before.items():
            if question_id not in after:
                errors.append(f"{path}: removed committed question {question_id}")
            elif after[question_id] != immutable_block:
                errors.append(
                    f"{path}: rewrote committed question/answer {question_id}; append a correction instead"
                )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", default="", help="Commit/ref to compare against")
    args = parser.parse_args()
    base_ref = args.base_ref.strip()
    if not base_ref or set(base_ref) == {"0"}:
        print("No usable base ref; append-only diff validation skipped.")
        return 0

    try:
        git("rev-parse", "--verify", base_ref)
        errors = validate(base_ref)
    except subprocess.CalledProcessError as error:
        print(error.stderr.strip() or str(error), file=sys.stderr)
        return 1

    if errors:
        print("Shaping-history append-only validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Shaping histories are append-only relative to {base_ref}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
