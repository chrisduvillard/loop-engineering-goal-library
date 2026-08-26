---
name: goal-engine
description: Execute one approved Goal Contract safely inside a native /goal loop. Start only after shape-goal has resolved owner decisions and recorded explicit approval. Use for brownfield orientation, any library profile or custom loop, assurance overlays, repository-native verification, regression protection, independent review, durable progress, reusable closeout, and goal-drift detection. Never invent or materially redefine the target, and never interview the user while autonomous execution is active.
compatibility: Portable Agent Skills host with repository read/write tools. Native /goal support is required for durable continuation and host-side completion evaluation.
user-invocable: true
disable-model-invocation: false
argument-hint: "[approved Goal Contract path or issue]"
metadata:
  author: chrisduvillard
  version: "0.8.0"
  source: "github.com/chrisduvillard/loop-engineering-goal-library"
---

# Goal Engine

Execute one approved outcome without losing brownfield safety, changing the goal silently, reopening settled decisions without cause, or discarding reusable knowledge.

> **Profile = loop shape · overlays = additional proof · harness = project mechanics · shaping history = decision trail · contract = project truth · native `/goal` = persistence**

## Non-negotiable invariants

- Execute only an approved contract and the approval shaping round recorded by it.
- Read the contract, shaping history, repository instructions, harness, progress, and Git state before editing.
- Preserve user and unrelated work; keep changes small, reversible, verified, and reviewable.
- Never treat shaping, planning, test creation, or documentation alone as completion when production behavior remains.
- Surface evaluator-visible evidence, protect corrected failures, and keep only changes that preserve or improve the verified state.
- Never ask a material owner question while autonomous `/goal` execution is active.
- Material goal drift stops execution as **Approval required** and returns to interactive `shape-goal`; prior decisions remain immutable.
- Autonomous continuation never expands deployment, destructive, credential, billing, security-testing, legal, or production authority.

## Approved-contract handoff

The normal workflow is:

```text
shape-goal outside /goal → explicit approval → new /goal + goal-engine
```

Before production work:

1. Re-read the approved contract, shaping history, input ledger, profile, overlays, harness, and state paths.
2. Confirm the contract names its approval shaping round.
3. Surface the exact outcome and acceptance evidence for the native evaluator.
4. Continue execution; do not treat shaping as completion.

If an advanced autonomous preflight reaches `goal-engine` without an approved contract:

1. Preserve the draft, shaping history, unresolved decision, and recommended question.
2. Stop as **Approval required**, never Achieved.
3. Do not ask the question or take another autonomous turn.
4. Tell the user to resume `shape-goal` outside `/goal`.

## Required inputs

Identify:

1. Approved Goal Contract, Goal ID, revision, state, and priority
2. Shaping-history path, completed rounds, last round, and approval round
3. Dependencies, related goals, portfolio path, and branch/worktree
4. Primary profile or custom-loop definition
5. Assurance overlays
6. Project harness or authoritative setup/run/verify sources
7. Acceptance evidence and protected behavior
8. Progress, archive, history, library version, and authority boundaries

The contract is current authority. Shaping history explains rationale and rejected alternatives but does not override a later approved revision. Profiles and overlays may strengthen proof but may not weaken the contract or expand authority.

## 1. Orient from actual state

Before persistent changes, read applicable:

- Repository and agent instructions
- Approved contract, shaping history, input ledger, and authoritative sources
- Architecture, ADRs, PRDs, specifications, plans, portfolio, prior goal archives, and handoffs
- Project harness, native scripts, CI, tests, fixtures, benchmarks, release gates, and runtime entry points
- Git status, diff, branch, HEAD, worktrees, and relevant history

Use shaping history to understand non-goals, priorities, accepted trade-offs, and rejected alternatives. Do not reopen a settled owner decision merely because implementation is difficult.

Protect uncommitted, user-authored, and unrelated work. Never discard changes merely to obtain a clean tree.

## 2. Reconcile before trusting

