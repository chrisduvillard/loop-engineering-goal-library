<div align="center">

# Loop Engineering

### Shape first. Execute second. Prove it is done.

A reusable workflow for long-running AI coding work in mature repositories.

[![Codex](https://img.shields.io/badge/OpenAI%20Codex-compatible-111827?style=flat-square&logo=openai&logoColor=white)](https://learn.chatgpt.com/use-cases/follow-goals)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97757?style=flat-square)](https://code.claude.com/docs/en/goal)
[![Validation](https://img.shields.io/github/actions/workflow/status/chrisduvillard/loop-engineering-goal-library/validate.yml?branch=main&style=flat-square&label=validation)](https://github.com/chrisduvillard/loop-engineering-goal-library/actions/workflows/validate.yml)
![Version](https://img.shields.io/badge/version-0.7.0-7C3AED?style=flat-square)
![Profiles](https://img.shields.io/badge/profiles-29-16A34A?style=flat-square)

```text
shape-goal → answer → approve → /goal + goal-engine → verify → archive → reuse
```

</div>

> [!IMPORTANT]
> **`shape-goal` is the main command.** Run it outside an active `/goal`. It asks one question, saves it, and stops so you can reply normally. Autonomous work starts only after you approve the Goal Contract.

## Quick start

### 1. Install once

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' --global --agent codex --agent claude-code --yes
```

### 2. Shape the next goal

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Continue this project` | `$shape-goal Continue this project` |

`shape-goal` reads the repository, resolves facts itself, and asks only decisions that belong to you. Each question and answer is saved in:

```text
docs/goals/<goal-id>/SHAPING.md
```

After each question it ends the turn. Your next normal message is the answer—**no Steer message required**.

Need more depth?

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Deepen the current goal` | `$shape-goal Deepen the current goal` |

Earlier answers stay intact. A new round asks only materially new questions.

### 3. Approve, then execute

Review the proposed outcome, proof, protected behavior, and authority boundaries. After approval, `shape-goal` returns the exact `/goal` command for `goal-engine`.

Paste it once. The agent can then work autonomously:

```text
Orient → Reconcile → Select → Verify → Change
       → Check → Review → Record → Repeat
```

## Why shaping and execution are separate

Native `/goal` loops automatically start another turn until their condition is met. That is excellent for implementation—but awkward when the agent must wait for your answer.

| Interactive shaping | Autonomous execution |
|---|---|
| `shape-goal` asks one question and stops | `/goal + goal-engine` keeps working |
| You answer normally | The agent verifies, retries, and records |
| You approve what “done” means | Evidence decides when it stops |

If you see **Pursuing goal…** while a shaping question is waiting:

- **Codex:** `/goal pause` or `/goal clear`, then `$shape-goal Resume goal-id`
- **Claude Code:** `/goal clear`, then `/shape-goal Resume goal-id`

## Start with a specific profile

Let `shape-goal` choose, or name the type of work:

| Need | Codex example |
|---|---|
| Finish existing work | `$shape-goal Use the Brownfield Continue / Finish profile` |
| Improve UI and UX | `$shape-goal Use the Frontend UI / UX / Accessibility profile` |
| Fix documentation | `$shape-goal Use the Documentation Synchronization / Knowledge Transfer profile` |
| Repair tests and CI | `$shape-goal Use the Test Suite / CI Health profile` |
| Prepare deployment safely | `$shape-goal Use the Infrastructure / Deployment Readiness profile` |

<!-- goal-catalog:start -->

## Goal profiles

You usually do not need to choose one: `shape-goal` can select the best profile from repository evidence. Choose directly only when the type of work is already clear.

<details>
<summary><strong>Core goals (7)</strong></summary>

| Profile | Best for |
|---|---|
| [**Brownfield Continue / Finish**](goals/01-brownfield-continue-finish.md) | Understand the real current state and keep completing the most important unblocked work. |
| [**PRD / Spec Compliance**](goals/02-prd-spec-compliance.md) | Compare the real product with its requirements and close every proven gap. |
| [**Next Milestone**](goals/03-next-milestone.md) | Deliver one useful next milestone without wandering into the whole backlog. |
| [**Deep Audit + Remediation**](goals/04-deep-audit-remediation.md) | Find important problems, prove they are real, fix root causes, and prevent recurrence. |
| [**QA / Regression / UAT**](goals/05-qa-regression-uat.md) | Exercise the real product until required workflows and regression gates pass. |
| [**Safe Refactor / Modernization**](goals/06-safe-refactor-modernization.md) | Improve internals while proving users and integrations still see the intended behavior. |
| [**Release Readiness**](goals/07-release-readiness.md) | Remove verified release blockers and stop at release-ready. |

</details>

<details>
<summary><strong>Specialist goals (8)</strong></summary>

| Profile | Best for |
|---|---|
| [**Incident Recovery / Stabilization**](goals/08-incident-recovery.md) | Contain damage, restore health, prove the cause, and add prevention. |
| [**Dependency / Framework Upgrade**](goals/09-dependency-framework-upgrade.md) | Upgrade through safe version steps while checking the full compatibility surface. |
| [**Data Migration / Integrity**](goals/10-data-migration-integrity.md) | Migrate data through reversible phases and prove no unexplained loss, duplication, or corruption. |
| [**Branch Rescue / Integration**](goals/11-branch-rescue-integration.md) | Recover useful behavioral slices without overwriting newer target work. |
| [**Measured Optimization / Benchmark**](goals/12-measured-optimization-benchmark.md) | Freeze a baseline, test one challenger at a time, and keep only reproducible wins. |
| [**Technical Spike / Feasibility**](goals/13-technical-spike-feasibility.md) | Run an isolated experiment and return a Go, Conditional Go, or No-Go decision. |
| [**AI / LLM Evaluation & Improvement**](goals/25-ai-llm-evaluation-improvement.md) | Build a trustworthy eval set, classify failures, test one change at a time, and keep only improvements that survive repeated runs. |
| [**Deprecation / Legacy Sunset**](goals/26-deprecation-legacy-sunset.md) | Find who still depends on the old path, provide a safe migration, prove adoption, then remove it in controlled stages. |

</details>

<details>
<summary><strong>Product and quality goals (14)</strong></summary>

| Profile | Best for |
|---|---|
| [**Frontend UI / UX / Accessibility**](goals/14-frontend-ui-ux-accessibility.md) | Improve the real interface through browser-based user journeys, visual evidence, and accessibility checks. |
| [**Documentation Synchronization / Knowledge Transfer**](goals/15-documentation-synchronization.md) | Find documentation drift, verify examples and commands, and make the maintained knowledge trustworthy. |
| [**Security / Privacy Hardening**](goals/16-security-privacy-hardening.md) | Threat-model the scoped system, prove actionable findings, remediate safely, and add lasting protection. |
| [**Reliability / Resilience Hardening**](goals/17-reliability-resilience-hardening.md) | Model failure modes, inject safe faults, improve recovery, and prove reliability objectives. |
| [**API / Integration Contract Compatibility**](goals/18-api-integration-contract-compatibility.md) | Map contracts and consumers, prove compatibility, and evolve interfaces without hidden breakage. |
| [**Observability / Operability**](goals/19-observability-operability.md) | Make system health visible and actionable, then prove it with drills. |
| [**Developer Experience / Tooling**](goals/20-developer-experience-tooling.md) | Make the common developer path work from clean state with clear commands and actionable failures. |
| [**Data Quality / Pipeline Assurance**](goals/21-data-quality-pipeline-assurance.md) | Define data invariants, test the real pipeline, correct root causes, and make quality continuously observable. |
| [**Compliance / Audit Readiness**](goals/22-compliance-audit-readiness.md) | Map controls to implementation and evidence, close technical gaps, and leave an auditable package for qualified human review. |
| [**Test Suite / CI Health**](goals/23-test-suite-ci-health.md) | Find flaky, misleading, slow, skipped, or environment-dependent checks and turn the test pipeline into reliable evidence. |
| [**Infrastructure / Deployment Readiness**](goals/24-infrastructure-deployment-readiness.md) | Verify that the system can be provisioned and deployed consistently, diagnosed after rollout, and safely rolled back before a human authorizes production change. |
| [**Internationalization / Localization Readiness**](goals/27-internationalization-localization-readiness.md) | Find hard-coded locale assumptions, build a locale matrix, test translated and right-to-left experiences, and prove every supported locale works. |
| [**Backup / Restore / Disaster Recovery**](goals/28-backup-restore-disaster-recovery.md) | Define what must survive, create trustworthy backups, restore them in a clean environment, and prove recovery meets the agreed targets. |
| [**Product Analytics / Experimentation Integrity**](goals/29-product-analytics-experimentation-integrity.md) | Define the events and metrics, verify collection end to end, test experiment assignment, and prove the numbers mean what the team thinks they mean. |

</details>

When no preset fits, use the [**Custom Contract-Driven fallback**](skills/shape-goal/templates/custom-contract-driven-goal.md).

<!-- goal-catalog:end -->

## Everything is saved for reuse

```text
GOAL.md                         approved active contract
GOAL_PROGRESS.md                evidence and next action

docs/goals/<goal-id>/
├── SHAPING.md                  questions, answers, corrections, approval
├── CONTRACT.md                 outcome, scope, proof, protections
├── PROGRESS.md                 attempts, evidence, blockers
└── RESULT.md                   result, lessons, residual risk
```

Stable knowledge is promoted into tests, ADRs, documentation, runbooks, fixtures, scripts, benchmarks, design references, or the reusable Project Harness. Sensitive answers are redacted when the repository is not a safe place to store them.

When priorities change, run `shape-goal` again. It can amend, pause, resume, reprioritize, split, supersede, or create a separate follow-on goal without erasing the old decision trail.

## Advanced modes

<details>
<summary><strong>Autonomous and no-skill fallbacks</strong></summary>

Each profile file also contains two advanced `/goal` prompts:

- **Autonomous preflight** — use only when an approved artifact already answers every owner decision.
- **Self-contained preflight** — use when the skills are unavailable.

Both stop as **Approval required** when a human decision is missing. They must not ask a question and keep looping inside `/goal`.

</details>

## Learn more

[`Install`](INSTALL.md) · [`Profiles`](goals/README.md) · [`Quick reference`](QUICK_REFERENCE.md) · [`Architecture`](SKILLS_AND_GOALS.md) · [`Worked example`](examples/complete-brownfield-cycle/) · [`Research`](FULL_REPORT.md)

> **Use conversation to decide what “done” means. Use `/goal` only after “done” is approved and verifiable.**
