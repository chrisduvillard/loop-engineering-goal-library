#!/usr/bin/env python3
"""Apply the final specialist-review changes, then remove this one-time script."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def replace(text: str, old: str, new: str, *, label: str) -> str:
    if old not in text:
        raise ValueError(f"{label}: expected text not found: {old[:100]!r}")
    return text.replace(old, new, 1)


def insert_before(text: str, marker: str, addition: str, *, label: str) -> str:
    if addition.strip() in text:
        return text
    if marker not in text:
        raise ValueError(f"{label}: marker not found: {marker!r}")
    return text.replace(marker, addition.rstrip() + "\n\n" + marker, 1)


# Catalog: two genuinely distinct primary control loops.
catalog_path = "goals/catalog.json"
catalog = json.loads(read(catalog_path))
quality = next(item for item in catalog["categories"] if item["key"] == "quality")
quality["intro"] = (
    "Eleven focused loops for frontend, documentation, security, reliability, APIs, operations, "
    "developer experience, data quality, test/CI health, infrastructure/deployment, and audit readiness."
)
new_goals = [
    {
        "id": "23",
        "file": "23-test-suite-ci-health.md",
        "title": "Test Suite / CI Health",
        "category": "quality",
        "simple": "Find flaky, misleading, slow, skipped, or environment-dependent checks and turn the test pipeline into reliable evidence.",
        "use_when": "Automated tests and CI must become trustworthy, deterministic, appropriately fast, and consistent with local development.",
    },
    {
        "id": "24",
        "file": "24-infrastructure-deployment-readiness.md",
        "title": "Infrastructure / Deployment Readiness",
        "category": "quality",
        "simple": "Verify that the system can be provisioned and deployed consistently, diagnosed after rollout, and safely rolled back before a human authorizes production change.",
        "use_when": "Infrastructure, environment configuration, deployment automation, smoke checks, and rollback must be proven ready without silently changing production.",
    },
]
known = {item["id"] for item in catalog["goals"]}
for item in new_goals:
    if item["id"] not in known:
        catalog["goals"].append(item)
write(catalog_path, json.dumps(catalog, indent=2, ensure_ascii=False) + "\n")

# Profile-specific shaping inputs.
profile_path = "skills/shape-goal/references/profile-inputs.md"
profile = read(profile_path)
profile_addition = """## 23. Test Suite / CI Health

**Use for:** Automated tests and CI must become trustworthy, deterministic, appropriately fast, and consistent with local development.

**Required profile inputs**

- Test and CI topology, owners, supported environments, and required gates
- Flake rate, failure classes, skipped or quarantined coverage, runtime, and feedback targets
- Reproduction protocol, fixtures, caches, services, retries, parallelism, and isolation boundaries
- Local/CI parity, diagnostic quality, completion evidence, and forbidden verifier weakening

**Suggested overlays:** Reliability & Recovery, Documentation & Knowledge Transfer, Performance & Cost

**Execution emphasis**

- Treat the test pipeline as an evidence system, not merely a command that should turn green.
- Reproduce and classify flaky, misleading, slow, skipped, or environment-dependent checks.
- Fix root causes, preserve required coverage, and prove clean local/CI parity repeatedly.

## 24. Infrastructure / Deployment Readiness

**Use for:** Infrastructure, environment configuration, deployment automation, smoke checks, and rollback must be proven ready without silently changing production.

**Required profile inputs**

- Target environments, infrastructure scope, ownership, dependencies, and parity expectations
- Infrastructure-as-code, configuration, secret-reference, artifact, migration, and pipeline sources of truth
- Provisioning validation, smoke/health checks, observability, failure scenarios, and rollback evidence
- Production authority, maintenance/change windows, residual-risk policy, and readiness criteria

**Suggested overlays:** Reliability & Recovery, Operability & Observability, Security & Privacy, Compatibility & Portability

**Execution emphasis**

- Reconcile infrastructure and application assumptions as one deployment surface.
- Validate through approved non-production, ephemeral, dry-run, or simulated environments.
- Prove artifacts, configuration, migrations, health signals, failure handling, and rollback without silently exercising production authority.
"""
profile = insert_before(profile, "## Custom Contract-Driven", profile_addition, label=profile_path)
write(profile_path, profile)

# Execution profiles.
loop_path = "skills/goal-engine/references/loop-profiles.md"
loop = read(loop_path)
loop_addition = """## 23. Test Suite / CI Health

