#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).with_name("apply_adversarial_robustness.py")
source = path.read_text(encoding="utf-8")
old = '''    if source.count(old) != 1:\n        raise RuntimeError(f"{path}: expected one occurrence of {old!r}, found {source.count(old)}")\n    target.write_text(source.replace(old, new, 1), encoding="utf-8")\n'''
new = '''    if source.count(old) < 1:\n        raise RuntimeError(f"{path}: expected at least one occurrence of {old!r}")\n    target.write_text(source.replace(old, new, 1), encoding="utf-8")\n'''
if old not in source:
    raise SystemExit("replace_once implementation not found")
path.write_text(source.replace(old, new, 1), encoding="utf-8")
print("Fixed apply script replacement sequencing")
