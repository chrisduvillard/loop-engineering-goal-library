#!/usr/bin/env python3
"""Validate the zero-friction goal library, shaping history, skills, and lifecycle."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import sync_goal_docs  # noqa: E402

ERRORS: list[str] = []
PLACEHOLDER = re.compile(r"\[[A-Z][A-Z0-9 _/.,:+-]{2,}\]")
ACTION_PIN = re.compile(r"uses:\s+[^@\s]+@([0-9a-f]{40})(?:\s+#.*)?$")


def fail(message: str) -> None:
    ERRORS.append(message)


def require(path: str) -> Path:
    candidate = ROOT / path
    if not candidate.exists():
        fail(f"Missing required path: {path}")
    return candidate


def require_absent(path: str) -> None:
    if (ROOT / path).exists():
        fail(f"Temporary or forbidden path must not be committed: {path}")


def load_catalog() -> dict:
    path = require("goals/catalog.json")
    if not path.exists():
        return {"categories": [], "goals": []}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        fail(f"goals/catalog.json is invalid JSON: {error}")
        return {"categories": [], "goals": []}


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
        else:
            top[key] = unquote_yaml(value)
    return top, metadata


def validate_version() -> str:
    version_path = require("VERSION")
    version = version_path.read_text(encoding="utf-8").strip() if version_path.exists() else ""
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", version):
        fail(f"VERSION is not semantic: {version!r}")
    changelog = require("CHANGELOG.md")
    if changelog.exists() and f"## [{version}]" not in changelog.read_text(encoding="utf-8"):
        fail(f"CHANGELOG.md has no section for VERSION {version}")
    return version


def validate_catalog(catalog: dict) -> list[dict]:
    if catalog.get("schema_version") != 1:
        fail("goals/catalog.json: schema_version must be 1")
    categories = catalog.get("categories", [])
    goals = catalog.get("goals", [])
    keys = [item.get("key") for item in categories]
    if keys != ["core", "specialist", "quality"]:
        fail(f"Unexpected category order: {keys}")
    expected_counts = {"core": 7, "specialist": 6, "quality": 9}
    counts = {key: 0 for key in expected_counts}
    seen_ids: set[str] = set()
    seen_files: set[str] = set()
    for index, item in enumerate(goals, start=1):
        goal_id = item.get("id", "")
        filename = item.get("file", "")
        category = item.get("category", "")
        if goal_id != f"{index:02d}":
            fail(f"Catalog goal {filename}: expected id {index:02d}, found {goal_id}")
        if goal_id in seen_ids or filename in seen_files:
            fail(f"Duplicate catalog goal: {goal_id} / {filename}")
        seen_ids.add(goal_id)
        seen_files.add(filename)
        if category not in counts:
            fail(f"Catalog goal {filename}: unknown category {category}")
        else:
            counts[category] += 1
        for field in ("title", "simple", "use_when"):
            if not item.get(field):
                fail(f"Catalog goal {filename}: missing {field}")
    if len(goals) != 22:
        fail(f"Expected 22 goals, found {len(goals)}")
    if counts != expected_counts:
        fail(f"Unexpected category counts: {counts}")
    return goals


def extract_commands(text: str) -> list[str]:
    return [item.strip() for item in re.findall(r"```text\n(/goal .*?)\n```", text, flags=re.DOTALL)]


def validate_goal_files(catalog_goals: list[dict]) -> None:
    expected = {item["file"] for item in catalog_goals}
    actual = {
        path.name
        for path in (ROOT / "goals").glob("*.md")
        if path.name != "README.md"
    }
    if actual != expected:
        fail(f"Goal catalog/file mismatch. Missing={sorted(expected-actual)}; extra={sorted(actual-expected)}")

    profile_inputs = require("skills/shape-goal/references/profile-inputs.md")
    profile_text = profile_inputs.read_text(encoding="utf-8") if profile_inputs.exists() else ""
    loop_profiles = require("skills/goal-engine/references/loop-profiles.md")
    loop_text = loop_profiles.read_text(encoding="utf-8") if loop_profiles.exists() else ""

    for item in catalog_goals:
        path = ROOT / "goals" / item["file"]
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        lower = text.lower()
        if not text.startswith(f"# {item['title']}\n"):
            fail(f"goals/{item['file']}: title differs from catalog")
        for field, marker in (("use_when", "**Use when:**"), ("simple", "**In simple terms:**")):
            if f"{marker} {item[field]}" not in text:
                fail(f"goals/{item['file']}: {field} differs from catalog")
        for heading in (
            "## Run unchanged — recommended",
            "## Inputs the skills resolve",
            "## Run unchanged — self-contained fallback",
        ):
            if heading not in text:
                fail(f"goals/{item['file']}: missing {heading!r}")

        commands = extract_commands(text)
        if len(commands) != 2:
            fail(f"goals/{item['file']}: expected exactly 2 /goal commands, found {len(commands)}")
            continue
        recommended, fallback = commands

        if PLACEHOLDER.search(recommended):
            fail(f"goals/{item['file']}: recommended launcher contains placeholder {PLACEHOLDER.search(recommended).group(0)!r}")
        for fragment in (
            "shape-goal",
            "goal-engine",
            item["title"],
            "do not make production changes until the user approves a Goal Contract",
            "Do not declare success when shaping is complete",
        ):
            if fragment not in recommended:
                fail(f"goals/{item['file']}: recommended launcher missing {fragment!r}")

        if PLACEHOLDER.search(fallback):
            fail(f"goals/{item['file']}: fallback contains placeholder {PLACEHOLDER.search(fallback).group(0)!r}")
        for fragment in (
            "without requiring the user to prefill placeholders",
            "Search before asking",
            "Goal Contract is approved",
            "reusable closeout packet",
            "Never perform",
        ):
            if fragment not in fallback:
                fail(f"goals/{item['file']}: fallback missing {fragment!r}")

        if "secrets" not in lower or "private data" not in lower:
            fail(f"goals/{item['file']}: sensitive-data guard is incomplete")
        if item["title"] not in profile_text:
            fail(f"profile-inputs.md: missing {item['title']}")
        if item["title"] not in loop_text:
            fail(f"loop-profiles.md: missing {item['title']}")

    if "## Custom Contract-Driven" not in profile_text:
        fail("profile-inputs.md: missing Custom Contract-Driven")
    if "## Custom Contract-Driven" not in loop_text:
        fail("loop-profiles.md: missing Custom Contract-Driven")


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
                fail(f"{rel}: missing {key}")
        for key in ("user-invocable", "disable-model-invocation"):
            if key not in top:
                fail(f"{rel}: missing {key}")
        name = top.get("name", "")
        names.add(name)
        if name != path.parent.name:
            fail(f"{rel}: name {name!r} does not match directory")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            fail(f"{rel}: invalid skill name {name!r}")
        for key in ("author", "version", "source"):
            if not metadata.get(key):
                fail(f"{rel}: metadata.{key} is missing")
        if metadata.get("version") != version:
            fail(f"{rel}: metadata.version does not match VERSION {version}")
        if metadata.get("source") != "github.com/chrisduvillard/loop-engineering-goal-library":
            fail(f"{rel}: unexpected metadata.source")

        host_metadata = require(str(path.parent.relative_to(ROOT) / "agents/openai.yaml"))
        if host_metadata.exists():
            host_text = host_metadata.read_text(encoding="utf-8")
            for fragment in ("display_name:", "short_description:", "default_prompt:", "allow_implicit_invocation: true"):
                if fragment not in host_text:
                    fail(f"{host_metadata.relative_to(ROOT)}: missing {fragment!r}")

    if names != {"shape-goal", "goal-engine"}:
        fail(f"Unexpected skill set: {sorted(names)}")

    shape = require("skills/shape-goal/SKILL.md")
    if shape.exists():
        text = shape.read_text(encoding="utf-8").lower()
        for fragment in (
            "zero-friction bootstrap",
            "input ledger",
            "save every asked question and answer",
            "deepening round",
            "approval shaping round",
            "references/profile-inputs.md",
            "references/input-resolution.md",
            "references/shaping-history.md",
            "templates/shaping-history-template.md",
            "shaping is complete; the enclosing goal is not complete",
        ):
            if fragment.lower() not in text:
                fail(f"{shape.relative_to(ROOT)}: missing {fragment!r}")

    engine = require("skills/goal-engine/SKILL.md")
    if engine.exists():
        text = engine.read_text(encoding="utf-8").lower()
        for fragment in (
            "zero-friction handoff",
            "shaping history",
            "approval shaping round",
            "deeper reshaping",
            "do not treat shaping as completion",
            "goal-fit gate",
            "evidence for the evaluator",
            "preserve `shaping.md`",
        ):
            if fragment.lower() not in text:
                fail(f"{engine.relative_to(ROOT)}: missing {fragment!r}")


def require_fragments(path: Path, fragments: tuple[str, ...]) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    for fragment in fragments:
        if fragment not in text:
            fail(f"{path.relative_to(ROOT)}: missing {fragment!r}")


def validate_state_and_docs() -> None:
    required_paths = (
        "README.md", "INSTALL.md", "CHANGELOG.md", "ROADMAP.md", "CONTRIBUTING.md",
        "FULL_REPORT.md", "CURRENT_IMPLEMENTATION.md", "SOURCES.md", "VERSION", "GOAL_LIBRARY.md",
        "SPECIALIST_LOOPS.md", "QUALITY_GOALS.md", "QUICK_REFERENCE.md",
        "SKILLS_AND_GOALS.md", "goals/README.md", "goals/catalog.json",
        "skills/shape-goal/SKILL.md",
        "skills/shape-goal/goal-contract-template.md",
        "skills/shape-goal/references/input-resolution.md",
        "skills/shape-goal/references/profile-inputs.md",
        "skills/shape-goal/references/shaping-history.md",
        "skills/shape-goal/templates/shaping-history-template.md",
        "skills/shape-goal/templates/goal-portfolio-template.md",
        "skills/shape-goal/templates/custom-contract-driven-goal.md",
        "skills/goal-engine/SKILL.md",
        "skills/goal-engine/references/loop-profiles.md",
        "skills/goal-engine/references/assurance-overlays.md",
        "skills/goal-engine/references/state-and-evidence.md",
        "skills/goal-engine/templates/project-harness-template.md",
        "skills/goal-engine/templates/goal-progress-template.md",
        "skills/goal-engine/templates/goal-result-template.md",
        "skills/goal-engine/templates/goal-history-index-template.md",
        "scripts/package_skills.py", "scripts/sync_goal_docs.py",
        "scripts/validate_repository.py", ".github/workflows/validate.yml",
        "examples/complete-brownfield-cycle/README.md",
        "examples/complete-brownfield-cycle/SHAPING.md",
        "examples/complete-brownfield-cycle/PORTFOLIO.md",
        "examples/complete-brownfield-cycle/CONTRACT.md",
        "examples/complete-brownfield-cycle/PROGRESS.md",
        "examples/complete-brownfield-cycle/RESULT.md",
        "docs/goals/INDEX.md",
        "docs/goals/2026-08-25-zero-friction-profile-coverage/SHAPING.md",
        "docs/goals/2026-08-25-zero-friction-profile-coverage/CONTRACT.md",
        "docs/goals/2026-08-25-zero-friction-profile-coverage/PROGRESS.md",
        "docs/goals/2026-08-25-zero-friction-profile-coverage/RESULT.md",
    )
    for path in required_paths:
        require(path)

    require_absent(".github/workflows/apply-zero-friction-update.yml")

    require_fragments(require("CURRENT_IMPLEMENTATION.md"), (
        "Version `0.4.0`", "22 zero-friction goal profiles", "## Shaping history", "## Verification",
    ))
    require_fragments(require("README.md"), (
        "## Quick start", "Every question and answer is saved immediately",
        "## One-command example", "## Strict two-step mode", "## Deep-review guarantees",
        "/shape-goal Deepen the current goal", "SHAPING.md",
        "<!-- goal-catalog:start -->", "<!-- goal-catalog:end -->",
    ))
    require_fragments(require("skills/shape-goal/goal-contract-template.md"), (
        "**Launcher:**", "**Input ledger:**", "**Shaping history:**",
        "**Approval shaping round:**", "## Shaping history and decision trace",
        "## Input resolution record", "## Profile-specific inputs",
        "## Goal-drift review triggers", "├── SHAPING.md",
    ))
    require_fragments(require("skills/shape-goal/references/input-resolution.md"), (
        "## The input ledger", "## Create or resume shaping history", "## Search before asking",
        "## Ask one material decision at a time", "## Standard and deeper rounds",
        "## Round close and approval gate", "## Handoff inside a zero-friction `/goal`",
    ))
    require_fragments(require("skills/shape-goal/references/shaping-history.md"), (
        "## Append-only rule", "## What to record for every question",
        "## Standard and deepening rounds", "## Repeatable deepening",
        "R1-Q1", "├── SHAPING.md",
    ))
    require_fragments(require("skills/shape-goal/templates/shaping-history-template.md"), (
        "## Current decision index", "## Round R1", "### Questions and answers",
        "**Exact question:**", "**User answer:**", "## Corrections and supersessions",
    ))
    require_fragments(require("skills/goal-engine/references/state-and-evidence.md"), (
        "Shaping history", "## Shaping-history rules", "approval round", "├── SHAPING.md",
    ))
    require_fragments(require("skills/goal-engine/templates/goal-progress-template.md"), (
        "**Shaping history:**", "**Completed / approval shaping rounds:**",
        "## Dependencies, shaping, and goal fit",
    ))
    require_fragments(require("skills/goal-engine/templates/goal-result-template.md"), (
        "**Shaping history:**", "## Shaping decision trace", "Completed / approval shaping rounds",
    ))
    require_fragments(require("skills/goal-engine/templates/goal-history-index-template.md"), (
        "| Goal ID | Rev |", "Shaping", "├── SHAPING.md",
    ))
    require_fragments(require("examples/complete-brownfield-cycle/SHAPING.md"), (
        "R1-Q1", "R1-Q2", "R2-Q1", "R2-Q2", "Approval round:** R2",
        "## Corrections and supersessions",
    ))
    require_fragments(require("examples/complete-brownfield-cycle/CONTRACT.md"), (
        "**Shaping history:** `SHAPING.md`", "**Approval shaping round:** R2",
        "## Shaping history and decision trace",
    ))
    require_fragments(require("examples/complete-brownfield-cycle/PROGRESS.md"), (
        "**Completed / approval shaping rounds:** R1, R2 / R2", "Latest shaping round: R2",
    ))
    require_fragments(require("examples/complete-brownfield-cycle/RESULT.md"), (
        "**Shaping history:** `SHAPING.md`", "## Shaping decision trace", "Approval round: R2",
    ))
    require_fragments(require("skills/goal-engine/references/assurance-overlays.md"), (
        "## Dedicated profile or overlay?", "Frontend UI / UX / Accessibility",
        "Documentation Synchronization / Knowledge Transfer", "Compliance / Audit Readiness",
    ))
    require_fragments(require("docs/goals/2026-08-25-zero-friction-profile-coverage/SHAPING.md"), (
        "Round R1", "Round R2", "Question preservation", "Deeper shaping",
    ))
    require_fragments(require("docs/goals/2026-08-25-zero-friction-profile-coverage/RESULT.md"), (
        "**Outcome:** Achieved", "22 zero-friction launchers", "Frontend UI / UX / Accessibility",
        "Documentation Synchronization / Knowledge Transfer", "CI validation",
    ))


def validate_generated_docs() -> None:
    try:
        documents = sync_goal_docs.render_documents()
    except Exception as error:  # noqa: BLE001
        fail(f"Could not render generated docs: {error}")
        return
    for path, expected in documents.items():
        actual = path.read_text(encoding="utf-8") if path.exists() else ""
        if actual != expected:
            fail(f"{path.relative_to(ROOT)} is out of date; run python3 scripts/sync_goal_docs.py --write")


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


def validate_scripts_and_ci() -> None:
    for path in sorted((ROOT / "scripts").glob("*.py")):
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except SyntaxError as error:
            fail(f"{path.relative_to(ROOT)}: syntax error: {error}")

    workflow = require(".github/workflows/validate.yml")
    if workflow.exists():
        for line in workflow.read_text(encoding="utf-8").splitlines():
            if "uses:" not in line:
                continue
            match = ACTION_PIN.search(line.strip())
            if not match:
                fail(f".github/workflows/validate.yml: action is not pinned to a full commit SHA: {line.strip()}")
        text = workflow.read_text(encoding="utf-8")
        for fragment in (
            "skills@1.5.23", "scripts/sync_goal_docs.py --check",
            "scripts/package_skills.py", "scripts/validate_repository.py",
        ):
            if fragment not in text:
                fail(f".github/workflows/validate.yml: missing {fragment!r}")


def main() -> int:
    version = validate_version()
    catalog = load_catalog()
    catalog_goals = validate_catalog(catalog)
    validate_goal_files(catalog_goals)
    validate_skills(version)
    validate_state_and_docs()
    validate_generated_docs()
    validate_markdown_links()
    validate_scripts_and_ci()

    if ERRORS:
        print("Repository validation failed:\n")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print("Repository validation passed.")
    print(f"- version {version}")
    print("- 2 portable skills with host metadata")
    print("- 22 zero-friction recommended launchers")
    print("- 22 self-contained no-placeholder fallbacks")
    print("- 7 core, 6 specialist, and 9 quality profiles")
    print("- profile-specific input resolution and append-only shaping rounds")
    print("- durable question/answer history with corrections and approval linkage")
    print("- multi-goal portfolio, project harness, and reusable closeout")
    print("- generated catalogs synchronized")
    print("- temporary update workflow absent")
    print("- GitHub Actions pinned to immutable commits")
    print("- local Markdown links resolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
