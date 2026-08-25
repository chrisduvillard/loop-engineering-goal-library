<div align="center">

# Loop Engineering `/goal` Library

**Know what to do next, run it safely, and keep the evidence for later.**

Portable Agent Skills and copy-ready `/goal` loops for OpenAI Codex, Anthropic Claude Code, and mature brownfield repositories.

[![OpenAI Codex](https://img.shields.io/badge/OpenAI%20Codex-compatible-111827?style=flat-square&logo=openai&logoColor=white)](https://developers.openai.com/codex/use-cases/follow-goals/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97757?style=flat-square)](https://code.claude.com/docs/en/goal)
[![Validation](https://img.shields.io/github/actions/workflow/status/chrisduvillard/loop-engineering-goal-library/validate.yml?branch=main&style=flat-square&label=validation)](https://github.com/chrisduvillard/loop-engineering-goal-library/actions/workflows/validate.yml)
![Version](https://img.shields.io/badge/version-0.3.0-7C3AED?style=flat-square)
![Brownfield first](https://img.shields.io/badge/focus-brownfield--first-2563EB?style=flat-square)
![Presets](https://img.shields.io/badge/standalone%20goals-13-16A34A?style=flat-square)

```text
Portfolio → Shape → Contract → Execute → Verify → Archive → Next goal
```

</div>

> [!IMPORTANT]
> A project can have many goals over time, but one native `/goal` session or worktree should execute one approved, dependency-safe Goal Contract. New requests are queued, reprioritized, paused, split, or superseded—never silently added to the current goal.

## Step-by-step example

This is the recommended workflow for an existing project when you are not yet sure what the exact target should be.

### 0. Install both skills once

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' --global --agent codex --agent claude-code --yes
```

Verify the installation:

```bash
npx -y skills@latest list --global --agent codex --agent claude-code
```

You should see `shape-goal` and `goal-engine`. More installation and update options are in [`INSTALL.md`](INSTALL.md).

### 1. Open the project and shape the next goal

Start Codex or Claude Code from the repository root, then run:

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Continue this project` | `$shape-goal Continue this project` |

You do **not** need to invent a perfect `TARGET`. `shape-goal` reads the repository, current Git state, instructions, PRDs, plans, progress, tests, prior goals, and native commands. It asks only owner decisions it cannot derive.

For a new request later, use:

| Need | Claude Code | Codex CLI / IDE |
|---|---|---|
| Add another goal | `/shape-goal New goal: [INTENT]` | `$shape-goal New goal: [INTENT]` |
| Change direction | `/shape-goal Change current goal: [NEED]` | `$shape-goal Change current goal: [NEED]` |
| Review priorities | `/shape-goal Review the goal portfolio` | `$shape-goal Review the goal portfolio` |
| Resume saved work | `/shape-goal Resume [GOAL ID]` | `$shape-goal Resume [GOAL ID]` |

### 2. Review the proposed Goal Contract

`shape-goal` returns a launch packet similar to:

```text
Lifecycle decision: NEW
Approved target: The documented portfolio import workflow passes all acceptance flows without regressing exports.
Goal ID / revision: 2026-08-25-portfolio-import-v1-4 / 1
Contract: GOAL.md
Execution profile: PRD / Spec Compliance
Assurance overlays: Data Integrity & Governance
Project harness: existing repository scripts and CI
Progress state: GOAL_PROGRESS.md
Archive: docs/goals/2026-08-25-portfolio-import-v1-4/
Run with goal-engine: /goal ...
```

Before approving it, check only four things:

1. **Outcome** — Is this the result you actually want?
2. **Evidence** — Will the listed commands or workflows prove completion?
3. **Protection** — Does it name the behavior and user work that must survive?
4. **Authority** — Are deployments, destructive actions, credentials, and other irreversible boundaries explicit?

After approval, the contract is saved in `GOAL.md` or an existing authoritative issue, PRD, or milestone.

### 3. Start the native `/goal`

Copy the command returned by `shape-goal`. The universal form is:

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use its selected execution profile, assurance overlays, and project harness. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. At checkpoints, detect material goal drift instead of silently expanding scope. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve reusable state and leave a restartable handoff.
```

`goal-engine` then orients from the real repository state, chooses the next unblocked gap, makes small reversible changes, runs repository-native checks, adds regression protection, reviews important diffs, and keeps working until the evidence satisfies the contract.

### 4. Follow progress without steering every step

When the repository has no stronger progress system, the active files are:

```text
GOAL.md             approved target and boundaries
GOAL_PROGRESS.md    baseline, acceptance ledger, evidence, attempts, blockers, and next action
```

The agent should continue autonomously when the contract and repository answer what comes next. Check the progress file or the host's native goal status when you want a summary.

### 5. Handle a new need safely

Do not append unrelated work to the active contract. Run `shape-goal` again. It decides whether to:

- clarify or amend the same goal;
- pause and resume it later;
- reprioritize a different ready goal;
- split an oversized goal;
- supersede it with a new Goal ID; or
- add the new request to `docs/goals/PORTFOLIO.md` or the project's existing tracker.

Parallel goals use separate sessions and worktrees with explicit ownership and dependency rules.

### 6. Close, archive, and reuse

Every terminal outcome—achieved, blocked, cancelled, superseded, budget-exhausted, or stalled—preserves a searchable packet:

```text
docs/goals/
├── PORTFOLIO.md          optional non-closed goal coordination
├── INDEX.md              closed-goal history
└── <goal-id>/
    ├── CONTRACT.md       what was approved
    ├── PROGRESS.md       evidence, attempts, blockers, and final state
    └── RESULT.md         outcome, delivered behavior, lessons, and residual risk
```

Verified learning is promoted to its permanent home: regression tests, ADRs, product docs, runbooks, fixtures, scripts, benchmarks, or the reusable Project Harness. Secrets, private data, production dumps, exploit-enabling evidence, and unnecessary large logs are never archived.

See the [complete brownfield example](examples/complete-brownfield-cycle/) for finished contract, progress, result, and follow-on portfolio files.

## All 13 standalone goals

With the skills installed, `shape-goal` normally selects the right profile for you. Every linked file also contains a fully self-contained standalone `/goal` for environments where the skills are not installed.

### Core goals

| Goal | In simple terms | Use it when |
|---|---|---|
| [**Brownfield Continue / Finish**](goals/01-brownfield-continue-finish.md) | Understand the current repository and keep completing the most important unblocked work. | The project already has an approved outcome, plan, partial implementation, or unfinished milestone. |
| [**PRD / Spec Compliance**](goals/02-prd-spec-compliance.md) | Compare the real product with its requirements and close every proven gap. | A PRD, specification, contract, or acceptance checklist is the source of truth. |
| [**Next Milestone**](goals/03-next-milestone.md) | Deliver one coherent next step without wandering into the whole backlog. | The roadmap is large and you want the next dependency-safe milestone finished end to end. |
| [**Deep Audit + Remediation**](goals/04-deep-audit-remediation.md) | Find important problems, prove they are real, fix their root causes, and prevent recurrence. | You need a serious codebase, architecture, reliability, security, or product-health audit. |
| [**QA / Regression / UAT**](goals/05-qa-regression-uat.md) | Exercise the actual product and realistic user workflows until the required flows pass. | Unit tests are not enough, a release has regressions, or you need end-to-end/UAT confidence. |
| [**Safe Refactor / Modernization**](goals/06-safe-refactor-modernization.md) | Improve internals while proving users and integrations still see the same behavior. | You are restructuring architecture, reducing technical debt, or modernizing implementation safely. |
| [**Release Readiness**](goals/07-release-readiness.md) | Remove every verified release blocker without actually publishing or deploying. | A version or milestone should become ready for a separate human release decision. |

### Specialist goals

| Goal | In simple terms | Use it when |
|---|---|---|
| [**Incident Recovery / Stabilization**](goals/08-incident-recovery.md) | Contain damage, restore health, prove the root cause, and add prevention. | A severe regression, outage, corrupted workflow, or production-like incident needs controlled recovery. |
| [**Dependency / Framework Upgrade**](goals/09-dependency-framework-upgrade.md) | Upgrade through safe version steps while checking the whole compatibility surface. | A dependency, framework, runtime, language, or toolchain must move to a target version. |
| [**Data Migration / Integrity**](goals/10-data-migration-integrity.md) | Change schemas or stored data while proving correctness, restartability, and recovery. | You need a schema change, backfill, format conversion, data move, or cutover. |
| [**Branch Rescue / Integration**](goals/11-branch-rescue-integration.md) | Recover the useful parts of stale or divergent work without overwriting newer behavior. | Valuable work is stranded in an old, conflicting, oversized, or abandoned branch. |
| [**Measured Optimization / Benchmark**](goals/12-measured-optimization-benchmark.md) | Freeze a baseline, test one challenger at a time, and keep only measurable wins. | You need to improve latency, throughput, cost, memory, build time, model quality, ranking accuracy, or another stable metric. |
| [**Technical Spike / Feasibility**](goals/13-technical-spike-feasibility.md) | Run a small isolated experiment to answer a technical question and make a Go / Conditional Go / No-Go decision. | You must evaluate an architecture, vendor, integration, migration, algorithm, or risky approach before production commitment. |

### When none fits

Use the [**Custom Contract-Driven fallback**](skills/shape-goal/templates/custom-contract-driven-goal.md). The contract must define a bounded iteration, primary verifier, keep-or-revert rule, review strategy, and objective stop condition. This gives unusual projects a safe path without turning the library into dozens of overlapping prompts.

## Add the proof your project needs

The primary goal controls **how the work progresses**. Assurance overlays add cross-cutting proof without creating duplicate goals:

- Security & Privacy
- Reliability & Recovery
- Performance & Cost
- UX & Accessibility
- Data Integrity & Governance
- Compatibility & Portability
- Operability & Observability
- Documentation & Knowledge Transfer
- Compliance & Auditability

See [`assurance-overlays.md`](skills/goal-engine/references/assurance-overlays.md).

## Reuse project mechanics instead of rediscovering them

`goal-engine` prefers existing READMEs, instructions, task runners, CI, and runbooks. When setup, run, reset, supported environments, or verification commands are fragmented, it creates or refreshes a vendor-neutral [Project Harness](skills/goal-engine/templates/project-harness-template.md).

## Update the installed skills

```bash
npx -y skills@latest update shape-goal goal-engine --global --yes
```

## Explore

[**Quick reference**](QUICK_REFERENCE.md) · [**Architecture**](SKILLS_AND_GOALS.md) · [**Core goal library**](GOAL_LIBRARY.md) · [**Specialist goal library**](SPECIALIST_LOOPS.md) · [**Complete example**](examples/complete-brownfield-cycle/) · [**Research**](FULL_REPORT.md) · [**Roadmap**](ROADMAP.md) · [**Contributing**](CONTRIBUTING.md)

---

<sub>Version 0.3.0. Research checked against current sources on August 25, 2026. License selection remains an explicit pre-1.0 owner decision.</sub>
