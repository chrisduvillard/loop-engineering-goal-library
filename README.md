<div align="center">

# Loop Engineering `/goal` Library

**Safe, reusable autonomous coding loops for mature repositories.**

Turn “keep working” into a controlled system with evidence, rollback, durable state, and an objective finish line.

[![OpenAI Codex](https://img.shields.io/badge/OpenAI%20Codex-compatible-111827?style=flat-square&logo=openai&logoColor=white)](https://developers.openai.com/codex/use-cases/follow-goals/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97757?style=flat-square)](https://docs.anthropic.com/en/docs/claude-code/goal)
![Brownfield first](https://img.shields.io/badge/focus-brownfield--first-2563EB?style=flat-square)
![Copy-ready goals](https://img.shields.io/badge/copy--ready%20goals-11-16A34A?style=flat-square)

```text
Orient → Reconcile → Select → Change → Verify → Review → Record → Repeat
```

</div>

> **The rule:** Never ask an autonomous agent to “make it better.” Give it a state to reach, a check that decides, a boundary it cannot cross, and a record the next iteration can trust.

## Start here

```text
/goal Bring this existing project to [TARGET]...
```

Use the **[Universal Brownfield Goal](templates/universal-brownfield-goal.md)** for maximum safety, or the **[Ultra-Short Default](templates/ultra-short-default-goal.md)** when the repository already has strong instructions, plans, and tests.

## The golden set

These seven loops cover most long-running work in an established codebase.

| | Loop | Best for |
|---:|---|---|
| 🧭 | [**Brownfield Continue / Finish**](goals/01-brownfield-continue-finish.md) | Safely advancing an unfinished project to a defined target |
| 📐 | [**PRD / Spec Compliance**](goals/02-prd-spec-compliance.md) | Closing every verified requirement gap |
| 🎯 | [**Next Milestone**](goals/03-next-milestone.md) | Delivering one coherent increment without scope sprawl |
| 🔎 | [**Deep Audit + Remediation**](goals/04-deep-audit-remediation.md) | Proving findings, fixing root causes, and preventing recurrence |
| 🧪 | [**QA / Regression / UAT**](goals/05-qa-regression-uat.md) | Exercising the real product until acceptance flows pass |
| 🏗️ | [**Safe Refactor / Modernization**](goals/06-safe-refactor-modernization.md) | Improving internals while proving behavioral equivalence |
| 🚀 | [**Release Readiness**](goals/07-release-readiness.md) | Removing release blockers without publishing or deploying |

## Specialist extensions

Keep these for situations with a distinct risk model that generic loops can miss.

| | Loop | Best for |
|---:|---|---|
| 🚨 | [**Incident Recovery / Stabilization**](goals/08-incident-recovery.md) | Containment, recovery, root cause, and prevention |
| ⬆️ | [**Dependency / Framework Upgrade**](goals/09-dependency-framework-upgrade.md) | Staged ecosystem upgrades with compatibility evidence |
| 🗃️ | [**Data Migration / Integrity**](goals/10-data-migration-integrity.md) | Reversible schema or data changes with reconciliation |
| 🌿 | [**Branch Rescue / Integration**](goals/11-branch-rescue-integration.md) | Recovering valuable work from divergent or stale branches |

## Why these loops are safe

- **Actual state first.** Code, tests, runtime behavior, documentation, and Git history are reconciled before editing.
- **Small reversible changes.** Each iteration has a narrow blast radius and a keep-or-revert decision.
- **Native verification.** The agent discovers the repository’s own checks instead of assuming a stack.
- **Evidence over confidence.** Completion requires surfaced results, not “implemented” or “looks correct.”
- **Durable continuity.** Existing progress and handoff artifacts record evidence, failures, blockers, and the next action.
- **Bounded autonomy.** Stagnation, budgets, external blockers, and irreversible actions have explicit exits.

## Explore

[**Quick reference**](QUICK_REFERENCE.md) · [**All core loops**](GOAL_LIBRARY.md) · [**Specialist loops**](SPECIALIST_LOOPS.md) · [**Full research report**](FULL_REPORT.md) · [**Sources**](SOURCES.md) · [**Safety kernel**](templates/brownfield-safety-kernel.md)

The prompts are deliberately vendor-neutral: no required model, framework, package manager, test runner, or subagent syntax. They describe the repository operation and evidence contract so Codex and Claude Code can apply their own native goal machinery.

---

<sub>Research checked against current sources on August 25, 2026. No license has been added; public visibility alone does not grant redistribution rights.</sub>
