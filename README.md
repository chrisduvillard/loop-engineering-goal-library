<div align="center">

# Loop Engineering

### Shape first. Execute second. Prove it is done.

A reusable workflow for long-running AI coding work in mature repositories.

[![Codex](https://img.shields.io/badge/OpenAI%20Codex-compatible-111827?style=flat-square&logo=openai&logoColor=white)](https://learn.chatgpt.com/use-cases/follow-goals)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97757?style=flat-square)](https://code.claude.com/docs/en/goal)
[![Validation](https://img.shields.io/github/actions/workflow/status/chrisduvillard/loop-engineering-goal-library/validate.yml?branch=main&style=flat-square&label=validation)](https://github.com/chrisduvillard/loop-engineering-goal-library/actions/workflows/validate.yml)
![Version](https://img.shields.io/badge/version-0.6.0-7C3AED?style=flat-square)
![Profiles](https://img.shields.io/badge/profiles-24-16A34A?style=flat-square)

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

Catalog generated from `goals/catalog.json`.

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
