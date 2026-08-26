#!/usr/bin/env python3
"""Apply the v0.8.0 final review, profile expansion, and README refresh."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.8.0"
GOAL_ID = "2026-08-26-final-review-readme-onboarding"

PROFILES = [
    {
        "id": "30",
        "file": "30-codebase-onboarding-knowledge-recovery.md",
        "title": "Codebase Onboarding / Knowledge Recovery",
        "category": "specialist",
        "simple": "Turn an unfamiliar repository into a verified map that a new maintainer or agent can safely use.",
        "use_when": "A mature, inherited, or poorly documented codebase must become understandable, runnable, and safe to change before major delivery work begins.",
        "inspect": "repository instructions, Git history, architecture and ADRs, runtime entry points, critical user and data flows, ownership, setup and reset paths, tests and CI, operational runbooks, prior goals, and the project harness",
        "execute": "map the real architecture and ownership, trace representative user and data flows through code and runtime evidence, verify setup/run/reset/debug/test paths from clean state, reconcile stale or contradictory knowledge, and leave a reviewed Project Harness, architecture map, vocabulary, risk register, and handoff that a fresh maintainer can use without rediscovery",
        "finish": "a fresh maintainer can reproduce the approved setup, critical journeys, verification commands, and architecture decisions from the durable artifacts; every important claim is linked to code or runtime evidence; unresolved uncertainty is explicitly recorded; and protected behavior has not regressed",
        "inputs": [
            "Target maintainer or agent audience and the decisions they must be able to make",
            "Critical product journeys, runtime entry points, architecture boundaries, dependencies, and ownership",
            "Supported setup, run, reset, debug, and repository-native verification paths",
            "Required architecture map, Project Harness, vocabulary, risk register, freshness triggers, and maintainer-readiness evidence",
        ],
        "overlays": "Documentation & Knowledge Transfer, Compatibility & Portability",
        "why": "It makes understanding a testable deliverable. Repository claims must be traced to code or runtime evidence, and the result becomes durable project infrastructure instead of another disposable audit note.",
    },
    {
        "id": "31",
        "file": "31-search-seo-web-discoverability.md",
        "title": "Search / SEO / Web Discoverability",
        "category": "quality",
        "simple": "Make public web content crawlable, understandable, fast, and internally connected without promising rankings.",
        "use_when": "A public website or web application must improve its technical search readiness, rendered metadata, structured data, crawl paths, internal links, and discoverable content quality.",
        "inspect": "public routes and rendered pages, audience and search intent, canonical URLs, robots and sitemap rules, metadata, structured data, internal links, redirects and status codes, localization signals, performance, accessibility, analytics, prior audits, and connected authoritative search tooling when available",
        "execute": "inventory the public surface and search intent, crawl representative routes, verify rendered HTML and status behavior, correct canonical, robots, sitemap, metadata, structured-data, internal-link, redirect, locale, performance, accessibility, and content-discoverability defects, and rerun the same crawler and page-quality gates across the approved route matrix",
        "finish": "every approved public route is reachable and returns the intended status; canonical, robots, sitemap, metadata, structured-data, locale, internal-link, performance, accessibility, and content gates pass; broken or misleading discovery paths are resolved; and the result is stated as technical readiness rather than an unsupported ranking guarantee",
        "inputs": [
            "Target audiences, search intent, public routes, content types, and supported environments",
            "Canonical URL, redirect, robots, sitemap, pagination, duplicate-content, and crawl-budget rules",
            "Rendered titles, descriptions, social metadata, structured data, headings, internal links, and content-quality rubric",
            "Locale or hreflang matrix, performance and accessibility budgets, crawler or validation tools, and ranking-claim boundaries",
        ],
        "overlays": "Search & Discoverability, Performance & Cost, UX & Accessibility, Internationalization & Localization",
        "why": "It uses a repeatable crawl-and-render evidence loop, fixes the full discovery path rather than isolated tags, and explicitly separates technical readiness from search-ranking promises that the repository cannot prove.",
    },
]

README = r'''<div align="center">

# Loop Engineering

### Give AI coding agents a clear finish line—and a safe way to reach it.

Reusable Agent Skills and execution profiles for OpenAI Codex, Anthropic Claude Code, and established software projects.

<p>
  <img alt="1 Shape" src="https://img.shields.io/badge/1-Shape-7C3AED?style=for-the-badge">
  <img alt="2 Approve" src="https://img.shields.io/badge/2-Approve-0284C7?style=for-the-badge">
  <img alt="3 Execute" src="https://img.shields.io/badge/3-Execute-16A34A?style=for-the-badge">
  <img alt="4 Reuse" src="https://img.shields.io/badge/4-Reuse-F59E0B?style=for-the-badge">
</p>

[![Codex](https://img.shields.io/badge/OpenAI%20Codex-compatible-111827?style=flat-square&logo=openai&logoColor=white)](https://learn.chatgpt.com/use-cases/follow-goals)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97757?style=flat-square)](https://code.claude.com/docs/en/goal)
[![Validation](https://img.shields.io/github/actions/workflow/status/chrisduvillard/loop-engineering-goal-library/validate.yml?branch=main&style=flat-square&label=validation)](https://github.com/chrisduvillard/loop-engineering-goal-library/actions/workflows/validate.yml)
![Version](https://img.shields.io/badge/version-0.8.0-7C3AED?style=flat-square)
![Profiles](https://img.shields.io/badge/profiles-31-16A34A?style=flat-square)

</div>

> [!IMPORTANT]
> **`shape-goal` is the main command.** Run it outside an active `/goal`. It asks one question, saves it, and stops so you can reply normally. Autonomous work starts only after you approve what “done” means.

## 🚀 Start in three steps

### 1. Install—or update

**Install once**

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' --global --agent codex --agent claude-code --yes
```

**Get the latest version later**

```bash
npx -y skills@latest update shape-goal goal-engine --global --yes
```

Restart Codex or Claude Code after updating. See [`INSTALL.md`](INSTALL.md) for verification and a safe reinstall fallback.

### 2. Shape the next goal

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Continue this project` | `$shape-goal Continue this project` |

`shape-goal` reads the repository, resolves facts itself, and asks only decisions that belong to you. Every question and answer is saved in:

```text
docs/goals/<goal-id>/SHAPING.md
```

After each question, it ends the turn. Your next normal message is the answer—**no Steer message required**.

Need more depth?

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Deepen the current goal` | `$shape-goal Deepen the current goal` |

Earlier answers stay intact. Each new round asks only materially new questions.

### 3. Approve, then execute

Review four things: **outcome, proof, protected behavior, and authority**.

After approval, `shape-goal` returns the exact `/goal` command for `goal-engine`. Paste it once; the agent can then work autonomously:

```text
Orient → Reconcile → Select → Verify → Change
       → Check → Review → Record → Repeat
```

## 🧭 Why two phases?

A native `/goal` automatically starts another turn until its condition is met. That is excellent for implementation, but awkward when the agent must wait for your answer.

| Interactive shaping | Autonomous execution |
|---|---|
| `shape-goal` asks one question and stops | `/goal + goal-engine` keeps working |
| You answer normally | The agent verifies, retries, and records |
| You approve what “done” means | Evidence decides when it stops |

If you see **Pursuing goal…** while a shaping question is waiting:

- **Codex:** `/goal pause` or `/goal clear`, then `$shape-goal Resume goal-id`
- **Claude Code:** `/goal clear`, then `/shape-goal Resume goal-id`

<!-- goal-catalog:start -->

## Goal profiles

Catalog generated from `goals/catalog.json`.

<!-- goal-catalog:end -->

## 💾 Everything is saved for reuse

```text
GOAL.md                         approved active contract
GOAL_PROGRESS.md                evidence and next action

docs/goals/<goal-id>/
├── SHAPING.md                  questions, answers, corrections, approval
├── CONTRACT.md                 outcome, scope, proof, protections
├── PROGRESS.md                 attempts, evidence, blockers
└── RESULT.md                   result, lessons, residual risk
```

Stable knowledge is promoted into tests, ADRs, documentation, runbooks, fixtures, evals, locale and crawl matrices, scripts, benchmarks, design references, or the reusable Project Harness. Sensitive answers are redacted when the repository is not a safe place to store them.

When priorities change, run `shape-goal` again. It can amend, pause, resume, reprioritize, split, supersede, or create a follow-on goal without erasing the old decision trail.

## ⚙️ Advanced modes

<details>
<summary><strong>Autonomous and no-skill preflights</strong></summary>

Each profile file also contains two advanced `/goal` prompts:

- **Autonomous preflight** — use only when an approved artifact already answers every owner decision.
- **Self-contained preflight** — use when the skills are unavailable.

Both stop as **Approval required** when a human decision is missing. They never ask a question and keep looping inside `/goal`.

</details>

## Learn more

[`Install`](INSTALL.md) · [`Profiles`](goals/README.md) · [`Quick reference`](QUICK_REFERENCE.md) · [`Architecture`](SKILLS_AND_GOALS.md) · [`Worked example`](examples/complete-brownfield-cycle/) · [`Research`](FULL_REPORT.md)

> **Use conversation to decide what “done” means. Use `/goal` only after “done” is approved and verifiable.**
'''


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def replace_once(source: str, old: str, new: str, label: str) -> str:
    if old not in source:
        raise RuntimeError(f"Missing {label}")
    return source.replace(old, new, 1)


def goal_file(profile: dict[str, object]) -> str:
    title = str(profile["title"])
    inspect = str(profile["inspect"])
    execute = str(profile["execute"])
    finish = str(profile["finish"])
    lines = [
        f"# {title}", "", f"**Use when:** {profile['use_when']}", "", f"**In simple terms:** {profile['simple']}", "",
        "## Recommended — interactive shaping", "",
        "`shape-goal` is the main command. Run it **outside an active `/goal`** so you can answer each question normally.", "",
        "| Host | Command |", "|---|---|",
        f"| Claude Code | `/shape-goal Use the {title} profile` |",
        f"| Codex CLI / IDE | `$shape-goal Use the {title} profile` |", "",
        "`shape-goal` searches first, asks one material question, saves the answer, and ends the turn. After you approve the Goal Contract, paste the exact `/goal` command it returns.", "",
        "## Advanced — autonomous preflight", "",
        "Use this only when an approved contract or authoritative artifact already resolves every owner decision. It must stop and return control instead of asking questions inside the active `/goal`.", "", "```text",
        f"/goal Use the installed shape-goal and goal-engine skills to complete this repository's next {title} objective. Inspect {inspect} plus repository instructions, Git state, prior goals, and available connected authoritative sources. Continue inside this `/goal` only when an already-approved Goal Contract or authoritative artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to resume `shape-goal` outside `/goal`; do not ask the question or take another autonomous turn, and do not make production changes before approval. Once approved, use goal-engine to {execute}. Apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when {finish}. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.",
        "```", "", "## Inputs the skills resolve", "",
    ]
    lines.extend(f"- {item}" for item in profile["inputs"])
    lines.extend(["", f"**Suggested assurance overlays:** {profile['overlays']}", "",
        "`shape-goal` must search the repository and connected authoritative sources before asking. It asks only material unresolved decisions, one at a time with a recommendation. Execution starts only after explicit contract approval.", "",
        "## Advanced — self-contained preflight", "",
        "Use this only when the skills are unavailable and no owner interaction is expected. If a decision is missing, it must save one proposed question and stop instead of looping.", "", "```text",
        f"/goal Determine, obtain explicit approval for, and complete this repository's next {title} objective without requiring the user to prefill placeholders. Phase 1 — shape: inspect {inspect} plus repository instructions, Git state/history, prior goals, and available authoritative sources. Search before asking. Continue inside this `/goal` only when an existing approved artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to reply outside `/goal` and continue shaping from the saved state; do not ask the question or take another autonomous turn. Do not edit production before approval. Phase 2 — execute: {execute}. Make small coherent reversible changes; use repository-native checks; verify findings before fixing; add regression protection; review important diffs independently when practical; keep only changes that preserve or improve the verified baseline; and persist evidence, failed approaches, reusable outputs, and the next action. Finish only when {finish}. Stop for a genuine blocker, required approval, exhausted approved budget, material goal drift, or two consecutive no-progress cycles. At every terminal outcome, preserve a reusable closeout packet containing SHAPING.md, CONTRACT.md, final PROGRESS.md, and RESULT.md; update the portfolio and history, promote durable tests, documentation, ADRs, runbooks, fixtures, tooling, evaluations, or benchmarks, and never archive secrets or private data, including personal, customer, or confidential business information, production dumps, exploit-enabling evidence, or unnecessary large logs. Never perform destructive, deployment, release, credential, billing, legal, or external-system actions without explicit approval.",
        "```", "", f"**Why it works:** {profile['why']}", ""])
    return "\n".join(lines)


def profile_input_section(profile: dict[str, object]) -> str:
    return "\n".join([
        f"## {profile['id']}. {profile['title']}", "", f"**Use for:** {profile['use_when']}", "", "**Required profile inputs**", "",
        *[f"- {item}" for item in profile["inputs"]], "", f"**Suggested overlays:** {profile['overlays']}", "", "**Execution emphasis**", "",
        f"- {profile['execute']}.", f"- Finish only when {profile['finish']}.", "",
    ])


def loop_section(profile: dict[str, object]) -> str:
    if profile["id"] == "30":
        bullets = [
            "Inventory authoritative sources, runtime entry points, architecture boundaries, critical journeys, dependencies, ownership, and supported environments.",
            "Trace representative user, API, data, and operational flows through code and runtime evidence; verify setup, run, reset, debug, and check commands from clean state.",
            "Create or update a reviewed Project Harness, architecture map, vocabulary, risk register, and freshness triggers instead of copying stale descriptions.",
            "Finish when a fresh maintainer can reproduce the critical paths and make safe change decisions without relying on chat history.",
        ]
    else:
        bullets = [
            "Build an approved public-route and search-intent matrix, then crawl rendered pages rather than judging source templates alone.",
            "Verify status codes, redirects, canonical URLs, robots, sitemaps, metadata, structured data, internal links, locale signals, performance, accessibility, and content discoverability together.",
            "Fix root causes and rerun the same crawler, rendered-HTML, schema, link, and page-quality gates across representative routes.",
            "Finish at evidence-backed technical readiness; never claim or promise search ranking from repository checks alone.",
        ]
    return "\n".join([f"## {profile['id']}. {profile['title']}", "", f"**Use for:** {profile['use_when']}", "", *[f"- {item}" for item in bullets], ""])


def update_catalog() -> None:
    path = ROOT / "goals/catalog.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    intros = {
        "core": "Default control loops for most long-running work in established repositories.",
        "specialist": "Distinct loops for unfamiliar codebases, incidents, upgrades, migrations, branch recovery, optimization, feasibility, AI evaluation, and legacy retirement.",
        "quality": "Focused loops for interface quality, documentation, search, localization, security, reliability, APIs, operations, developer experience, data, CI, infrastructure, recovery, analytics, and audit readiness.",
    }
    for category in data["categories"]:
        category["intro"] = intros[category["key"]]
    existing = {item["file"] for item in data["goals"]}
    for profile in PROFILES:
        if profile["file"] not in existing:
            data["goals"].append({key: profile[key] for key in ("id", "file", "title", "category", "simple", "use_when")})
    expected = [f"{index:02d}" for index in range(1, len(data["goals"]) + 1)]
    actual = [item["id"] for item in data["goals"]]
    if actual != expected:
        raise RuntimeError(f"Non-sequential catalog IDs: {actual}")
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def update_profile_references() -> None:
    path = "skills/shape-goal/references/profile-inputs.md"
    source = read(path)
    if "## 30. Codebase Onboarding / Knowledge Recovery" not in source:
        block = "\n".join(profile_input_section(item) for item in PROFILES)
        source = replace_once(source, "## Routing distinctions for profiles 25–29", block + "## Routing distinctions for profiles 25–31", "profile routing heading")
        source = source.replace(
            "- Use **Product Analytics / Experimentation Integrity** instead of Data Quality or Observability when trusted product decisions, event semantics, experiment assignment, exposure, and causal-interpretation boundaries are the main outcome.",
            "- Use **Product Analytics / Experimentation Integrity** instead of Data Quality or Observability when trusted product decisions, event semantics, experiment assignment, exposure, and causal-interpretation boundaries are the main outcome.\n"
            "- Use **Codebase Onboarding / Knowledge Recovery** instead of Documentation or Developer Experience when verified maintainer understanding, architecture tracing, and a runnable Project Harness are the primary deliverable.\n"
            "- Use **Search / SEO / Web Discoverability** instead of Frontend or Documentation when rendered crawl paths, canonicalization, structured data, internal linking, and technical discovery evidence drive completion.",
        )
    source = source.replace("**Suggested overlays:** Security & Privacy, Performance & Cost, Data Integrity & Governance", "**Suggested overlays:** AI Quality & Safety, Security & Privacy, Performance & Cost, Data Integrity & Governance", 1)
    source = source.replace("**Suggested overlays:** UX & Accessibility, Compatibility & Portability, Documentation & Knowledge Transfer", "**Suggested overlays:** Internationalization & Localization, UX & Accessibility, Compatibility & Portability, Documentation & Knowledge Transfer", 1)
    write(path, source)

    path = "skills/goal-engine/references/loop-profiles.md"
    source = read(path)
    if "## 30. Codebase Onboarding / Knowledge Recovery" not in source:
        block = "\n".join(loop_section(item) for item in PROFILES)
        source = replace_once(source, "## Boundary checks for profiles 25–29", block + "## Boundary checks for profiles 25–31", "loop boundary heading")
        source = source.replace(
            "Choose these profiles only when their distinctive verifier controls the loop: repeated AI evals, staged legacy retirement, per-locale evidence, clean-room restore drills, or trustworthy product/experiment measurement.",
            "Choose these profiles only when their distinctive verifier controls the loop: repeated AI evals, staged legacy retirement, per-locale evidence, clean-room restore drills, trustworthy product/experiment measurement, verified maintainer readiness, or rendered crawl-and-discovery evidence.",
        )
    write(path, source)


def update_overlays_and_existing_profiles() -> None:
    path = "skills/goal-engine/references/assurance-overlays.md"
    source = read(path)
    if "| AI behavior and evaluation quality |" not in source:
        source = replace_once(
            source,
            "| Technical audit evidence | Compliance / Audit Readiness | Compliance & Auditability |",
            "| Technical audit evidence | Compliance / Audit Readiness | Compliance & Auditability |\n"
            "| AI behavior and evaluation quality | AI / LLM Evaluation & Improvement | AI Quality & Safety |\n"
            "| Language and locale support | Internationalization / Localization Readiness | Internationalization & Localization |\n"
            "| Public web discovery | Search / SEO / Web Discoverability | Search & Discoverability |",
            "overlay profile table",
        )
    if "## AI Quality & Safety" not in source:
        block = """## AI Quality & Safety

