#!/usr/bin/env python3
"""Reject destructive edits and malformed additions in durable shaping histories."""

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
        fence = re.match(r"(`{3,}|~{3,})", stripped)
        if active is None and fence:
            token = fence.group(1)
            active = (token[0], len(token))
        elif active is not None:
            char, minimum = active
            if re.match(re.escape(char) + "{" + str(minimum) + r",}\s*$", stripped):
                active = None
        if active is not None or fence:
            masked.append("".join("\n" if char == "\n" else "\r" if char == "\r" else " " for char in line))
        else:
            masked.append(line)
    return "".join(masked)


def shaping_paths(ref: str) -> list[str]:
    output = git("ls-tree", "-r", "--name-only", ref)
    return sorted(
        path
        for path in output.splitlines()
        if (path.endswith("/SHAPING.md") or path == "SHAPING.md")
        and not any(part in IGNORED_PARTS for part in Path(path).parts)
    )


def current_shaping_paths() -> list[str]:
    return sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("SHAPING.md")
        if not any(part in IGNORED_PARTS for part in path.relative_to(ROOT).parts)
    )


def read_at(ref: str, path: str) -> str:
    return git("show", f"{ref}:{path}")


def id_tuple(question_id: str) -> tuple[int, int]:
    match = re.fullmatch(r"R(\d+)-Q(\d+)", question_id)
    if not match:
        raise ValueError(f"invalid shaping question ID: {question_id}")
    round_number, question_number = int(match.group(1)), int(match.group(2))
    if round_number < 1 or question_number < 1:
        raise ValueError(f"shaping question IDs must start at R1-Q1 or later: {question_id}")
    return round_number, question_number


def raw_question_entries(text: str) -> list[tuple[str, str]]:
    masked = mask_fenced_code(text)
    entries: list[tuple[str, str]] = []
    seen: set[str] = set()
    previous: tuple[int, int] | None = None
    for match in QUESTION.finditer(masked):
        question_id = match.group(1)
        if question_id in seen:
            raise ValueError(f"duplicate shaping question ID: {question_id}")
        current = id_tuple(question_id)
        if previous is not None and current <= previous:
            raise ValueError(f"shaping question IDs are out of order: {question_id}")
        previous = current
        seen.add(question_id)
        next_heading = NEXT_HEADING.search(masked, match.end())
        end = next_heading.start() if next_heading else len(text)
        entries.append((question_id, text[match.start():end].strip()))
    return entries


def question_entries(text: str) -> list[tuple[str, str]]:
    return [(question_id, MUTABLE_LINES.sub("", block).strip()) for question_id, block in raw_question_entries(text)]


def question_blocks(text: str) -> dict[str, str]:
    return dict(question_entries(text))


def approval_entries(text: str) -> list[tuple[str, str]]:
    masked = mask_fenced_code(text)
    sections = list(APPROVAL_SECTION.finditer(masked))
    if len(sections) > 1:
        raise ValueError("duplicate Approval record sections")
    if not sections:
        return []
    section = sections[0]
    start, end = section.span("body")
    masked_body = masked[start:end]
    original_body = text[start:end]
    entries: list[tuple[str, str]] = []
    seen: set[str] = set()
    previous = 0
    for match in APPROVAL_ROW.finditer(masked_body):
        round_id = match.group(1)
        number = int(round_id[1:])
        if number < 1:
            raise ValueError(f"approval rounds must start at R1 or later: {round_id}")
        if round_id in seen:
            raise ValueError(f"duplicate approval row for round: {round_id}")
        if number <= previous:
            raise ValueError(f"approval rows are out of order: {round_id}")
        previous = number
        seen.add(round_id)
        row = original_body[match.start():match.end()]
        entries.append((round_id, " ".join(row.split())))
    return entries


def validate_current_document(text: str, path: str) -> list[str]:
    errors: list[str] = []
    if len(text.encode("utf-8")) > MAX_HISTORY_BYTES:
        errors.append(f"{path}: shaping history exceeds {MAX_HISTORY_BYTES} bytes")
        return errors
    try:
        raw_questions = raw_question_entries(text)
        approval_entries(text)
    except ValueError as error:
        return [f"{path}: {error}"]

    for question_id, block in raw_questions:
        if "**Exact question:**" not in block:
            errors.append(f"{path}: {question_id} is missing an Exact question field")
        status = re.search(r"^- \*\*Status:\*\*\s*(.+)$", block, flags=re.MULTILINE)
        if status and status.group(1).strip().lower().startswith("answered"):
            if "**User answer:**" not in block:
                errors.append(f"{path}: answered question {question_id} is missing a User answer field")
            if "**Normalized decision:**" not in block:
                errors.append(f"{path}: answered question {question_id} is missing a Normalized decision field")
    return errors


