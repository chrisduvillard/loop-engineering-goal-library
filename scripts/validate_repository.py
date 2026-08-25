#!/usr/bin/env python3
"""Validate the goal library's structure, skills, lifecycle, generated docs, and links."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import sync_goal_docs  # noqa: E402

ERRORS: list[str] = []

CORE_GOALS = list(sync_goal_docs.CORE_GOALS)
SPECIALIST_GOALS = list(sync_goal_docs.SPECIALIST_GOALS)
ALL_GOALS = CORE_GOALS + SPECIALIST_GOALS

PROFILE_NAMES = (
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
)

REQUIRED_PATHS = (
    "README.md", "INSTALL.md", "CHANGELOG.md", "ROADMAP.md", "VERSION",
    "GOAL_LIBRARY.md", "SPECIALIST_LOOPS.md", "QUICK_REFERENCE.md",
    "SKILLS_AND_GOALS.md", "skills/shape-goal/SKILL.md",
    "skills/shape-goal/goal-contract-template.md", "skills/goal-engine/SKILL.md",
    "skills/goal-engine/references/loop-profiles.md",
    "skills/goal-engine/references/state-and-evidence.md",
    "skills/goal-engine/templates/goal-progress-template.md",
    "skills/goal-engine/templates/goal-result-template.md",
    "skills/goal-engine/templates/goal-history-index-template.md",
    "scripts/package_skills.py", "scripts/sync_goal_docs.py",
    "examples/complete-brownfield-cycle/README.md",
    "examples/complete-brownfield-cycle/CONTRACT.md",
    "examples/complete-brownfield-cycle/PROGRESS.md",
    "examples/complete-brownfield-cycle/RESULT.md",
    ".github/workflows/validate.yml",
)


def fail(message: str) -> None:
    ERRORS.append(message)


def require(path: str) -> Path:
    candidate = ROOT / path
    if not candidate.exists():
        fail(f"Missing required path: {path}")
    return candidate


def unquote_yaml(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_frontmatter(path: Path) -> tuple[dict[str, str], dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return {}, {}
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        fail(f"{path.relative_to(ROOT)}: unterminated YAML frontmatter")
        return {}, {}

    top: dict[str, str] = {}
    metadata: dict[str, str] = {}
    in_metadata = False
    for raw_line in parts[1].splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.startswith(("  ", "\t")):
            if in_metadata and ":" in raw_line:
                key, value = raw_line.strip().split(":", 1)
                metadata[key.strip()] = unquote_yaml(value)
            continue
        in_metadata = False
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        key = key.strip()
        if key == "metadata":
            in_metadata = True
            continue
        top[key] = unquote_yaml(value)
    return top, metadata


def validate_version() -> str:
    path = require("VERSION")
    if not path.exists():
        return ""
    version = path.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", version):
        fail(f"VERSION is not semantic: {version!r}")
    changelog = require("CHANGELOG.md")
    if changelog.exists() and f"## [{version}]" not in changelog.read_text(encoding="utf-8"):
        fail(f"CHANGELOG.md has no release section for VERSION {version}")
    return version


def validate_skills(version: str) -> None:
    skills_root = require("skills")
    skill_files = sorted(skills_root.glob("*/SKILL.md")) if skills_root.exists() else []
    if len(skill_files) != 2:
        fail(f"Expected exactly 2 skills, found {len(skill_files)}")
    names: set[str] = set()
    for path in skill_files:
        top, metadata = parse_frontmatter(path)
        rel = path.relative_to(ROOT)
        for key in ("name", "description", "compatibility"):
            if not top.get(key):
                fail(f"{rel}: missing non-empty {key}")
        name = top.get("name", "")
        if name:
            if name in names:
                fail(f"Duplicate skill name: {name}")
            names.add(name)
            if name != path.parent.name:
                fail(f"{rel}: name {name!r} does not match directory {path.parent.name!r}")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
                fail(f"{rel}: invalid portable skill name {name!r}")
        if len(top.get("description", "")) > 1024:
            fail(f"{rel}: description exceeds 1024 characters")
        if len(top.get("compatibility", "")) > 500:
            fail(f"{rel}: compatibility exceeds 500 characters")
        for key in ("author", "version", "source"):
            if not metadata.get(key):
                fail(f"{rel}: metadata.{key} is missing")
        if version and metadata.get("version") != version:
            fail(f"{rel}: metadata.version does not match VERSION {version!r}")
        if metadata.get("source") != "github.com/chrisduvillard/loop-engineering-goal-library":
            fail(f"{rel}: unexpected metadata.source")
    if names != {"shape-goal", "goal-engine"}:
        fail(f"Unexpected skill set: {sorted(names)}")


def extract_goal_command(text: str) -> str:
    matches = re.findall(r"```text\n(/goal .*?)\n```", text, flags=re.DOTALL)
    return matches[-1].strip() if matches else ""


def validate_goals_and_generated_docs() -> None:
    goal_dir = require("goals")
    actual = sorted(path.name for path in goal_dir.glob("*.md")) if goal_dir.exists() else []
    if actual != ALL_GOALS:
        fail(f"Goal files differ from expected set. Expected {ALL_GOALS}; found {actual}")
    for filename in ALL_GOALS:
        path = goal_dir / filename
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        lower = text.lower()
        if not text.startswith("# "):
            fail(f"goals/{filename}: must begin with one H1 title")
        if "**Use when:**" not in text:
            fail(f"goals/{filename}: missing Use when guidance")
        if not extract_goal_command(text):
            fail(f"goals/{filename}: no copy-ready /goal command found")
        if "reusable closeout packet" not in lower:
            fail(f"goals/{filename}: no reusable closeout requirement")
        if "secrets" not in lower and "private data" not in lower:
            fail(f"goals/{filename}: no sensitive-data archive guard")
    for path, expected in sync_goal_docs.render_documents().items():
        if path.exists() and path.read_text(encoding="utf-8") != expected:
            fail(f"{path.relative_to(ROOT)} is out of date; run python3 scripts/sync_goal_docs.py --write")


def validate_profiles() -> None:
    path = require("skills/goal-engine/references/loop-profiles.md")
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    for name in PROFILE_NAMES:
        if name not in text:
            fail(f"Execution profile missing from loop-profiles.md: {name}")


def require_fragments(path: Path, fragments: tuple[str, ...]) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    for fragment in fragments:
        if fragment not in text:
            fail(f"{path.relative_to(ROOT)}: missing required text {fragment!r}")


def validate_state_and_examples() -> None:
    require_fragments(require("skills/shape-goal/goal-contract-template.md"), (
        "**Goal ID:**", "**Library:**", "**Progress state:**", "**Archive path:**",
        "## Target", "## Acceptance evidence", "## Protected behavior",
        "## Authority boundaries", "## Stop and escalation", "## Reuse and closeout",
        "## Native `/goal` command", "CONTRACT.md", "PROGRESS.md", "RESULT.md",
    ))
    require_fragments(require("skills/goal-engine/references/state-and-evidence.md"), (
        "GOAL.md", "GOAL_PROGRESS.md", "docs/goals/INDEX.md",
        "Durable-knowledge promotion", "Closeout archive", "Sensitive-data guard",
    ))
    require_fragments(require("examples/complete-brownfield-cycle/CONTRACT.md"), (
        "2026-08-25-portfolio-import-v1-4", "PRD / Spec Compliance", "## Reuse and closeout",
    ))
    require_fragments(require("examples/complete-brownfield-cycle/PROGRESS.md"), (
        "## Acceptance ledger", "68 passed", "12/12", "42 passed", "## Next action",
    ))
    require_fragments(require("examples/complete-brownfield-cycle/RESULT.md"), (
        "**Outcome:** Achieved", "## Reusable lessons", "tests/imports/test_spreadsheet_dates.py",
    ))


def normalize_link(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    target = re.split(r"\s+[\"']", target, maxsplit=1)[0]
    return unquote(target.split("#", 1)[0])


def validate_markdown_links() -> None:
    pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for match in pattern.finditer(text):
            raw_target = match.group(1)
            target = normalize_link(raw_target)
            if not target or target.startswith(("http://", "https://", "mailto:", "data:", "tel:")):
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
    checks = {
        require("README.md"): ("Install once, use everywhere", "Archive and reuse", "Update without drift", "shape-goal", "goal-engine"),
        require("INSTALL.md"): ("install globally", "Verify the installation", "Update", "Build reusable ZIP packages"),
        require("QUICK_REFERENCE.md"): ("Global install", "Close and preserve", "Ultra-short default"),
        require("SKILLS_AND_GOALS.md"): ("Goal Contract", "native `/goal`", "goal-engine", "Reusable closeout archive"),
        require("ROADMAP.md"): ("Before `1.0.0`", "live Codex", "live Claude Code", "license"),
    }
    for path, fragments in checks.items():
        if not path.exists():
            continue
        lower = path.read_text(encoding="utf-8").lower()
        for fragment in fragments:
            if fragment.lower() not in lower:
                fail(f"{path.relative_to(ROOT)}: missing entry-point text {fragment!r}")


def validate_scripts_and_ci() -> None:
    for path in sorted((ROOT / "scripts").glob("*.py")):
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except SyntaxError as error:
            fail(f"{path.relative_to(ROOT)}: syntax error: {error}")
    workflow = require(".github/workflows/validate.yml")
    if workflow.exists():
        text = workflow.read_text(encoding="utf-8")
        for fragment in (
            "actions/checkout@v7", "actions/setup-python@v7", "actions/upload-artifact@v7",
            "skills@1.5.23", "scripts/sync_goal_docs.py --check", "scripts/package_skills.py",
        ):
            if fragment not in text:
                fail(f"{workflow.relative_to(ROOT)}: missing {fragment!r}")


def main() -> int:
    for path in REQUIRED_PATHS:
        require(path)
    version = validate_version()
    validate_skills(version)
    validate_goals_and_generated_docs()
    validate_profiles()
    validate_state_and_examples()
    validate_markdown_links()
    validate_entry_points()
    validate_scripts_and_ci()
    if ERRORS:
        print("Repository validation failed:\n")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print("Repository validation passed.")
    print(f"- version {version}")
    print("- 2 portable skills")
    print("- 11 canonical execution profiles and standalone goals")
    print("- generated consolidated libraries are synchronized")
    print("- reusable Goal Contract, progress, result, and history schemas")
    print("- completed-cycle example")
    print("- local Markdown links resolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
