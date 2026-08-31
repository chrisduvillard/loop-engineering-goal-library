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
import validate_goal_archives  # noqa: E402
import validate_question_state  # noqa: E402
import validate_tooling_contract  # noqa: E402

ERRORS: list[str] = []
PLACEHOLDER = re.compile(r"\[[A-Z][A-Z0-9 _/.,:+-]{2,}\]")
ACTION_PIN = re.compile(r"uses:\s+[^@\s]+@([0-9a-f]{40})(?:\s+#.*)?$")
SEMVER = re.compile(
    r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
)
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
    "AI Quality & Safety",
    "Internationalization & Localization",
    "Search & Discoverability",
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
    seen_top: set[str] = set()
    seen_metadata: set[str] = set()
    in_metadata = False
    for raw_line in parts[1].splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if "\t" in raw_line[: len(raw_line) - len(raw_line.lstrip())]:
            fail(f"{path.relative_to(ROOT)}: tabs are not allowed in skill frontmatter")
        if raw_line.startswith(("  ", "\t")):
            if not in_metadata or ":" not in raw_line:
                fail(f"{path.relative_to(ROOT)}: unsupported nested frontmatter line {raw_line!r}")
                continue
            key, value = raw_line.strip().split(":", 1)
            key = key.strip()
            if key in seen_metadata:
                fail(f"{path.relative_to(ROOT)}: duplicate metadata key {key!r}")
            seen_metadata.add(key)
            metadata[key] = unquote_yaml(value)
            continue
        in_metadata = False
        if ":" not in raw_line:
            fail(f"{path.relative_to(ROOT)}: malformed frontmatter line {raw_line!r}")
            continue
        key, value = raw_line.split(":", 1)
        key = key.strip()
        if key in seen_top:
            fail(f"{path.relative_to(ROOT)}: duplicate frontmatter key {key!r}")
        seen_top.add(key)
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
    if not SEMVER.fullmatch(version):
        fail(f"VERSION is not semantic: {version!r}")
    changelog = text("CHANGELOG.md")
    if version and f"## [{version}]" not in changelog:
        fail(f"CHANGELOG.md has no section for VERSION {version}")
    readme = text("README.md")
    expected_badge = (
        f"![Version](https://img.shields.io/badge/version-{version}-7C3AED?style=flat-square)"
    )
    if version and expected_badge not in readme:
        fail(f"README.md version badge does not match VERSION {version}")
    current = text("CURRENT_IMPLEMENTATION.md")
    if version and f"## Version `{version}`" not in current:
        fail(f"CURRENT_IMPLEMENTATION.md does not describe VERSION {version}")
    return version

def load_catalog() -> dict:
    source = text("goals/catalog.json")
    try:
        return json.loads(source) if source else {"categories": [], "goals": []}
    except json.JSONDecodeError as error:
        fail(f"goals/catalog.json is invalid JSON: {error}")
        return {"categories": [], "goals": []}


def validate_catalog(catalog: dict) -> list[dict]:
    if not isinstance(catalog, dict):
        fail("goals/catalog.json: root must be an object")
        return []
    if catalog.get("schema_version") != 1:
        fail("goals/catalog.json: schema_version must be 1")

    categories = catalog.get("categories", [])
    goals = catalog.get("goals", [])
    if not isinstance(categories, list) or not isinstance(goals, list):
        fail("goals/catalog.json: categories and goals must be arrays")
        return []

    category_keys = [item.get("key") if isinstance(item, dict) else None for item in categories]
    expected_order = ["core", "specialist", "quality"]
    if category_keys != expected_order:
        fail(f"Unexpected category order: {category_keys}")

    counts = {key: 0 for key in expected_order}
    seen_ids: set[str] = set()
    seen_files: set[str] = set()

    for index, item in enumerate(goals, start=1):
        if not isinstance(item, dict):
            fail(f"Catalog goal {index}: entry must be an object")
            continue
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

    if not goals:
        fail("Goal catalog must contain at least one profile")
    for category, count in counts.items():
        if count == 0:
            fail(f"Goal catalog category {category!r} must not be empty")

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
    return [item for item in goals if isinstance(item, dict)]

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
        if top.get("user-invocable") != "true":
            fail(f"{rel}: user-invocable must be true")
        if top.get("disable-model-invocation") != "true":
            fail(f"{rel}: disable-model-invocation must be true")
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
                "allow_implicit_invocation: false",
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
            "references/question-quality.md",
            "no material ambiguity",
            "answer quality gate",
            "prompt-injection",
            "without symlink traversal",
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
            "prompt-injection",
            "execution lease",
            "shaping history",
        ):
            if fragment.lower() not in source:
                fail(f"{engine.relative_to(ROOT)}: missing {fragment!r}")


