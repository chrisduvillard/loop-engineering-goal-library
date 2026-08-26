#!/usr/bin/env python3
"""Apply the final profile-gap review and add high-value execution profiles."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.7.0"

NEW_GOALS = [{'id': '25',
  'file': '25-ai-llm-evaluation-improvement.md',
  'title': 'AI / LLM Evaluation & Improvement',
  'category': 'specialist',
  'simple': 'Build a trustworthy eval set, classify failures, test one change at a time, and keep only improvements that survive repeated runs.',
  'use_when': 'An AI, agent, retrieval, ranking, or LLM-powered feature must improve under representative evaluations while controlling quality, safety, latency, and cost.',
  'inputs': ['Target users, tasks, failure modes, and supported model/provider/tooling surfaces',
   'Versioned evaluation set, provenance, privacy, representative splits, and leakage or contamination controls',
   'Graders, rubrics, human-review boundaries, stochastic repetition, and calibration rules',
   'Baseline and target metrics plus grounding, safety, latency, cost, and reliability floors'],
  'overlays': 'Security & Privacy, Performance & Cost, Data Integrity & Governance',
  'inspect': 'prompts, model and provider settings, tool and agent workflows, retrieval sources, eval datasets, graders, safety checks, traces, costs, latency, and prior experiment evidence',
  'execute': 'freeze a versioned evaluation protocol, capture a baseline and error taxonomy, test one prompt/model/retrieval/tool/workflow hypothesis at a time, repeat stochastic trials, compare quality plus guardrail floors, and keep only reproducible improvements with regression cases',
  'finish': 'the approved evaluation targets and all safety, grounding, latency, cost, and reliability floors pass on the fixed representative set, no test leakage or unexplained regression remains, and the winning configuration and evidence are versioned',
  'why': 'It treats nondeterministic AI behavior as an evaluation problem rather than a demo, so prompt, model, retrieval, and workflow changes are kept only when representative repeated evidence improves without breaking safety or operating constraints.',
  'input_section': '## 25. AI / LLM Evaluation & Improvement\n\n**Use for:** An AI, agent, retrieval, ranking, or LLM-powered feature must improve under representative evaluations while controlling quality, safety, latency, and cost.\n\n**Required profile inputs**\n\n- Target users, tasks, failure modes, and supported model/provider/tooling surfaces\n- Versioned evaluation set, provenance, privacy, representative splits, and leakage or contamination controls\n- Graders, rubrics, human-review boundaries, stochastic repetition, and calibration rules\n- Baseline and target metrics plus grounding, safety, latency, cost, and reliability floors\n\n**Suggested overlays:** Security & Privacy, Performance & Cost, Data Integrity & Governance\n\n**Execution emphasis**\n\n- Freeze and version the eval protocol before optimizing.\n- Build an error taxonomy from representative failures, then change one hypothesis at a time.\n- Repeat stochastic trials and compare quality, grounding, safety, latency, cost, and reliability together.\n- Keep only reproducible improvements and promote newly found failures into regression evals.\n',
  'loop_section': '## 25. AI / LLM Evaluation & Improvement\n\n**Use for:** An AI, agent, retrieval, ranking, or LLM-powered feature must improve under representative evaluations while controlling quality, safety, latency, and cost.\n\n- Freeze a versioned evaluation set, grader/rubric, sampling protocol, and operational floors before changing the system.\n- Capture a baseline and failure taxonomy, then test one prompt, model, retrieval, tool, or orchestration hypothesis at a time.\n- Repeat nondeterministic runs and compare capability, grounding, safety, latency, cost, and reliability together.\n- Keep only reproducible improvements, add discovered failures to regression evals, and version the winning configuration.\n'},
 {'id': '26',
  'file': '26-deprecation-legacy-sunset.md',
  'title': 'Deprecation / Legacy Sunset',
  'category': 'specialist',
  'simple': 'Find who still depends on the old path, provide a safe migration, prove adoption, then remove it in controlled stages.',
  'use_when': 'A legacy API, feature, format, service, flag, dependency, or code path must be retired without abandoning active consumers or removing rollback too early.',
  'inputs': ['Legacy surface, supported replacement, owners, and authoritative retirement reason',
   'Known and unknown consumers, usage evidence, compatibility window, and support commitments',
   'Migration tooling, warnings, documentation, telemetry, and adoption thresholds',
   'Removal authority, retention or archival needs, rollback path, and final cleanup evidence'],
  'overlays': 'Compatibility & Portability, Documentation & Knowledge Transfer, Operability & Observability',
  'inspect': 'the legacy surface and replacement, call sites and consumers, runtime usage and telemetry, compatibility promises, support policy, feature flags, migration tooling, documentation, data retention, and rollback paths',
  'execute': 'inventory consumers, make the replacement production-ready, add migration tooling and visible warnings, measure adoption and errors, migrate dependency-safe slices, and remove the legacy surface only after the approved usage and compatibility thresholds plus explicit breaking-change authority are satisfied',
  'finish': 'the replacement is proven, every supported consumer is migrated or explicitly accepted, usage and error thresholds meet the retirement policy, removal and cleanup gates pass, documentation is current, and rollback or recovery evidence remains until the approved sunset is complete',
  'why': 'Retiring a legacy path is not a normal refactor: success depends on consumer discovery, migration adoption, staged warnings, compatibility windows, and evidence-backed removal rather than merely deleting old code.',
  'input_section': '## 26. Deprecation / Legacy Sunset\n\n**Use for:** A legacy API, feature, format, service, flag, dependency, or code path must be retired without abandoning active consumers or removing rollback too early.\n\n**Required profile inputs**\n\n- Legacy surface, supported replacement, owners, and authoritative retirement reason\n- Known and unknown consumers, usage evidence, compatibility window, and support commitments\n- Migration tooling, warnings, documentation, telemetry, and adoption thresholds\n- Removal authority, retention or archival needs, rollback path, and final cleanup evidence\n\n**Suggested overlays:** Compatibility & Portability, Documentation & Knowledge Transfer, Operability & Observability\n\n**Execution emphasis**\n\n- Discover consumers and actual usage before announcing or removing anything.\n- Make the replacement complete, provide migration tooling and warnings, and observe adoption.\n- Retire in stages; do not remove compatibility or recovery paths before approved evidence.\n- Finish with consumer accounting, cleanup, current documentation, and a tested recovery route where required.\n',
  'loop_section': '## 26. Deprecation / Legacy Sunset\n\n**Use for:** A legacy API, feature, format, service, flag, dependency, or code path must be retired without abandoning active consumers or removing rollback too early.\n\n- Inventory consumers and real usage, including undocumented integrations and long-tail versions.\n- Make the replacement production-ready, ship migration tooling and warnings, and measure adoption and error rates.\n- Migrate dependency-safe slices and preserve compatibility or rollback through the approved window.\n- Remove the legacy surface only after the contract\'s consumer, telemetry, support, and authority gates pass; then clean up and verify.\n'},
 {'id': '27',
  'file': '27-internationalization-localization-readiness.md',
  'title': 'Internationalization / Localization Readiness',
  'category': 'quality',
  'simple': 'Find hard-coded locale assumptions, build a locale matrix, test translated and right-to-left experiences, and prove every supported locale works.',
  'use_when': 'A product must work correctly across approved languages, regions, scripts, reading directions, time zones, and local formats.',
  'inputs': ['Supported locales, regions, scripts, fallback policy, and rollout order',
   'Translation source of truth, ownership, review workflow, and content or legal boundaries',
   'Dates, numbers, currency, units, time zones, pluralization, collation, names, and address rules',
   'RTL, text expansion, fonts, routing or SEO, accessibility, pseudo-localization, and per-locale UAT evidence'],
  'overlays': 'UX & Accessibility, Compatibility & Portability, Documentation & Knowledge Transfer',
  'inspect': 'user-facing strings and content, locale detection and routing, translation resources, formatting and time-zone logic, pluralization, fonts, layouts, right-to-left behavior, accessibility, SEO, tests, screenshots, and translation ownership',
  'execute': 'create a supported locale matrix, remove hard-coded assumptions, centralize messages and local formatting, define fallbacks, run pseudo-localization and text-expansion checks, exercise right-to-left and locale-specific flows, and verify functional, visual, accessibility, and content evidence per locale',
  'finish': 'every approved locale passes the defined functional, formatting, fallback, visual, accessibility, routing, and content gates; untranslated or unreviewed material is explicitly accounted for; and qualified human review is recorded wherever linguistic or legal judgment is required',
  'why': 'Localization quality depends on more than translated strings: the loop verifies data formats, directionality, layout expansion, fallbacks, routing, accessibility, and human language review as one supported-locale contract.',
  'input_section': '## 27. Internationalization / Localization Readiness\n\n**Use for:** A product must work correctly across approved languages, regions, scripts, reading directions, time zones, and local formats.\n\n**Required profile inputs**\n\n- Supported locales, regions, scripts, fallback policy, and rollout order\n- Translation source of truth, ownership, review workflow, and content or legal boundaries\n- Dates, numbers, currency, units, time zones, pluralization, collation, names, and address rules\n- RTL, text expansion, fonts, routing or SEO, accessibility, pseudo-localization, and per-locale UAT evidence\n\n**Suggested overlays:** UX & Accessibility, Compatibility & Portability, Documentation & Knowledge Transfer\n\n**Execution emphasis**\n\n- Inventory hard-coded language, region, direction, and formatting assumptions.\n- Centralize messages and locale-aware formatting, then define explicit fallback behavior.\n- Use pseudo-localization, text expansion, and RTL checks before relying on translation review.\n- Verify each supported locale through functional, visual, accessibility, routing, and qualified linguistic evidence.\n',
  'loop_section': '## 27. Internationalization / Localization Readiness\n\n**Use for:** A product must work correctly across approved languages, regions, scripts, reading directions, time zones, and local formats.\n\n- Build a supported locale matrix and inventory strings, content, routing, formatting, directionality, fonts, and layout assumptions.\n- Centralize messages and locale-aware behavior, define fallbacks, and prevent untranslated or ambiguous states.\n- Run pseudo-localization, expansion, RTL, locale-format, browser, visual, and accessibility checks.\n- Require qualified human review for linguistic or legal meaning and finish only when every supported locale\'s evidence passes.\n'},
 {'id': '28',
  'file': '28-backup-restore-disaster-recovery.md',
  'title': 'Backup / Restore / Disaster Recovery',
  'category': 'quality',
  'simple': 'Define what must survive, create trustworthy backups, restore them in a clean environment, and prove recovery meets the agreed targets.',
  'use_when': 'Critical application state must be recoverable within approved recovery objectives, with backups and restore procedures proven by realistic drills.',
  'inputs': ['Critical systems, data, configuration, secrets or keys, dependencies, owners, and recovery tiers',
   'Recovery point and recovery time objectives, retention rules, and acceptable data loss or downtime',
   'Backup frequency, immutability, encryption, off-site or cross-region design, access, and key recovery',
   'Clean-room restore environment, integrity reconciliation, failover or failback, drill scope, and production authority'],
  'overlays': 'Reliability & Recovery, Security & Privacy, Operability & Observability, Compliance & Auditability',
  'inspect': 'critical state and dependencies, backup jobs and artifacts, retention and immutability, encryption and key recovery, monitoring, restore scripts, environment definitions, runbooks, incident history, recovery objectives, and prior drill evidence',
  'execute': 'map recovery tiers, verify backup creation and monitoring, restore approved artifacts into an isolated clean environment, reconcile data and application behavior, exercise representative partial and full failure scenarios, measure recovery objectives, and improve automation and runbooks without performing destructive production tests',
  'finish': 'approved backups are current, protected, and observable; clean-room restores and required disaster drills succeed; integrity reconciliation passes; measured recovery point and time objectives meet the contract; and runbooks, ownership, residual risks, and production approval boundaries are current',
  'why': 'A backup is only useful when it can be restored. This loop makes clean-room recovery, integrity checks, measured RPO/RTO, and operational drills the completion evidence instead of trusting job-success messages.',
  'input_section': '## 28. Backup / Restore / Disaster Recovery\n\n**Use for:** Critical application state must be recoverable within approved recovery objectives, with backups and restore procedures proven by realistic drills.\n\n**Required profile inputs**\n\n- Critical systems, data, configuration, secrets or keys, dependencies, owners, and recovery tiers\n- Recovery point and recovery time objectives, retention rules, and acceptable data loss or downtime\n- Backup frequency, immutability, encryption, off-site or cross-region design, access, and key recovery\n- Clean-room restore environment, integrity reconciliation, failover or failback, drill scope, and production authority\n\n**Suggested overlays:** Reliability & Recovery, Security & Privacy, Operability & Observability, Compliance & Auditability\n\n**Execution emphasis**\n\n- Inventory critical state and recovery dependencies before judging backup coverage.\n- Verify backup freshness, retention, encryption, immutability, access, and alerting.\n- Restore into an isolated clean environment and reconcile data plus application behavior.\n- Measure recovery objectives through approved drills; never use destructive production failure as an implicit test.\n',
  'loop_section': '## 28. Backup / Restore / Disaster Recovery\n\n**Use for:** Critical application state must be recoverable within approved recovery objectives, with backups and restore procedures proven by realistic drills.\n\n- Map recovery tiers, critical state, dependencies, owners, RPO/RTO, retention, encryption, and key-recovery assumptions.\n- Verify backup freshness and integrity, then restore approved artifacts into an isolated clean environment.\n- Reconcile recovered data and application behavior, exercise representative disaster scenarios, and measure recovery objectives.\n- Improve automation, monitoring, and runbooks; never claim readiness from backup-job success alone or run destructive production drills without authority.\n'},
 {'id': '29',
  'file': '29-product-analytics-experimentation-integrity.md',
  'title': 'Product Analytics / Experimentation Integrity',
  'category': 'quality',
  'simple': 'Define the events and metrics, verify collection end to end, test experiment assignment, and prove the numbers mean what the team thinks they mean.',
  'use_when': 'Product events, funnels, metrics, dashboards, or controlled experiments must become trustworthy enough to support decisions without misleading attribution.',
  'inputs': ['Decision questions, metric definitions, primary outcomes, guardrails, owners, and acceptable interpretation boundaries',
   'Event taxonomy, schemas, identity and session rules, consent, privacy, retention, and source-to-report lineage',
   'Missing, late, duplicate, reordered, or joined-event behavior plus reconciliation and monitoring thresholds',
   'Experiment unit, randomization, exposure, assignment persistence, sample-ratio checks, analysis window, power or stopping policy, and qualified decision owner'],
  'overlays': 'Data Integrity & Governance, Security & Privacy, Compliance & Auditability, Documentation & Knowledge Transfer',
  'inspect': 'metric definitions, event schemas and producers, identity and consent logic, collection and transport, warehouse transformations, dashboards, experiment assignment and exposure, joins, loss and duplication, sample-ratio checks, analysis code, and prior decision records',
  'execute': 'map decisions to versioned metrics and event contracts, instrument or correct the smallest verified gaps, trace representative events end to end, reconcile counts and identities, test experiment assignment and exposure, detect sample-ratio or telemetry-loss problems, validate dashboards and guardrails, and document what conclusions the evidence can and cannot support',
  'finish': 'the approved events, metrics, funnels, dashboards, and experiment checks reconcile within defined thresholds; identity, consent, privacy, assignment, exposure, sample-ratio, guardrail, and lineage gates pass; and qualified owners can reproduce the analysis without unsupported causal claims',
  'why': 'Analytics can be technically present yet decision-dangerous. This loop ties every metric to a decision, verifies the full event and experiment path, and blocks conclusions when assignment, telemetry, identity, or interpretation evidence is not trustworthy.',
  'input_section': '## 29. Product Analytics / Experimentation Integrity\n\n**Use for:** Product events, funnels, metrics, dashboards, or controlled experiments must become trustworthy enough to support decisions without misleading attribution.\n\n**Required profile inputs**\n\n- Decision questions, metric definitions, primary outcomes, guardrails, owners, and acceptable interpretation boundaries\n- Event taxonomy, schemas, identity and session rules, consent, privacy, retention, and source-to-report lineage\n- Missing, late, duplicate, reordered, or joined-event behavior plus reconciliation and monitoring thresholds\n- Experiment unit, randomization, exposure, assignment persistence, sample-ratio checks, analysis window, power or stopping policy, and qualified decision owner\n\n**Suggested overlays:** Data Integrity & Governance, Security & Privacy, Compliance & Auditability, Documentation & Knowledge Transfer\n\n**Execution emphasis**\n\n- Start from the decision and define versioned metrics and event contracts before changing instrumentation.\n- Trace representative events from producer to report and reconcile missing, duplicate, late, reordered, or misjoined data.\n- Validate experiment assignment, exposure, persistence, sample ratios, guardrails, and analysis windows.\n- Separate reproducible measurement evidence from product or causal judgment that still belongs to qualified owners.\n',
  'loop_section': '## 29. Product Analytics / Experimentation Integrity\n\n**Use for:** Product events, funnels, metrics, dashboards, or controlled experiments must become trustworthy enough to support decisions without misleading attribution.\n\n- Map each product decision to versioned metric definitions, event contracts, identity rules, consent, and source-to-report lineage.\n- Trace representative events end to end and reconcile loss, duplication, lateness, ordering, joins, and dashboard calculations.\n- Validate experiment randomization, assignment persistence, exposure, sample ratios, guardrails, and analysis windows.\n- Finish only when the measurement path is reproducible and qualified owners can interpret results without unsupported causal claims.\n'}]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    source = read(path)
    if new in source:
        return
    if old not in source:
        raise RuntimeError(f"{path}: replacement anchor not found: {old!r}")
    write(path, source.replace(old, new, 1))


def insert_before(path: str, marker: str, block: str, sentinel: str) -> None:
    source = read(path)
    if sentinel in source:
        return
    if marker not in source:
        raise RuntimeError(f"{path}: marker not found: {marker!r}")
    write(path, source.replace(marker, block.rstrip() + "\n\n" + marker, 1))


def goal_markdown(goal: dict) -> str:
    inputs = "\n".join(f"- {item}" for item in goal["inputs"])
    recommended = (
        f"/goal Use the installed shape-goal and goal-engine skills to complete this repository's next {goal['title']} objective. "
        f"Inspect {goal['inspect']} plus repository instructions, Git state, prior goals, and the project harness. "
        "Continue inside this `/goal` only when an already-approved Goal Contract or authoritative artifact resolves every owner decision. "
        "Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, "
        "and tell the user to resume `shape-goal` outside `/goal`; do not ask the question or take another autonomous turn, "
        "and do not make production changes before approval. "
        f"Once approved, use goal-engine to {goal['execute']}. "
        "Apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. "
        "Do not declare success when shaping is complete. "
        f"Finish only when {goal['finish']}. "
        "Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles."
    )
    fallback = (
        f"/goal Determine, obtain explicit approval for, and complete this repository's next {goal['title']} objective without requiring the user to prefill placeholders. "
        f"Phase 1 — shape: inspect {goal['inspect']} plus repository instructions, Git state/history, prior goals, and available authoritative sources. "
        "Search before asking. Continue inside this `/goal` only when an existing approved artifact resolves every owner decision. "
        "Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, "
        "and tell the user to reply outside `/goal` and continue shaping from the saved state; do not ask the question or take another autonomous turn. "
        "Do not edit production before approval. "
        f"Phase 2 — execute: {goal['execute']}. "
        "Make small coherent reversible changes; use repository-native checks; verify findings before fixing; add regression protection; "
        "review important diffs independently when practical; keep only changes that preserve or improve the verified baseline; "
        "and persist evidence, failed approaches, reusable outputs, and the next action. "
        f"Finish only when {goal['finish']}. "
        "Stop for a genuine blocker, required approval, exhausted approved budget, material goal drift, or two consecutive no-progress cycles. "
        "At every terminal outcome, preserve a reusable closeout packet containing SHAPING.md, CONTRACT.md, final PROGRESS.md, and RESULT.md; "
        "update the portfolio and history, promote durable tests, documentation, ADRs, runbooks, fixtures, tooling, evaluations, or benchmarks, "
        "and never archive secrets or private data, including personal, customer, or confidential business information, production dumps, exploit-enabling evidence, or unnecessary large logs. "
        "Never perform destructive, deployment, release, credential, billing, legal, or external-system actions without explicit approval."
    )
    lines = [
        f"# {goal['title']}", "",
        f"**Use when:** {goal['use_when']}", "",
        f"**In simple terms:** {goal['simple']}", "",
        "## Recommended — interactive shaping", "",
        "`shape-goal` is the main command. Run it **outside an active `/goal`** so you can answer each question normally.", "",
        "| Host | Command |",
        "|---|---|",
        f"| Claude Code | `/shape-goal Use the {goal['title']} profile` |",
        f"| Codex CLI / IDE | `$shape-goal Use the {goal['title']} profile` |", "",
        "`shape-goal` searches first, asks one material question, saves the answer, and ends the turn. After you approve the Goal Contract, paste the exact `/goal` command it returns.", "",
        "## Advanced — autonomous preflight", "",
        "Use this only when an approved contract or authoritative artifact already resolves every owner decision. It must stop and return control instead of asking questions inside the active `/goal`.", "",
        "```text", recommended, "```", "",
        "## Inputs the skills resolve", "",
        inputs, "",
        f"**Suggested assurance overlays:** {goal['overlays']}", "",
        "`shape-goal` must search the repository and connected authoritative sources before asking. It asks only material unresolved decisions, one at a time with a recommendation. Execution starts only after explicit contract approval.", "",
        "## Advanced — self-contained preflight", "",
        "Use this only when the skills are unavailable and no owner interaction is expected. If a decision is missing, it must save one proposed question and stop instead of looping.", "",
        "```text", fallback, "```", "",
        f"**Why it works:** {goal['why']}", "",
    ]
    return "\n".join(lines)


def update_catalog() -> None:
    path = ROOT / "goals/catalog.json"
    catalog = json.loads(path.read_text(encoding="utf-8"))
    category_updates = {
        "specialist": (
            "Eight distinct loops for incidents, upgrades, migrations, branch recovery, optimization, feasibility, "
            "AI/LLM evaluation, and legacy retirement."
        ),
        "quality": (
            "Fourteen focused loops for frontend, documentation, security, reliability, APIs, operations, developer experience, "
            "data quality, test/CI health, infrastructure/deployment, audit readiness, internationalization, disaster recovery, "
            "and product analytics."
        ),
    }
    for category in catalog["categories"]:
        if category["key"] in category_updates:
            category["intro"] = category_updates[category["key"]]

    by_file = {item["file"]: item for item in catalog["goals"]}
    for goal in NEW_GOALS:
        item = {
            "id": goal["id"],
            "file": goal["file"],
            "title": goal["title"],
            "category": goal["category"],
            "simple": goal["simple"],
            "use_when": goal["use_when"],
        }
        by_file[goal["file"]] = item
    catalog["goals"] = sorted(by_file.values(), key=lambda item: int(item["id"]))
    path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def update_profiles() -> None:
    for goal in NEW_GOALS:
        write(f"goals/{goal['file']}", goal_markdown(goal))

    input_blocks = "\n\n".join(goal["input_section"].strip() for goal in NEW_GOALS)
    routing = """## Routing distinctions for profiles 25–29