**Use for:** Making automated tests and CI reliable evidence rather than a flaky, slow, or misleading gate.

- Map suites, environments, fixtures, services, retries, skips, quarantines, caches, and workflow dependencies.
- Reproduce and classify flakes, false positives/negatives, hidden skips, isolation failures, and local/CI drift.
- Fix root causes without weakening required assertions or silently excluding difficult coverage.
- Finish only after repeated clean runs meet the approved determinism, runtime, diagnostic, coverage, and parity gates.

## 24. Infrastructure / Deployment Readiness

**Use for:** Proving infrastructure and deployment mechanics ready without performing an unauthorized production rollout.

- Reconcile infrastructure-as-code, configuration, artifacts, migrations, application assumptions, and environment differences.
- Validate provisioning and deployment stages in approved non-production, ephemeral, dry-run, or simulated environments.
- Exercise smoke checks, health signals, failure handling, observability, and rollback together.
- Finish at evidence-backed readiness; never provision or mutate production without explicit contract authority.
"""
loop = insert_before(loop, "## Custom Contract-Driven", loop_addition, label=loop_path)
write(loop_path, loop)

# Dedicated-profile guidance.
overlay_path = "skills/goal-engine/references/assurance-overlays.md"
overlays = read(overlay_path)
overlays = replace(
    overlays,
    "| Dataset or pipeline quality | Data Quality / Pipeline Assurance | Data Integrity & Governance |\n| Technical audit evidence | Compliance / Audit Readiness | Compliance & Auditability |",
    "| Dataset or pipeline quality | Data Quality / Pipeline Assurance | Data Integrity & Governance |\n"
    "| Automated test and CI trust | Test Suite / CI Health | Reliability, documentation, or performance overlays |\n"
    "| Infrastructure and deployment readiness | Infrastructure / Deployment Readiness | Reliability, operability, security, or compatibility overlays |\n"
    "| Technical audit evidence | Compliance / Audit Readiness | Compliance & Auditability |",
    label=overlay_path,
)
write(overlay_path, overlays)

# Version and skill metadata.
write("VERSION", "0.5.0\n")
for skill in ("skills/shape-goal/SKILL.md", "skills/goal-engine/SKILL.md"):
    text = read(skill).replace('version: "0.4.0"', 'version: "0.5.0"', 1)
    write(skill, text)

# Put compaction-critical invariants near the top of both skills.
shape_path = "skills/shape-goal/SKILL.md"
shape = read(shape_path)
shape_invariants = """## Non-negotiable invariants

- No production edit before an explicitly approved Goal Contract.
- Search repository and connected authoritative evidence before asking the user.
- Save every asked question and safe answer in append-only `SHAPING.md`; corrections append and supersede.
- A dissatisfied user may request repeated deeper, non-duplicate shaping rounds.
- Use the actual persisted contract reference in every handoff; `GOAL.md` is only the default fallback.
- Contract creation is not completion: after approval, hand off to `goal-engine` and continue until evidence passes.
- Material goal drift pauses execution and reopens shaping without rewriting prior decisions.
"""
shape = insert_before(shape, "## Invocation modes", shape_invariants, label=shape_path)
shape = replace(
    shape,
    "For a normal shaping session, return the copy-ready command:\n\n```text\n/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md.",
    "For a normal shaping session, render the copy-ready command with the **actual persisted contract path or authoritative issue/spec reference**. Use `GOAL.md` only when it is the resolved contract location. Example:\n\n```text\n/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md.",
    label=shape_path,
)
shape = shape.replace(
    "private personal data, raw production data, and exploit-enabling details",
    "private personal data, confidential business or customer information, third-party restricted material, raw production data, and exploit-enabling details",
)
write(shape_path, shape)

engine_path = "skills/goal-engine/SKILL.md"
engine = read(engine_path)
engine_invariants = """## Non-negotiable invariants

