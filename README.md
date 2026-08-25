<div align="center">

# Loop Engineering `/goal` Library

**Adaptive autonomous coding workflows for projects that change over time.**

Portable Agent Skills, reusable state, and copy-ready `/goal` profiles for OpenAI Codex, Anthropic Claude Code, and mature brownfield repositories.

[![OpenAI Codex](https://img.shields.io/badge/OpenAI%20Codex-compatible-111827?style=flat-square&logo=openai&logoColor=white)](https://developers.openai.com/codex/use-cases/follow-goals/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97757?style=flat-square)](https://code.claude.com/docs/en/goal)
[![Validation](https://img.shields.io/github/actions/workflow/status/chrisduvillard/loop-engineering-goal-library/validate.yml?branch=main&style=flat-square&label=validation)](https://github.com/chrisduvillard/loop-engineering-goal-library/actions/workflows/validate.yml)
![Version](https://img.shields.io/badge/version-0.2.0-7C3AED?style=flat-square)
![Brownfield first](https://img.shields.io/badge/focus-brownfield--first-2563EB?style=flat-square)
![Presets](https://img.shields.io/badge/execution%20presets-11-16A34A?style=flat-square)

```text
Portfolio → Shape → Contract → Goal → Verify → Archive → Reprioritize
```

</div>

> [!IMPORTANT]
> A project can have many goals over time. One native `/goal` session or worktree executes one approved, dependency-safe contract. New needs are clarified, queued, reprioritized, paused, split, or superseded—never silently appended to the current goal.

## Install once, use everywhere

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' --global --agent codex --agent claude-code --yes
```

Verify:

```bash
npx -y skills@latest list --global --agent codex --agent claude-code
```

See [`INSTALL.md`](INSTALL.md) for project-local, temporary-use, update, and ZIP-package options.

## Run or change a project

### 1. Ask `shape-goal` for what you need

| Need | Claude Code | Codex CLI / IDE |
|---|---|---|
| Continue or choose the next goal | `/shape-goal Continue this project` | `$shape-goal Continue this project` |
| Add a different goal | `/shape-goal New goal: [INTENT]` | `$shape-goal New goal: [INTENT]` |
| Change current direction | `/shape-goal Change current goal: [NEED]` | `$shape-goal Change current goal: [NEED]` |
| Review priorities | `/shape-goal Review the goal portfolio` | `$shape-goal Review the goal portfolio` |
| Resume saved work | `/shape-goal Resume [GOAL ID]` | `$shape-goal Resume [GOAL ID]` |

`shape-goal` reads the repository first, reconciles current evidence, manages existing goals, asks only material owner decisions, and writes the next approved Goal Contract.

### 2. Start one native goal

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use its selected execution profile, assurance overlays, and project harness. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. At checkpoints, detect material goal drift instead of silently expanding scope. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve reusable state and leave a restartable handoff.
```

Claude Code currently allows one active `/goal` per session, which matches the library's one-contract-per-session rule. Parallel project goals should use isolated sessions and worktrees.

### 3. Preserve the result and choose what follows

Simple active state:

```text
GOAL.md
GOAL_PROGRESS.md
```

When multiple non-closed goals need coordination:

```text
docs/goals/PORTFOLIO.md
```

Terminal evidence remains searchable:

```text
docs/goals/
├── INDEX.md
└── <goal-id>/
    ├── CONTRACT.md
    ├── PROGRESS.md
    └── RESULT.md
```

See the [complete brownfield cycle and next-goal portfolio](examples/complete-brownfield-cycle/).

## Eleven presets—not eleven limits

The standalone goals are reusable **control-loop presets**, not an attempt to enumerate every project.

```text
one primary profile
+ relevant assurance overlays
+ the repository's project harness
+ a custom contract-driven fallback when needed
```

The seven core presets cover continuation, specification compliance, milestones, audit/remediation, QA/UAT, safe refactoring, and release readiness. Specialist presets cover incidents, ecosystem upgrades, data migrations, and branch rescue.

Cross-cutting concerns—security, reliability, performance, cost, UX, accessibility, data governance, compatibility, operability, documentation, and compliance—are selected as [assurance overlays](skills/goal-engine/references/assurance-overlays.md), not duplicated into dozens of goals.

When no preset fits, the Goal Contract defines a **Custom Contract-Driven** loop with an iteration unit, verifier, keep-or-revert rule, review strategy, and objective stop condition. A [standalone custom fallback](skills/shape-goal/templates/custom-contract-driven-goal.md) is included for environments without installed skills.

## Reuse project knowledge instead of rediscovering it

`goal-engine` prefers existing READMEs, instructions, task runners, CI, and runbooks. When setup or verification is repeatedly rediscovered, it creates or refreshes a vendor-neutral [Project Harness](skills/goal-engine/templates/project-harness-template.md) that records verified setup, run, reset, realistic workflows, supported environments, and native checks.

Verified learning is promoted to regression tests, ADRs, product docs, runbooks, fixtures, scripts, benchmarks, or project skills. Secrets, private data, raw production dumps, exploit-enabling evidence, and unnecessary logs are never archived.

## No skills installed?

Every file under [`goals/`](goals/) contains a self-contained standalone `/goal`. Start with the [core library](GOAL_LIBRARY.md), [specialist library](SPECIALIST_LOOPS.md), [custom fallback](skills/shape-goal/templates/custom-contract-driven-goal.md), or [quick reference](QUICK_REFERENCE.md).

## Explore

[**Architecture**](SKILLS_AND_GOALS.md) · [**Quick reference**](QUICK_REFERENCE.md) · [**Example portfolio**](examples/complete-brownfield-cycle/PORTFOLIO.md) · [**Core presets**](GOAL_LIBRARY.md) · [**Specialist presets**](SPECIALIST_LOOPS.md) · [**Research**](FULL_REPORT.md) · [**Roadmap**](ROADMAP.md) · [**Contributing**](CONTRIBUTING.md)

---

<sub>Version 0.2.0. Research checked against current sources on August 25, 2026. License selection remains an explicit pre-1.0 owner decision.</sub>