def validate_document(before_text: str, after_text: str, path: str) -> list[str]:
    errors = validate_current_document(after_text, path)
    try:
        before_questions = question_entries(before_text)
        after_questions = question_entries(after_text)
        before_approvals = approval_entries(before_text)
        after_approvals = approval_entries(after_text)
    except ValueError as error:
        return errors + [f"{path}: {error}"]

    before_ids = [item[0] for item in before_questions]
    after_ids = [item[0] for item in after_questions]
    if after_ids[: len(before_ids)] != before_ids:
        errors.append(f"{path}: reordered or inserted questions before committed history")
    after_map = dict(after_questions)
    for question_id, immutable_block in before_questions:
        if question_id not in after_map:
            errors.append(f"{path}: removed committed question {question_id}")
        elif after_map[question_id] != immutable_block:
            errors.append(
                f"{path}: rewrote committed question/answer {question_id}; append a correction instead"
            )

    before_rounds = [item[0] for item in before_approvals]
    after_rounds = [item[0] for item in after_approvals]
    if after_rounds[: len(before_rounds)] != before_rounds:
        errors.append(f"{path}: reordered or inserted approval rows before committed history")
    after_approval_map = dict(after_approvals)
    for round_id, immutable_row in before_approvals:
        if round_id not in after_approval_map:
            errors.append(f"{path}: removed committed approval record for {round_id}")
        elif after_approval_map[round_id] != immutable_row:
            errors.append(
                f"{path}: rewrote committed approval record for {round_id}; append a new round instead"
            )
    return errors


def validate(base_ref: str) -> list[str]:
    errors: list[str] = []
    current_paths = set(current_shaping_paths())
    for path in sorted(current_paths):
        current = ROOT / path
        if current.is_symlink():
            errors.append(f"{path}: shaping history may not be a symlink")
            continue
        errors.extend(validate_current_document(current.read_text(encoding="utf-8"), path))

    if not base_ref or set(base_ref) == {"0"}:
        return errors
    base_paths = set(shaping_paths(base_ref))
    for path in sorted(base_paths):
        current = ROOT / path
        if not current.exists():
            errors.append(f"Deleted committed shaping history: {path}")
            continue
        if current.is_symlink():
            errors.append(f"{path}: committed shaping history was replaced by a symlink")
            continue
        errors.extend(validate_document(read_at(base_ref, path), current.read_text(encoding="utf-8"), path))
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
    assert not validate_document(original, appended, "self-test")
    assert validate_document(
        original,
        original.replace("- **User answer:** Yes.", "- **User answer:** No.", 1),
        "self-test",
    )
    assert validate_document(
        original,
        original.replace(
            "| R1 | Approve? | Yes | 1 | today |",
            "| R1 | Approve? | No | 1 | today |",
        ),
        "self-test",
    )
    status_change = original.replace("- **Status:** Answered", "- **Status:** Superseded")
    assert not validate_document(original, status_change, "self-test")
    inserted = original.replace(
        "#### R1-Q1",
        "#### R1-Q0 — Inserted\n\n- **Status:** Proposed\n- **Exact question:** Hidden?\n\n#### R1-Q1",
    )
    assert validate_document(original, inserted, "self-test")
    fenced = """# History

```md
#### R1-Q1 — Fake
```

## Round R1

#### R1-Q1 — Real

- **Status:** Answered
- **Exact question:** Real?
- **User answer:** Yes.
- **Normalized decision:** Real.
"""
    assert list(question_blocks(fenced)) == ["R1-Q1"]
    try:
        question_blocks(original + original)
    except ValueError:
        pass
    else:
        raise AssertionError("duplicate question IDs must fail")
    try:
        question_blocks("#### R0-Q1 — Invalid\n\n- **Exact question:** Invalid?\n")
    except ValueError:
        pass
    else:
        raise AssertionError("zero-based question IDs must fail")
    duplicate_approval = original + "\n## Approval record\n\n| R2 | Again? | Yes | 2 | later |\n"
    assert validate_current_document(duplicate_approval, "self-test")


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
        if base_ref and set(base_ref) != {"0"}:
            git("rev-parse", "--verify", base_ref)
        errors = validate(base_ref)
    except (subprocess.CalledProcessError, ValueError, AssertionError, OSError) as error:
        detail = error.stderr.strip() if isinstance(error, subprocess.CalledProcessError) else str(error)
        print(detail or str(error), file=sys.stderr)
        return 1
    if errors:
        print("Shaping-history append-only validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    if not base_ref or set(base_ref) == {"0"}:
        print("Current shaping histories are structurally valid; no usable base ref for append-only comparison.")
    else:
        print(f"Shaping histories are append-only relative to {base_ref}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
