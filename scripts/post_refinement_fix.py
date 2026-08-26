#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    source = target.read_text(encoding="utf-8")
    if old not in source:
        if new in source:
            return
        raise SystemExit(f"{path}: expected source pattern not found")
    target.write_text(source.replace(old, new, 1), encoding="utf-8")


replace_once(
    "tests/test_adversarial_robustness.py",
    '        ignore=shutil.ignore_patterns(".git", "dist", "__pycache__", "*.pyc"),\n',
    '        ignore=shutil.ignore_patterns(".git", "dist", "node_modules", "__pycache__", "*.pyc"),\n',
)

replace_once(
    "scripts/validate_repository.py",
    '    for path in ROOT.rglob("*.md"):\n        source = path.read_text(encoding="utf-8")\n',
    '    for path in ROOT.rglob("*.md"):\n        if any(part in {"node_modules", "dist", "build", "__pycache__", ".venv", "venv", ".tox", ".nox", ".pytest_cache", ".mypy_cache", ".ruff_cache"} for part in path.parts):\n            continue\n        source = path.read_text(encoding="utf-8")\n',
)

print("Applied post-refinement generated-directory exclusions")
