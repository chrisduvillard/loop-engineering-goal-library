#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).with_name("refine_adversarial_robustness.py")
source = path.read_text(encoding="utf-8")

attack_marker = "# Expand attack tests for the second-pass findings.\n"
copy_insertion = '''replace_once(
    "tests/test_adversarial_robustness.py",
    '        ignore=shutil.ignore_patterns(".git", "dist", "__pycache__", "*.pyc"),\\n',
    '        ignore=shutil.ignore_patterns(".git", "dist", "node_modules", "__pycache__", "*.pyc"),\\n',
)

'''
if attack_marker not in source:
    raise SystemExit("attack-test marker not found")
if copy_insertion not in source:
    source = source.replace(attack_marker, attack_marker + copy_insertion, 1)

validator_marker = "# Repository validator: ignore local generated environments, inspect both workflow extensions,\n"
link_insertion = '''replace_once(
    "scripts/validate_repository.py",
    '    for path in ROOT.rglob("*.md"):\\n        source = path.read_text(encoding="utf-8")\\n',
    '    for path in ROOT.rglob("*.md"):\\n        if any(part in {"node_modules", "dist", "build", "__pycache__", ".venv", "venv", ".tox", ".nox", ".pytest_cache", ".mypy_cache", ".ruff_cache"} for part in path.parts):\\n            continue\\n        source = path.read_text(encoding="utf-8")\\n',
)

'''
if validator_marker not in source:
    raise SystemExit("repository-validator marker not found")
if link_insertion not in source:
    source = source.replace(validator_marker, validator_marker + link_insertion, 1)

path.write_text(source, encoding="utf-8")
print("Fixed copied-repository and Markdown-link dependency isolation")