- Use **AI / LLM Evaluation & Improvement** instead of Measured Optimization when outputs are stochastic and the loop must manage eval sets, graders, leakage, safety, grounding, latency, and cost together.
- Use **Deprecation / Legacy Sunset** instead of Safe Refactor or API Compatibility when the primary outcome is staged retirement and consumer migration, not continued compatibility.
- Use **Internationalization / Localization Readiness** instead of Frontend UI / UX / Accessibility when locale semantics, translation ownership, local formats, directionality, and per-locale evidence drive completion.
- Use **Backup / Restore / Disaster Recovery** instead of Reliability or Infrastructure Readiness when clean-room restoration and measured recovery objectives are the primary verifier.
- Use **Product Analytics / Experimentation Integrity** instead of Data Quality or Observability when trusted product decisions, event semantics, experiment assignment, exposure, and causal-interpretation boundaries are the main outcome.
"""
    profile_input_block = input_blocks + "\n\n" + routing.strip()
    insert_before(
        "skills/shape-goal/references/profile-inputs.md",
        "## Custom Contract-Driven",
        profile_input_block,
        "## 25. AI / LLM Evaluation & Improvement",
    )
    replace_once(
        "skills/shape-goal/references/profile-inputs.md",
        "Use this reference when a zero-friction launcher names a primary execution profile.",
        "Use this reference when `shape-goal` selects or is given a primary execution profile.",
    )

    loop_blocks = "\n\n".join(goal["loop_section"].strip() for goal in NEW_GOALS)
    boundaries = """## Boundary checks for profiles 25–29