- Execute only an approved contract and the approval shaping round recorded by it.
- Read the contract, shaping history, repository instructions, harness, progress, and Git state before editing.
- Preserve user and unrelated work; keep changes small, reversible, verified, and reviewable.
- Never treat shaping, planning, test creation, or documentation alone as completion when production behavior remains.
- Surface evaluator-visible evidence, protect corrected failures, and keep only changes that preserve or improve the verified state.
- Material goal drift pauses execution and appends a new shaping round; prior decisions remain immutable.
- Autonomous continuation never expands deployment, destructive, credential, billing, security-testing, legal, or production authority.
"""
engine = insert_before(engine, "## Zero-friction handoff", engine_invariants, label=engine_path)
write(engine_path, engine)

# Shaping data-classification and approval schema.
shaping_ref_path = "skills/shape-goal/references/shaping-history.md"
shaping_ref = read(shaping_ref_path)
shaping_ref = shaping_ref.replace(
    "secrets, credentials, private personal data, raw production data, or exploit-enabling detail",
    "secrets, credentials, private personal data, confidential business/customer strategy, third-party restricted material, raw production data, or exploit-enabling detail",
)
classification = """## Repository visibility and data classification

Before committing a verbatim answer, determine whether the repository and shaping path are public, private, or externally shared. Public visibility is not consent to publish confidential decisions.

- Store verbatim answers only when their classification permits repository storage.
- For confidential product strategy, customer commitments, unreleased roadmap, private commercial terms, or third-party restricted material, store a normalized redacted decision plus an approved secure reference.
- Record who can access the secure source and whether the reference is sufficient for a future authorized agent.
- Never reduce the decision to a misleading summary merely to avoid secure storage; mark the contract Blocked when essential evidence cannot be referenced safely.
"""
shaping_ref = insert_before(shaping_ref, "## Standard and deepening rounds", classification, label=shaping_ref_path)
write(shaping_ref_path, shaping_ref)

input_path = "skills/shape-goal/references/input-resolution.md"
input_text = read(input_path)
input_text = input_text.replace(
    "private personal data, raw production data, or exploit-enabling detail",
    "private personal data, confidential business/customer information, third-party restricted material, raw production data, or exploit-enabling detail",
)
input_text = input_text.replace(
    "## Safe defaults",
    "## Visibility and information classification\n\nBefore persisting a verbatim answer, determine repository visibility and whether the answer contains confidential business strategy, customer commitments, unreleased roadmap, commercial terms, or third-party restricted material. Store a redacted normalized decision plus an approved secure reference when repository storage is not appropriate.\n\n## Safe defaults",
    1,
)
write(input_path, input_text)

template_path = "skills/shape-goal/templates/shaping-history-template.md"
template = read(template_path)
template = template.replace(
    "**Lifecycle state:** Candidate / Ready / Active / Paused / Closed",
    "**Lifecycle state:** Candidate / Ready / Active / Paused / Blocked / Closed",
)
template = template.replace(
    "**Storage note:** Preserve every asked question and answer; redact sensitive material and link approved secure evidence when necessary.",
    "**Repository visibility / information classification:** [PUBLIC / PRIVATE / RESTRICTED + POLICY]\n"
    "**Storage note:** Preserve every asked question and answer; redact personal, confidential business/customer, third-party restricted, secret, production, or exploit-enabling material and link approved secure evidence when necessary.",
)
approval = """## Approval record

| Round | Approval question | User answer | Approved contract revision | Date / actor |
|---|---|---|---:|---|
| [R1] | [EXACT APPROVAL QUESTION] | [VERBATIM WHEN SAFE OR REDACTED SUMMARY] | [REVISION] | [DATE / OWNER] |

Approval is itself a shaping question and must be recorded. A later deeper round supersedes the earlier execution approval until the revised contract is approved again.
"""
template = insert_before(template, "## Corrections and supersessions", approval, label=template_path)
write(template_path, template)

# Installation prerequisites and resilient host-specific verification.
install_path = "INSTALL.md"
install = read(install_path)
prereq = """## Prerequisites

- Node.js **22.20.0 or newer** for the pinned `skills` CLI used by this repository.
- Python **3.9 or newer** only when running repository validation or package scripts; CI uses Python 3.12.
- A current Codex and/or Claude Code installation with Agent Skills support.

Check Node before installation:

```bash
node --version
```
"""
install = insert_before(install, "## Recommended: global Codex + Claude Code install", prereq, label=install_path)
troubleshooting = """## Discovery troubleshooting

If `skills list` shows both skills but one host cannot invoke them:

