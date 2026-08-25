<div align="center">

# Loop Engineering `/goal` Library

**Safe autonomous coding loops for mature repositories.**

Turn vague intent into a verified target, then keep Codex or Claude Code working until the evidence says it is done.

[![OpenAI Codex](https://img.shields.io/badge/OpenAI%20Codex-compatible-111827?style=flat-square&logo=openai&logoColor=white)](https://developers.openai.com/codex/use-cases/follow-goals/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97757?style=flat-square)](https://docs.anthropic.com/en/docs/claude-code/goal)
![Brownfield first](https://img.shields.io/badge/focus-brownfield--first-2563EB?style=flat-square)
![Copy-ready goals](https://img.shields.io/badge/copy--ready%20goals-11-16A34A?style=flat-square)
![Goal shaper](https://img.shields.io/badge/skill-shape--goal-7C3AED?style=flat-square)

```text
Orient → Reconcile → Select → Change → Verify → Review → Record → Repeat
```

</div>

> **The rule:** Give the agent a state to reach, a check that decides, a boundary it cannot cross, and a record the next iteration can trust.

## Start here

### You do not know the target yet

That is normal. `TARGET` is not a task list or a perfect project description. It is a **verifiable outcome** or a pointer to an approved issue, PRD, milestone, or Goal Contract.

Install the portable [`shape-goal`](skills/shape-goal/SKILL.md) skill:

```bash
npx skills add chrisduvillard/loop-engineering-goal-library --skill shape-goal
```

Then run:

```text
/shape-goal Continue this project
```

It reads the repository first, reconciles stale state, asks only decisions it cannot derive, writes an approved [Goal Contract](skills/shape-goal/goal-contract-template.md), selects the right loop, and returns the exact `/goal` command.

```text
Rough intent → /shape-goal → Goal Contract → /goal → Passing evidence
```

### You already know the target

Use the **[Universal Brownfield Goal](templates/universal-brownfield-goal.md)**, or the **[Ultra-Short Default](templates/ultra-short-default-goal.md)** when the repository already has strong instructions, plans, and tests.

## The golden set

These seven loops cover most long-running work in an established codebase.

| | Loop | Best for |
|---:|---|---|
| 🧭 | [**Brownfield Continue / Finish**](goals/01-brownfield-continue-finish.md) | Advancing an unfinished project to an approved outcome |
| 📐 | [**PRD / Spec Compliance**](goals/02-prd-spec-compliance.md) | Closing every verified requirement gap |
| 🎯 | [**Next Milestone**](goals/03-next-milestone.md) | Delivering one coherent increment without scope sprawl |
| 🔎 | [**Deep Audit + Remediation**](goals/04-deep-audit-remediation.md) | Proving findings, fixing root causes, preventing recurrence |
| 🧪 | [**QA / Regression / UAT**](goals/05-qa-regression-uat.md) | Exercising the real product until acceptance flows pass |
| 🏗️ | [**Safe Refactor / Modernization**](goals/06-safe-refactor-modernization.md) | Improving internals while proving behavioral equivalence |
| 🚀 | [**Release Readiness**](goals/07-release-readiness.md) | Removing release blockers without publishing or deploying |

## Specialist extensions

| | Loop | Best for |
|---:|---|---|
| 🚨 | [**Incident Recovery / Stabilization**](goals/08-incident-recovery.md) | Containment, recovery, root cause, and prevention |
| ⬆️ | [**Dependency / Framework Upgrade**](goals/09-dependency-framework-upgrade.md) | Staged upgrades with compatibility evidence |
| 🗃️ | [**Data Migration / Integrity**](goals/10-data-migration-integrity.md) | Reversible schema or data changes with reconciliation |
| 🌿 | [**Branch Rescue / Integration**](goals/11-branch-rescue-integration.md) | Recovering valuable work from divergent branches |

## Why these loops are safe

- **Actual state first** — reconcile code, tests, runtime behavior, documentation, and Git history before editing.
- **Small reversible changes** — every iteration has a narrow blast radius and a keep-or-revert decision.
- **Native verification** — discover the repository's own checks instead of assuming a stack.
- **Evidence over confidence** — completion requires surfaced results, not “implemented” or “looks correct.”
- **Durable continuity** — progress and handoff artifacts record evidence, failures, blockers, and the next action.
- **Bounded autonomy** — stagnation, budgets, external blockers, and irreversible actions have explicit exits.

## Explore

[**Quick reference**](QUICK_REFERENCE.md) · [**All core loops**](GOAL_LIBRARY.md) · [**Specialist loops**](SPECIALIST_LOOPS.md) · [**Full research**](FULL_REPORT.md) · [**Sources**](SOURCES.md) · [**Safety kernel**](templates/brownfield-safety-kernel.md)

The prompts and `shape-goal` skill follow the portable Agent Skills format and avoid required models, frameworks, package managers, test runners, or vendor-specific subagent syntax.

---

<sub>Research checked against current sources on August 25, 2026. No license has been added; public visibility alone does not grant redistribution rights.</sub>