**Apply when:** Prompts, models, retrieval, agents, graders, or tool use are affected but AI evaluation is not the primary outcome.

Add evidence for:

- Versioned prompts, models, retrieval sources, tools, eval data, graders, and sampling settings
- Representative, adversarial, and production-like cases with leakage controls
- Repeated trials and stochastic-variation reporting
- Human or domain-expert calibration of model-based graders
- Grounding, refusal, privacy, tool-safety, latency, and cost gates

## Internationalization & Localization

**Apply when:** A change affects language, region, script, time zone, direction, or locale-sensitive data but localization is not the primary outcome.

Add evidence for:

- Supported locale and fallback matrix
- Pseudo-localization, text expansion, and missing-translation behavior
- Date, time-zone, number, currency, unit, plural, and collation behavior
- Encoding, input, keyboard, font, and right-to-left support
- Localized layout, routing, and accessibility checks

## Search & Discoverability

**Apply when:** A change affects public web pages, crawl paths, metadata, structured data, internal links, or discoverable content but search readiness is not the primary outcome.

Add evidence for:

- Public-route, canonical, redirect, robots, and sitemap behavior
- Rendered titles, descriptions, social metadata, headings, and structured data
- Internal links, broken links, duplicate-content rules, and locale signals
- Representative crawl, performance, accessibility, and rendered-page checks
- Honest separation between technical readiness and ranking claims

