#!/usr/bin/env python3
"""Reject destructive edits to previously committed shaping decisions."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION = re.compile(r"^#### (R\d+-Q\d+)\b.*$", flags=re.MULTILINE)
NEXT_HEADING = re.compile(r"^#{1,4}\s", flags=re.MULTILINE)
MUTABLE_LINES = re.compile(r"^- \*\*(?:Status|Supersedes):\*\*.*$", flags=re.MULTILINE)
APPROVAL_SECTION = re.compile(
    r"^## Approval record\s*$\n(?P<body>.*?)(?=^##\s|\Z)",
    flags=re.MULTILINE | re.DOTALL,
)
APPROVAL_ROW = re.compile(r"^\|\s*(R\d+)\s*\|(?P<rest>.*)\|\s*$", flags=re.MULTILINE)


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
    blocks: dict[str, str] = {}
    for match in QUESTION.finditer(text):
        question_id = match.group(1)
        if question_id in blocks:
            raise ValueError(f"duplicate shaping question ID: {question_id}")

        next_heading = NEXT_HEADING.search(text, match.end())
        end = next_heading.start() if next_heading else len(text)
        block = text[match.start():end]
        # A correction may update status and the supersession pointer. The original
        # question, safe answer, evidence, recommendation, and normalized decision stay immutable.
        blocks[question_id] = MUTABLE_LINES.sub("", block).strip()
    return blocks


def approval_rows(text: str) -> dict[str, str]:
    section = APPROVAL_SECTION.search(text)
    if not section:
        return {}

    rows: dict[str, str] = {}
    for match in APPROVAL_ROW.finditer(section.group("body")):
        round_id = match.group(1)
        if round_id in rows:
            raise ValueError(f"duplicate approval row for round: {round_id}")
        rows[round_id] = " ".join(match.group(0).split())
    return rows


def validate_document(before_text: str, after_text: str, path: str) -> list[str]:
    errors: list[str] = []
    before_questions = question_blocks(before_text)
    after_questions = question_blocks(after_text)
    for question_id, immutable_block in before_questions.items():
        if question_id not in after_questions:
            errors.append(f"{path}: removed committed question {question_id}")
        elif after_questions[question_id] != immutable_block:
            errors.append(
                f"{path}: rewrote committed question/answer {question_id}; append a correction instead"
            )

    before_approvals = approval_rows(before_text)
    after_approvals = approval_rows(after_text)
    for round_id, immutable_row in before_approvals.items():
        if round_id not in after_approvals:
            errors.append(f"{path}: removed committed approval record for {round_id}")
        elif after_approvals[round_id] != immutable_row:
            errors.append(
                f"{path}: rewrote committed approval record for {round_id}; append a new round instead"
            )
    return errors


def validate(base_ref: str) -> list[str]:
    errors: list[str] = []
    for path in shaping_paths(base_ref):
        current = ROOT / path
        if not current.exists():
            errors.append(f"Deleted committed shaping history: {path}")
            continue
        errors.extend(
            validate_document(
                read_at(base_ref, path),
                current.read_text(encoding="utf-8"),
                path,
            )
        )
    return errors


def self_test() -> None:
    original = """# History

## Round R1

#### R1-Q1 — Scope

- **Status:** Answered
- **Exact question:** Keep exports?
- **User answer:** Yes.
- **Normalized decision:** Preserve exports.
- **Supersedes:** none

### Round summary

Ready.

## Approval record

| Round | Approval question | User answer | Revision | Date |
|---|---|---|---:|---|
| R1 | Approve? | Yes | 1 | today |
"""
    appended = original + """

## Round R2

#### R2-Q1 — Performance

- **Status:** Answered
- **Exact question:** Separate performance work?
- **User answer:** Yes.
- **Normalized decision:** New goal.
- **Supersedes:** none
"""
    if validate_document(original, appended, "self-test"):
        raise AssertionError("appending a new round must be accepted")

    rewritten = original.replace("- **User answer:** Yes.", "- **User answer:** No.", 1)
    if not validate_document(original, rewritten, "self-test"):
        raise AssertionError("rewriting an answer must be rejected")

    approval_rewrite = original.replace("| R1 | Approve? | Yes | 1 | today |", "| R1 | Approve? | No | 1 | today |")
    if not validate_document(original, approval_rewrite, "self-test"):
        raise AssertionError("rewriting approval must be rejected")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", default="", help="Commit/ref to compare against")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    try:
        if args.self_test:
            self_test()
            print("Shaping-history parser self-test passed.")

        base_ref = args.base_ref.strip()
        if not base_ref or set(base_ref) == {"0"}:
            print("No usable base ref; append-only diff validation skipped.")
            return 0

        git("rev-parse", "--verify", base_ref)
        errors = validate(base_ref)
    except (subprocess.CalledProcessError, ValueError, AssertionError) as error:
        detail = error.stderr.strip() if isinstance(error, subprocess.CalledProcessError) else str(error)
        print(detail or str(error), file=sys.stderr)
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
