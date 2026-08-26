#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).with_name("refine_adversarial_robustness.py")
source = path.read_text(encoding="utf-8")
marker = "# Expand attack tests for the second-pass findings.\n"
insertion = '''replace_once(
    "tests/test_adversarial_robustness.py",
    '        ignore=shutil.ignore_patterns(".git", "dist", "__pycache__", "*.pyc"),\\n',
    '        ignore=shutil.ignore_patterns(".git", "dist", "node_modules", "__pycache__", "*.pyc"),\\n',
)

'''
if marker not in source:
    raise SystemExit("attack-test marker not found")
if insertion not in source:
    source = source.replace(marker, marker + insertion, 1)
path.write_text(source, encoding="utf-8")
print("Fixed copied-repository dependency isolation")