def validate_state_and_docs(version: str) -> None:
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
        "skills/shape-goal/references/question-quality.md",
        "skills/shape-goal/references/profile-inputs.md",
        "skills/shape-goal/references/shaping-history.md",
        "skills/shape-goal/templates/shaping-history-template.md",
        "skills/shape-goal/templates/goal-portfolio-template.md",
        "skills/shape-goal/templates/custom-contract-driven-goal.md",
        "skills/goal-engine/SKILL.md",
        "skills/goal-engine/references/loop-profiles.md",
        "skills/goal-engine/references/assurance-overlays.md",
        "skills/goal-engine/references/state-and-evidence.md",
        "skills/goal-engine/references/specialist-reviewers.md",
        "skills/goal-engine/templates/project-harness-template.md",
        "skills/goal-engine/templates/goal-progress-template.md",
        "skills/goal-engine/templates/goal-result-template.md",
        "skills/goal-engine/templates/goal-history-index-template.md",
        "scripts/package_skills.py",
        "scripts/sync_goal_docs.py",
        "scripts/sync_goal_launchers.py",
        "scripts/validate_shaping_history_diff.py",
        "scripts/validate_question_state.py",
        "scripts/validate_goal_archives.py",
        "scripts/validate_tooling_contract.py",
        "scripts/validate_repository.py",
        "tests/test_adversarial_robustness.py",
        "tests/test_adversarial_second_pass.py",
        "tests/test_specialist_audit_regressions.py",
        "docs/ROBUSTNESS_AUDIT.md",
        "docs/SPECIALIST_AUDIT.md",
        "docs/audits/2026-08-27-specialist-review/README.md",
        "docs/audits/2026-08-27-specialist-review/contract-state.md",
        "docs/audits/2026-08-27-specialist-review/agent-control.md",
        "docs/audits/2026-08-27-specialist-review/security-supply-chain.md",
        "docs/audits/2026-08-27-specialist-review/tooling-portability.md",
        "docs/audits/2026-08-27-specialist-review/verification-mutation.md",
        "docs/audits/2026-08-27-specialist-review/documentation-adoption.md",
        "package.json",
        "package-lock.json",
        "docs/goals/2026-08-26-adversarial-robustness/SHAPING.md",
        "docs/goals/2026-08-26-adversarial-robustness/CONTRACT.md",
        "docs/goals/2026-08-26-adversarial-robustness/PROGRESS.md",
        "docs/goals/2026-08-26-adversarial-robustness/UAT.md",
        "docs/goals/2026-08-26-adversarial-robustness/RESULT.md",
        "docs/goals/2026-08-27-specialist-audit/SHAPING.md",
        "docs/goals/2026-08-27-specialist-audit/CONTRACT.md",
        "docs/goals/2026-08-27-specialist-audit/PROGRESS.md",
        "docs/goals/2026-08-27-specialist-audit/UAT.md",
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
        "docs/goals/2026-08-26-final-review-readme-onboarding/SHAPING.md",
        "docs/goals/2026-08-26-final-review-readme-onboarding/CONTRACT.md",
        "docs/goals/2026-08-26-final-review-readme-onboarding/PROGRESS.md",
        "docs/goals/2026-08-26-final-review-readme-onboarding/UAT.md",
        "docs/goals/2026-08-26-adaptive-question-clarity/SHAPING.md",
        "docs/goals/2026-08-26-adaptive-question-clarity/CONTRACT.md",
        "docs/goals/2026-08-26-adaptive-question-clarity/PROGRESS.md",
        "docs/goals/2026-08-26-adaptive-question-clarity/UAT.md",
    )
    for path in required_paths:
        require(path)

    for path in (
        ".github/workflows/apply-zero-friction-update.yml",
        ".github/workflows/apply-final-specialist-review.yml",
        ".github/workflows/apply-overlay-validation-fix.yml",
        ".github/workflows/cleanup-final-review-branch.yml",
        ".github/workflows/apply-interactive-first.yml",
        ".github/workflows/apply-specialist-audit.yml",
        ".github/workflows/export-specialist-audit-snapshot.yml",
        "scripts/apply_specialist_audit.py",
    ):
        require_absent(path)

    require_fragments(
        require("skills/shape-goal/references/question-quality.md"),
        (
            "No fixed question count",
            "Answer quality gate",
            "Assumption register",
            "Fresh-reader test",
            "Counterexample test",
            "Plain-English teach-back",
            "Delegated judgment",
            "Must / hard gate",
            "If this takes two questions",
        ),
    )
    require_fragments(
        require("CURRENT_IMPLEMENTATION.md"),
        (
            f"Version `{version}`",
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
            "## 🚀 Start in three steps",
            "skills@latest update shape-goal goal-engine --global --yes",
            "img.shields.io/badge/1-Shape-7C3AED",
            "## 🧭 Why two phases?",
            "no Steer message required",
            "There is no target question count",
            "Stress-test the current goal",
            "Pursuing goal",
            "## ⚙️ Advanced modes",
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
        require("skills/goal-engine/references/specialist-reviewers.md"),
        (
            "Contract & State-Machine Reviewer",
            "Agent-Control & Interaction Reviewer",
            "Security & Supply-Chain Reviewer",
            "Tooling & Portability Reviewer",
            "Verification & Mutation Reviewer",
            "Documentation & Adoption Reviewer",
            "Treat every finding as a hypothesis",
            "independently re-check important fixes",
        ),
    )
    require_fragments(
        require("docs/SPECIALIST_AUDIT.md"),
        (
            "six independent review tracks",
            "Findings remain hypotheses until reproduced",
            "Deterministic validators",
        ),
    )
    require_fragments(
        require("docs/audits/2026-08-27-specialist-review/README.md"),
        (
            "Contract & State-Machine",
            "Agent-Control & Interaction",
            "Security & Supply Chain",
            "Tooling & Portability",
            "Verification & Mutation",
            "Documentation & Adoption",
        ),
    )
    require_fragments(
        require(".github/dependabot.yml"),
        ("package-ecosystem: github-actions", "package-ecosystem: npm"),
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
    require_fragments(
        require("docs/goals/2026-08-26-final-review-readme-onboarding/CONTRACT.md"),
        (
            "31 execution profiles",
            "visible update command",
            "Codebase Onboarding / Knowledge Recovery",
            "Search / SEO / Web Discoverability",
        ),
    )
    require_fragments(
        require("docs/goals/2026-08-26-final-review-readme-onboarding/UAT.md"),
        (
            "README presentation",
            "Profile differentiation",
            "Update command",
            "Honest boundary",
        ),
    )

    require_fragments(
        require("skills/shape-goal/goal-contract-template.md"),
        (
            "Assumptions and interpretation register",
            "Clarity stress test",
            "Pre-approval clarity gate",
            "Approval fingerprint",
            "Execution lease",
        ),
    )
    require_fragments(
        require("skills/shape-goal/templates/shaping-history-template.md"),
        (
            "Answer quality",
            "Clarity audit",
            "Assumption class",
        ),
    )
    readme = require("README.md")
    if readme.exists() and len(readme.read_text(encoding="utf-8").splitlines()) > 235:
        fail("README.md is too long; keep the generated landing page at 235 lines or fewer")


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
        if any(part in {"node_modules", "dist", "build", "__pycache__", ".venv", "venv", ".tox", ".nox", ".pytest_cache", ".mypy_cache", ".ruff_cache"} for part in path.parts):
            continue
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


def validate_tree_hygiene() -> None:
    text_suffixes = {".md", ".py", ".json", ".yml", ".yaml", ".txt", ".toml"}
    for path in ROOT.rglob("*"):
        if any(part in {".git", "dist", "build", "node_modules", "__pycache__", ".venv", "venv", ".tox", ".nox", ".pytest_cache", ".mypy_cache", ".ruff_cache"} for part in path.parts):
            continue
        if path.is_symlink():
            fail(f"{path.relative_to(ROOT)}: repository symlinks are not allowed")
            continue
        if not path.is_file():
            continue
        if path.stat().st_size > 2 * 1024 * 1024 and any(part in {"skills", "scripts", "goals", "tests"} for part in path.parts):
            fail(f"{path.relative_to(ROOT)}: unexpectedly large source file")
        if path.suffix.lower() in text_suffixes:
            try:
                content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError as error:
                fail(f"{path.relative_to(ROOT)}: invalid UTF-8: {error}")
                continue
            if "\x00" in content:
                fail(f"{path.relative_to(ROOT)}: NUL byte in text file")


def validate_package_manifest() -> None:
    try:
        package = json.loads(text("package.json"))
        lock = json.loads(text("package-lock.json"))
    except (json.JSONDecodeError, TypeError) as error:
        fail(f"npm package metadata is invalid: {error}")
        return
    if not isinstance(package, dict) or not isinstance(lock, dict):
        fail("npm package metadata must use JSON objects")
        return

    if package.get("name") != "loop-engineering-goal-library" or package.get("private") is not True:
        fail("package.json must remain the private loop-engineering-goal-library package")
    expected = package.get("devDependencies", {}).get("skills")
    if not isinstance(expected, str) or not SEMVER.fullmatch(expected):
        fail("package.json must pin skills to one exact semantic version")
        return
    if package.get("scripts") != {"test": "python -m unittest discover -s tests -v"}:
        fail("package.json may contain only the reviewed test script")
    if lock.get("lockfileVersion") != 3:
        fail("package-lock.json must use lockfileVersion 3")
    packages = lock.get("packages")
    if not isinstance(packages, dict):
        fail("package-lock.json packages must be an object")
        return

    root_package = packages.get("", {})
    skills_package = packages.get("node_modules/skills", {})
    if root_package.get("devDependencies", {}).get("skills") != expected:
        fail("package-lock.json root dependency does not match package.json")
    expected_tarball = f"https://registry.npmjs.org/skills/-/skills-{expected}.tgz"
    if (
        skills_package.get("version") != expected
        or skills_package.get("resolved") != expected_tarball
        or not skills_package.get("integrity")
    ):
        fail(f"package-lock.json must pin skills {expected} with matching provenance and integrity")

    for package_path, entry in packages.items():
        if package_path == "":
            continue
        if not isinstance(entry, dict):
            fail(f"package-lock.json entry {package_path!r} must be an object")
            continue
        version = entry.get("version")
        resolved = entry.get("resolved")
        integrity = entry.get("integrity")
        if not isinstance(version, str) or not version:
            fail(f"package-lock.json entry {package_path!r} has no version")
        if not isinstance(resolved, str) or not resolved.startswith("https://registry.npmjs.org/"):
            fail(f"package-lock.json entry {package_path!r} must resolve from the npm registry over HTTPS")
        if not isinstance(integrity, str) or not integrity.startswith("sha512-"):
            fail(f"package-lock.json entry {package_path!r} must have a sha512 integrity hash")
        if entry.get("dev") is not True:
            fail(f"package-lock.json entry {package_path!r} must remain development-only")
        if entry.get("hasInstallScript") is True:
            fail(f"package-lock.json entry {package_path!r} may not declare an install script")

def validate_scripts_and_ci() -> None:
    for path in sorted(list((ROOT / "scripts").glob("*.py")) + list((ROOT / "tests").glob("*.py"))):
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except SyntaxError as error:
            fail(f"{path.relative_to(ROOT)}: syntax error: {error}")

    workflow_dir = require(".github/workflows")
    workflows = sorted(set(workflow_dir.glob("*.yml")) | set(workflow_dir.glob("*.yaml"))) if workflow_dir.exists() else []
    if [path.name for path in workflows] != ["validate.yml"]:
        fail(f"Only the permanent read-only validate.yml workflow may be committed: {[path.name for path in workflows]}")
    workflow = require(".github/workflows/validate.yml")
    if not workflow.exists():
        return
    source = workflow.read_text(encoding="utf-8")
    if "concurrency:" not in source or "cancel-in-progress: true" not in source:
        fail(".github/workflows/validate.yml: superseded runs must be cancelled")
    if "contents: read" not in source:
        fail(".github/workflows/validate.yml: contents permission must remain read-only")
    if re.search(r"^\s*[A-Za-z-]+:\s*write(?:-all)?\s*$", source, flags=re.MULTILINE):
        fail(".github/workflows/validate.yml: write permission is forbidden")
    if re.search(r"^\s*permissions:\s*\{[^}]*\bwrite(?:-all)?\b", source, flags=re.MULTILINE):
        fail(".github/workflows/validate.yml: inline write permission is forbidden")
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
        "npm ci --ignore-scripts",
        "npx --no-install skills",
        "scripts/sync_goal_launchers.py --check",
        "scripts/sync_goal_docs.py --check",
        "scripts/validate_shaping_history_diff.py --self-test",
        "scripts/validate_question_state.py --self-test",
        "scripts/validate_goal_archives.py --self-test",
        "scripts/validate_tooling_contract.py --self-test",
        "scripts/package_skills.py",
        "scripts/validate_repository.py",
        "python -m unittest discover -s tests -v",
    ):
        if fragment not in source:
            fail(f".github/workflows/validate.yml: missing {fragment!r}")


def main() -> int:
    version = validate_version()
    try:
        catalog = load_catalog()
        goals = validate_catalog(catalog)
    except Exception as error:  # noqa: BLE001
        fail(f"Catalog validation crashed safely: {error}")
        goals = []
    validate_goal_files(goals)
    validate_skills(version)
    validate_state_and_docs(version)
    validate_generated_docs()
    validate_markdown_links()
    validate_tree_hygiene()
    validate_package_manifest()
    validate_scripts_and_ci()
    for error in validate_question_state.validate(""):
        fail(f"Question-state contract: {error}")
    for error in validate_goal_archives.validate():
        fail(f"Goal-archive contract: {error}")
    for error in validate_tooling_contract.validate():
        fail(f"Tooling contract: {error}")

    if ERRORS:
        print("Repository validation failed:\n")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print("Repository validation passed.")
    print(f"- version {version}")
    print("- shape-goal is the interactive main entry point")
    print("- 2 portable skills with host metadata")
    category_counts = {key: 0 for key in ("core", "specialist", "quality")}
    for item in goals:
        category = item.get("category")
        if category in category_counts:
            category_counts[category] += 1
    print(f"- {len(goals)} interactive profile start commands")
    print(f"- {len(goals)} advanced autonomous preflights")
    print(f"- {len(goals)} advanced self-contained preflights")
    print("- question barrier and normal-reply workflow enforced")
    print(
        f"- {category_counts['core']} core, {category_counts['specialist']} specialist, "
        f"and {category_counts['quality']} quality profiles"
    )
    print("- 12 assurance overlays")
    print("- append-only shaping history and explicit approval")
    print("- multi-goal portfolio, project harness, and reusable closeout")
    print("- synchronized launchers and generated catalogs")
    print("- GitHub Actions pinned to immutable commits")
    print("- local Markdown links resolve")
    print("- adversarial mutation tests and repository hygiene are enforced")
    print("- locked transitive dependencies, strict frontmatter, and archive-source parity are enforced")
    print("- shaping question state, goal archives, and tooling controls have deterministic validators")
    print("- six isolated specialist reviewer roles are available for high-impact audits")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
