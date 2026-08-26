---
name: shape-goal
description: Resolve vague, incomplete, or changing project needs into an approved Goal Contract and managed goal portfolio. Also powers zero-friction /goal launchers by discovering every profile-specific input from repository and connected evidence before asking the user, preserving every asked question and answer in durable shaping rounds, asking only material owner decisions one at a time, then handing the approved contract to goal-engine. Use before production execution, for another deeper shaping round, or whenever the target, priority, scope, proof, lifecycle, profile, or boundaries are unclear.
compatibility: Portable Agent Skills host. Reads repository and connected authoritative evidence and writes planning/state artifacts; production implementation remains the responsibility of goal-engine.
user-invocable: true
disable-model-invocation: false
argument-hint: "[continue | new goal | deepen | profile | goal ID | changed need]"
metadata:
  author: chrisduvillard
  version: "0.5.0"
  source: "github.com/chrisduvillard/loop-engineering-goal-library"
---

# Shape Goal

Turn rough or changing intent into one safe, approved, executable contract while preserving the full decision trail.

> **Search facts first. Ask only decisions. Save every asked question and answer. Never let shaping masquerade as implementation or completion.**

```text
project need → evidence search → shaping rounds → approved contract → goal-engine
```

## Non-negotiable invariants

- No production edit before an explicitly approved Goal Contract.
- Search repository and connected authoritative evidence before asking the user.
- Save every asked question and safe answer in append-only `SHAPING.md`; corrections append and supersede.
- A dissatisfied user may request repeated deeper, non-duplicate shaping rounds.
- Use the actual persisted contract reference in every handoff; `GOAL.md` is only the default fallback.
- Contract creation is not completion: after approval, hand off to `goal-engine` and continue until evidence passes.
- Material goal drift pauses execution and reopens shaping without rewriting prior decisions.

## Invocation modes

These are natural-language modes, not a rigid parser.

| Need | Claude Code | Codex CLI / IDE |
|---|---|---|
| Continue or shape the next goal | `/shape-goal Continue this project` | `$shape-goal Continue this project` |
| Add a new goal | `/shape-goal New goal: describe the intent` | `$shape-goal New goal: describe the intent` |
| Change the current goal | `/shape-goal Change current goal: describe the need` | `$shape-goal Change current goal: describe the need` |
| Go deeper before approval | `/shape-goal Deepen the current goal` | `$shape-goal Deepen the current goal` |
| Challenge a saved goal | `/shape-goal Run another shaping round for goal-id` | `$shape-goal Run another shaping round for goal-id` |
| Review priorities | `/shape-goal Review the goal portfolio` | `$shape-goal Review the goal portfolio` |
| Resume prior shaping or work | `/shape-goal Resume goal-id` | `$shape-goal Resume goal-id` |

Other Agent Skills hosts should explicitly select or mention `shape-goal`.

## Zero-friction bootstrap

A copied standalone `/goal` may name both `shape-goal` and `goal-engine` without supplying repository-specific placeholders. In that mode:

1. The launcher fixes the primary profile.
2. This skill resolves every required input and records the shaping history.
3. Production edits remain forbidden during shaping.
4. The user may approve, request another deeper round, or pause.
5. After approval, hand off inside the same native goal to `goal-engine`.
6. The native goal is **not complete** when the contract is created.

Read all three references whenever bootstrap mode is active:

- [references/input-resolution.md](references/input-resolution.md)
- [references/profile-inputs.md](references/profile-inputs.md)
- [references/shaping-history.md](references/shaping-history.md)

## Required outputs

Produce and persist, as applicable:

1. Lifecycle decision for every affected goal
2. Stable Goal ID and revision
3. Durable shaping-history path containing every asked question and answer
4. Completed shaping-round IDs, summaries, corrections, and deferred decisions
5. Approved Goal Contract for the next executable outcome
6. Portfolio disposition when several non-closed goals exist
7. One primary profile or a Custom Contract-Driven definition
8. Required assurance overlays
9. Reused or newly verified project-harness path
10. Progress, archive, and history paths
11. Copy-ready native `/goal` handoff
12. Standalone fallback reference
13. Input ledger showing how every material field was resolved

## 1. Orient before asking

Read the applicable:

- Repository and agent instructions
- Git status, diff, branch, worktrees, and relevant history
- Current contract, shaping history, progress, portfolio, handoffs, and prior goal archives
- Approved issues, PRDs, specifications, plans, milestones, ADRs, architecture, and design references
- Native scripts, task runners, package configuration, CI, tests, fixtures, benchmarks, and release gates
- Runtime entry points, actual product behavior, screenshots, logs, and generated artifacts
- Project Harness and supported-environment documentation
- Connected authoritative systems available to the host

Reconcile contradictions by authority, approved recency, and executable evidence. Protect uncommitted and unrelated work.