Choose these profiles only when their distinctive verifier controls the loop: repeated AI evals, staged legacy retirement, per-locale evidence, clean-room restore drills, or trustworthy product/experiment measurement. When the concern is secondary, keep the existing primary profile and add the appropriate assurance overlay.
"""
    insert_before(
        "skills/goal-engine/references/loop-profiles.md",
        "## Custom Contract-Driven",
        loop_blocks + "\n\n" + boundaries.strip(),
        "## 25. AI / LLM Evaluation & Improvement",
    )


def update_version_and_docs() -> None:
    write("VERSION", VERSION + "\n")
    for path in ("skills/shape-goal/SKILL.md", "skills/goal-engine/SKILL.md"):
        source = read(path)
        source, count = re.subn(r'  version: "[^"]+"', f'  version: "{VERSION}"', source, count=1)
        if count != 1:
            raise RuntimeError(f"{path}: could not update metadata.version")
        write(path, source)

    replace_once("README.md", "version-0.6.0", "version-0.7.0")
    replace_once("README.md", "profiles-24", "profiles-29")

    current = read("CURRENT_IMPLEMENTATION.md")
    current = current.replace("## Version `0.6.0`", "## Version `0.7.0`")
    current = current.replace("24 execution profiles", "29 execution profiles")
    current = current.replace(
        "Incident recovery, ecosystem upgrades, data migration, branch rescue, measured optimization, and technical feasibility.",
        "Incident recovery, ecosystem upgrades, data migration, branch rescue, measured optimization, technical feasibility, AI/LLM evaluation, and legacy sunset.",
    )
    current = current.replace(
        "Frontend UI/UX/accessibility, documentation, security/privacy, reliability/resilience, API compatibility, observability/operability, developer experience, data quality, test/CI health, infrastructure/deployment readiness, and audit readiness.",
        "Frontend UI/UX/accessibility, documentation, security/privacy, reliability/resilience, API compatibility, observability/operability, developer experience, data quality, test/CI health, infrastructure/deployment readiness, audit readiness, internationalization/localization, backup/restore/disaster recovery, and product analytics/experimentation integrity.",
    )
    current = current.replace("CI validates the 24-profile catalog", "CI validates the 29-profile catalog")
    write("CURRENT_IMPLEMENTATION.md", current)

    roadmap = read("ROADMAP.md")
    roadmap = roadmap.replace("## Implemented through `0.6.0`", "## Implemented through `0.7.0`")
    roadmap = roadmap.replace(
        "- Twenty-four profiles with host-specific `shape-goal` start commands.",
        "- Twenty-nine profiles with host-specific `shape-goal` start commands.\n"
        "- Dedicated loops for AI/LLM evaluation, legacy retirement, internationalization/localization, backup and disaster recovery, and trustworthy product analytics/experimentation.",
    )
    roadmap = roadmap.replace(
        "- Field-test Frontend UI / UX / Accessibility and Documentation Synchronization on mature projects.",
        "- Field-test Frontend UI / UX / Accessibility and Documentation Synchronization on mature projects.\n"
        "- Field-test the five `0.7.0` profiles on representative projects and promote no additional global profile without repeated evidence.",
    )
    write("ROADMAP.md", roadmap)

    quick = read("QUICK_REFERENCE.md")
    rows = (
        "| Improve an AI or LLM feature with evals | AI / LLM Evaluation & Improvement |\n"
        "| Retire a legacy path safely | Deprecation / Legacy Sunset |\n"
        "| Prepare multiple languages and regions | Internationalization / Localization Readiness |\n"
        "| Prove backups and disaster recovery | Backup / Restore / Disaster Recovery |\n"
        "| Make analytics and experiments trustworthy | Product Analytics / Experimentation Integrity |\n"
    )
    if "AI / LLM Evaluation & Improvement" not in quick:
        quick = quick.replace("| None fits | Custom Contract-Driven |", rows + "| None fits | Custom Contract-Driven |")
    write("QUICK_REFERENCE.md", quick)

    architecture = read("SKILLS_AND_GOALS.md")
    sentence = (
        "\nThe catalog also has dedicated verifier-driven loops for AI/LLM evaluation, legacy sunset, "
        "internationalization/localization, backup and disaster recovery, and product analytics/experimentation. "
        "Use them only when that concern controls the main iteration and finish condition.\n"
    )
    anchor = "Use a dedicated profile when a quality concern is the main outcome. Use its overlay when secondary.\n"
    if sentence.strip() not in architecture:
        if anchor not in architecture:
            raise RuntimeError("SKILLS_AND_GOALS.md: profile anchor not found")
        architecture = architecture.replace(anchor, anchor + sentence, 1)
    write("SKILLS_AND_GOALS.md", architecture)

    sources = read("SOURCES.md")
    profile_sources = """## Profile-specific primary references

