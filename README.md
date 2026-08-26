<div align="center">

# Loop Engineering for AI Coding Agents

### Shape the right goal. Then let the agent finish it.

Portable Agent Skills and reusable execution profiles for OpenAI Codex, Anthropic Claude Code, and mature brownfield repositories.

[![OpenAI Codex](https://img.shields.io/badge/OpenAI%20Codex-compatible-111827?style=flat-square&logo=openai&logoColor=white)](https://learn.chatgpt.com/use-cases/follow-goals)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97757?style=flat-square)](https://code.claude.com/docs/en/goal)
[![Validation](https://img.shields.io/github/actions/workflow/status/chrisduvillard/loop-engineering-goal-library/validate.yml?branch=main&style=flat-square&label=validation)](https://github.com/chrisduvillard/loop-engineering-goal-library/actions/workflows/validate.yml)
![Version](https://img.shields.io/badge/version-0.6.0-7C3AED?style=flat-square)
![Profiles](https://img.shields.io/badge/profiles-24-16A34A?style=flat-square)

```text
shape-goal → answer → approve → /goal + goal-engine → verify → archive → reuse
```

</div>

> [!IMPORTANT]
> **`shape-goal` is the main command.** Run it outside an active `/goal`. It investigates the repository, asks one material question, saves your answer, and returns control. Only after you approve the Goal Contract should autonomous `/goal` execution begin.

## Quick start

### 1. Install the two skills

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' --global --agent codex --agent claude-code --yes
```

Verify:

```bash
npx -y skills@latest list --global --agent codex --agent claude-code
```

You should see:

```text
shape-goal
goal-engine
```

### 2. Open the project and shape its next goal

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Continue this project` | `$shape-goal Continue this project` |

`shape-goal` will:

1. Read repository instructions, Git state, requirements, plans, tests, runtime behavior, and prior goal history.
2. Resolve facts itself before asking you anything.
3. Ask **one owner decision at a time** with evidence and a recommendation.
4. Save every question and answer in `docs/goals/<goal-id>/SHAPING.md`.
5. End the turn after each question so you can reply normally—no Steer message required.

### 3. Approve the Goal Contract

Review only what matters:

- **Outcome** — Is this the result you actually want?
- **Evidence** — Will the proposed checks prove completion?
- **Protection** — What existing behavior, data, and user work must survive?
- **Authority** — Which destructive, production, release, credential, or external actions still need approval?

Not satisfied? Run another round:

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Deepen the current goal` | `$shape-goal Deepen the current goal` |

Earlier questions and answers remain intact; the new round asks only materially new questions.

### 4. Start autonomous execution

After approval, `shape-goal` returns the exact copy-ready command, for example:

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles; preserve reusable state and leave a restartable handoff.
```

Paste it once. `goal-engine` then runs the brownfield loop:

```text
Orient → Reconcile → Select → Verify gap → Change → Check
       → Review → Keep or revert → Record → Repeat
```

## Why shaping and execution are separate

Native `/goal` loops are designed to start another turn automatically until a completion condition is met. That is ideal for implementation, testing, migrations, and remediation—but awkward for an interview that must wait for your answer.

The smooth workflow is therefore:

```text
Interactive conversation                  Autonomous loop
────────────────────────                  ───────────────
shape-goal                                /goal + goal-engine
asks one question and stops               keeps working without prompting
builds and approves the contract           stops on evidence or a real boundary
```

If you already see **“Pursuing goal…”** while a shaping question is waiting:

- **Codex:** run `/goal pause` or `/goal clear`, then `$shape-goal Resume goal-id`.
- **Claude Code:** run `/goal clear`, then `/shape-goal Resume goal-id`.

## Start with a specific profile

You can let `shape-goal` choose automatically, or name a profile directly:

| Need | Claude Code | Codex CLI / IDE |
|---|---|---|
| Finish existing work | `/shape-goal Use the Brownfield Continue / Finish profile` | `$shape-goal Use the Brownfield Continue / Finish profile` |
| Improve UI and UX | `/shape-goal Use the Frontend UI / UX / Accessibility profile` | `$shape-goal Use the Frontend UI / UX / Accessibility profile` |
| Synchronize documentation | `/shape-goal Use the Documentation Synchronization / Knowledge Transfer profile` | `$shape-goal Use the Documentation Synchronization / Knowledge Transfer profile` |
| Repair tests and CI | `/shape-goal Use the Test Suite / CI Health profile` | `$shape-goal Use the Test Suite / CI Health profile` |
| Prepare deployment safely | `/shape-goal Use the Infrastructure / Deployment Readiness profile` | `$shape-goal Use the Infrastructure / Deployment Readiness profile` |

<!-- goal-catalog:start -->

## Goal profiles

Catalog generated from `goals/catalog.json`.

<!-- goal-catalog:end -->

## What gets saved

When the repository has no stronger convention:

```text
GOAL.md                         active approved contract
GOAL_PROGRESS.md                current evidence and next action

docs/goals/
├── PORTFOLIO.md                optional multi-goal coordination
├── INDEX.md                    closed-goal history
└── <goal-id>/
    ├── SHAPING.md              questions, answers, corrections, approval
    ├── CONTRACT.md             approved outcome and boundaries
    ├── PROGRESS.md             attempts, evidence, blockers, next action
    └── RESULT.md               outcome, reusable learning, residual risk
```

Verified learning is promoted into regression tests, ADRs, product documentation, runbooks, fixtures, scripts, benchmarks, design references, or the reusable Project Harness.

Sensitive answers are not committed verbatim when repository visibility or information classification makes that unsafe; the record stores a redacted decision plus an approved secure reference.

## When priorities change

Run `shape-goal` again. It can:

- Clarify or amend the current goal
- Pause and resume it
- Reprioritize several goals
- Split an oversized goal
- Supersede it with a different outcome
- Create a separate follow-on goal

The old decision trail is never silently overwritten.

## Advanced modes

Each file under [`goals/`](goals/) also contains:

- **Autonomous preflight:** for repositories where an approved artifact already resolves every owner decision.
- **Self-contained preflight:** for environments where the skills are unavailable.

These modes deliberately stop as **Approval required** when interaction is needed. They should not ask questions and continue looping inside `/goal`.

## Documentation

| Guide | Purpose |
|---|---|
| [`INSTALL.md`](INSTALL.md) | Install, update, troubleshoot, and package the skills |
| [`goals/README.md`](goals/README.md) | Complete profile catalog |
| [`SKILLS_AND_GOALS.md`](SKILLS_AND_GOALS.md) | Architecture and responsibilities |
| [`QUICK_REFERENCE.md`](QUICK_REFERENCE.md) | Compact operational reference |
| [`examples/complete-brownfield-cycle/`](examples/complete-brownfield-cycle/) | Saved shaping rounds, contract, progress, and result |
| [`FULL_REPORT.md`](FULL_REPORT.md) | Historical research foundation |

## Core principle

> **Use conversation to decide what “done” means. Use `/goal` only after “done” is approved and verifiable.**
