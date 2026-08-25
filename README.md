<div align="center">

# Loop Engineering `/goal` Library

**From vague project intent to verified, reusable autonomous completion.**

Portable Agent Skills and copy-ready `/goal` profiles for OpenAI Codex, Anthropic Claude Code, and mature brownfield repositories.

[![OpenAI Codex](https://img.shields.io/badge/OpenAI%20Codex-compatible-111827?style=flat-square&logo=openai&logoColor=white)](https://developers.openai.com/codex/use-cases/follow-goals/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97757?style=flat-square)](https://docs.anthropic.com/en/docs/claude-code/goal)
[![Validation](https://img.shields.io/github/actions/workflow/status/chrisduvillard/loop-engineering-goal-library/validate.yml?branch=main&style=flat-square&label=validation)](https://github.com/chrisduvillard/loop-engineering-goal-library/actions/workflows/validate.yml)
![Version](https://img.shields.io/badge/version-0.1.0-7C3AED?style=flat-square)
![Brownfield first](https://img.shields.io/badge/focus-brownfield--first-2563EB?style=flat-square)
![Profiles](https://img.shields.io/badge/execution%20profiles-11-16A34A?style=flat-square)

```text
Shape → Contract → Goal → Execute → Verify → Archive → Reuse
```

</div>

> [!IMPORTANT]
> A long-running `/goal` should not invent what “done” means while already executing. `shape-goal` defines the contract, `goal-engine` executes it safely, and the host's native `/goal` provides persistence and completion evaluation.

## Install once, use everywhere

Install both skills globally for Codex and Claude Code:

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' \
  --global \
  --agent codex \
  --agent claude-code \
  --yes
```

Verify:

```bash
npx -y skills@latest list --global --agent codex --agent claude-code
```

Full installation, project-local, temporary-use, update, and ZIP-package options are in [`INSTALL.md`](INSTALL.md).

## Run a project

### 1. Shape an unclear target

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Continue this project` | `$shape-goal Continue this project` |

`shape-goal` reads the repository first, reconciles stale plans with current evidence, asks only decisions it cannot derive, selects an execution profile, and persists an approved Goal Contract.

### 2. Start the native goal

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use the selected execution profile. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve a reusable closeout packet and leave a restartable handoff.
```

Already have a precise approved issue, PRD, or milestone? Point the command at it and skip shaping.

### 3. Archive and reuse

Active state stays easy to find:

```text
GOAL.md
GOAL_PROGRESS.md
```

Every terminal outcome—success, blocker, approval required, exhausted budget, stall, or supersession—gets a durable packet:

```text
docs/goals/
├── INDEX.md
└── <goal-id>/
    ├── CONTRACT.md
    ├── PROGRESS.md
    └── RESULT.md
```

Verified learning is promoted to its permanent home: regression tests, ADRs, product docs, runbooks, fixtures, scripts, or benchmarks. Secrets, private data, production dumps, and unnecessary large logs are never archived.

See the [complete fictional brownfield cycle](examples/complete-brownfield-cycle/).

## How the pieces fit

| Component | Responsibility |
|---|---|
| [`shape-goal`](skills/shape-goal/SKILL.md) | Decide and persist what “done” means |
| [Goal Contract](skills/shape-goal/goal-contract-template.md) | Hold the outcome, scope, proof, protected behavior, authority, and archive paths |
| [`goal-engine`](skills/goal-engine/SKILL.md) | Orient, implement, verify, review, checkpoint, and preserve reusable results |
| Native `/goal` | Keep work running and evaluate the stopping condition |
| Closeout archive | Make every completed or interrupted run searchable and reusable |

> **Skills carry reusable process. The contract carries project truth. Evidence earns the right to say “done.”**

## Choose an execution profile

| Profile | Best for |
|---|---|
| [Brownfield Continue / Finish](goals/01-brownfield-continue-finish.md) | Advancing unfinished work to an approved outcome |
| [PRD / Spec Compliance](goals/02-prd-spec-compliance.md) | Closing every verified requirement gap |
| [Next Milestone](goals/03-next-milestone.md) | Delivering one coherent increment without scope sprawl |
| [Deep Audit + Remediation](goals/04-deep-audit-remediation.md) | Proving findings, fixing root causes, and preventing recurrence |
| [QA / Regression / UAT](goals/05-qa-regression-uat.md) | Exercising the real product until acceptance flows pass |
| [Safe Refactor / Modernization](goals/06-safe-refactor-modernization.md) | Improving internals while proving behavioral equivalence |
| [Release Readiness](goals/07-release-readiness.md) | Removing release blockers without publishing or deploying |

Specialist profiles cover [incident recovery](goals/08-incident-recovery.md), [dependency upgrades](goals/09-dependency-framework-upgrade.md), [data migrations](goals/10-data-migration-integrity.md), and [branch rescue](goals/11-branch-rescue-integration.md).

## Update without drift

```bash
npx -y skills@latest update shape-goal goal-engine --global --yes
```

The repository keeps one source of truth:

- Individual files under [`goals/`](goals/) are canonical.
- Consolidated libraries are generated and checked in CI.
- Skill metadata, `VERSION`, and [`CHANGELOG.md`](CHANGELOG.md) stay aligned.
- CI validates links, lifecycle schemas, CLI discovery, and deterministic ZIP packages.
- Packaged skills are uploaded as a workflow artifact on every validated change.

## No skills installed?

Every canonical profile contains a self-contained standalone `/goal` fallback. Start with the [core library](GOAL_LIBRARY.md), [specialist library](SPECIALIST_LOOPS.md), or [quick reference](QUICK_REFERENCE.md).

## Explore

[**Install & update**](INSTALL.md) · [**Skills + goals architecture**](SKILLS_AND_GOALS.md) · [**Complete example**](examples/complete-brownfield-cycle/) · [**Core profiles**](GOAL_LIBRARY.md) · [**Specialist profiles**](SPECIALIST_LOOPS.md) · [**Research**](FULL_REPORT.md) · [**Roadmap**](ROADMAP.md) · [**Contributing**](CONTRIBUTING.md)

---

<sub>Version 0.1.0. Research checked against current sources on August 25, 2026. License selection remains an explicit pre-1.0 owner decision.</sub>
