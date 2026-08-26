#!/usr/bin/env python3
"""Remove one obsolete validator replacement from the one-time profile script."""

from pathlib import Path

path = Path(__file__).resolve().parent / "apply_additional_profiles.py"
source = path.read_text(encoding="utf-8")
old = "        '\"24 execution profiles\",': '\"29 execution profiles\",',\n"
if old not in source:
    raise SystemExit("obsolete replacement entry was not found")
path.write_text(source.replace(old, "", 1), encoding="utf-8")