- [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [W3C Internationalization resources](https://www.w3.org/International/)
- [RFC 9745: Deprecation HTTP Response Header Field](https://www.rfc-editor.org/info/rfc9745/)
- [RFC 8594: Sunset HTTP Header Field](https://www.rfc-editor.org/info/rfc8594/)
- [NIST SP 1339: OT Backup Quick Start Guide](https://csrc.nist.gov/pubs/sp/1339/final)
- [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/)
- [Microsoft Research: Diagnosing Sample Ratio Mismatch in Online Controlled Experiments](https://www.microsoft.com/en-us/research/publication/diagnosing-sample-ratio-mismatch-in-online-controlled-experiments-a-taxonomy-and-rules-of-thumb-for-practitioners/)

These sources informed the distinctive verification mechanics of the new profiles: repeated stochastic evals, locale-aware checks, staged deprecation and sunset, tested restoration, and trustworthy event and experiment evidence.
"""
    insert_before(
        "SOURCES.md",
        "## Current implementation interpretation",
        profile_sources,
        "## Profile-specific primary references",
    )

    changelog = read("CHANGELOG.md")
    entry = """## [0.7.0] - 2026-08-26

### Added

- **AI / LLM Evaluation & Improvement** for versioned representative evals, stochastic repetition, error taxonomies, graders, leakage controls, and quality/safety/latency/cost trade-offs.
- **Deprecation / Legacy Sunset** for consumer discovery, migration tooling, adoption evidence, compatibility windows, staged removal, and rollback.
- **Internationalization / Localization Readiness** for locale matrices, local formats, pseudo-localization, RTL, text expansion, accessibility, and qualified linguistic review.
- **Backup / Restore / Disaster Recovery** for backup integrity, clean-room restoration, reconciliation, recovery-objective measurement, and realistic drills.
- **Product Analytics / Experimentation Integrity** for event contracts, identity and consent, lineage, experiment assignment, exposure, sample-ratio checks, and reproducible interpretation.
- Routing distinctions that prevent the new profiles from replacing existing profiles or overlays when their verifier is only secondary.
- A durable profile-gap review record under `docs/goals/2026-08-26-additional-profile-coverage/`.

### Changed

- The catalog now contains 29 profiles: 7 core, 8 specialist, and 14 product/quality profiles.
- README catalogs, generated collections, quick reference, current implementation, roadmap, validator, and packaged skill metadata now reflect version `0.7.0`.

"""
    if "## [0.7.0]" not in changelog:
        marker = "## [0.6.0]"
        if marker not in changelog:
            raise RuntimeError("CHANGELOG.md: 0.6.0 marker not found")
        changelog = changelog.replace(marker, entry + marker, 1)
    write("CHANGELOG.md", changelog)


def update_validator() -> None:
    path = "scripts/validate_repository.py"
    source = read(path)
    replacements = {
        'expected_counts = {"core": 7, "specialist": 6, "quality": 11}':
            'expected_counts = {"core": 7, "specialist": 8, "quality": 14}',
        'if len(goals) != 24:': 'if len(goals) != 29:',
        'fail(f"Expected 24 goals, found {len(goals)}")': 'fail(f"Expected 29 goals, found {len(goals)}")',
        '"24 execution profiles",': '"29 execution profiles",',
        'print("- 24 interactive profile start commands")': 'print("- 29 interactive profile start commands")',
        'print("- 24 advanced autonomous preflights")': 'print("- 29 advanced autonomous preflights")',
        'print("- 24 advanced self-contained preflights")': 'print("- 29 advanced self-contained preflights")',
        'print("- 7 core, 6 specialist, and 11 quality profiles")':
            'print("- 7 core, 8 specialist, and 14 quality profiles")',
    }
    for old, new in replacements.items():
        if new in source:
            continue
        if old not in source:
            raise RuntimeError(f"{path}: validator anchor not found: {old!r}")
        source = source.replace(old, new, 1)
    write(path, source)


def write_review_record() -> None:
    base = "docs/goals/2026-08-26-additional-profile-coverage"
    shaping = """# Shaping History: Additional profile coverage

**Goal ID:** `2026-08-26-additional-profile-coverage`  
**State:** Approved  
**Completed / approval shaping rounds:** R1 / R1

## Round R1

### Evidence reviewed

- The existing 24 profiles cover general brownfield delivery, quality, data, operations, security, frontend, documentation, CI, and infrastructure.
- `shape-goal` can route automatically, so adding a profile is justified only when it has a distinct iteration, verifier, failure mode, and stop condition.
- Current primary vendor guidance still supports interactive shaping before autonomous `/goal` execution.

### Owner request

The user explicitly requested a final review of the tool and additional Goal profiles.

### Decision

Add only five gaps with clearly distinct completion evidence:

1. AI / LLM Evaluation & Improvement
2. Deprecation / Legacy Sunset
3. Internationalization / Localization Readiness
4. Backup / Restore / Disaster Recovery
5. Product Analytics / Experimentation Integrity

Do not add separate profiles for search/relevance, mobile, FinOps, feature flags, or open-source readiness because existing profiles plus overlays already cover their dominant loops.

### Approval record

**Approval round:** R1  
**Basis:** The user's explicit request authorized the review and addition of more profiles; no unresolved owner decision remained after the evidence-based gap analysis.
"""
    contract = """# Goal Contract: Additional profile coverage

**Goal ID:** `2026-08-26-additional-profile-coverage`  
**Revision:** 1  
**State:** Approved  
**Profile:** PRD / Spec Compliance  
**Shaping history:** `SHAPING.md`  
**Approval shaping round:** R1

## Outcome

Review the complete profile taxonomy and add only reusable Goal profiles whose iteration, verifier, failure mode, and stopping logic are materially distinct from the existing catalog.

## In scope

- Profile-gap review
- Five new profile guides
- `shape-goal` input specifications
- `goal-engine` execution rules
- Routing distinctions
- Catalog, generated docs, README, quick reference, versioning, sources, validation, and packages

## Out of scope

- Technology-specific profiles
- Duplicate combinations of existing profiles and overlays
- Licensing, publishing a release, deployment, or external-system changes

## Acceptance evidence

- 29 catalog entries with sequential IDs and valid categories
- Each new profile exposes interactive-first commands plus two safe advanced preflights
- Every advanced `/goal` remains within 4,000 characters
- Profile inputs and execution rules exist for all five additions
- Generated collections and README remain synchronized
- Repository validation, append-only history tests, Agent Skills discovery, and deterministic packaging pass
- Pull-request and final `main` CI pass

## Protected behavior

- `shape-goal` remains the main interactive entry point
- The one-question turn barrier remains intact
- `goal-engine` never interviews the user during autonomous execution
- Existing 24 profile links, IDs, contracts, overlays, archives, and packaging remain compatible
"""
    progress = """# Goal Progress: Additional profile coverage

**Goal ID:** `2026-08-26-additional-profile-coverage`  
**Contract revision:** 1  
**State:** Active  
**Shaping history:** `SHAPING.md`  
**Completed / approval shaping rounds:** R1 / R1

## Baseline

- Version `0.6.0`
- 24 profiles: 7 core, 6 specialist, 11 product/quality
- Interactive-first shaping and advanced preflight boundaries already validated

## Planned work

- Add five evidence-distinct profiles
- Update routing and profile input specifications
- Regenerate catalogs and collections
- Update version, README, sources, roadmap, quick reference, and validation
- Run CI, package both skills, merge, close out, and clean the branch
"""
    write(f"{base}/SHAPING.md", shaping)
    write(f"{base}/CONTRACT.md", contract)
    write(f"{base}/PROGRESS.md", progress)


def main() -> None:
    update_catalog()
    update_profiles()
    update_version_and_docs()
    update_validator()
    write_review_record()
    print("Applied additional profile coverage for version", VERSION)


if __name__ == "__main__":
    main()
