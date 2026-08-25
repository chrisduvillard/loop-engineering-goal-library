#!/usr/bin/env python3
"""Validate the goal library's structure, skills, profiles, and Markdown links."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

CORE_GOALS = [
    "01-brownfield-continue-finish.md",
    "02-prd-spec-compliance.md",
    "03-next-milestone.md",
    "04-deep-audit-remediation.md",
    "05-qa-regression-uat.md",
    "06-safe-refactor-modernization.md",
    "07-release-readiness.md",
]

SPECIALIST_GOALS = [
    "08-incident-recovery.md",
    "09-dependency-framework-upgrade.md",
    "10-data-migration-integrity.md",
    "11-branch-rescue-integration.md",
]

PROFILE_NAMES = [
    "Brownfield Continue / Finish",
    "PRD / Spec Compliance",
    "Next Milestone",
    "Deep Audit + Remediation",
    "QA / Regression / UAT",
    "Safe Refactor / Modernization",
    "Release Readiness",
    "Incident Recovery / Stabilization",
    "Dependency / Framework Upgrade",
    "Data Migration / Integrity",
    "Branch Rescue / Integration",
]


def fail(message: str) -> None:
    ERRORS.append(message)


def require(path: str) -> Path:
    candidate = ROOT / path
    if not candidate.exists():
        fail(f"Missing required path: {path}")
    return candidate


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return {}

    parts = text.split("---\n", 2)
    if len(parts) < 3:
        fail(f"{path.relative_to(ROOT)}: unterminated YAML frontmatter")
        return {}

    values: dict[str, str] = {}
    for raw_line in parts[1].splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values


def validate_skills() -> None:
    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if len(skill_files) != 2:
        fail(f"Expected exactly 2 skills, found {len(skill_files)}")

    names: set[str] = set()
    for path in skill_files:
        frontmatter = parse_frontmatter(path)
        for key in ("name", "description"):
            if not frontmatter.get(key):
                fail(f"{path.relative_to(ROOT)}: missing non-empty {key}")

        name = frontmatter.get("name", "")
        if name and name in names:
            fail(f"Duplicate skill name: {name}")
        names.add(name)

        if name and name != path.parent.name:
            fail(
                f"{path.relative_to(ROOT)}: frontmatter name {name!r} "
                f"does not match directory {path.parent.name!r}"
            )

    if names != {"shape-goal", "goal-engine"}:
        fail(f"Unexpected skill set: {sorted(names)}")


def validate_goals_and_profiles() -> None:
    goal_dir = require("goals")
    expected = CORE_GOALS + SPECIALIST_GOALS
    actual = sorted(path.name for path in goal_dir.glob("*.md")) if goal_dir.exists() else []
    if actual != expected:
        fail(f"Goal files differ from expected set. Expected {expected}; found {actual}")

    for filename in expected:
        path = goal_dir / filename
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "/goal " not in text:
            fail(f"goals/{filename}: no copy-ready /goal command found")
        if "**Use when:**" not in text:
            fail(f"goals/{filename}: missing Use when guidance")

    profiles_path = require("skills/goal-engine/references/loop-profiles.md")
    if profiles_path.exists():
        profiles = profiles_path.read_text(encoding="utf-8")
        for name in PROFILE_NAMES:
            if name not in profiles:
                fail(f"Execution profile missing from loop-profiles.md: {name}")


def validate_contract() -> None:
    path = require("skills/shape-goal/goal-contract-template.md")
    if not path.exists():
        return

    text = path.read_text(encoding="utf-8")
    required_fragments = [
        "## Target",
        "## In scope",
        "## Out of scope",
        "## Acceptance evidence",
        "## Protected behavior",
        "## Authority boundaries",
        "## Stop and escalation",
        "## Sources of truth",
        "**Execution profile:**",
        "**Progress state:**",
        "## Native `/goal` command",
    ]
    for fragment in required_fragments:
        if fragment not in text:
            fail(f"Goal Contract template missing: {fragment}")


def normalize_link(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    # Remove an optional Markdown title after a whitespace separator.
    target = re.split(r"\s+[\"']", target, maxsplit=1)[0]
    return unquote(target.split("#", 1)[0])


def validate_markdown_links() -> None:
    link_pattern = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")

    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for match in link_pattern.finditer(text):
            raw_target = match.group(1)
            target = normalize_link(raw_target)
            if not target or target.startswith(("http://", "https://", "mailto:", "data:")):
                continue
            if target.startswith("#"):
                continue

            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                fail(f"{path.relative_to(ROOT)}: link escapes repository: {raw_target}")
                continue

            if not resolved.exists():
                fail(f"{path.relative_to(ROOT)}: broken local link: {raw_target}")


def validate_entry_points() -> None:
    readme = require("README.md")
    architecture = require("SKILLS_AND_GOALS.md")
    quick_reference = require("QUICK_REFERENCE.md")

    checks = {
        readme: ["shape-goal", "goal-engine", "/goal Follow"],
        architecture: ["Goal Contract", "native `/goal`", "goal-engine"],
        quick_reference: ["$shape-goal", "/shape-goal", "Ultra-short default"],
    }

    for path, fragments in checks.items():
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        folded_text = text.casefold()
        for fragment in fragments:
            if fragment.casefold() not in folded_text:
                fail(f"{path.relative_to(ROOT)}: missing entry-point text {fragment!r}")


def main() -> int:
    for required_path in (
        "README.md",
        "GOAL_LIBRARY.md",
        "SPECIALIST_LOOPS.md",
        "QUICK_REFERENCE.md",
        "SKILLS_AND_GOALS.md",
        "skills/shape-goal/SKILL.md",
        "skills/goal-engine/SKILL.md",
        "skills/goal-engine/references/state-and-evidence.md",
    ):
        require(required_path)

    validate_skills()
    validate_goals_and_profiles()
    validate_contract()
    validate_markdown_links()
    validate_entry_points()

    if ERRORS:
        print("Repository validation failed:\n")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print("Repository validation passed.")
    print("- 2 portable skills")
    print("- 11 execution profiles and standalone goals")
    print("- Goal Contract schema present")
    print("- Local Markdown links resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
