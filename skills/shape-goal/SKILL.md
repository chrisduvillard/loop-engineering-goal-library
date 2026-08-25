---
name: shape-goal
description: Resolve vague, incomplete, or changing project needs into an approved Goal Contract and managed goal portfolio. Also powers zero-friction /goal launchers by discovering every profile-specific input from repository and connected evidence before asking the user, asking only material owner decisions one at a time, then handing the approved contract to goal-engine. Use before production execution or whenever the target, priority, scope, proof, lifecycle, profile, or boundaries are unclear.
compatibility: Portable Agent Skills host. Reads repository and connected authoritative evidence and writes planning/state artifacts; production implementation remains the responsibility of goal-engine.
user-invocable: true
disable-model-invocation: false
argument-hint: "[continue | new goal | profile | goal ID | changed need]"
metadata:
  author: chrisduvillard
  version: "0.4.0"
  source: "github.com/chrisduvillard/loop-engineering-goal-library"
---

# Shape Goal

Turn rough or changing intent into one safe, approved, executable contract.

> **Search facts first. Ask only decisions. Never let shaping masquerade as implementation or completion.**

```text
project need → evidence search → input ledger → owner decisions → approved contract → goal-engine
```

## Invocation modes

### Direct shaping

- **Claude Code:** `/shape-goal Continue this project`
- **Codex CLI / IDE:** `$shape-goal Continue this project`
- Other Agent Skills hosts: explicitly select or mention `shape-goal`

### Zero-friction bootstrap

A copied standalone `/goal` may name both `shape-goal` and `goal-engine` without supplying repository-specific placeholders. In that mode:

1. The launcher fixes the primary profile.
2. This skill resolves every required input and obtains approval.
3. Production edits remain forbidden during shaping.
4. After approval, hand off inside the same native goal to `goal-engine`.
5. The native goal is **not complete** when the contract is created.

Read [references/input-resolution.md](references/input-resolution.md) and [references/profile-inputs.md](references/profile-inputs.md) whenever bootstrap mode is active.

## Required outputs

Produce and persist, as applicable:

1. Lifecycle decision for each affected goal
2. Stable Goal ID and revision
3. Approved Goal Contract for the next executable outcome
4. Portfolio disposition when several non-closed goals exist
5. One primary profile or a Custom Contract-Driven definition
6. Required assurance overlays
7. Reused or newly verified project-harness path
8. Progress, archive, and history paths
9. Copy-ready native `/goal` handoff
10. Standalone fallback reference
11. Input ledger showing how every material field was resolved

## 1. Orient before asking

Read the applicable:

- Repository and agent instructions
- Git status, diff, branch, worktrees, and relevant history
- Current contract, progress, portfolio, handoffs, and prior goal archives
- Approved issues, PRDs, specifications, plans, milestones, ADRs, and architecture
- Native scripts, task runners, package configuration, CI, tests, fixtures, benchmarks, and release gates
- Runtime entry points, actual product behavior, screenshots, logs, and generated artifacts
- Project Harness and supported-environment documentation
- Connected authoritative systems available to the host

Reconcile contradictions by authority, approved recency, and executable evidence. Protect uncommitted and unrelated work.

**Facts are the agent's job; decisions are the user's.**

## 2. Resolve inputs exhaustively

Use [references/input-resolution.md](references/input-resolution.md).

Build an input ledger. Resolve common contract fields plus the selected profile's fields from [references/profile-inputs.md](references/profile-inputs.md).

Search all lawful, authoritative sources before asking. Use safe defaults only when reversible, low-risk, and consistent with repository conventions. Never default product direction, acceptance thresholds, risk acceptance, compatibility removal, destructive authority, or legal/compliance judgments.

When evidence cannot resolve a material choice:

- Ask one decision at a time
- Show the relevant evidence
- Offer at most three materially different options
- Recommend one answer and explain the trade-off
- Record the answer
- Continue until every material input is resolved or a genuine blocker exists

Do not ask users to find repository facts, commands, paths, or implementation details that tools can discover.

## 3. Manage the goal portfolio

A project may contain candidate, ready, active, paused, blocked, and closed goals.

Use the existing tracker when it can represent priority, dependencies, state, contract, and progress. Otherwise use [templates/goal-portfolio-template.md](templates/goal-portfolio-template.md) at `docs/goals/PORTFOLIO.md` when more than one non-closed goal needs coordination.