**Facts are the agent's job; decisions are the user's.**

## 2. Initialize or resume durable shaping history

As soon as a stable Goal ID exists, use the repository's existing decision log when it is suitable; otherwise create:

```text
docs/goals/<goal-id>/SHAPING.md
```

Use [templates/shaping-history-template.md](templates/shaping-history-template.md) and [references/shaping-history.md](references/shaping-history.md).

Before asking a question:

1. Read every prior shaping round for this goal.
2. Read the current Goal Contract and revision history.
3. Check whether the question was already answered, deferred, declined, or superseded.
4. Ask again only when materially new evidence changes the decision.

The history is append-only. Corrections create new entries that reference and supersede old ones; earlier answers are never silently rewritten.

## 3. Resolve inputs exhaustively

Use [references/input-resolution.md](references/input-resolution.md).

Build an input ledger. Resolve common contract fields plus the selected profile's fields from [references/profile-inputs.md](references/profile-inputs.md).

Search all lawful, authoritative sources before asking. Use safe defaults only when reversible, low-risk, and consistent with repository conventions. Never default product direction, acceptance thresholds, risk acceptance, compatibility removal, destructive authority, or legal/compliance judgments.

When evidence cannot resolve a material choice:

- Ask one decision at a time
- Show the relevant evidence
- Offer at most three materially different options
- Recommend one answer and explain the trade-off
- Record the exact question and the user's answer immediately in `SHAPING.md`
- Normalize the answer into a contract decision and record its contract impact
- Continue until every material input is resolved or a genuine blocker exists

Preserve the user's answer verbatim when safe and useful. Redact secrets, credentials, private personal data, confidential business or customer information, third-party restricted material, raw production data, and exploit-enabling details; store a safe decision summary plus an approved secure reference instead.

Do not ask users to find repository facts, commands, paths, or implementation details that tools can discover.

## 4. Run standard or deeper shaping rounds

### Standard round

Resolve the minimum material owner decisions required for a safe, verifiable contract. This is not permission to skip important ambiguity; it avoids interrogating the user about reversible implementation details.

### Deepening round

Run when the user says the proposed target is not satisfactory, requests another batch of questions, asks to go deeper, or challenges the contract.

Before the round:

1. Read all previous questions, answers, evidence, and contract revisions.
2. Build a gap map of weak assumptions, unresolved trade-offs, hidden scope, and fragile evidence.
3. Select the highest-value unexplored lens.
4. Avoid duplicate questions.

Possible lenses include outcome and value, users and journeys, scope and dependencies, acceptance and failure cases, compatibility, UI/UX/accessibility, data/security/privacy, reliability/recovery, performance/cost, maintainability/ownership, and authority/risk.

A round is a sequence of one-at-a-time questions, never a large questionnaire. At round close, append:

- New decisions
- Contract revisions
- Remaining uncertainty
- Readiness assessment
- Recommended next step

The user may request repeated deepening rounds. Each round must add new decision value; circular questioning is a shaping stall.

At the end of every round, present the three valid dispositions:

```text
Approve the current Goal Contract
Run another deeper shaping round
Pause shaping and preserve the current state
```

Do not start production execution until the approved contract records the shaping round that authorized it.

## 5. Manage the goal portfolio

A project may contain candidate, ready, active, paused, blocked, and closed goals.

Use the existing tracker when it can represent priority, dependencies, state, contract, shaping history, and progress. Otherwise use [templates/goal-portfolio-template.md](templates/goal-portfolio-template.md) at `docs/goals/PORTFOLIO.md` when more than one non-closed goal needs coordination.

One native `/goal` session or worktree executes one dependency-safe leaf contract. Parallel goals require isolated sessions/worktrees, non-overlapping ownership, and explicit shared-resource coordination.

## 6. Classify lifecycle changes

Do not silently append a new request to the current goal.

- **Clarify** — wording or evidence references change without semantic change; keep Goal ID and record a shaping entry and revision.
- **Amend** — same outcome, but scope, evidence, protection, authority, profile, overlays, or exits materially change; pause, run a new shaping round, approve, and increment revision.
- **Reprioritize** — reorder the portfolio without rewriting contracts.
- **Pause / Resume** — preserve shaping history, progress, branch/SHA, next action, and resume condition.
- **Supersede** — a different outcome replaces the current one; preserve its shaping record, archive it, and create a new Goal ID.
- **Split** — create dependency-safe child goals and choose one leaf.
- **Merge** — combine only when outcome, evidence, authority, and shaping decisions truly align.
- **Cancel** — close with reason and reusable evidence.
- **Close** — archive the terminal outcome and update history.

Keep the same Goal ID only while the observable outcome remains the same.

## 7. Classify ambiguity

### One target is strongly supported