1. Verify the host-specific locations exist:

   ```text
   Codex:       ~/.agents/skills/shape-goal and ~/.agents/skills/goal-engine
   Claude Code: ~/.claude/skills/shape-goal and ~/.claude/skills/goal-engine
   ```

2. Rerun the install with `--copy` when symlinks are unsupported or not followed:

   ```bash
   npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \\
     --skill '*' --global --agent codex --agent claude-code --copy --yes
   ```

3. Restart the host and run the direct invocation test again.
4. Inspect `CLAUDE_CONFIG_DIR` or `CODEX_HOME` when a custom configuration directory is used.

Do not maintain divergent manual copies unless necessary; record the installed library version in each Goal Contract.
"""
install = insert_before(install, "## Project-local install", troubleshooting, label=install_path)
write(install_path, install)

# Historical research banner.
report_path = "FULL_REPORT.md"
report = read(report_path)
banner = """> [!IMPORTANT]
> This file is the **historical research foundation**, not the current copy-ready implementation. The live workflow, zero-friction launchers, shaping history, and profile catalog are maintained in [`README.md`](README.md), [`CURRENT_IMPLEMENTATION.md`](CURRENT_IMPLEMENTATION.md), and [`goals/`](goals/). Placeholder commands later in this report are preserved as research history.
"""
report = insert_before(report, "*Research checked", banner, label=report_path)
write(report_path, report)

# Current implementation, README framing, quick reference, architecture, roadmap, contribution rules.
current_path = "CURRENT_IMPLEMENTATION.md"
current = read(current_path)
current = current.replace("Version `0.4.0`", "Version `0.5.0`")
current = current.replace("22 zero-friction goal profiles", "24 zero-friction goal profiles")
current = current.replace(
    "Frontend UI/UX/accessibility, documentation, security/privacy, reliability/resilience, API compatibility, observability/operability, developer experience, data quality, and audit readiness.",
    "Frontend UI/UX/accessibility, documentation, security/privacy, reliability/resilience, API compatibility, observability/operability, developer experience, data quality, test/CI health, infrastructure/deployment readiness, and audit readiness.",
)
current = current.replace(
    "- Questions are one at a time with evidence and a recommendation.",
    "- Questions are one at a time with evidence and a recommendation.\n- Public repositories never receive confidential strategy or restricted answers verbatim; safe summaries link approved secure evidence.",
)
current = current.replace(
    "CI validates the catalog, every launcher and fallback, profile input coverage, generated docs, skill metadata, OpenAI host metadata, state schemas, links, package discovery, and deterministic ZIP builds.",
    "CI validates the catalog, every launcher and fallback, the 4,000-character native-goal limit, profile input coverage, generated docs, append-only shaping history across diffs, skill metadata, host metadata, state schemas, links, package discovery, and deterministic ZIP builds.",
)
write(current_path, current)

readme_path = "README.md"
readme = read(readme_path)
readme = readme.replace("version-0.4.0", "version-0.5.0")
readme = readme.replace("zero--friction%20goals-22", "zero--friction%20goals-24")
readme = readme.replace(
    "Every question and answer is saved immediately under the stable Goal ID:",
    "Every question and answer is saved immediately under the stable Goal ID. Before storing a verbatim answer, the skill checks repository visibility and information classification; confidential strategy, customer commitments, restricted third-party material, secrets, and private data are redacted and linked to approved secure evidence:",
)
readme = readme.replace(
    "- All profile-specific required inputs exist in the shaping skill",
    "- All profile-specific required inputs exist in the shaping skill\n- Every native `/goal` command stays within the portable 4,000-character condition limit\n- Previously committed shaping questions and answers cannot be deleted or rewritten in a PR",
)
write(readme_path, readme)

quick_path = "QUICK_REFERENCE.md"
quick = read(quick_path)
quick = quick.replace(
    "| Assure pipeline and dataset quality | Data Quality / Pipeline Assurance |\n| Prepare technical evidence for an audit | Compliance / Audit Readiness |",
    "| Assure pipeline and dataset quality | Data Quality / Pipeline Assurance |\n"
    "| Make tests and CI trustworthy | Test Suite / CI Health |\n"
    "| Prove infrastructure and deployment readiness | Infrastructure / Deployment Readiness |\n"
    "| Prepare technical evidence for an audit | Compliance / Audit Readiness |",
)
quick = quick.replace(
    "- Recorded in an input ledger and contract",
    "- Recorded in an input ledger, append-only shaping history, and contract\n- Redacted or securely referenced when repository visibility does not permit verbatim storage",
)
write(quick_path, quick)

architecture_path = "SKILLS_AND_GOALS.md"
architecture = read(architecture_path)
architecture = architecture.replace(
    "When a quality concern is itself the main outcome, use its dedicated profile. When it is secondary to another outcome, add the overlay.",
    "When a quality concern is itself the main outcome, use its dedicated profile—including Test Suite / CI Health and Infrastructure / Deployment Readiness. When it is secondary to another outcome, add the overlay.",
)
architecture = architecture.replace(
    "It creates an input ledger, searches all available authoritative sources, applies only safe reversible defaults, and asks one unresolved material decision at a time with a recommendation.",
    "It creates an input ledger, searches all available authoritative sources, applies only safe reversible defaults, checks repository visibility and information classification, and asks one unresolved material decision at a time with a recommendation.",
)
write(architecture_path, architecture)

roadmap_path = "ROADMAP.md"
roadmap = read(roadmap_path)
roadmap = roadmap.replace("## Implemented in `0.4.0`", "## Implemented through `0.5.0`")
roadmap = roadmap.replace(
    "- Dedicated frontend, documentation, security, reliability, API, observability, developer-experience, data-quality, and audit-readiness profiles.",
    "- Dedicated frontend, documentation, security, reliability, API, observability, developer-experience, data-quality, test/CI-health, infrastructure/deployment-readiness, and audit-readiness profiles.",
)
roadmap = roadmap.replace(
    "- Immutable GitHub Action pins and stronger launcher validation.",
    "- Immutable GitHub Action pins, native-goal length checks, append-only shaping-history diff validation, and stronger launcher validation.\n- Repository-visibility and information-classification rules for shaping answers.\n- Current CLI prerequisites and symlink/copy troubleshooting.",
)
write(roadmap_path, roadmap)

contrib_path = "CONTRIBUTING.md"
contrib = read(contrib_path)
contrib = contrib.replace(
    "- Ask only unresolved material owner decisions\n- Forbid production edits before contract approval",
    "- Ask only unresolved material owner decisions\n- Preserve exact safe questions and answers in append-only `SHAPING.md`, with deeper rounds and superseding corrections\n- Classify repository visibility and redact or securely reference confidential/restricted answers\n- Stay within the portable 4,000-character native-goal condition limit\n- Forbid production edits before contract approval",
)
contrib = contrib.replace(
    "python3 scripts/sync_goal_docs.py --write\npython3 scripts/sync_goal_docs.py --check",
    "python3 scripts/sync_goal_launchers.py --write\npython3 scripts/sync_goal_launchers.py --check\npython3 scripts/sync_goal_docs.py --write\npython3 scripts/sync_goal_docs.py --check",
)
write(contrib_path, contrib)

# Changelog.
changelog_path = "CHANGELOG.md"
changelog = read(changelog_path)
release = """## [0.5.0] - 2026-08-26