One native `/goal` session or worktree executes one dependency-safe leaf contract. Parallel goals require isolated sessions/worktrees, non-overlapping ownership, and explicit shared-resource coordination.

## 4. Classify lifecycle changes

Do not silently append a new request to the current goal.

- **Clarify** — wording or evidence references change without semantic change; keep Goal ID and record revision.
- **Amend** — same outcome, but scope, evidence, protection, authority, profile, overlays, or exits materially change; pause, approve, and increment revision.
- **Reprioritize** — reorder the portfolio without rewriting contracts.
- **Pause / Resume** — preserve progress, branch/SHA, next action, and resume condition.
- **Supersede** — a different outcome replaces the current one; archive it and create a new Goal ID.
- **Split** — create dependency-safe child goals and choose one leaf.
- **Merge** — combine only when outcome, evidence, and authority truly align.
- **Cancel** — close with reason and reusable evidence.
- **Close** — archive the terminal outcome and update history.

Keep the same Goal ID only while the observable outcome remains the same.

## 5. Classify ambiguity

### One target is strongly supported

Draft the contract and recommend priority directly.

### Several targets are plausible

Present no more than three candidates with repository evidence, expected value, dependencies, scope, trade-off, likely verifier, and recommendation. Ask one owner decision at a time.

### The destination is still foggy

Do not manufacture a target. Recommend product discovery, wayfinding, an ADR, or a bounded Technical Spike / Feasibility goal when no stable outcome or verifier exists.

## 6. Select the execution pattern

Choose one primary profile from [../goal-engine/references/loop-profiles.md](../goal-engine/references/loop-profiles.md).

Profiles are control-loop presets, not project types. When none fits, use **Custom Contract-Driven** and define:

- Bounded iteration unit
- Primary verifier
- Keep-or-revert rule
- Review and regression strategy
- Objective success, blocker, approval, budget, and stall exits

Select only relevant overlays from [../goal-engine/references/assurance-overlays.md](../goal-engine/references/assurance-overlays.md). When two profiles imply different outcomes, split the goal.

## 7. Reuse the project harness

Prefer verified repository instructions and scripts. When setup, run, reset, supported environments, or verification knowledge is fragmented, contradictory, or repeatedly rediscovered, update an authoritative source or create `docs/agent/PROJECT_HARNESS.md` from [../goal-engine/templates/project-harness-template.md](../goal-engine/templates/project-harness-template.md).

The harness links canonical mechanics; it does not duplicate the entire README or CI configuration.

## 8. Build and approve the Goal Contract

Use [goal-contract-template.md](goal-contract-template.md). The contract must include:

- Goal identity, revision, state, priority, relationships, and durable paths
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

Before production edits, surface a concise review of outcome, evidence, protection, authority, and exits. Obtain explicit approval unless an already-approved authoritative artifact has identical semantics.

## 9. Readiness gate

Proceed to execution only when:

- One outcome is clear
- Every material input ledger row is resolved
- Scope and exclusions are understandable to a fresh agent
- Completion has observable proof
- Protected behavior and user work are named
- Dependencies and priority are handled
- Profile, overlays, harness, state, and archive paths are clear
- Authority and stop conditions are explicit
- No different active goal will be overwritten
- The contract is approved

A draft contract is not an execution-ready goal.

## 10. Persist without competing state

Update existing authoritative artifacts when possible. Otherwise use:

```text
GOAL.md
GOAL_PROGRESS.md
docs/goals/PORTFOLIO.md
docs/goals/INDEX.md
docs/goals/<goal-id>/
```

Link detailed requirements instead of duplicating them. Preserve prior revisions and immutable closeout packets. Record approvals and lifecycle transitions.

## 11. Handoff to goal-engine

For a normal shaping session, return the copy-ready command:

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use its selected execution profile, assurance overlays, and project harness. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. At checkpoints, detect material goal drift instead of silently expanding scope. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve reusable state and leave a restartable handoff.
```

For a zero-friction launcher already running inside native `/goal`:

1. Surface the approved outcome and acceptance evidence in the conversation.
2. State explicitly: **shaping is complete; the enclosing goal is not complete**.
3. Load or invoke `goal-engine`.
4. Continue execution in the same session.
5. Do not emit terminal success until the approved contract passes.

## 12. Launch packet

```text
Lifecycle decision:
Approved target:
Goal ID / revision:
Priority and dependencies:
Contract:
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
