---
name: shape-goal
description: Main interactive entry point for turning vague, incomplete, or changing project needs into an approved Goal Contract and managed goal portfolio. Search repository and connected evidence first, save every asked question and answer, ask one material owner decision at a time, stop the turn while waiting for each answer, support deeper shaping rounds, and return the exact goal-engine /goal command only after approval. Use before autonomous execution or whenever target, priority, scope, proof, lifecycle, profile, or boundaries are unclear.
compatibility: Portable Agent Skills host. Reads repository and connected authoritative evidence and writes planning/state artifacts; production implementation remains the responsibility of goal-engine inside a later native /goal.
user-invocable: true
disable-model-invocation: false
argument-hint: "[continue | new goal | deepen | profile | goal ID | changed need]"
metadata:
  author: chrisduvillard
  version: "0.9.0"
  source: "github.com/chrisduvillard/loop-engineering-goal-library"
---

# Shape Goal

`shape-goal` is the main command. It turns rough intent into one safe, approved, executable contract while preserving the full decision trail.

```text
project need → evidence search → one question → user answer → approved contract
                                                        ↓
                                              native /goal + goal-engine
```

> **Interactive first. Shape outside `/goal`; execute inside `/goal`.**

## Non-negotiable invariants

- Do not make production changes during shaping.
- Search repository and connected authoritative evidence before asking the user.
- Save every asked question and safe answer in append-only `SHAPING.md`; corrections append and supersede.
- Ask one material owner decision at a time, then **end the turn immediately**.
- Do not optimize for a small question count; ask until no material ambiguity remains.
- Never convert an ambiguous, partial, conditional, or conflicting reply into a stronger decision than the user made.
- No High- or Medium-impact assumption may survive approval unless it is evidence-backed or explicitly owner-approved.
- After asking a question, do not call tools, continue research, start background work, ask another question, or keep pursuing an active goal until the user answers.
- A dissatisfied user may request repeated deeper, non-duplicate shaping rounds.
- Record approval as a shaping answer; do not infer approval from silence or partial agreement.
- Use the actual persisted contract reference in the execution handoff; `GOAL.md` is only the default fallback.
- Contract creation is not completion. After approval, return the exact `/goal` command; do not silently start autonomous execution.
- Material goal drift reopens shaping without rewriting prior decisions.

## Start here

| Need | Claude Code | Codex CLI / IDE |
|---|---|---|
| Shape the next goal | `/shape-goal Continue this project` | `$shape-goal Continue this project` |
| Use a specific profile | `/shape-goal Use the Frontend UI / UX / Accessibility profile` | `$shape-goal Use the Frontend UI / UX / Accessibility profile` |
| Add a different goal | `/shape-goal New goal: describe the intent` | `$shape-goal New goal: describe the intent` |
| Change the current goal | `/shape-goal Change current goal: describe the need` | `$shape-goal Change current goal: describe the need` |
| Go deeper | `/shape-goal Deepen the current goal` | `$shape-goal Deepen the current goal` |
| Stress-test clarity | `/shape-goal Stress-test the current goal` | `$shape-goal Stress-test the current goal` |
| Resume saved shaping | `/shape-goal Resume goal-id` | `$shape-goal Resume goal-id` |
| Review priorities | `/shape-goal Review the goal portfolio` | `$shape-goal Review the goal portfolio` |

Other Agent Skills hosts should explicitly select or mention `shape-goal`.

## Interaction model

### Interactive shaping — default and recommended

Run `shape-goal` directly, with no active native `/goal` around it.

1. Investigate the repository and resolve every discoverable fact.
2. When one owner decision remains, save and ask that single question.
3. End the turn immediately.
4. On the user's next message, first save the answer, normalize the decision, update the contract impact, and then continue.
5. Repeat until the user approves the contract or pauses shaping.
6. Return the exact copy-ready `/goal` command for `goal-engine`.

The user's normal reply is the answer. Never require a Steer message merely to answer a shaping question.

### Active-goal rescue

If interactive shaping is already running inside a native `/goal` and an owner answer is required:

1. Persist the current round, unresolved decision, recommended option, and exact proposed question.
2. Do not ask and then continue autonomously.
3. Stop as **Approval required** and tell the user to leave the active goal before resuming shaping:
   - Codex: `/goal pause` or `/goal clear`, then `$shape-goal Resume goal-id`
   - Claude Code: `/goal clear`, then `/shape-goal Resume goal-id`
4. Resume with the question in an ordinary interactive turn.

### Autonomous bootstrap — advanced only

A profile file may contain a combined `/goal` bootstrap for repositories that already contain enough approved evidence to shape without owner questions.

- Continue inside that `/goal` only when every material input can be resolved without user interaction.
- At the first unresolved owner decision, save the proposed question and stop as **Approval required**.
- Do not ask inside the active goal, take another autonomous turn, or hand off to `goal-engine`.
- Resume with `shape-goal` outside `/goal`, obtain approval, then start a new execution `/goal`.

