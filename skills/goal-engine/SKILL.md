---
name: goal-engine
description: Execute one approved Goal Contract safely inside a native /goal loop. Also receives zero-friction launchers after shape-goal has discovered and approved their missing inputs. Use for brownfield orientation, any library profile or custom loop, assurance overlays, repository-native verification, regression protection, independent review, durable progress, reusable closeout, and goal-drift detection. Never invent or materially redefine the target.
compatibility: Portable Agent Skills host with repository read/write tools. Native /goal support is required for durable continuation and host-side completion evaluation.
user-invocable: true
disable-model-invocation: false
argument-hint: "[Goal Contract path or issue]"
metadata:
  author: chrisduvillard
  version: "0.4.0"
  source: "github.com/chrisduvillard/loop-engineering-goal-library"
---

# Goal Engine

Execute one approved outcome without losing brownfield safety, changing the goal silently, or discarding reusable knowledge.

> **Profile = loop shape · overlays = additional proof · harness = project mechanics · contract = project truth · native `/goal` = persistence**

## Zero-friction handoff

A native `/goal` may begin with `shape-goal` because the user copied a parameterless profile launcher.

In that case:

1. Do not edit production until `shape-goal` has produced an approved contract.
2. Re-read the approved contract, input ledger, profile, overlays, harness, and state paths.
3. Surface the exact outcome and acceptance evidence for the native evaluator.
4. Continue execution; do not treat shaping as completion.
5. If the contract cannot be approved, preserve the draft and stop as Blocked or Approval required, never Achieved.

Outside bootstrap mode, if no approved contract exists, stop before production edits and invoke `shape-goal`.

## Required inputs

Identify:

1. Approved Goal Contract, Goal ID, revision, state, and priority
2. Dependencies, related goals, portfolio path, and branch/worktree
3. Primary profile or custom-loop definition
4. Assurance overlays
5. Project harness or authoritative setup/run/verify sources
6. Acceptance evidence and protected behavior
7. Progress, archive, history, library version, and authority boundaries

Contract clauses override profile and overlay defaults. Profiles and overlays may strengthen proof but may not weaken acceptance criteria or expand authority.

## 1. Orient from actual state

Before persistent changes, read applicable:

- Repository and agent instructions
- Approved contract, input ledger, and authoritative sources
- Architecture, ADRs, PRDs, specifications, plans, portfolio, prior goal archives, and handoffs
- Project harness, native scripts, CI, tests, fixtures, benchmarks, release gates, and runtime entry points
- Git status, diff, branch, HEAD, worktrees, and relevant history

Protect uncommitted, user-authored, and unrelated work. Never discard changes merely to obtain a clean tree.

## 2. Reconcile before trusting

Resolve contradictions using:

1. Explicit authority in repository instructions or the contract
2. Later approved decisions over drafts
3. Current executable evidence over unsupported status claims
4. Owner escalation when materially different outcomes remain plausible

A stale checkbox is not proof that work remains. Existing code is not proof that a requirement passes.

## 3. Validate lifecycle and isolation

Proceed only when:

- Contract is Approved or Active and names one outcome
- Goal ID, revision, profile/custom loop, overlays, state, and archive paths are defined
- Dependencies are satisfied or explicitly handled
- Scope, verifiers, protected behavior, authority, review triggers, and exits are clear
- Branch/worktree matches the active portfolio entry
- No different goal, shared mutable resource, or unrelated work will be overwritten

One native `/goal` session or worktree executes one dependency-safe leaf contract. Parallel goals require isolation and coordination.

## 4. Load profile and overlays

Read [references/loop-profiles.md](references/loop-profiles.md).

- Apply one primary profile
- For Custom Contract-Driven, require iteration unit, verifier, keep-or-revert rule, review strategy, and stop condition
- Borrow a narrow technique from another profile only when it improves evidence without changing the outcome

Read [references/assurance-overlays.md](references/assurance-overlays.md) and apply each selected overlay as additional acceptance, review, and authority obligations.

When a quality concern is the primary outcome, use its dedicated profile. Use the matching overlay when it is secondary to another outcome.

## 5. Reuse the project harness

Use verified setup, run, reset, realistic workflow, and check commands. Do not rediscover them every goal.

If sources are absent, contradictory, or stale:

1. Verify commands and supported environments
2. Update an authoritative document or create `docs/agent/PROJECT_HARNESS.md` from [templates/project-harness-template.md](templates/project-harness-template.md)
3. Link canonical scripts instead of copying them
4. Record freshness triggers and unverified assumptions