### Added

- **Test Suite / CI Health** for flakiness, hidden skips, false confidence, isolation, runtime, diagnostics, and local/CI parity.
- **Infrastructure / Deployment Readiness** for infrastructure-as-code, environment parity, artifacts, deployment stages, health checks, observability, and rollback without unauthorized production mutation.
- Shared launcher synchronization with a portable 4,000-character native-goal limit.
- Append-only shaping-history diff validation across pull requests and direct pushes.
- Repository-visibility and information-classification rules for confidential shaping answers.
- Current Node/Python prerequisites and host-specific discovery troubleshooting.

### Changed

- All self-contained fallbacks now preserve `SHAPING.md`, exact safe questions and answers, recommendations, normalized decisions, corrections, and repeatable deeper rounds.
- Compaction-critical safety and handoff invariants now appear near the top of both skills.
- `shape-goal` renders the actual persisted contract reference instead of always assuming `GOAL.md`.
- The shaping template now includes Blocked state and a durable approval-question record.
- The historical research report is clearly separated from the live implementation.
- The library now contains 24 zero-friction goal profiles: 7 core, 6 specialist, and 11 product/quality profiles.

"""
changelog = insert_before(changelog, "## [0.4.0]", release, label=changelog_path)
write(changelog_path, changelog)

# Validator and workflow.
validator_path = "scripts/validate_repository.py"
validator = read(validator_path)
validator = validator.replace('expected_counts = {"core": 7, "specialist": 6, "quality": 9}', 'expected_counts = {"core": 7, "specialist": 6, "quality": 11}')
validator = validator.replace("if len(goals) != 22:", "if len(goals) != 24:")
validator = validator.replace('fail(f"Expected 22 goals, found {len(goals)}")', 'fail(f"Expected 24 goals, found {len(goals)}")')
validator = validator.replace(
    "        recommended, fallback = commands\n\n        if PLACEHOLDER.search(recommended):",
    "        recommended, fallback = commands\n        for command_index, command in enumerate(commands, start=1):\n            if len(command) > 4000:\n                fail(f\"goals/{item['file']}: command {command_index} exceeds 4,000 characters ({len(command)})\")\n\n        if PLACEHOLDER.search(recommended):",
)
validator = validator.replace(
    '        "scripts/package_skills.py", "scripts/sync_goal_docs.py",\n        "scripts/validate_repository.py", ".github/workflows/validate.yml",',
    '        "scripts/package_skills.py", "scripts/sync_goal_docs.py",\n        "scripts/sync_goal_launchers.py", "scripts/validate_shaping_history_diff.py",\n        "scripts/validate_repository.py", ".github/dependabot.yml", ".github/workflows/validate.yml",',
)
validator = validator.replace(
    '    require_absent(".github/workflows/apply-zero-friction-update.yml")',
    '    require_absent(".github/workflows/apply-zero-friction-update.yml")\n    require_absent(".github/workflows/apply-final-specialist-review.yml")',
)
validator = validator.replace(
    '("Version `0.4.0`", "22 zero-friction goal profiles", "## Shaping history", "## Verification",)',
    '("Version `0.5.0`", "24 zero-friction goal profiles", "## Shaping history", "## Verification",)',
)
validator = validator.replace(
    '        "**Exact question:**", "**User answer:**", "## Corrections and supersessions",',
    '        "**Exact question:**", "**User answer:**", "Blocked", "## Approval record", "## Corrections and supersessions",',
)
validator = validator.replace(
    '            "skills@1.5.23", "scripts/sync_goal_docs.py --check",\n            "scripts/package_skills.py", "scripts/validate_repository.py",',
    '            "skills@1.5.23", "fetch-depth: 0", "scripts/sync_goal_launchers.py --check",\n            "scripts/sync_goal_docs.py --check", "scripts/validate_shaping_history_diff.py",\n            "scripts/package_skills.py", "scripts/validate_repository.py",',
)
validator = validator.replace('print("- 22 zero-friction recommended launchers")', 'print("- 24 zero-friction recommended launchers")')
validator = validator.replace('print("- 22 self-contained no-placeholder fallbacks")', 'print("- 24 self-contained no-placeholder fallbacks")')
validator = validator.replace('print("- 7 core, 6 specialist, and 9 quality profiles")', 'print("- 7 core, 6 specialist, and 11 quality profiles")')
write(validator_path, validator)

workflow_path = ".github/workflows/validate.yml"
workflow = read(workflow_path)
workflow = workflow.replace(
    "      - name: Check out repository\n        uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1",
    "      - name: Check out repository\n        uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1\n        with:\n          fetch-depth: 0",
)
workflow = workflow.replace(
    "      - name: Verify generated goal libraries\n        run: python scripts/sync_goal_docs.py --check",
    "      - name: Verify canonical goal launchers\n        run: python scripts/sync_goal_launchers.py --check\n\n"
    "      - name: Verify generated goal libraries\n        run: python scripts/sync_goal_docs.py --check\n\n"
    "      - name: Protect append-only shaping history\n        env:\n          BASE_SHA: ${{ github.event.pull_request.base.sha || github.event.before }}\n        run: python scripts/validate_shaping_history_diff.py --base-ref \"$BASE_SHA\"",
)
write(workflow_path, workflow)

# Dependabot keeps immutable action pins maintainable.
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
""",
)

# Remove this one-time migration before committing the generated result.
(ROOT / "scripts/apply_final_specialist_review.py").unlink()