## Required outputs

Produce and persist, as applicable:

1. Lifecycle decision for every affected goal
2. Stable Goal ID and revision
3. Durable shaping-history path containing every asked question and answer
4. Completed shaping-round IDs, summaries, corrections, deferred decisions, and approval record
5. Approved Goal Contract for one executable outcome
6. Portfolio disposition when several non-closed goals exist
7. One primary execution profile or a Custom Contract-Driven definition
8. Required assurance overlays
9. Reused or newly verified project-harness path
10. Progress, archive, and history paths
11. Exact copy-ready native `/goal` handoff
12. Input ledger showing how every material field was resolved
13. Assumption register, selected shaping depth, and final clarity-stress-test result

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

As soon as a stable Goal ID exists, use the repository's existing decision log when suitable; otherwise create:

```text
docs/goals/<goal-id>/SHAPING.md
```

Use [templates/shaping-history-template.md](templates/shaping-history-template.md) and [references/shaping-history.md](references/shaping-history.md).

Before asking:

1. Read every prior shaping round for this goal.
2. Read the current Goal Contract and revision history.
3. Check whether the decision was already answered, deferred, declined, or superseded.
4. Ask again only when materially new evidence changes the choice.

The history is append-only. Earlier answers are never silently rewritten.

## 3. Resolve inputs exhaustively

Use [references/input-resolution.md](references/input-resolution.md), [references/question-quality.md](references/question-quality.md), and build an input ledger covering common contract fields plus the selected profile's fields from [references/profile-inputs.md](references/profile-inputs.md).

Search all lawful authoritative sources before asking. Use a default only when it is reversible, low-risk, and consistent with repository conventions. Never default product direction, acceptance thresholds, risk acceptance, compatibility removal, destructive authority, or legal/compliance judgments.

When evidence cannot resolve one material choice:

1. Show the relevant evidence.
2. Offer at most three materially different options.
3. Recommend one answer and explain the trade-off.
4. State what materially changes based on the answer.
5. Ensure the question is atomic rather than bundling independent choices.
6. Save the exact question before sending it.
7. Ask only that question.
8. End the turn immediately.

When the answer arrives:

1. Save it verbatim when safe and useful.
2. Redact secrets, credentials, private personal data, confidential business/customer information, third-party restricted material, raw production data, and exploit-enabling details; store a safe decision summary plus an approved secure reference instead.
3. Run the answer quality gate: Clear, Clear with conditions, Partial, Ambiguous, Conflicting, or Deferred / Blocked.
4. Normalize only the meaning the user actually supplied; ask a targeted follow-up when multiple material interpretations remain.
5. Record the contract sections affected, confidence, assumptions, and any superseded decision.
6. Continue resolving the ledger.

Do not ask users to discover repository facts, commands, paths, or implementation details that tools can find.

## 4. Run adaptive, standard, deeper, or stress-test shaping rounds

### Adaptive depth — default

There is no target question count. Score unresolved items by impact, uncertainty, irreversibility, and confidence; ask the highest-risk decision first and continue until the clarity gate in [references/question-quality.md](references/question-quality.md) passes. Escalate automatically to Thorough or Exhaustive depth for high-risk, subjective, cross-cutting, weakly verified, or irreversible goals.

### Standard round

Resolve the minimum material owner decisions required for a safe, verifiable contract without interrogating the user about reversible implementation details.

### Deepening round

Run when the user says the target is unsatisfactory, asks another batch of questions, requests more depth, or challenges the contract.

Before the round:

1. Read all previous questions, answers, evidence, and contract revisions.
2. Build a gap map of weak assumptions, hidden scope, fragile evidence, and unresolved trade-offs.
3. Select the highest-value unexplored lens.
4. Avoid duplicate questions.

Useful lenses include outcome and value, users and journeys, scope and dependencies, acceptance and failure cases, codebase knowledge, AI evaluation, deprecation and adoption, localization, public discoverability, compatibility, UI/UX/accessibility, data/security/privacy, reliability/recovery, performance/cost, maintainability/ownership, and authority/risk.

### Stress-test round

Run when the user asks for zero ambiguity, requests a challenge pass, or the contract is high-risk or subjective. Apply the fresh-reader, counterexample, scenario, verifier, contradiction, traceability, assumption, and plain-English teach-back checks from [references/question-quality.md](references/question-quality.md). Turn each material ambiguity into one saved question; do not merely rewrite the contract from your own interpretation.

At round close, append new decisions, contract revisions, remaining uncertainty, shaping depth, assumption status, clarity-test findings, readiness, and the recommended next step. Then ask one disposition question and end the turn:

```text
Approve the current Goal Contract
Run another deeper shaping round
Pause shaping and preserve the current state
```

## 5. Manage the goal portfolio

A project may contain candidate, ready, active, paused, blocked, and closed goals.