Draft the contract and recommend priority directly. Record the evidence and any owner confirmation in the shaping round.

### Several targets are plausible

Present no more than three candidates with repository evidence, expected value, dependencies, scope, trade-off, likely verifier, and recommendation. Ask one owner decision at a time and persist every answer.

### The destination is still foggy

Do not manufacture a target. Recommend product discovery, wayfinding, an ADR, or a bounded Technical Spike / Feasibility goal when no stable outcome or verifier exists. Preserve the discovery questions and answers even when the result is not yet execution-ready.

## 8. Select the execution pattern

Choose one primary profile from [../goal-engine/references/loop-profiles.md](../goal-engine/references/loop-profiles.md).

Profiles are control-loop presets, not project types. When none fits, use **Custom Contract-Driven** and define:

- Bounded iteration unit
- Primary verifier
- Keep-or-revert rule
- Review and regression strategy
- Objective success, blocker, approval, budget, and stall exits

Select only relevant overlays from [../goal-engine/references/assurance-overlays.md](../goal-engine/references/assurance-overlays.md). When two profiles imply different outcomes, split the goal.

## 9. Reuse the project harness

Prefer verified repository instructions and scripts. When setup, run, reset, supported environments, or verification knowledge is fragmented, contradictory, or repeatedly rediscovered, update an authoritative source or create `docs/agent/PROJECT_HARNESS.md` from [../goal-engine/templates/project-harness-template.md](../goal-engine/templates/project-harness-template.md).

The harness links canonical mechanics; it does not duplicate the entire README or CI configuration.

## 10. Build, deepen, and approve the Goal Contract

Use [goal-contract-template.md](goal-contract-template.md). The contract must include:

- Goal identity, revision, state, priority, relationships, and durable paths
- Shaping-history path, completed rounds, last round, and approval round
- One observable outcome and why it is next
- Scope and exclusions
- Acceptance evidence
- Protected behavior
- Baseline and known exceptions
- Primary profile or custom loop
- Assurance overlays
- Project harness
- Authority and stop boundaries
- Goal-drift review triggers
- Reuse and closeout expectations

Before production edits, surface a concise review of outcome, evidence, protection, authority, exits, and the shaping decisions that materially formed them.

If the user is not satisfied, do not pressure them to approve. Run another shaping round and preserve the previous one. Obtain explicit approval only when the user accepts the current contract, unless an already-approved authoritative artifact has identical semantics.

## 11. Readiness gate

Proceed to execution only when:

- One outcome is clear
- Every material input-ledger row is resolved
- Every asked question and answer is saved or safely redacted in the shaping history
- Scope and exclusions are understandable to a fresh agent
- Completion has observable proof
- Protected behavior and user work are named
- Dependencies and priority are handled
- Profile, overlays, harness, state, shaping, and archive paths are clear
- Authority and stop conditions are explicit
- No different active goal will be overwritten
- The contract identifies its approval shaping round
- The contract is explicitly approved

A draft contract or completed shaping round is not an execution-ready success state.

## 12. Persist without competing state

Update existing authoritative artifacts when possible. Otherwise use:

```text
GOAL.md
GOAL_PROGRESS.md
docs/goals/PORTFOLIO.md
docs/goals/INDEX.md
docs/goals/<goal-id>/
├── SHAPING.md
├── CONTRACT.md
├── PROGRESS.md
└── RESULT.md
```

`SHAPING.md` exists from shaping onward. The other archive snapshots are finalized at closeout. Link detailed requirements instead of duplicating them. Preserve prior revisions, prior answers, and immutable closeout packets. Record approvals and lifecycle transitions.

## 13. Handoff to goal-engine

For a normal shaping session, render the copy-ready command with the **actual persisted contract path or authoritative issue/spec reference**. Use `GOAL.md` only when it is the resolved contract location. Example:

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use its selected execution profile, assurance overlays, project harness, and shaping decision record. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. At checkpoints, detect material goal drift instead of silently expanding scope. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve reusable state and leave a restartable handoff.
```

For a zero-friction launcher already running inside native `/goal`:

1. Surface the approved outcome, acceptance evidence, and approval shaping round in the conversation.
2. State explicitly: **shaping is complete; the enclosing goal is not complete**.
3. Load or invoke `goal-engine`.
4. Continue execution in the same session.
5. Do not emit terminal success until the approved contract passes.

## 14. Launch packet

```text
Lifecycle decision:
Approved target:
Goal ID / revision:
Priority and dependencies:
Contract:
Shaping history:
Completed / approval shaping rounds:
Input ledger:
Portfolio:
Execution profile:
Assurance overlays:
Project harness:
Progress state:
Archive:
Run with goal-engine:
Standalone fallback:
Open owner decisions: None
```

If open material decisions remain, the contract is not approved and production execution must not start.
