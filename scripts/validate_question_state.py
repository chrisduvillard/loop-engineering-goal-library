#!/usr/bin/env python3
"""Validate shaping-question state, sequencing, and lifecycle transitions."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION = re.compile(r"^#### (R(?P<round>\d+)-Q(?P<question>\d+))\b.*$", re.MULTILINE)
NEXT_HEADING = re.compile(r"^#{1,4}\s", re.MULTILINE)
ROUND_HEADING = re.compile(r"^## Round R(\d+)\b", re.MULTILINE)
APPROVAL_SECTION = re.compile(
    r"^## Approval record\s*$\n(?P<body>.*?)(?=^##\s|\Z)",
    re.MULTILINE | re.DOTALL,
)
APPROVAL_ROW = re.compile(r"^\|\s*(R\d+)\s*\|(?P<rest>.*)\|\s*$", re.MULTILINE)
FIELD = re.compile(r"^- \*\*(?P<name>[^*]+):\*\*\s*(?P<value>.*)$", re.MULTILINE)
IGNORED_PARTS = {
    ".git",
    "dist",
    "build",
    "node_modules",
    "__pycache__",
    ".venv",
    "venv",
    ".tox",
    ".nox",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}
ALLOWED_STATUSES = {
    "proposed",
    "answered",
    "deferred",
    "declined",
    "blocked",
    "superseded",
}
ALLOWED_TRANSITIONS = {
    "proposed": ALLOWED_STATUSES,
    "deferred": {"deferred", "answered", "declined", "blocked", "superseded"},
    "blocked": {"blocked", "answered", "deferred", "declined", "superseded"},
    "answered": {"answered", "superseded"},
    "declined": {"declined", "superseded"},
    "superseded": {"superseded"},
}
MAX_HISTORY_BYTES = 2 * 1024 * 1024


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


def mask_fenced_code(text: str) -> str:
    lines = text.splitlines(keepends=True)
    active: tuple[str, int] | None = None
    masked: list[str] = []
    for line in lines:
        stripped = line.lstrip()
        opening = re.match(r"(`{3,}|~{3,})", stripped)
        if active is None and opening:
            token = opening.group(1)
            active = (token[0], len(token))
        elif active is not None:
            char, minimum = active
            if re.match(re.escape(char) + "{" + str(minimum) + r",}\s*$", stripped):
                active = None
        if active is not None or opening:
            masked.append(
                "".join(
                    "\n" if char == "\n" else "\r" if char == "\r" else " "
                    for char in line
                )
            )
        else:
            masked.append(line)
    return "".join(masked)


def current_paths() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("SHAPING.md")
        if not any(part in IGNORED_PARTS for part in path.relative_to(ROOT).parts)
    )


def paths_at(ref: str) -> list[str]:
    output = git("ls-tree", "-r", "--name-only", ref)
    return sorted(
        path
        for path in output.splitlines()
        if (path == "SHAPING.md" or path.endswith("/SHAPING.md"))
        and not any(part in IGNORED_PARTS for part in Path(path).parts)
    )


def text_at(ref: str, path: str) -> str:
    return git("show", f"{ref}:{path}")


def fields(block: str) -> dict[str, list[str]]:
    found: dict[str, list[str]] = {}
    for match in FIELD.finditer(block):
        key = match.group("name").strip().lower()
        found.setdefault(key, []).append(match.group("value").strip())
    return found


def question_blocks(text: str) -> list[tuple[str, int, int, str]]:
    masked = mask_fenced_code(text)
    blocks: list[tuple[str, int, int, str]] = []
    last_round = 0
    last_question = 0
    seen: set[str] = set()

    for match in QUESTION.finditer(masked):
        question_id = match.group(1)
        round_number = int(match.group("round"))
        question_number = int(match.group("question"))
        if round_number < 1 or question_number < 1:
            raise ValueError(f"question IDs must start at R1-Q1 or later: {question_id}")
        if question_id in seen:
            raise ValueError(f"duplicate question ID: {question_id}")
        if round_number < last_round:
            raise ValueError(f"question rounds are out of order at {question_id}")
        if round_number == last_round:
            if question_number != last_question + 1:
                raise ValueError(
                    f"question IDs must be contiguous within R{round_number}; found {question_id}"
                )
        elif question_number != 1:
            raise ValueError(f"each new question round must start at Q1; found {question_id}")

        next_heading = NEXT_HEADING.search(masked, match.end())
        end = next_heading.start() if next_heading else len(text)
        blocks.append((question_id, round_number, question_number, text[match.start():end].strip()))
        seen.add(question_id)
        last_round = round_number
        last_question = question_number
    return blocks


def status_for(block: str) -> str | None:
    values = fields(block).get("status", [])
    if len(values) != 1:
        return None
    return values[0].strip().lower()


def validate_current(text: str, path: str) -> list[str]:
    errors: list[str] = []
    if len(text.encode("utf-8")) > MAX_HISTORY_BYTES:
        return [f"{path}: shaping history exceeds {MAX_HISTORY_BYTES} bytes"]

    try:
        blocks = question_blocks(text)
    except ValueError as error:
        return [f"{path}: {error}"]

    declared_rounds = [int(item) for item in ROUND_HEADING.findall(mask_fenced_code(text))]
    if len(declared_rounds) != len(set(declared_rounds)):
        errors.append(f"{path}: duplicate shaping round headings")
    if declared_rounds != sorted(declared_rounds):
        errors.append(f"{path}: shaping round headings are out of order")

    pending: list[str] = []
    for question_id, round_number, _, block in blocks:
        found = fields(block)
        for required in ("status", "exact question"):
            count = len(found.get(required, []))
            if count != 1:
                errors.append(
                    f"{path}: {question_id} must contain exactly one {required.title()} field; found {count}"
                )
        status = status_for(block)
        if status is None:
            continue
        if status not in ALLOWED_STATUSES:
            errors.append(f"{path}: {question_id} has unsupported status {status!r}")
            continue
        if declared_rounds and round_number not in declared_rounds:
            errors.append(f"{path}: {question_id} has no matching Round R{round_number} heading")
        if status == "proposed":
            pending.append(question_id)
            if found.get("user answer") or found.get("normalized decision"):
                errors.append(f"{path}: proposed question {question_id} already contains an answer or decision")
        if status == "answered":
            for required in ("user answer", "normalized decision"):
                count = len(found.get(required, []))
                if count != 1:
                    errors.append(
                        f"{path}: answered question {question_id} must contain exactly one {required.title()} field; found {count}"
                    )
        if status == "superseded":
            supersedes = found.get("supersedes", [])
            if len(supersedes) != 1 or supersedes[0].strip().lower() in {"", "none", "n/a"}:
                errors.append(f"{path}: superseded question {question_id} must name what it supersedes")

    if len(pending) > 1:
        errors.append(f"{path}: at most one question may be Proposed; found {', '.join(pending)}")

    masked = mask_fenced_code(text)
    approval_sections = list(APPROVAL_SECTION.finditer(masked))
    if len(approval_sections) > 1:
        errors.append(f"{path}: duplicate Approval record sections")
    elif approval_sections:
        body = approval_sections[0].group("body")
        previous = 0
        seen: set[str] = set()
        for match in APPROVAL_ROW.finditer(body):
            round_id = match.group(1)
            number = int(round_id[1:])
            if number < 1 or number <= previous or round_id in seen:
                errors.append(f"{path}: invalid or out-of-order approval row {round_id}")
            if declared_rounds and number not in declared_rounds:
                errors.append(f"{path}: approval row {round_id} has no matching shaping round")
            previous = number
            seen.add(round_id)
    return errors


def validate_transition(before: str, after: str, path: str) -> list[str]:
    errors: list[str] = []
    try:
        old = {question_id: block for question_id, _, _, block in question_blocks(before)}
        new = {question_id: block for question_id, _, _, block in question_blocks(after)}
    except ValueError as error:
        return [f"{path}: {error}"]

    for question_id, old_block in old.items():
        if question_id not in new:
            continue
        old_status = status_for(old_block)
        new_status = status_for(new[question_id])
        if old_status in ALLOWED_TRANSITIONS and new_status in ALLOWED_STATUSES:
            if new_status not in ALLOWED_TRANSITIONS[old_status]:
                errors.append(
                    f"{path}: invalid status transition for {question_id}: {old_status} -> {new_status}"
                )
    return errors


def validate(base_ref: str) -> list[str]:
    errors: list[str] = []
    current = current_paths()
    for path in current:
        relative = path.relative_to(ROOT).as_posix()
        if path.is_symlink():
            errors.append(f"{relative}: shaping history may not be a symlink")
            continue
        errors.extend(validate_current(path.read_text(encoding="utf-8"), relative))

    if not base_ref or set(base_ref) == {"0"}:
        return errors
    base_paths = set(paths_at(base_ref))
    for path in current:
        relative = path.relative_to(ROOT).as_posix()
        if relative in base_paths:
            errors.extend(validate_transition(text_at(base_ref, relative), path.read_text(encoding="utf-8"), relative))
    return errors


def self_test() -> None:
    answered = """# History