Resolve contradictions using:

1. Explicit authority in repository instructions or the approved contract
2. Later approved revisions over earlier drafts or shaping answers
3. Current executable evidence over unsupported status claims
4. Shaping history for rationale and intended semantics
5. A new interactive shaping round when materially different outcomes remain plausible

A stale checkbox is not proof that work remains. Existing code is not proof that a requirement passes.

## 3. Validate lifecycle and isolation

Proceed only when:

- Contract is Approved or Active and names one outcome
- Goal ID, revision, profile/custom loop, overlays, state, shaping, and archive paths are defined
- Approval shaping round is recorded
- Dependencies are satisfied or explicitly handled
- Scope, verifiers, protected behavior, authority, drift triggers, and exits are clear
- Branch/worktree matches the active portfolio entry
- No different goal, shared mutable resource, or unrelated work will be overwritten

One native `/goal` session or worktree executes one dependency-safe leaf contract. Parallel goals require isolation and coordination.

## 4. Load profile and overlays

Read [references/loop-profiles.md](references/loop-profiles.md).

- Apply one primary profile.
- For Custom Contract-Driven, require an iteration unit, verifier, keep-or-revert rule, review strategy, and stop condition.
- Borrow a narrow technique from another profile only when it improves evidence without changing the outcome.

Read [references/assurance-overlays.md](references/assurance-overlays.md) and apply every selected overlay as an additional acceptance, review, and authority obligation.

## 5. Reuse the project harness

Use verified setup, run, reset, realistic workflow, and check commands. Do not rediscover them every goal.

If sources are absent, contradictory, or stale:

1. Verify commands and supported environments.
2. Update an authoritative document or create `docs/agent/PROJECT_HARNESS.md` from [templates/project-harness-template.md](templates/project-harness-template.md).
3. Link canonical scripts instead of copying them.
4. Record freshness triggers and unverified assumptions.

A stale harness is a hypothesis, not authority.

## 6. Establish the verified baseline

Record:

- Branch/SHA/worktree and preserved changes
- Contract revision and approval shaping round
- Exact native checks and results
- Known pre-existing failures and accepted exceptions
- Acceptance and overlay ledger
- Dependencies and current goal fit
- No-progress count
- Highest-priority unblocked gap

Use [references/state-and-evidence.md](references/state-and-evidence.md) and its templates when the repository lacks an established format.

## 7. Run the brownfield loop

Repeat:

1. **Select** the highest-priority dependency-safe unblocked gap.
2. **Verify** the gap is real.
3. **Change** the smallest coherent reversible production slice.
4. **Check** with the smallest relevant repository-native verifier.
5. **Protect** corrected failures with regression coverage.
6. **Review** scope drift, unrelated edits, and new risk.
7. **Apply overlays** and broaden verification at meaningful checkpoints.
8. **Keep or revert** based on evidence.
9. **Record** evidence, failed approaches, reusable discoveries, and the next action.
10. **Repeat** without asking what comes next when the contract and repository answer it.

Do not stop at planning, scaffolding, documentation, analysis, or test creation while required production implementation remains.

## 8. Goal-fit gate and interaction boundary

At meaningful checkpoints, confirm the approved contract still represents the user's need.

Continue when new information is only an implementation detail, safer route, clarified reproduction, or evidence for the same outcome.

A material change includes outcome, priority, scope, acceptance evidence, protected behavior, authority, dependencies, lifecycle, profile, overlays, budget, stop conditions, or user satisfaction.

When a material owner decision is required:

1. Preserve current progress, branch/SHA, evidence, and next safe action.
2. Append the drift trigger and proposed question to `SHAPING.md`.
3. Stop the current native goal as **Approval required**.
4. Do not ask the question inside the active `/goal` and do not take another autonomous turn.
5. Tell the user to resume interactive shaping:
   - Codex: `/goal pause` or `/goal clear`, then `$shape-goal Resume goal-id`
   - Claude Code: `/goal clear`, then `/shape-goal Resume goal-id`
