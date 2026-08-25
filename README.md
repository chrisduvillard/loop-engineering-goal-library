<div align="center">

# Loop Engineering `/goal` Library

**From vague project intent to verified autonomous completion.**

Portable Agent Skills and copy-ready `/goal` loops for OpenAI Codex, Anthropic Claude Code, and mature brownfield repositories.

[![OpenAI Codex](https://img.shields.io/badge/OpenAI%20Codex-compatible-111827?style=flat-square&logo=openai&logoColor=white)](https://developers.openai.com/codex/use-cases/follow-goals/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97757?style=flat-square)](https://docs.anthropic.com/en/docs/claude-code/goal)
[![Validation](https://img.shields.io/github/actions/workflow/status/chrisduvillard/loop-engineering-goal-library/validate.yml?branch=main&style=flat-square&label=validation)](https://github.com/chrisduvillard/loop-engineering-goal-library/actions/workflows/validate.yml)
![Brownfield first](https://img.shields.io/badge/focus-brownfield--first-2563EB?style=flat-square)
![Skills](https://img.shields.io/badge/agent%20skills-2-7C3AED?style=flat-square)
![Profiles](https://img.shields.io/badge/execution%20profiles-11-16A34A?style=flat-square)

```text
Shape → Contract → Goal → Execute → Verify → Finish
```

</div>

> [!IMPORTANT]
> A long-running `/goal` should not invent what “done” means while already executing. `shape-goal` defines the contract, `goal-engine` executes it safely, and the host's native `/goal` provides persistence and completion evaluation.

## Quick start

### 1. Install both skills

```bash
npx skills add chrisduvillard/loop-engineering-goal-library --skill '*'
```

### 2. Shape the target

Not sure what `TARGET` should be? That is exactly what `shape-goal` solves.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Continue this project` | `$shape-goal Continue this project` |

It reads the repository first, reconciles stale plans and current evidence, asks only decisions it cannot derive, selects an execution profile, and writes an approved Goal Contract such as `GOAL.md`.

### 3. Start the native goal

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use the selected execution profile. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; leave a restartable handoff.
```

Already have a precise approved issue, PRD, or milestone? Point the command at it and skip shaping.

```text
Rough intent → shape-goal → Goal Contract → /goal + goal-engine → Passing evidence
```

## How the pieces fit

| Component | Responsibility |
|---|---|
| [`shape-goal`](skills/shape-goal/SKILL.md) | Decide and persist what “done” means |
| [Goal Contract](skills/shape-goal/goal-contract-template.md) | Hold the outcome, scope, evidence, protected behavior, and boundaries |
| [`goal-engine`](skills/goal-engine/SKILL.md) | Apply brownfield-safe execution, verification, review, and state management |
| Native `/goal` | Keep work running and evaluate the stopping condition |

> **Skills carry reusable process. The contract carries project truth. Evidence earns the right to say “done.”**

## Execution profiles

Seven profiles cover most long-running work in an established codebase.

| | Profile | Best for |
|---:|---|---|
| 🧭 | [**Brownfield Continue / Finish**](goals/01-brownfield-continue-finish.md) | Advancing unfinished work to an approved outcome |
| 📐 | [**PRD / Spec Compliance**](goals/02-prd-spec-compliance.md) | Closing every verified requirement gap |
| 🎯 | [**Next Milestone**](goals/03-next-milestone.md) | Delivering one coherent increment without scope sprawl |
| 🔎 | [**Deep Audit + Remediation**](goals/04-deep-audit-remediation.md) | Proving findings, fixing root causes, and preventing recurrence |
| 🧪 | [**QA / Regression / UAT**](goals/05-qa-regression-uat.md) | Exercising the real product until acceptance flows pass |
| 🏗️ | [**Safe Refactor / Modernization**](goals/06-safe-refactor-modernization.md) | Improving internals while proving behavioral equivalence |
| 🚀 | [**Release Readiness**](goals/07-release-readiness.md) | Removing release blockers without publishing or deploying |

Specialist profiles cover [incident recovery](goals/08-incident-recovery.md), [dependency upgrades](goals/09-dependency-framework-upgrade.md), [data migrations](goals/10-data-migration-integrity.md), and [branch rescue](goals/11-branch-rescue-integration.md).

## Brownfield guarantees

- **Actual state first** — reconcile instructions, code, tests, runtime behavior, documentation, and Git history before editing.
- **Small reversible changes** — verify each gap, change one coherent slice, and keep or revert based on evidence.
- **Repository-native proof** — use the project's own checks and surface results before claiming completion.
- **Durable bounded autonomy** — preserve user work, record progress, detect stalls, and stop at approval or irreversible-action boundaries.

## No skills installed?

Every file under [`goals/`](goals/) also contains a self-contained `/goal` command. The skill-backed workflow is shorter and easier to maintain; the standalone goals remain the portable fallback.

## Explore

[**Skills + goals architecture**](SKILLS_AND_GOALS.md) · [**Quick reference**](QUICK_REFERENCE.md) · [**Core profiles**](GOAL_LIBRARY.md) · [**Specialist profiles**](SPECIALIST_LOOPS.md) · [**Research**](FULL_REPORT.md) · [**Sources**](SOURCES.md)

---

<sub>Research checked against current sources on August 25, 2026. No license has been added; public visibility alone does not grant redistribution rights.</sub>