## Round R1

#### R1-Q1 — Scope

- **Status:** Answered
- **Exact question:** Scope?
- **User answer:** Keep it narrow.
- **Normalized decision:** Narrow scope.
- **Supersedes:** none

## Approval record

| Round | Question | Answer | Revision | Date |
|---|---|---|---:|---|
| R1 | Approve? | Yes | 1 | today |
"""
    assert not validate_current(answered, "self-test")
    proposed = answered.replace("Answered", "Proposed", 1).replace(
        "- **User answer:** Keep it narrow.\n- **Normalized decision:** Narrow scope.\n", ""
    )
    assert not validate_transition(proposed, answered, "self-test")
    assert validate_transition(answered, proposed, "self-test")
    duplicate_pending = proposed + """

#### R1-Q2 — Another

- **Status:** Proposed
- **Exact question:** Another?
- **Supersedes:** none
"""
    assert validate_current(duplicate_pending, "self-test")
    skipped = answered.replace("R1-Q1", "R1-Q2")
    assert validate_current(skipped, "self-test")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", default="", help="Optional commit/ref for transition checks")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_test:
            self_test()
            print("Question-state self-test passed.")
        base_ref = args.base_ref.strip()
        if base_ref and set(base_ref) != {"0"}:
            git("rev-parse", "--verify", base_ref)
        errors = validate(base_ref)
    except (AssertionError, OSError, subprocess.CalledProcessError, ValueError) as error:
        detail = error.stderr.strip() if isinstance(error, subprocess.CalledProcessError) else str(error)
        print(detail or str(error), file=sys.stderr)
        return 1
    if errors:
        print("Question-state validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Shaping question state is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