6. Resume execution only after the revised contract is explicitly approved and the user starts a new `/goal`.

Never silently expand scope or edit prior shaping answers.

## 9. Evidence for the evaluator

After each checkpoint, surface:

- Command/workflow and relevant result
- Acceptance and overlay status changes
- Regressions checked
- Diff and review status
- Goal-fit result
- Current contract revision and approval shaping round
- No-progress count
- Remaining gap and next action
- State artifact updated

The evaluator may not inspect files or run commands independently. “Implemented,” task counts, code inspection, or weakened checks are not completion evidence.

## 10. Independent review

Use fresh review or isolated subagents for high-blast-radius, security, authorization, migration, concurrency, reliability, architecture, compliance, accessibility, or subjective visual changes when practical.

Provide the reviewer the contract, relevant shaping decisions, diff, evidence, and overlays—not the implementer's persuasive narrative. Treat findings as hypotheses until verified.

## 11. Stall detection

Progress requires at least one of:

- New verified evidence
- Smaller reproducible failure
- Changed testable hypothesis
- Closed acceptance gap
- Newly proven blocker or approval boundary
- Reusable verifier, fixture, diagnostic, or harness improvement that materially advances the next cycle

Repeated searches or questions without new evidence do not count. After two consecutive no-progress cycles, stop as Stalled and preserve a restartable handoff.

## 12. Authority boundaries

Unless explicitly authorized, require approval before:

- Merge, push, tag, publish, deploy, release, or production mutation
- Destructive data, schema, infrastructure, or branch operations
- Credential, billing, account, secret, or external-system changes
- Irreversible migrations or removal of recovery paths
- Security testing outside approved scope
- Legal, compliance, privacy, or risk acceptance conclusions

Autonomous continuation never implies broader authority.

## 13. Promote durable knowledge

Move verified recurring knowledge to the correct maintained home:

- Corrected failure → regression test
- Product or architecture decision → approved document or ADR
- Operational procedure → runbook
- Setup/run/verify knowledge → Project Harness or canonical script
- Reusable data or visual specimen → maintained fixture/reference
- Stable evaluation → benchmark, versioned AI eval, crawl matrix, or test
- Repository knowledge → reviewed architecture map and Project Harness
- Locale-sensitive behavior → pseudo-localization and locale fixtures
- Important limitation → residual-risk documentation

The shaping history remains the durable decision trail. Promote only stable decisions that belong in maintained artifacts; do not duplicate the entire interview elsewhere.

## 14. Preserve lifecycle state and closeout

- **Paused** is non-terminal: persist shaping history, progress, branch/SHA, next action, and resume condition.
- **Achieved, Cancelled, Superseded, Blocked, Approval required, Budget exhausted, and Stalled** receive closeout packets when the run is closed.

At closeout:

1. Preserve `SHAPING.md` and snapshot `CONTRACT.md`, `PROGRESS.md`, and `RESULT.md`.
2. Update portfolio and history.
3. Link reusable outputs, important decision IDs, and related goals.
4. Record library version, contract revision, shaping rounds, and approval round.
5. Exclude secrets, private data, production dumps, exploit-enabling evidence, and unnecessary logs.

Closed evidence is immutable. Later work receives a new Goal ID or approved revision and links back.

## 15. Completion

Declare **Achieved** only when:

- Every acceptance item passes with surfaced evidence
- Required overlay and broader gates pass
- Protected behavior and baseline have not regressed
- Important changes are reviewed and unexplained diffs resolved
- Durable shaping history, contract, progress, harness, and knowledge are current
- Closeout packet is complete
- Working tree has no unexplained agent-created changes

Close with:

```text
Outcome:
Goal ID / revision / portfolio state:
Shaping history / completed rounds / approval round:
Acceptance and overlay evidence:
Delivered behavior:
Regression and review status:
Reusable outputs and harness updates:
Residual risk:
State and archive paths:
Next action: only when not achieved
```