"""
        source = replace_once(source, "## Project-specific overlay", block + "## Project-specific overlay", "project overlay heading")
    write(path, source)

    changes = (
        ("goals/25-ai-llm-evaluation-improvement.md", "**Suggested assurance overlays:** Security & Privacy, Performance & Cost, Data Integrity & Governance", "**Suggested assurance overlays:** AI Quality & Safety, Security & Privacy, Performance & Cost, Data Integrity & Governance"),
        ("goals/27-internationalization-localization-readiness.md", "**Suggested assurance overlays:** UX & Accessibility, Compatibility & Portability, Documentation & Knowledge Transfer", "**Suggested assurance overlays:** Internationalization & Localization, UX & Accessibility, Compatibility & Portability, Documentation & Knowledge Transfer"),
    )
    for file, old, new in changes:
        source = read(file)
        if old in source:
            write(file, source.replace(old, new, 1))


def update_skills_and_version() -> None:
    write("VERSION", VERSION + "\n")
    for path in ("skills/shape-goal/SKILL.md", "skills/goal-engine/SKILL.md"):
        source = read(path)
        source = re.sub(r'  version: "\d+\.\d+\.\d+"', f'  version: "{VERSION}"', source, count=1)
        write(path, source)
    path = "skills/shape-goal/SKILL.md"
    source = read(path).replace(
        "Useful lenses include outcome and value, users and journeys, scope and dependencies, acceptance and failure cases, compatibility, UI/UX/accessibility, data/security/privacy, reliability/recovery, performance/cost, maintainability/ownership, and authority/risk.",
        "Useful lenses include outcome and value, users and journeys, scope and dependencies, acceptance and failure cases, codebase knowledge, AI evaluation, deprecation and adoption, localization, public discoverability, compatibility, UI/UX/accessibility, data/security/privacy, reliability/recovery, performance/cost, maintainability/ownership, and authority/risk.",
    )
    write(path, source)
    path = "skills/goal-engine/SKILL.md"
    source = read(path).replace(
        "- Stable evaluation → benchmark or test\n- Important limitation → residual-risk documentation",
        "- Stable evaluation → benchmark, versioned AI eval, crawl matrix, or test\n"
        "- Repository knowledge → reviewed architecture map and Project Harness\n"
        "- Locale-sensitive behavior → pseudo-localization and locale fixtures\n"
        "- Important limitation → residual-risk documentation",
    )
    write(path, source)


def update_readme_and_docs() -> None:
    write("README.md", README)
    write("CURRENT_IMPLEMENTATION.md", f'''# Current Implementation

[`FULL_REPORT.md`](FULL_REPORT.md) is the historical research foundation. The live implementation is an interactive-first workflow for shaping and then autonomously executing software goals.

## Version `{VERSION}`

```text
shape-goal                    main interactive entry point
31 execution profiles        reusable loop shapes
12 assurance overlays        extra proof when a concern is secondary
goal-engine                   autonomous brownfield execution
SHAPING.md                    durable questions and answers
Goal Contract                 approved definition of done
Project Harness               reusable project mechanics
Goal Portfolio                multiple goals over time
```

## Primary workflow

```text
shape-goal outside /goal
→ inspect repository evidence
→ ask one material question
→ save the answer and stop the turn
→ repeat or deepen
→ approve the Goal Contract
→ return an exact /goal command
→ goal-engine executes autonomously
→ verify, close out, archive, and reuse
```

The **question barrier** means that `shape-goal` asks once and ends the turn. It never forces the user to steer an active autonomous loop merely to answer.

## Advanced preflight

Each canonical profile contains skill-backed and self-contained `/goal` preflights for environments where an already-approved artifact resolves every owner decision. At the first missing decision they save one recommended question and stop as **Approval required**.

## Coverage

### Core

Continuation, requirements compliance, milestone delivery, audit/remediation, QA/UAT, safe refactoring, and release readiness.

### Specialist

Incident recovery, upgrades, data migration, branch rescue, optimization, feasibility, AI/LLM evaluation, legacy sunset, and codebase onboarding/knowledge recovery.

### Product and quality

Frontend UI/UX/accessibility, documentation, security/privacy, reliability/resilience, API compatibility, observability/operability, developer experience, data quality, test/CI health, infrastructure/deployment readiness, audit readiness, internationalization/localization, backup/restore/disaster recovery, product analytics/experimentation integrity, and search/SEO/web discoverability.

Custom Contract-Driven remains the fallback for unusual loops.

## Safety and reuse

- Facts are discovered before users are questioned.
- One material owner question is asked per turn.
- Safe questions, answers, corrections, and approvals are append-only.
- Production execution begins only from an explicitly approved contract.
- Autonomous execution never interviews the user or expands authority.
- Profiles and overlays cannot weaken the contract.
- Reusable knowledge is promoted into tests, ADRs, documentation, runbooks, fixtures, evals, locale/crawl matrices, architecture maps, scripts, benchmarks, design references, and the Project Harness.

## Verification

CI validates the 31-profile catalog, 12 recognized overlays, interactive starts, advanced preflight stop behavior, the 4,000-character native-goal limit, profile input coverage, shaping-history rules, generated docs, README install/update guidance, skill metadata, links, package discovery, and deterministic ZIP builds.
''')

    install = read("INSTALL.md").replace(
        "Verify again afterward.",
        "Restart Codex or Claude Code, then verify again afterward.\n\nIf the update command fails or does not repair a changed local install, rerun the global install command above. Reinstalling fetches the current repository version and is the safest repair path.",
        1,
    )
    write("INSTALL.md", install)

    quick = read("QUICK_REFERENCE.md").replace("## Update\n", "## Update to the latest version\n", 1)
    if "Restart Codex or Claude Code after updating." not in quick:
        quick = quick.replace("npx -y skills@latest update shape-goal goal-engine --global --yes\n```", "npx -y skills@latest update shape-goal goal-engine --global --yes\n```\n\nRestart Codex or Claude Code after updating.", 1)
    quick = quick.replace("| None fits | Custom Contract-Driven |", "| Understand an inherited codebase | Codebase Onboarding / Knowledge Recovery |\n| Improve public crawlability and discovery | Search / SEO / Web Discoverability |\n| None fits | Custom Contract-Driven |")
    write("QUICK_REFERENCE.md", quick)

    architecture = read("SKILLS_AND_GOALS.md").replace(
        "When a quality concern is itself the main outcome, use its dedicated profile—including Test Suite / CI Health and Infrastructure / Deployment Readiness. When it is secondary to another outcome, add the overlay.",
        "When a concern is itself the main outcome, use its dedicated profile—including AI / LLM Evaluation & Improvement, Internationalization / Localization Readiness, Search / SEO / Web Discoverability, Test Suite / CI Health, and Infrastructure / Deployment Readiness. When it is secondary, add the matching overlay.",
    )
    write("SKILLS_AND_GOALS.md", architecture)

    roadmap = read("ROADMAP.md").replace("## Implemented through `0.7.0`", "## Implemented through `0.8.0`")
    roadmap = roadmap.replace("- Twenty-nine profiles with host-specific `shape-goal` start commands.", "- Thirty-one profiles with host-specific `shape-goal` start commands.")
    roadmap = roadmap.replace("- Dedicated loops for AI/LLM evaluation, legacy retirement, internationalization/localization, backup and disaster recovery, and trustworthy product analytics/experimentation.", "- Dedicated loops for AI/LLM evaluation, legacy retirement, internationalization/localization, backup and disaster recovery, trustworthy product analytics/experimentation, codebase onboarding, and search/SEO/web discoverability.")
    roadmap = roadmap.replace("- Field-test the five `0.7.0` profiles", "- Field-test the seven `0.7.0`–`0.8.0` profiles")
    write("ROADMAP.md", roadmap)

    changelog = read("CHANGELOG.md")
    if "## [0.8.0]" not in changelog:
        entry = '''## [0.8.0] - 2026-08-26

### Added

- **Codebase Onboarding / Knowledge Recovery** for verified architecture tracing, clean-state setup, maintainer readiness, Project Harness creation, and durable knowledge recovery.
- **Search / SEO / Web Discoverability** for rendered crawling, canonicalization, robots and sitemaps, metadata, structured data, internal links, locale signals, performance, and accessibility without unsupported ranking claims.
- **AI Quality & Safety**, **Internationalization & Localization**, and **Search & Discoverability** assurance overlays.
- A prominent README command for updating both installed skills to the latest repository version.

### Changed

- The catalog now contains 31 profiles: 7 core, 9 specialist, and 15 product/quality profiles.
- The README uses color-coded workflow badges, emoji section markers, callouts, code blocks, tables, and collapsed catalogs while remaining short and plain.
- Installation guidance documents restart and safe reinstall behavior after updates.
- Validation covers the expanded catalog, 12 overlay names, README update path, and this repository's final review record.

'''
        changelog = replace_once(changelog, "## [0.7.0]", entry + "## [0.7.0]", "changelog release marker")
    write("CHANGELOG.md", changelog)

    sources = read("SOURCES.md")
    if "## Profile-expansion references" not in sources:
        sources += '''
## Profile-expansion references

- [Skills CLI documentation](https://www.skills.sh/docs/cli) and the [`skills update` command](https://github.com/vercel-labs/skills#skills-update)
- [OpenAI: How evals drive the next chapter of AI](https://openai.com/index/evals-drive-next-chapter-of-ai/)
- [Unicode Common Locale Data Repository](https://cldr.unicode.org/) and [Locale Data Markup Language](https://www.unicode.org/reports/tr35/)
- [Google Search Central: SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Google Search Central: Structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)

These inform the update workflow, AI evaluation overlay, standards-based locale checks, and the technical search-readiness profile. The SEO profile deliberately proves crawlability and rendered correctness rather than promising rankings.
'''
    write("SOURCES.md", sources)


def update_generator() -> None:
    path = "scripts/sync_goal_docs.py"
    source = read(path)
    if "CATEGORY_ICONS" not in source:
        source = source.replace('README_END = "<!-- goal-catalog:end -->"\n', 'README_END = "<!-- goal-catalog:end -->"\nCATEGORY_ICONS = {"core": "🟣", "specialist": "🔵", "quality": "🟢"}\nPROFILE_BADGE = re.compile(r"!\\[Profiles\\]\\(https://img\\.shields\\.io/badge/profiles-\\d+-16A34A\\?style=flat-square\\)")\n')
    source = source.replace('    for category in catalog["categories"]:\n        lines.extend([\n            "",\n            "<details>",', '    for index, category in enumerate(catalog["categories"]):\n        details_tag = "<details open>" if index == 0 else "<details>"\n        lines.extend([\n            "",\n            details_tag,')
    source = source.replace('            f"<summary><strong>{category[\'title\']} ({len(by_category.get(category[\'key\'], []))})</strong></summary>",', '            f"<summary><strong>{CATEGORY_ICONS[category[\'key\']]} {category[\'title\']} ({len(by_category.get(category[\'key\'], []))})</strong></summary>",')
    source = source.replace('    readme = readme_path.read_text(encoding="utf-8")\n    documents[readme_path] = replace_readme_catalog(readme, render_readme_catalog(catalog, parsed))', '    readme = readme_path.read_text(encoding="utf-8")\n    readme = PROFILE_BADGE.sub(\n        f"![Profiles](https://img.shields.io/badge/profiles-{len(parsed)}-16A34A?style=flat-square)",\n        readme,\n    )\n    documents[readme_path] = replace_readme_catalog(readme, render_readme_catalog(catalog, parsed))')
    write(path, source)


def update_validator() -> None:
    path = "scripts/validate_repository.py"
    source = read(path)
    source = source.replace('    "Compliance & Auditability",\n}', '    "Compliance & Auditability",\n    "AI Quality & Safety",\n    "Internationalization & Localization",\n    "Search & Discoverability",\n}')
    source = source.replace('expected_counts = {"core": 7, "specialist": 8, "quality": 14}', 'expected_counts = {"core": 7, "specialist": 9, "quality": 15}')
    source = source.replace('if len(goals) != 29:\n        fail(f"Expected 29 goals, found {len(goals)}")', 'if len(goals) != 31:\n        fail(f"Expected 31 goals, found {len(goals)}")')
    source = source.replace('"Version `0.7.0`",', '"Version `0.8.0`",')
    source = source.replace('"## Quick start",', '"## 🚀 Start in three steps",\n            "skills@latest update shape-goal goal-engine --global --yes",\n            "img.shields.io/badge/1-Shape-7C3AED",')
    source = source.replace('"## Why shaping and execution are separate",', '"## 🧭 Why two phases?",')
    source = source.replace('"## Advanced modes",', '"## ⚙️ Advanced modes",')
    source = source.replace('> 230', '> 235').replace('at 230 lines or fewer', 'at 235 lines or fewer')
    source = source.replace('print("- 29 interactive profile start commands")', 'print("- 31 interactive profile start commands")')
    source = source.replace('print("- 29 advanced autonomous preflights")', 'print("- 31 advanced autonomous preflights")')
    source = source.replace('print("- 29 advanced self-contained preflights")', 'print("- 31 advanced self-contained preflights")')
    source = source.replace('print("- 7 core, 8 specialist, and 14 quality profiles")', 'print("- 7 core, 9 specialist, and 15 quality profiles")')
    source = source.replace('print("- append-only shaping history and explicit approval")', 'print("- 12 assurance overlays")\n    print("- append-only shaping history and explicit approval")')
    source = source.replace('        "docs/goals/2026-08-26-interactive-shaping-first/UAT.md",\n', '        "docs/goals/2026-08-26-interactive-shaping-first/UAT.md",\n        "docs/goals/2026-08-26-final-review-readme-onboarding/SHAPING.md",\n        "docs/goals/2026-08-26-final-review-readme-onboarding/CONTRACT.md",\n        "docs/goals/2026-08-26-final-review-readme-onboarding/PROGRESS.md",\n        "docs/goals/2026-08-26-final-review-readme-onboarding/UAT.md",\n')
    marker = '''    require_fragments(
        require("docs/goals/2026-08-26-interactive-shaping-first/UAT.md"),
        (
            "Scenario A — Normal interactive shaping",
            "Steer is not required",
            "Scenario C — Owner decision discovered during autonomous execution",
            "Honest boundary",
        ),
    )
'''
    if 'require("docs/goals/2026-08-26-final-review-readme-onboarding/UAT.md")' not in source:
        addition = marker + '''    require_fragments(
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
'''
        source = replace_once(source, marker, addition, "validator dogfood marker")
    write(path, source)


def create_review_record() -> None:
    base = f"docs/goals/{GOAL_ID}"
    write(f"{base}/CONTRACT.md", f'''# Goal Contract: Final review, README update, and profile expansion

**Goal ID:** `{GOAL_ID}`  
**Revision:** 1  
**State:** Approved  
**Profile:** PRD / Spec Compliance  
**Shaping history:** `SHAPING.md`  
**Approval shaping round:** R1

## Outcome

The library has 31 execution profiles, 12 assurance overlays, a visible update command, and a short, polished README that explains the interactive-first workflow in plain English.

## In scope

- Reconcile the repository's actual current state and preserve the completed 0.7.0 work
- Add Codebase Onboarding / Knowledge Recovery
- Add Search / SEO / Web Discoverability
- Add AI, localization, and search assurance overlays
- Improve README formatting and color while keeping it short
- Add update, restart, and reinstall guidance
- Synchronize catalog, collections, references, validator, metadata, and packages
- Test the change on this repository

## Out of scope

Tagging or publishing a release, choosing a license, promising search rankings, or claiming product-specific maintainer, linguistic, AI, or search outcomes without project evidence.

## Acceptance evidence

- 31 canonical goal files: 7 core, 9 specialist, and 15 quality
- Profile input and execution specifications for every catalog item
- 12 recognized assurance overlays
- README shows install and update commands, colored workflow badges, interactive-first guidance, and a generated collapsed catalog
- README remains within 235 source lines
- Synchronizers, append-only shaping validation, repository validator, real Skills CLI discovery, and deterministic packaging pass
- Pull-request CI and final-main CI pass
- Only `main` remains after cleanup

## Protected behavior

Interactive one-question shaping, no-Steer replies, explicit approval before `/goal`, all existing profile links and semantics, append-only history, brownfield safety, Project Harness, portfolio, reusable closeout, sensitive-data handling, and authority boundaries.

## Authority

Repository changes, PR creation, merge after passing validation, and branch cleanup are approved. Tagging, release publication, licensing, production mutation, or external-system changes are not authorized.
''')
    write(f"{base}/PROGRESS.md", f'''# Goal Progress: Final review, README update, and profile expansion

**Goal ID:** `{GOAL_ID}`  
**Contract revision:** 1  
**State:** Active  
**Branch:** `codex/v080-final-review`  
**Completed / approval shaping rounds:** R1 / R1

## Verified findings

- Main had advanced concurrently from 24 to 29 profiles; the completed work was reconciled and preserved.
- The README explained the workflow well but hid the update command in installation documentation.
- The catalog lacked a verifier-driven onboarding/knowledge-recovery loop and a rendered crawl/discoverability loop.
- Existing AI and localization profiles had no matching secondary assurance overlays.
- The README could gain color and hierarchy without adding cognitive load.

## Acceptance ledger

| Item | Status |
|---|---|
| Preserve current main and existing 29 profiles | Pass |
| Add profiles 30–31 | In progress |
| Add overlays and references | In progress |
| README update command and visual refresh | In progress |
| Generated docs and package metadata | Pending |
| Full validation and PR review | Pending |
| Merge, final-main validation, and cleanup | Pending |

## Next action

Apply the approved changes, regenerate all outputs, run the complete validation and package suite, inspect the diff and artifact, merge after CI, close the goal record, and clean every non-main branch.
''')
    write(f"{base}/UAT.md", '''# UAT: Final review, README update, and profile expansion

## README presentation

A first-time reader should see the four colored stages, understand that `shape-goal` comes first, and find install and update commands without opening another file.

**Pass criteria**

- Colored stage badges render near the title.
- Install and update commands are visible.
- The interaction problem and no-Steer workflow remain clear.
- Profile groups remain collapsed and the README stays within 235 source lines.

## Profile differentiation

- **Codebase Onboarding / Knowledge Recovery** finishes with verified maintainer readiness, a runnable Project Harness, an architecture map, and traceable knowledge—not code delivery or documentation volume.
- **Search / SEO / Web Discoverability** finishes with rendered crawl, canonical, sitemap, metadata, structured-data, internal-link, locale, accessibility, and performance evidence—not a ranking promise.

## Update command

```bash
npx -y skills@latest update shape-goal goal-engine --global --yes
```

Installation guidance must cover restart, verification, and safe reinstall fallback.

## Repository integrity

All 31 profiles, 12 overlays, generated collections, append-only shaping history, local links, skill discovery, and deterministic packages must validate on the branch, pull request, and final main branch.

## Honest boundary

Repository tests can prove prompt structure, catalog consistency, state durability, rendered documentation, command presence, and packaging. A real project must still provide human/domain evidence for maintainer comprehension, linguistic quality, AI behavior, and search performance; the profiles explicitly preserve those boundaries.
''')


def main() -> None:
    update_catalog()
    for profile in PROFILES:
        write(f"goals/{profile['file']}", goal_file(profile))
    update_profile_references()
    update_overlays_and_existing_profiles()
    update_skills_and_version()
    update_readme_and_docs()
    update_generator()
    update_validator()
    create_review_record()
    print("Applied v0.8.0 final review and profile expansion.")


if __name__ == "__main__":
    main()