Use the existing tracker when it can represent priority, dependencies, state, contract, shaping history, and progress. Otherwise use [templates/goal-portfolio-template.md](templates/goal-portfolio-template.md) at `docs/goals/PORTFOLIO.md` when more than one non-closed goal needs coordination.

One native `/goal` session or worktree executes one dependency-safe leaf contract. Parallel goals require isolated sessions/worktrees, non-overlapping ownership, and explicit shared-resource coordination.

## 6. Classify lifecycle changes

Do not silently append a new request to the current goal.

- **Clarify** — semantics do not change; keep Goal ID and append the clarification.
- **Amend** — same outcome but material scope, evidence, protection, authority, profile, overlays, or exits change; pause, shape, approve, and increment revision.
- **Reprioritize** — reorder the portfolio without rewriting contracts.
- **Pause / Resume** — preserve shaping history, progress, branch/SHA, next action, and resume condition.
- **Supersede** — a different outcome replaces the current one; archive it and create a new Goal ID.
- **Split** — create dependency-safe child goals and choose one leaf.
- **Merge** — combine only when outcome, evidence, authority, and shaping decisions align.
- **Cancel** — close with reason and reusable evidence.
- **Close** — archive the terminal outcome and update history.

Keep the same Goal ID only while the observable outcome remains the same.

## 7. Classify ambiguity

### One target is strongly supported

Draft the contract and recommend priority directly. Record the evidence and any owner confirmation.

### Several targets are plausible

Present no more than three candidates with evidence, expected value, dependencies, scope, trade-off, likely verifier, and recommendation. Ask one decision and end the turn.

### The destination is still foggy

Do not manufacture a target. Recommend product discovery, wayfinding, an ADR, or a bounded Technical Spike / Feasibility goal when no stable outcome or verifier exists. Preserve the discovery record even when execution is not ready.

## 8. Select the execution pattern

Choose one primary profile from [../goal-engine/references/loop-profiles.md](../goal-engine/references/loop-profiles.md).

When none fits, use **Custom Contract-Driven** and define:

- Bounded iteration unit
- Primary verifier
- Keep-or-revert rule
- Review and regression strategy
- Objective success, blocker, approval, budget, and stall exits

Select only relevant overlays from [../goal-engine/references/assurance-overlays.md](../goal-engine/references/assurance-overlays.md). Split the goal when two profiles imply different outcomes.

## 9. Reuse the project harness

Prefer verified repository instructions and scripts. When setup, run, reset, supported environments, or verification knowledge is fragmented, contradictory, or repeatedly rediscovered, update an authoritative source or create `docs/agent/PROJECT_HARNESS.md` from [../goal-engine/templates/project-harness-template.md](../goal-engine/templates/project-harness-template.md).

## 10. Build, deepen, and approve the Goal Contract

Use [goal-contract-template.md](goal-contract-template.md). The contract must include identity, revision, lifecycle, relationships, shaping history, one observable outcome, scope, exclusions, acceptance evidence, protected behavior, baseline, profile/custom loop, overlays, harness, authority, stop conditions, drift triggers, and closeout expectations.

Before approval, surface a concise review of:

- Outcome
- Acceptance evidence
- Protected behavior
- Authority boundaries
- Stop conditions
- Material shaping decisions

If the user is not satisfied, run another shaping round. Ask the explicit approval question and end the turn. On the next message, persist the approval answer before changing state.

## 11. Readiness gate

Proceed to execution only when:

- One outcome is clear
- Every material input-ledger row is resolved
- Every material answer passes the answer quality gate
- No High- or Medium-impact assumption remains unresolved
- Every applicable clarity-matrix row is resolved or marked Not applicable with a reason
- A fresh-reader and counterexample review reveals no blocking alternate interpretation
- Every asked question and answer is saved or safely redacted
- Scope and exclusions are understandable to a fresh agent
- Completion has observable proof
- Protected behavior and user work are named
- Dependencies and priority are handled
- Profile, overlays, harness, state, shaping, and archive paths are clear
- Authority and stop conditions are explicit
- No different active goal will be overwritten
- The approval shaping round is recorded
- The contract is explicitly approved

A draft contract or completed shaping round is not execution-ready.

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

`SHAPING.md` exists from shaping onward. Preserve prior revisions, prior answers, approvals, and lifecycle transitions.

## 13. Handoff to goal-engine

After the user approves, persist the approval and render one copy-ready command using the actual contract reference. Example:

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use its selected execution profile, assurance overlays, project harness, and shaping decision record. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. At checkpoints, detect material goal drift instead of silently expanding scope. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve reusable state and leave a restartable handoff.
```

Also save the exact command in the contract's launcher field. Do not execute it automatically. The user starts the autonomous run after reviewing the command.

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
Shaping depth / clarity review:
Assumption register:
Portfolio:
Execution profile:
Assurance overlays:
Project harness:
Progress state:
Archive:
Run with goal-engine:
Open owner decisions: None
```

If a material decision remains, the contract is not approved and production execution must not start.
