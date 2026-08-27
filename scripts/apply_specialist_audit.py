#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.11.0"
DATE = "2026-08-27"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8", newline="\n")


def replace_once(path: str, old: str, new: str) -> None:
    source = read(path)
    count = source.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one occurrence of {old!r}, found {count}")
    write(path, source.replace(old, new, 1))


def replace_function(path: str, name: str, next_name: str, replacement: str) -> None:
    source = read(path)
    start = source.index(f"def {name}(")
    end = source.index(f"\n\ndef {next_name}(", start)
    write(path, source[:start] + replacement.rstrip() + source[end:])


write("VERSION", VERSION + "\n")
for path in ("skills/shape-goal/SKILL.md", "skills/goal-engine/SKILL.md"):
    source = read(path)
    source, count = re.subn(
        r'(?m)^  version: "0\.10\.0"$', f'  version: "{VERSION}"', source
    )
    if count != 1:
        raise RuntimeError(f"{path}: could not update metadata version")
    write(path, source)

replace_once(
    "skills/goal-engine/SKILL.md",
    "Use fresh review or isolated subagents for high-blast-radius, security, authorization, migration, concurrency, reliability, architecture, compliance, accessibility, or subjective visual changes when practical.\n\nProvide the reviewer the contract, relevant shaping decisions, diff, evidence, and overlays—not the implementer's persuasive narrative. Treat findings as hypotheses until verified.",
    "Use fresh review or isolated subagents for high-blast-radius, security, authorization, migration, concurrency, reliability, architecture, compliance, accessibility, or subjective visual changes when practical. For broad audits, apply the six-role protocol in [references/specialist-reviewers.md](references/specialist-reviewers.md).\n\nProvide each reviewer the contract, relevant shaping decisions, diff, evidence, and overlays—not the implementer's persuasive narrative or another reviewer's conclusions. Treat findings as hypotheses until verified, consolidate by root cause, and independently re-check important fixes.",
)

replace_once(
    "README.md",
    "<!-- goal-catalog:start -->",
    "> [!TIP]\n> Running a high-impact audit? Use the isolated [specialist reviewer team](skills/goal-engine/references/specialist-reviewers.md): contract/state, agent control, security, portability, verification, and documentation.\n\n<!-- goal-catalog:start -->",
)

replace_once("CURRENT_IMPLEMENTATION.md", "## Version `0.10.0`", f"## Version `{VERSION}`")
replace_once(
    "CURRENT_IMPLEMENTATION.md",
    "31 execution profiles         reusable loop shapes\n12 assurance overlays         extra proof when a concern is secondary\ngoal-engine                   autonomous brownfield execution",
    "31 execution profiles         reusable loop shapes\n12 assurance overlays         extra proof when a concern is secondary\nspecialist reviewer team      six isolated audit roles with evidence-based consolidation\ngoal-engine                   autonomous brownfield execution",
)
replace_once(
    "CURRENT_IMPLEMENTATION.md",
    "## Verification\n\nCI validates",
    "## Specialist review\n\nHigh-impact audits can use six isolated reviewer roles covering contract/state, agent control, security/supply chain, portability, verification, and documentation/adoption. Findings use one evidence schema, remain hypotheses until reproduced, and important fixes receive independent re-review. See [`skills/goal-engine/references/specialist-reviewers.md`](skills/goal-engine/references/specialist-reviewers.md).\n\n## Verification\n\nCI validates",
)
replace_once("ROADMAP.md", "## Implemented through `0.10.0`", f"## Implemented through `{VERSION}`")
replace_once(
    "CHANGELOG.md",
    "## [Unreleased]\n\n- Reserved for changes after the current release.\n",
    f"""## [Unreleased]

- Reserved for changes after the current release.

## [{VERSION}] - {DATE}

### Added

- A reusable six-role specialist-review protocol for contract/state, agent-control, security/supply-chain, portability, verification, and documentation/adoption audits.
- Regression tests for generated README version metadata, dynamic catalog accounting, dependency-pin consistency, reviewer-protocol discoverability, and npm Dependabot coverage.
- Durable specialist-audit findings and closeout records.

### Changed

- README version metadata is generated from `VERSION`, preventing the public badge from drifting behind the released skills.
- Repository validation derives profile totals from the canonical catalog instead of freezing release-specific counts.
- Skills CLI validation derives the exact pin from `package.json` and verifies lockfile consistency and registry provenance instead of hardcoding one historical version.
- Dependabot now reviews npm dependencies as well as GitHub Actions.
- `goal-engine` routes broad audits through isolated evidence-based reviewers and independent re-review of important fixes.
""",
)

write(
    ".github/dependabot.yml",
    """version: 2
updates:
  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: weekly
    open-pull-requests-limit: 5
    labels:
      - dependencies
      - github-actions

  - package-ecosystem: npm
    directory: /
    schedule:
      interval: weekly
    open-pull-requests-limit: 5
    labels:
      - dependencies
      - npm
""",
)