A stale harness is a hypothesis, not authority.

## 6. Establish the verified baseline

Record:

- Branch/SHA/worktree and preserved changes
- Exact native checks and results
- Known pre-existing failures and accepted exceptions
- Acceptance and overlay ledger
- Dependencies and current goal-fit
- No-progress count
- Highest-priority unblocked gap

Use [references/state-and-evidence.md](references/state-and-evidence.md) and its templates when the repository lacks an established format.

## 7. Run the brownfield loop

Repeat:

1. **Select** the highest-priority dependency-safe unblocked gap in the contract.
2. **Verify** the gap is real.
3. **Change** the smallest coherent reversible production slice.
4. **Check** it with the smallest relevant repository-native verifier.
5. **Protect** corrected failures with regression coverage.
6. **Review** scope drift, contract changes, unrelated edits, and new risk.
7. **Apply overlays** and broaden verification at meaningful checkpoints.
8. **Keep or revert** based on evidence.
9. **Record** evidence, attempts, reusable discoveries, portfolio-relevant changes, and the next action.
10. **Repeat** without asking what comes next when the contract and repository answer it.

Do not stop at planning, scaffolding, documentation, analysis, or test creation while required production implementation remains.

## 8. Goal-fit gate

At meaningful checkpoints, ask whether the approved contract still represents the user's current need.

Continue when new information is only an implementation detail, safer route, clarified reproduction, or evidence for the same outcome.

Pause and invoke `shape-goal` when a material change affects:

- Observable outcome or priority
- Scope or acceptance evidence
- Protected behavior or authority
- Dependencies or lifecycle state
- Primary profile or assurance overlays
- Budget or stop conditions

Preserve progress before switching. Never silently expand scope.

## 9. Evidence for the evaluator

After each checkpoint, surface:

- Command/workflow and relevant result
- Acceptance and overlay status changes
- Regressions checked
- Diff and review status
- Goal-fit result
- No-progress count
- Remaining gap and next action
- State artifact updated

The evaluator may not inspect files or run commands independently. “Implemented,” task counts, code inspection, or weakened checks are not completion evidence.

## 10. Independent review

Use fresh review or isolated subagents for high-blast-radius, security, authorization, migration, concurrency, reliability, architecture, compliance, accessibility, or subjective visual changes when practical.

Provide the reviewer the contract, relevant diff, evidence, and overlays—not the implementer's persuasive narrative. Treat findings as hypotheses until verified.

## 11. Stall detection

Progress requires at least one of:

- New verified evidence
- Smaller reproducible failure
- Changed testable hypothesis
- Closed acceptance gap
- Newly proven blocker or approval boundary
- Reusable verifier, fixture, diagnostic, or harness improvement that materially advances the next cycle

After two consecutive no-progress cycles, stop as Stalled and preserve a restartable handoff. Do not repeat unchanged deterministic failures.

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
- Stable evaluation → benchmark or test
- Important limitation → residual-risk documentation

Do not permanently document speculation or duplicate authoritative material.

## 14. Preserve lifecycle state and closeout

- **Paused** is non-terminal: persist progress, branch/SHA, next action, and resume condition.
- **Achieved, Cancelled, Superseded, Blocked, Approval required, Budget exhausted, and Stalled** receive closeout packets when the run is closed.

At closeout:

1. Snapshot `CONTRACT.md`, `PROGRESS.md`, and `RESULT.md`
2. Update portfolio and history
3. Link reusable outputs and related goals
4. Record library version and contract revision
5. Exclude secrets, private data, production dumps, exploit-enabling evidence, and unnecessary logs

Closed evidence is immutable. Later work receives a new Goal ID or approved revision and links back.

## 15. Completion

Declare **Achieved** only when:

- Every acceptance item passes with surfaced evidence
- Required overlay and broader gates pass
- Protected behavior and baseline have not regressed
- Important changes are reviewed and unexplained diffs resolved
- Durable state, harness, and knowledge are current
- Closeout packet is complete
- Working tree has no unexplained agent-created changes

Close with:

```text
Outcome:
Goal ID / revision / portfolio state:
Acceptance and overlay evidence:
Delivered behavior:
Regression and review status:
Reusable outputs and harness updates:
Residual risk:
State and archive paths:
Next action: only when not achieved
```
