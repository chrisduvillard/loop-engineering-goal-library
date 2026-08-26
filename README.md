<div align="center">

# Loop Engineering `/goal` Library

**Choose the kind of outcome. The skills discover the missing inputs, preserve every decision, ask only what matters, and keep working until evidence says it is done.**

Portable Agent Skills and zero-friction `/goal` launchers for OpenAI Codex, Anthropic Claude Code, and mature brownfield repositories.

[![OpenAI Codex](https://img.shields.io/badge/OpenAI%20Codex-compatible-111827?style=flat-square&logo=openai&logoColor=white)](https://developers.openai.com/codex/use-cases/follow-goals/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97757?style=flat-square)](https://code.claude.com/docs/en/goal)
[![Validation](https://img.shields.io/github/actions/workflow/status/chrisduvillard/loop-engineering-goal-library/validate.yml?branch=main&style=flat-square&label=validation)](https://github.com/chrisduvillard/loop-engineering-goal-library/actions/workflows/validate.yml)
![Version](https://img.shields.io/badge/version-0.5.0-7C3AED?style=flat-square)
![Brownfield first](https://img.shields.io/badge/focus-brownfield--first-2563EB?style=flat-square)
![Goals](https://img.shields.io/badge/zero--friction%20goals-24-16A34A?style=flat-square)

```text
Choose profile → Search evidence → Ask + save decisions → Approve contract
               → Execute → Verify → Archive → Reuse
```

</div>

> [!IMPORTANT]
> Every recommended goal command runs unchanged. It first activates `shape-goal` to discover the exact target, scope, evidence, protections, and boundaries. Every question and answer is preserved in an append-only shaping history. Production edits start only after the Goal Contract is approved; `goal-engine` then executes it until the approved evidence passes.

## Quick start

### 1. Install both skills once

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' --global --agent codex --agent claude-code --yes
```

Verify:

```bash
npx -y skills@latest list --global --agent codex --agent claude-code
```

You should see `shape-goal` and `goal-engine`. See [`INSTALL.md`](INSTALL.md) for project-local, update, temporary-use, and ZIP options.

### 2. Open your repository

Start Codex or Claude Code from the repository root so it can inspect instructions, Git state, plans, tests, runtime entry points, and prior goal state.

### 3. Choose how you want to start

**You know the kind of work:** open a file under [`goals/`](goals/) and paste its first `/goal` command exactly as written.

Examples:

- Interface quality: [`Frontend UI / UX / Accessibility`](goals/14-frontend-ui-ux-accessibility.md)
- Documentation: [`Documentation Synchronization / Knowledge Transfer`](goals/15-documentation-synchronization.md)
- Finish existing work: [`Brownfield Continue / Finish`](goals/01-brownfield-continue-finish.md)
- Security: [`Security / Privacy Hardening`](goals/16-security-privacy-hardening.md)

**You do not know which goal fits:**

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Continue this project` | `$shape-goal Continue this project` |

`shape-goal` inspects the repository, selects a profile, and returns the exact native `/goal` command.

### 4. Let the skills resolve the inputs

The launcher builds an input ledger and searches, in order:

1. Repository and agent instructions
2. Git state, branches/worktrees, and relevant history
3. Current and previous goals, shaping histories, progress, portfolio, and handoffs
4. PRDs, specifications, issues, plans, ADRs, architecture, and design references
5. Scripts, CI, tests, fixtures, benchmarks, and release gates
6. Runtime behavior, screenshots, logs, and generated artifacts
7. Connected authoritative systems available to the host
8. Official external documentation when current platform or standard facts matter

Only unresolved **owner decisions** are asked. Questions are one at a time and include the evidence, options, recommendation, and trade-off.

Every question and answer is saved immediately under the stable Goal ID. Before storing a verbatim answer, the skill checks repository visibility and information classification; confidential strategy, customer commitments, restricted third-party material, secrets, and private data are redacted and linked to approved secure evidence:

```text
docs/goals/<goal-id>/SHAPING.md
```

The record is append-only. If the user later changes an answer, the skill adds a correction and marks the earlier decision superseded instead of rewriting history. Sensitive answers are redacted and linked to an approved secure source rather than committed verbatim.

### 5. Go deeper when the first contract is not enough

The initial shaping round resolves the minimum material decisions required for a safe contract. If the target still feels shallow, incomplete, or wrong, request another round:

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Deepen the current goal` | `$shape-goal Deepen the current goal` |
| `/shape-goal Run another shaping round for goal-id` | `$shape-goal Run another shaping round for goal-id` |

The skill reads every previous question and answer, identifies weak assumptions or unexplored lenses, and asks a new **non-duplicate** sequence of one-at-a-time questions. Useful lenses include user value, journeys, non-goals, edge cases, compatibility, UI/UX, data, security, recovery, performance, cost, maintenance, ownership, and authority.

You can run multiple deepening rounds. Each round is saved with stable IDs such as `R2-Q3`, summarized, and linked to the revised contract.

At the end of a round, choose:

```text
Approve the current Goal Contract
Run another deeper shaping round
Pause shaping and preserve the current state
```

### 6. Approve the Goal Contract

Before production changes, review:

- **Outcome** — Is this the result you want?
- **Evidence** — Will the checks or workflows prove it?
- **Protection** — What behavior, data, compatibility, and user work must survive?
- **Authority** — Which destructive, production, credential, release, or external actions still need approval?
- **Exit** — What counts as success, blocker, budget exhaustion, goal drift, or stall?
- **Decision trace** — Which shaping round and answers formed the contract?

The contract is saved in an existing authoritative issue/spec when possible, otherwise in `GOAL.md`. It records the shaping-history path, completed rounds, last round, and approval round.

### 7. Execution continues automatically

After approval, `shape-goal` hands off inside the same native `/goal` to `goal-engine`.

```text
Orient → Reconcile → Select → Verify gap → Change → Check
       → Review → Keep or revert → Record → Repeat
```

Shaping is **not** completion. The goal ends successfully only when every approved acceptance and assurance gate passes with surfaced evidence.

If a new need or dissatisfaction materially changes the contract during execution, `goal-engine` preserves progress and returns to `shape-goal` for a new appended shaping round. It never silently expands scope.

### 8. Follow progress and reuse the result

When the repository has no stronger convention:

```text
GOAL.md
GOAL_PROGRESS.md

docs/goals/
├── PORTFOLIO.md          optional non-closed goal coordination
├── INDEX.md              closed-goal history
└── <goal-id>/
    ├── SHAPING.md        every asked question, answer, correction, and round summary
    ├── CONTRACT.md       approved outcome and boundaries
    ├── PROGRESS.md       evidence, attempts, blockers, and next action
    └── RESULT.md         outcome, delivered behavior, lessons, and residual risk
```

Verified learning is promoted to regression tests, ADRs, product docs, runbooks, fixtures, scripts, benchmarks, design references, or the reusable Project Harness.

### When a new need appears

Run `shape-goal` again. It will clarify, amend, reprioritize, pause, resume, split, merge, supersede, cancel, or create a different Goal ID. It never silently appends an unrelated request to the active contract, and it never discards the prior shaping history.

Parallel goals use separate sessions and worktrees with explicit dependency and shared-resource coordination.

## One-command example

Suppose you want the agent to improve a mature frontend but you do not know every screen, viewport, browser, design reference, or acceptance check.

Open [`goals/14-frontend-ui-ux-accessibility.md`](goals/14-frontend-ui-ux-accessibility.md), copy **Run unchanged — recommended**, and paste it into Codex or Claude Code. The command tells `shape-goal` to discover those inputs, save every necessary product question and answer, let you request deeper rounds, obtain approval, then hand off to `goal-engine` for browser-based implementation and verification.

No placeholder replacement is required.

See the [complete shaping and brownfield example](examples/complete-brownfield-cycle/) for two saved rounds, an approved contract, execution evidence, and a follow-on portfolio goal.

<!-- goal-catalog:start -->

## All zero-friction standalone goals

Copy the first `/goal` command from any linked file **without changing it**. The command activates `shape-goal` to discover and approve missing repository-specific inputs, then hands the approved contract to `goal-engine` for execution.

### Core goals

| Goal | In simple terms | Use when |
|---|---|---|
| [**Brownfield Continue / Finish**](goals/01-brownfield-continue-finish.md) | Understand the real current state and keep completing the most important unblocked work. | An existing repository has an approved direction, partial implementation, or unfinished milestone and should advance autonomously. |
| [**PRD / Spec Compliance**](goals/02-prd-spec-compliance.md) | Compare the real product with its requirements and close every proven gap. | A product, feature, or repository must be brought into full alignment with documented requirements. |
| [**Next Milestone**](goals/03-next-milestone.md) | Deliver one useful next milestone without wandering into the whole backlog. | A roadmap is larger than one run and the next coherent, dependency-safe increment should be completed end to end. |
| [**Deep Audit + Remediation**](goals/04-deep-audit-remediation.md) | Find important problems, prove they are real, fix root causes, and prevent recurrence. | The codebase needs evidence-based discovery and repair of important defects or risks. |
| [**QA / Regression / UAT**](goals/05-qa-regression-uat.md) | Exercise the real product until required workflows and regression gates pass. | The actual product surface and realistic user workflows must pass defined acceptance gates. |
| [**Safe Refactor / Modernization**](goals/06-safe-refactor-modernization.md) | Improve internals while proving users and integrations still see the intended behavior. | Architecture, dependencies, or internals should change while external behavior and contracts remain stable. |
| [**Release Readiness**](goals/07-release-readiness.md) | Remove verified release blockers and stop at release-ready. | A version or milestone must satisfy all release gates without actually being published or deployed. |

### Specialist goals

| Goal | In simple terms | Use when |
|---|---|---|
| [**Incident Recovery / Stabilization**](goals/08-incident-recovery.md) | Contain damage, restore health, prove the cause, and add prevention. | A severe regression or production-like incident must be contained, diagnosed, and recovered without compounding damage. |
| [**Dependency / Framework Upgrade**](goals/09-dependency-framework-upgrade.md) | Upgrade through safe version steps while checking the full compatibility surface. | A dependency, framework, language runtime, or toolchain must move to a target version without breaking supported behavior. |
| [**Data Migration / Integrity**](goals/10-data-migration-integrity.md) | Migrate data through reversible phases and prove no unexplained loss, duplication, or corruption. | Stored data, schemas, formats, or backfills must change while preserving correctness, compatibility, and recoverability. |
| [**Branch Rescue / Integration**](goals/11-branch-rescue-integration.md) | Recover useful behavioral slices without overwriting newer target work. | Valuable work is stranded in a stale, divergent, oversized, or conflicting branch and must be recovered safely. |
| [**Measured Optimization / Benchmark**](goals/12-measured-optimization-benchmark.md) | Freeze a baseline, test one challenger at a time, and keep only reproducible wins. | A stable metric must improve under a fixed protocol without regressing required behavior. |
| [**Technical Spike / Feasibility**](goals/13-technical-spike-feasibility.md) | Run an isolated experiment and return a Go, Conditional Go, or No-Go decision. | A bounded technical unknown must be resolved before production commitment. |

### Product and quality goals

| Goal | In simple terms | Use when |
|---|---|---|
| [**Frontend UI / UX / Accessibility**](goals/14-frontend-ui-ux-accessibility.md) | Improve the real interface through browser-based user journeys, visual evidence, and accessibility checks. | A frontend surface must become coherent, usable, responsive, accessible, and visually polished without regressing behavior. |
| [**Documentation Synchronization / Knowledge Transfer**](goals/15-documentation-synchronization.md) | Find documentation drift, verify examples and commands, and make the maintained knowledge trustworthy. | Documentation, examples, runbooks, diagrams, or onboarding material must accurately match current behavior and be usable by its audience. |
| [**Security / Privacy Hardening**](goals/16-security-privacy-hardening.md) | Threat-model the scoped system, prove actionable findings, remediate safely, and add lasting protection. | Security and privacy are the primary outcome: attack surface, authorization, secrets, dependencies, or data handling must be hardened and verified. |
| [**Reliability / Resilience Hardening**](goals/17-reliability-resilience-hardening.md) | Model failure modes, inject safe faults, improve recovery, and prove reliability objectives. | A system must continue or recover correctly under defined failures, load, retries, restarts, and dependency degradation. |
| [**API / Integration Contract Compatibility**](goals/18-api-integration-contract-compatibility.md) | Map contracts and consumers, prove compatibility, and evolve interfaces without hidden breakage. | APIs, events, schemas, SDKs, or external integrations must remain compatible across producers, consumers, and versions. |
| [**Observability / Operability**](goals/19-observability-operability.md) | Make system health visible and actionable, then prove it with drills. | Operators and maintainers must be able to detect, understand, and recover from important failures using useful signals and runbooks. |
| [**Developer Experience / Tooling**](goals/20-developer-experience-tooling.md) | Make the common developer path work from clean state with clear commands and actionable failures. | Local setup, build, test, debug, CI, or contribution workflows must become faster, clearer, and reproducible. |
| [**Data Quality / Pipeline Assurance**](goals/21-data-quality-pipeline-assurance.md) | Define data invariants, test the real pipeline, correct root causes, and make quality continuously observable. | A data pipeline or dataset must satisfy defined freshness, completeness, validity, consistency, lineage, and reconciliation expectations. |
| [**Compliance / Audit Readiness**](goals/22-compliance-audit-readiness.md) | Map controls to implementation and evidence, close technical gaps, and leave an auditable package for qualified human review. | A repository or system must produce implementation evidence for an approved control set without falsely self-certifying legal or regulatory compliance. |
| [**Test Suite / CI Health**](goals/23-test-suite-ci-health.md) | Find flaky, misleading, slow, skipped, or environment-dependent checks and turn the test pipeline into reliable evidence. | Automated tests and CI must become trustworthy, deterministic, appropriately fast, and consistent with local development. |
| [**Infrastructure / Deployment Readiness**](goals/24-infrastructure-deployment-readiness.md) | Verify that the system can be provisioned and deployed consistently, diagnosed after rollout, and safely rolled back before a human authorizes production change. | Infrastructure, environment configuration, deployment automation, smoke checks, and rollback must be proven ready without silently changing production. |

### When no preset fits

Use the [**Custom Contract-Driven fallback**](skills/shape-goal/templates/custom-contract-driven-goal.md). It still requires a bounded iteration, primary verifier, keep-or-revert rule, review strategy, and objective stop condition.

<!-- goal-catalog:end -->

## Profiles versus assurance overlays

A profile controls the main execution loop. Assurance overlays add extra proof when a concern is secondary.

Example:

```text
Primary profile: Dependency / Framework Upgrade
Overlays: Security & Privacy; Compatibility & Portability; Reliability & Recovery
```

When security, frontend quality, documentation, reliability, API compatibility, observability, developer experience, data quality, or compliance is itself the main outcome, use its dedicated profile.

See [`assurance-overlays.md`](skills/goal-engine/references/assurance-overlays.md).

## Reuse project mechanics

`goal-engine` prefers existing READMEs, repository instructions, task runners, CI, and runbooks. When setup, run, reset, supported environments, or verification commands are fragmented, it creates or refreshes a vendor-neutral [Project Harness](skills/goal-engine/templates/project-harness-template.md).

## Strict two-step mode

The zero-friction commands intentionally combine shaping and execution inside one native goal while retaining an approval gate. For maximum control, run the traditional sequence instead:

```text
1. /shape-goal or $shape-goal
2. Review saved shaping rounds and GOAL.md
3. Approve, deepen again, or pause
4. Paste the /goal command returned by shape-goal after approval
```

Both modes use the same contract, profiles, overlays, shaping history, state, and evidence rules.

## Deep-review guarantees

CI verifies that:

- Every recommended launcher contains no unresolved placeholders
- Every launcher invokes both `shape-goal` and `goal-engine`
- All profile-specific required inputs exist in the shaping skill
- Every native `/goal` command stays within the portable 4,000-character condition limit
- Previously committed shaping questions and answers cannot be deleted or rewritten in a PR
- Durable shaping-history references and templates are packaged
- The contract, progress, result, and history schemas link shaping rounds
- The worked example preserves questions and answers across multiple rounds
- The README catalog matches the machine-readable goal catalog
- Generated core, specialist, and quality libraries are synchronized
- Skill metadata and versions match
- Agent Skills CLI discovers both skills
- Packaged ZIPs include all references, templates, and host metadata
- Markdown links and Python syntax are valid

## Explore

[**Current implementation**](CURRENT_IMPLEMENTATION.md) · [**Goal catalog**](goals/README.md) · [**Quick reference**](QUICK_REFERENCE.md) · [**Architecture**](SKILLS_AND_GOALS.md) · [**Core goals**](GOAL_LIBRARY.md) · [**Specialist goals**](SPECIALIST_LOOPS.md) · [**Quality goals**](QUALITY_GOALS.md) · [**Complete example**](examples/complete-brownfield-cycle/) · [**Research**](FULL_REPORT.md) · [**Roadmap**](ROADMAP.md) · [**Contributing**](CONTRIBUTING.md)

---

<sub>Version 0.4.0. Research checked against current sources on August 25, 2026. License selection remains an explicit pre-1.0 owner decision.</sub>
