#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).with_name("apply_adversarial_robustness.py")
source = path.read_text(encoding="utf-8")

old_function = '''    if source.count(old) != 1:\n        raise RuntimeError(f"{path}: expected one occurrence of {old!r}, found {source.count(old)}")\n    target.write_text(source.replace(old, new, 1), encoding="utf-8")\n'''
new_function = '''    if source.count(old) < 1:\n        raise RuntimeError(f"{path}: expected at least one occurrence of {old!r}")\n    target.write_text(source.replace(old, new, 1), encoding="utf-8")\n'''
if old_function in source:
    source = source.replace(old_function, new_function, 1)

old_required = '''replace_once(\n    "scripts/validate_repository.py",\n    "        \\\"scripts/validate_repository.py\\\",\\n",\n    "        \\\"scripts/validate_repository.py\\\",\\n"\n    "        \\\"tests/test_adversarial_robustness.py\\\",\\n"\n    "        \\\"docs/ROBUSTNESS_AUDIT.md\\\",\\n"\n    "        \\\"package.json\\\",\\n"\n    "        \\\"package-lock.json\\\",\\n"\n    "        \\\"docs/goals/2026-08-26-adversarial-robustness/SHAPING.md\\\",\\n"\n    "        \\\"docs/goals/2026-08-26-adversarial-robustness/CONTRACT.md\\\",\\n"\n    "        \\\"docs/goals/2026-08-26-adversarial-robustness/PROGRESS.md\\\",\\n"\n    "        \\\"docs/goals/2026-08-26-adversarial-robustness/UAT.md\\\",\\n",\n)\n'''
new_required = '''replace_once(\n    "scripts/validate_repository.py",\n    "        \\\"scripts/validate_shaping_history_diff.py\\\",\\n        \\\"scripts/validate_repository.py\\\",\\n        \\\".github/dependabot.yml\\\",\\n",\n    "        \\\"scripts/validate_shaping_history_diff.py\\\",\\n"\n    "        \\\"scripts/validate_repository.py\\\",\\n"\n    "        \\\"tests/test_adversarial_robustness.py\\\",\\n"\n    "        \\\"docs/ROBUSTNESS_AUDIT.md\\\",\\n"\n    "        \\\"package.json\\\",\\n"\n    "        \\\"package-lock.json\\\",\\n"\n    "        \\\"docs/goals/2026-08-26-adversarial-robustness/SHAPING.md\\\",\\n"\n    "        \\\"docs/goals/2026-08-26-adversarial-robustness/CONTRACT.md\\\",\\n"\n    "        \\\"docs/goals/2026-08-26-adversarial-robustness/PROGRESS.md\\\",\\n"\n    "        \\\"docs/goals/2026-08-26-adversarial-robustness/UAT.md\\\",\\n"\n    "        \\\".github/dependabot.yml\\\",\\n",\n)\n'''
if old_required not in source:
    raise SystemExit("required-path patch block not found")
source = source.replace(old_required, new_required, 1)

old_workflow = '''replace_once(\n    "scripts/validate_repository.py",\n    '        "scripts/validate_repository.py",\\n',\n    '        "scripts/validate_repository.py",\\n        "python -m unittest discover -s tests -v",\\n        "npm ci --ignore-scripts",\\n        "npx --no-install skills",\\n',\n)\n'''
new_workflow = '''replace_once(\n    "scripts/validate_repository.py",\n    '        "scripts/package_skills.py",\\n        "scripts/validate_repository.py",\\n    ):\\n',\n    '        "scripts/package_skills.py",\\n        "scripts/validate_repository.py",\\n        "python -m unittest discover -s tests -v",\\n        "npm ci --ignore-scripts",\\n        "npx --no-install skills",\\n    ):\\n',\n)\nreplace_once(\n    "scripts/validate_repository.py",\n    '        "skills@1.5.23",\\n',\n    '        "npm ci --ignore-scripts",\\n        "npx --no-install skills",\\n',\n)\n'''
if old_workflow not in source:
    raise SystemExit("workflow-fragment patch block not found")
source = source.replace(old_workflow, new_workflow, 1)

path.write_text(source, encoding="utf-8")
print("Fixed apply script replacement targeting")
