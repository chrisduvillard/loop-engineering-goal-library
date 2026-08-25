<div align="center">

# Loop Engineering `/goal` Library

**Safe autonomous coding loops for mature repositories.**

Turn vague intent into an approved target, then keep Codex or Claude Code working until the evidence says it is done.

[![OpenAI Codex](https://img.shields.io/badge/OpenAI%20Codex-compatible-111827?style=flat-square&logo=openai&logoColor=white)](https://developers.openai.com/codex/use-cases/follow-goals/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97757?style=flat-square)](https://docs.anthropic.com/en/docs/claude-code/goal)
![Brownfield first](https://img.shields.io/badge/focus-brownfield--first-2563EB?style=flat-square)
![Skills](https://img.shields.io/badge/agent%20skills-2-7C3AED?style=flat-square)
![Goals](https://img.shields.io/badge/goal%20profiles-11-16A34A?style=flat-square)

```text
Shape → Contract → Goal → Execute → Verify → Finish
```

</div>

> **The rule:** Skills carry reusable process. The Goal Contract carries project truth. Native `/goal` carries persistence. Evidence earns the right to say “done.”

## The recommended workflow

### 1. Install the two skills

```bash
npx skills add chrisduvillard/loop-engineering-goal-library --skill '*'
```

| Skill | Job |
|---|---|
| [`shape-goal`](skills/shape-goal/SKILL.md) | Reads the repository, resolves material ambiguity, and writes an approved Goal Contract |
| [`goal-engine`](skills/goal-engine/SKILL.md) | Executes that contract with brownfield safety, native verification, durable state, and bounded autonomy |

### 2. Shape the target

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Continue this project` | `$shape-goal Continue this project` |

`shape-goal` investigates facts itself, asks only decisions the repository cannot answer, selects the right execution profile, and persists `GOAL.md` or updates an existing issue, PRD, or milestone.

### 3. Start the native goal

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use the execution profile named in the contract. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; leave a restartable handoff.
```

```text
Rough intent → shape-goal → Goal Contract → /goal + goal-engine → Passing evidence
```

Already have a precise approved issue or spec? Point the same command at it and skip shaping.

## The golden set

Seven profiles cover most long-running work in an established codebase.

| | Profile | Best for |
|---:|---|---|
| 🧭 | [**Brownfield Continue / Finish**](goals/01-brownfield-continue-finish.md) | Advancing unfinished work to an approved outcome |
| 📐 | [**PRD / Spec Compliance**](goals/02-prd-spec-compliance.md) | Closing every verified requirement gap |
| 🎯 | [**Next Milestone**](goals/03-next-milestone.md) | Delivering one coherent increment without scope sprawl |
| 🔎 | [**Deep Audit + Remediation**](goals/04-deep-audit-remediation.md) | Proving findings, fixing root causes, preventing recurrence |
| 🧪 | [**QA / Regression / UAT**](goals/05-qa-regression-uat.md) | Exercising the real product until acceptance flows pass |
| 🏗️ | [**Safe Refactor / Modernization**](goals/06-safe-refactor-modernization.md) | Improving internals while proving behavioral equivalence |
| 🚀 | [**Release Readiness**](goals/07-release-readiness.md) | Removing release blockers without publishing or deploying |

Specialist profiles cover [incident recovery](goals/08-incident-recovery.md), [dependency upgrades](goals/09-dependency-framework-upgrade.md), [data migrations](goals/10-data-migration-integrity.md), and [branch rescue](goals/11-branch-rescue-integration.md).

## Why it is safe for brownfield work

- **Actual state first** — reconcile code, tests, runtime behavior, documentation, and Git history before editing.
- **Small reversible changes** — each iteration has a narrow blast radius and a keep-or-revert decision.
- **Native verification** — discover the repository's own checks instead of assuming a stack.
- **Evidence over confidence** — completion requires surfaced results, not “implemented” or “looks correct.”
- **Durable continuity** — progress state records evidence, failures, blockers, and the next action.
- **Bounded authority** — budgets, stalls, external blockers, and irreversible actions have explicit exits.

## Standalone mode

No skills installed? Every file under [`goals/`](goals/) contains a self-contained `/goal` command with the safety discipline embedded directly. The skill-backed workflow is shorter and easier to maintain; the standalone goals remain the portable fallback.

## Explore

[**Skills + goals architecture**](SKILLS_AND_GOALS.md) · [**Quick reference**](QUICK_REFERENCE.md) · [**Core goal library**](GOAL_LIBRARY.md) · [**Specialist loops**](SPECIALIST_LOOPS.md) · [**Full research**](FULL_REPORT.md) · [**Sources**](SOURCES.md)

---

<sub>Research checked against current sources on August 25, 2026. No license has been added; public visibility alone does not grant redistribution rights.</sub>
