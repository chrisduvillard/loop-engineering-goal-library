#!/usr/bin/env python3
"""Correct one overlay label and add overlay-name validation."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]

goal_path = root / "goals/23-test-suite-ci-health.md"
goal = goal_path.read_text(encoding="utf-8")
old = "**Suggested assurance overlays:** Reliability & Recovery, Developer Experience & Tooling, Performance & Cost"
new = "**Suggested assurance overlays:** Reliability & Recovery, Documentation & Knowledge Transfer, Performance & Cost"
if old not in goal:
    raise SystemExit("goal 23 overlay line not found")
goal_path.write_text(goal.replace(old, new, 1), encoding="utf-8")

validator_path = root / "scripts/validate_repository.py"
validator = validator_path.read_text(encoding="utf-8")
constant_anchor = 'ACTION_PIN = re.compile(r"uses:\\s+[^@\\s]+@([0-9a-f]{40})(?:\\s+#.*)?$")\n'
constant = '''ASSURANCE_OVERLAYS = {
    "Security & Privacy",
    "Reliability & Recovery",
    "Performance & Cost",
    "UX & Accessibility",
    "Data Integrity & Governance",
    "Compatibility & Portability",
    "Operability & Observability",
    "Documentation & Knowledge Transfer",
    "Compliance & Auditability",
}
'''
if "ASSURANCE_OVERLAYS = {" not in validator:
    if constant_anchor not in validator:
        raise SystemExit("validator constant anchor not found")
    validator = validator.replace(constant_anchor, constant_anchor + constant, 1)

loop_anchor = "        lower = text.lower()\n"
validation = '''        suggested = re.search(
            r"^\\*\\*Suggested assurance overlays:\\*\\*\\s*(.+)$",
            text,
            flags=re.MULTILINE,
        )
        if not suggested:
            fail(f"goals/{item['file']}: missing suggested assurance overlays")
        else:
            raw_overlays = suggested.group(1).strip()
            if not raw_overlays.lower().startswith(("none by default", "select only")):
                for overlay in (part.strip() for part in raw_overlays.split(",")):
                    if overlay not in ASSURANCE_OVERLAYS:
                        fail(f"goals/{item['file']}: unknown assurance overlay {overlay!r}")
'''
if "unknown assurance overlay" not in validator:
    if loop_anchor not in validator:
        raise SystemExit("validator loop anchor not found")
    validator = validator.replace(loop_anchor, loop_anchor + validation, 1)

validator_path.write_text(validator, encoding="utf-8")
Path(__file__).unlink()
