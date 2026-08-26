#!/usr/bin/env python3
"""Update the validator's version-specific documentation expectation for 0.7.0."""

from pathlib import Path

path = Path(__file__).resolve().parent / "validate_repository.py"
source = path.read_text(encoding="utf-8")
old = '            "Version `0.6.0`",\n'
new = '            "Version `0.7.0`",\n'
if new not in source:
    if old not in source:
        raise SystemExit("validator version expectation was not found")
    source = source.replace(old, new, 1)
path.write_text(source, encoding="utf-8")