replace_once(
    "scripts/sync_goal_docs.py",
    'CATALOG_PATH = ROOT / "goals" / "catalog.json"\nREADME_START',
    'CATALOG_PATH = ROOT / "goals" / "catalog.json"\nVERSION_PATH = ROOT / "VERSION"\nREADME_START',
)
replace_once(
    "scripts/sync_goal_docs.py",
    'PROFILE_BADGE = re.compile(\n    r"!\\[Profiles\\]\\(https://img\\.shields\\.io/badge/profiles-\\d+-16A34A\\?style=flat-square\\)"\n)\nCOMMAND',
    'VERSION_BADGE = re.compile(\n    r"!\\[Version\\]\\(https://img\\.shields\\.io/badge/version-[^)]*-7C3AED\\?style=flat-square\\)"\n)\nPROFILE_BADGE = re.compile(\n    r"!\\[Profiles\\]\\(https://img\\.shields\\.io/badge/profiles-\\d+-16A34A\\?style=flat-square\\)"\n)\nSEMVER = re.compile(\n    r"(?:0|[1-9]\\d*)\\.(?:0|[1-9]\\d*)\\.(?:0|[1-9]\\d*)"\n    r"(?:-[0-9A-Za-z-]+(?:\\.[0-9A-Za-z-]+)*)?"\n    r"(?:\\+[0-9A-Za-z-]+(?:\\.[0-9A-Za-z-]+)*)?"\n)\nCOMMAND',
)
replace_once(
    "scripts/sync_goal_docs.py",
    'def render_documents() -> dict[Path, str]:\n    catalog = load_catalog()\n    parsed = validate_catalog(catalog)\n    documents: dict[Path, str] = {}',
    'def render_documents() -> dict[Path, str]:\n    catalog = load_catalog()\n    parsed = validate_catalog(catalog)\n    version = VERSION_PATH.read_text(encoding="utf-8").strip()\n    if not SEMVER.fullmatch(version):\n        raise ValueError(f"VERSION is not semantic: {version!r}")\n    documents: dict[Path, str] = {}',
)
replace_once(
    "scripts/sync_goal_docs.py",
    '    readme = readme_path.read_text(encoding="utf-8")\n    readme, count = PROFILE_BADGE.subn(',
    '    readme = readme_path.read_text(encoding="utf-8")\n    version_badge = f"![Version](https://img.shields.io/badge/version-{version}-7C3AED?style=flat-square)"\n    readme, version_count = VERSION_BADGE.subn(version_badge, readme)\n    if version_count != 1:\n        raise ValueError(\n            f"README.md must contain exactly one generated Version badge, found {version_count}"\n        )\n    readme, count = PROFILE_BADGE.subn(',
)

replace_function(
    "scripts/validate_repository.py",
    "validate_version",
    "load_catalog",
    '''def validate_version() -> str:
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
    return version''',
)
replace_function(
    "scripts/validate_repository.py",
    "validate_catalog",
    "extract_commands",
    '''def validate_catalog(catalog: dict) -> list[dict]:
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
    return [item for item in goals if isinstance(item, dict)]''',
)
replace_function(
    "scripts/validate_repository.py",
    "validate_package_manifest",
    "validate_scripts_and_ci",
    '''def validate_package_manifest() -> None:
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
            fail(f"package-lock.json entry {package_path!r} may not declare an install script")''',
)

replace_once(
    "scripts/validate_repository.py",
    '        "skills/goal-engine/references/state-and-evidence.md",\n',
    '        "skills/goal-engine/references/state-and-evidence.md",\n        "skills/goal-engine/references/specialist-reviewers.md",\n',
)
replace_once(
    "scripts/validate_repository.py",
    '        "tests/test_adversarial_second_pass.py",\n',
    '        "tests/test_adversarial_second_pass.py",\n        "tests/test_specialist_audit_regressions.py",\n',
)
replace_once(
    "scripts/validate_repository.py",
    '        "docs/goals/2026-08-26-adversarial-robustness/UAT.md",\n',
    '        "docs/goals/2026-08-26-adversarial-robustness/UAT.md",\n        "docs/goals/2026-08-26-adversarial-robustness/RESULT.md",\n        "docs/goals/2026-08-27-specialist-audit/SHAPING.md",\n        "docs/goals/2026-08-27-specialist-audit/CONTRACT.md",\n        "docs/goals/2026-08-27-specialist-audit/PROGRESS.md",\n        "docs/goals/2026-08-27-specialist-audit/UAT.md",\n',
)
replace_once(
    "scripts/validate_repository.py",
    '            "Version `0.10.0`",',
    f'            "Version `{VERSION}`",',
)
needle = '''    require_fragments(
        require("skills/goal-engine/references/state-and-evidence.md"),
        ("Shaping history", "approval round", "├── SHAPING.md"),
    )
'''
addition = needle + '''    require_fragments(
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
        require(".github/dependabot.yml"),
        ("package-ecosystem: github-actions", "package-ecosystem: npm"),
    )
'''
replace_once("scripts/validate_repository.py", needle, addition)
replace_once(
    "scripts/validate_repository.py",
    '    print("- 31 interactive profile start commands")\n    print("- 31 advanced autonomous preflights")\n    print("- 31 advanced self-contained preflights")\n    print("- question barrier and normal-reply workflow enforced")\n    print("- 7 core, 9 specialist, and 15 quality profiles")',
    '    category_counts = {key: 0 for key in ("core", "specialist", "quality")}\n    for item in goals:\n        category = item.get("category")\n        if category in category_counts:\n            category_counts[category] += 1\n    print(f"- {len(goals)} interactive profile start commands")\n    print(f"- {len(goals)} advanced autonomous preflights")\n    print(f"- {len(goals)} advanced self-contained preflights")\n    print("- question barrier and normal-reply workflow enforced")\n    print(\n        f"- {category_counts[\'core\']} core, {category_counts[\'specialist\']} specialist, "\n        f"and {category_counts[\'quality\']} quality profiles"\n    )',
)

print("Applied specialist audit improvements")
