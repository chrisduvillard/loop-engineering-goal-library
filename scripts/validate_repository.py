#!/usr/bin/env python3
"""Validate the interactive-first goal library, skills, state, and generated docs."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import sync_goal_docs  # noqa: E402
import sync_goal_launchers  # noqa: E402

ERRORS: list[str] = []
PLACEHOLDER = re.compile(r"\[[A-Z][A-Z0-9 _/.,:+-]{2,}\]")
ACTION_PIN = re.compile(r"uses:\s+[^@\s]+@([0-9a-f]{40})(?:\s+#.*)?$")
ASSURANCE_OVERLAYS = {
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


def text(path: str) -> str:
    candidate = require(path)
    return candidate.read_text(encoding="utf-8") if candidate.exists() else ""


def unquote_yaml(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_frontmatter(path: Path) -> tuple[dict[str, str], dict[str, str]]:
    source = path.read_text(encoding="utf-8")
    if not source.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return {}, {}
    parts = source.split("---\n", 2)
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


def require_fragments(path: Path, fragments: tuple[str, ...]) -> None:
    if not path.exists():
        return
    source = path.read_text(encoding="utf-8")
    for fragment in fragments:
        if fragment not in source:
            fail(f"{path.relative_to(ROOT)}: missing {fragment!r}")


def validate_version() -> str:
    version = text("VERSION").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", version):
        fail(f"VERSION is not semantic: {version!r}")
    changelog = text("CHANGELOG.md")
    if version and f"## [{version}]" not in changelog:
        fail(f"CHANGELOG.md has no section for VERSION {version}")
    return version


def load_catalog() -> dict:
    source = text("goals/catalog.json")
    try:
        return json.loads(source) if source else {"categories": [], "goals": []}
    except json.JSONDecodeError as error:
        fail(f"goals/catalog.json is invalid JSON: {error}")
        return {"categories": [], "goals": []}


def validate_catalog(catalog: dict) -> list[dict]:
    if catalog.get("schema_version") != 1:
        fail("goals/catalog.json: schema_version must be 1")

    categories = catalog.get("categories", [])
    category_keys = [item.get("key") for item in categories]
    if category_keys != ["core", "specialist", "quality"]:
        fail(f"Unexpected category order: {category_keys}")

    expected_counts = {"core": 7, "specialist": 8, "quality": 14}
    counts = {key: 0 for key in expected_counts}
    goals = catalog.get("goals", [])
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

    if len(goals) != 29:
        fail(f"Expected 29 goals, found {len(goals)}")
    if counts != expected_counts:
        fail(f"Unexpected category counts: {counts}")

    actual_files = {
        path.name
        for path in (ROOT / "goals").glob("*.md")
        if path.name != "README.md"
    }
    if actual_files != seen_files:
        fail(
            "Goal catalog/file mismatch. "
            f"Missing={sorted(seen_files - actual_files)}; extra={sorted(actual_files - seen_files)}"
        )
    return goals


def extract_commands(source: str) -> list[str]:
    return [
        item.strip()
        for item in re.findall(r"```text\n(/goal .*?)\n```", source, flags=re.DOTALL)
    ]


def validate_goal_files(catalog_goals: list[dict]) -> None:
    profile_text = text("skills/shape-goal/references/profile-inputs.md")
    loop_text = text("skills/goal-engine/references/loop-profiles.md")

    for item in catalog_goals:
        path = ROOT / "goals" / item["file"]
        if not path.exists():
            continue
        source = path.read_text(encoding="utf-8")
        lower = source.lower()
        title = item["title"]

        if not source.startswith(f"# {title}\n"):
            fail(f"goals/{item['file']}: title differs from catalog")
        for field, marker in (
            ("use_when", "**Use when:**"),
            ("simple", "**In simple terms:**"),
        ):
            if f"{marker} {item[field]}" not in source:
                fail(f"goals/{item['file']}: {field} differs from catalog")

        for heading in (
            "## Recommended — interactive shaping",
            "## Advanced — autonomous preflight",
            "## Inputs the skills resolve",
            "## Advanced — self-contained preflight",
        ):
            if heading not in source:
                fail(f"goals/{item['file']}: missing {heading!r}")

        for fragment in (
            "`shape-goal` is the main command",
            "outside an active `/goal`",
            f"/shape-goal Use the {title} profile",
            f"$shape-goal Use the {title} profile",
            "ends the turn",
        ):
            if fragment not in source:
                fail(f"goals/{item['file']}: missing interactive guidance {fragment!r}")

        suggested = re.search(
            r"^\*\*Suggested assurance overlays:\*\*\s*(.+)$",
            source,
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

        commands = extract_commands(source)
        if len(commands) != 2:
            fail(f"goals/{item['file']}: expected exactly 2 advanced /goal commands, found {len(commands)}")
            continue

        for command_index, command in enumerate(commands, start=1):
            if len(command) > 4000:
                fail(
                    f"goals/{item['file']}: command {command_index} exceeds 4,000 characters "
                    f"({len(command)})"
                )
            placeholder = PLACEHOLDER.search(command)
            if placeholder:
                fail(
                    f"goals/{item['file']}: command {command_index} contains placeholder "
                    f"{placeholder.group(0)!r}"
                )
            for fragment in (
                "SHAPING.md",
                "Approval required",
                "outside `/goal`",
                "do not ask the question",
            ):
                if fragment not in command:
                    fail(f"goals/{item['file']}: command {command_index} missing {fragment!r}")

        recommended, fallback = commands
        for fragment in (
            "shape-goal",
            "goal-engine",
            title,
            "do not make production changes",
            "Do not declare success when shaping is complete",
        ):
            if fragment not in recommended:
                fail(f"goals/{item['file']}: autonomous preflight missing {fragment!r}")

        for fragment in (
            "without requiring the user to prefill placeholders",
            "Search before asking",
            "Do not edit production before approval",
            "reusable closeout packet",
            "explicit approval",
        ):
            if fragment not in fallback:
                fail(f"goals/{item['file']}: self-contained preflight missing {fragment!r}")

        if "secrets" not in lower or not any(
            term in lower for term in ("private data", "private personal", "confidential business")
        ):
            fail(f"goals/{item['file']}: sensitive-data guard is incomplete")
        if title not in profile_text:
            fail(f"profile-inputs.md: missing {title}")
        if title not in loop_text:
            fail(f"loop-profiles.md: missing {title}")

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
            for fragment in (
                "display_name:",
                "short_description:",
                "default_prompt:",
                "allow_implicit_invocation: true",
            ):
                if fragment not in host_text:
                    fail(f"{host_metadata.relative_to(ROOT)}: missing {fragment!r}")

    if names != {"shape-goal", "goal-engine"}:
        fail(f"Unexpected skill set: {sorted(names)}")

    shape = require("skills/shape-goal/SKILL.md")
    if shape.exists():
        source = shape.read_text(encoding="utf-8").lower()
        for fragment in (
            "`shape-goal` is the main command",
            "interactive first",
            "end the turn immediately",
            "the user's normal reply is the answer",
            "active-goal rescue",
            "autonomous bootstrap — advanced only",
            "do not execute it automatically",
            "references/profile-inputs.md",
            "references/input-resolution.md",
            "references/shaping-history.md",
            "templates/shaping-history-template.md",
        ):
            if fragment.lower() not in source:
                fail(f"{shape.relative_to(ROOT)}: missing {fragment!r}")

    engine = require("skills/goal-engine/SKILL.md")
    if engine.exists():
        source = engine.read_text(encoding="utf-8").lower()
        for fragment in (
            "approved-contract handoff",
            "never ask a material owner question",
            "interaction boundary",
            "stop as **approval required**",
            "resume `shape-goal` outside `/goal`",
            "evidence for the evaluator",
            "goal-fit gate",
            "shaping history",
        ):
            if fragment.lower() not in source:
                fail(f"{engine.relative_to(ROOT)}: missing {fragment!r}")


def validate_state_and_docs() -> None:
    required_paths = (
        "README.md",
        "INSTALL.md",
        "CHANGELOG.md",
        "ROADMAP.md",
        "CONTRIBUTING.md",
        "FULL_REPORT.md",
        "CURRENT_IMPLEMENTATION.md",
        "SOURCES.md",
        "VERSION",
        "GOAL_LIBRARY.md",
        "SPECIALIST_LOOPS.md",
        "QUALITY_GOALS.md",
        "QUICK_REFERENCE.md",
        "SKILLS_AND_GOALS.md",
        "goals/README.md",
        "goals/catalog.json",
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
        "scripts/package_skills.py",
        "scripts/sync_goal_docs.py",
        "scripts/sync_goal_launchers.py",
        "scripts/validate_shaping_history_diff.py",
        "scripts/validate_repository.py",
        ".github/dependabot.yml",
        ".github/workflows/validate.yml",
        "examples/complete-brownfield-cycle/README.md",
        "examples/complete-brownfield-cycle/SHAPING.md",
        "examples/complete-brownfield-cycle/PORTFOLIO.md",
        "examples/complete-brownfield-cycle/CONTRACT.md",
        "examples/complete-brownfield-cycle/PROGRESS.md",
        "examples/complete-brownfield-cycle/RESULT.md",
        "docs/goals/INDEX.md",
        "docs/goals/2026-08-26-interactive-shaping-first/SHAPING.md",
        "docs/goals/2026-08-26-interactive-shaping-first/CONTRACT.md",
        "docs/goals/2026-08-26-interactive-shaping-first/PROGRESS.md",
        "docs/goals/2026-08-26-interactive-shaping-first/UAT.md",
    )
    for path in required_paths:
        require(path)

    for path in (
        ".github/workflows/apply-zero-friction-update.yml",
        ".github/workflows/apply-final-specialist-review.yml",
        ".github/workflows/apply-overlay-validation-fix.yml",
        ".github/workflows/cleanup-final-review-branch.yml",
        ".github/workflows/apply-interactive-first.yml",
    ):
        require_absent(path)

    require_fragments(
        require("CURRENT_IMPLEMENTATION.md"),
        (
            "Version `0.7.0`",
            "shape-goal                    main interactive entry point",
            "question barrier",
            "Advanced preflight",
            "## Verification",
        ),
    )
    require_fragments(
        require("README.md"),
        (
            "**`shape-goal` is the main command.**",
            "## Quick start",
            "## Why shaping and execution are separate",
            "no Steer message required",
            "Pursuing goal",
            "## Advanced modes",
            "<!-- goal-catalog:start -->",
            "<!-- goal-catalog:end -->",
        ),
    )
    require_fragments(
        require("INSTALL.md"),
        (
            "without an active `/goal`",
            "If shaping is already trapped inside `/goal`",
            "$shape-goal Resume goal-id",
        ),
    )
    require_fragments(
        require("skills/shape-goal/references/input-resolution.md"),
        (
            "Question barrier",
            "## Ask one material decision at a time",
            "End the turn immediately",
            "never require a Steer message",
            "## Execution handoff after approval",
            "Do not execute it automatically",
        ),
    )
    require_fragments(
        require("skills/shape-goal/references/shaping-history.md"),
        (
            "## The question barrier",
            "The user should never need to use Steer",
            "one-question interactive turns",
            "Approval is itself recorded",
        ),
    )
    require_fragments(
        require("skills/shape-goal/templates/custom-contract-driven-goal.md"),
        (
            "## Recommended — interactive shaping",
            "/shape-goal Use a Custom Contract-Driven profile",
            "## Advanced — autonomous preflight",
            "Approval required",
        ),
    )
    require_fragments(
        require("skills/shape-goal/goal-contract-template.md"),
        (
            "**Launcher:**",
            "**Input ledger:**",
            "**Shaping history:**",
            "**Approval shaping round:**",
            "## Goal-drift review triggers",
        ),
    )
    require_fragments(
        require("skills/shape-goal/templates/shaping-history-template.md"),
        (
            "## Current decision index",
            "## Round R1",
            "**Exact question:**",
            "**User answer:**",
            "## Approval record",
            "## Corrections and supersessions",
        ),
    )
    require_fragments(
        require("skills/goal-engine/references/state-and-evidence.md"),
        ("Shaping history", "approval round", "├── SHAPING.md"),
    )
    require_fragments(
        require("examples/complete-brownfield-cycle/SHAPING.md"),
        ("R1-Q1", "R1-Q2", "R2-Q1", "R2-Q2", "Approval round:** R2"),
    )
    require_fragments(
        require("SOURCES.md"),
        (
            "ordinary interactive conversation",
            "another turn begins automatically",
            "stop as **Approval required**",
        ),
    )
    require_fragments(
        require("docs/goals/2026-08-26-interactive-shaping-first/SHAPING.md"),
        (
            "Main entry point",
            "Question behavior",
            "no additional owner question was necessary",
            "Approval round:** R1",
        ),
    )
    require_fragments(
        require("docs/goals/2026-08-26-interactive-shaping-first/CONTRACT.md"),
        (
            "The library uses `shape-goal` as the clear interactive entry point",
            "All 24 profile files expose interactive `shape-goal` commands first",
            "only `main` remains",
        ),
    )
    require_fragments(
        require("docs/goals/2026-08-26-interactive-shaping-first/UAT.md"),
        (
            "Scenario A — Normal interactive shaping",
            "Steer is not required",
            "Scenario C — Owner decision discovered during autonomous execution",
            "Honest boundary",
        ),
    )

    readme = require("README.md")
    if readme.exists() and len(readme.read_text(encoding="utf-8").splitlines()) > 230:
        fail("README.md is too long; keep the generated landing page at 230 lines or fewer")


def validate_generated_docs() -> None:
    try:
        launcher_docs = sync_goal_launchers.render()
    except Exception as error:  # noqa: BLE001
        fail(f"Could not render synchronized launchers: {error}")
        launcher_docs = {}
    for path, expected in launcher_docs.items():
        actual = path.read_text(encoding="utf-8") if path.exists() else ""
        if actual != expected:
            fail(
                f"{path.relative_to(ROOT)} is out of date; "
                "run python3 scripts/sync_goal_launchers.py --write"
            )

    try:
        documents = sync_goal_docs.render_documents()
    except Exception as error:  # noqa: BLE001
        fail(f"Could not render generated docs: {error}")
        return
    for path, expected in documents.items():
        actual = path.read_text(encoding="utf-8") if path.exists() else ""
        if actual != expected:
            fail(
                f"{path.relative_to(ROOT)} is out of date; "
                "run python3 scripts/sync_goal_docs.py --write"
            )


def normalize_link(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    target = re.split(r"\s+[\"']", target, maxsplit=1)[0]
    return unquote(target.split("#", 1)[0])


def validate_markdown_links() -> None:
    pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        source = path.read_text(encoding="utf-8")
        for match in pattern.finditer(source):
            raw_target = match.group(1)
            target = normalize_link(raw_target)
            if not target or target.startswith(
                ("http://", "https://", "mailto:", "data:", "tel:")
            ):
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
    if not workflow.exists():
        return
    source = workflow.read_text(encoding="utf-8")
    for line in source.splitlines():
        if "uses:" not in line:
            continue
        if not ACTION_PIN.search(line.strip()):
            fail(
                ".github/workflows/validate.yml: action is not pinned to a full commit SHA: "
                f"{line.strip()}"
            )
    for fragment in (
        "fetch-depth: 0",
        "skills@1.5.23",
        "scripts/sync_goal_launchers.py --check",
        "scripts/sync_goal_docs.py --check",
        "scripts/validate_shaping_history_diff.py --self-test",
        "scripts/package_skills.py",
        "scripts/validate_repository.py",
    ):
        if fragment not in source:
            fail(f".github/workflows/validate.yml: missing {fragment!r}")


def main() -> int:
    version = validate_version()
    catalog = load_catalog()
    goals = validate_catalog(catalog)
    validate_goal_files(goals)
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
    print("- shape-goal is the interactive main entry point")
    print("- 2 portable skills with host metadata")
    print("- 29 interactive profile start commands")
    print("- 29 advanced autonomous preflights")
    print("- 29 advanced self-contained preflights")
    print("- question barrier and normal-reply workflow enforced")
    print("- 7 core, 8 specialist, and 14 quality profiles")
    print("- append-only shaping history and explicit approval")
    print("- multi-goal portfolio, project harness, and reusable closeout")
    print("- synchronized launchers and generated catalogs")
    print("- GitHub Actions pinned to immutable commits")
    print("- local Markdown links resolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
