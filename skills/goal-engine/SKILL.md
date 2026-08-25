---
name: goal-engine
description: Execute one approved Goal Contract safely inside a native /goal loop while adapting to project goal portfolios, contract revisions, assurance overlays, and repository-specific harnesses. Use for brownfield orientation, profile- or custom-loop execution, native verification, regression protection, durable state, reusable closeout, and bounded autonomy. Use shape-goal when the target or lifecycle must materially change.
compatibility: Portable Agent Skills host with repository read/write tools. Native /goal support is required for durable continuation and host-side completion evaluation.
metadata:
  author: chrisduvillard
  version: "0.3.0"
  source: "github.com/chrisduvillard/loop-engineering-goal-library"
---

# Goal Engine

Execute one approved outcome without losing brownfield safety, adapting silently to a different goal, or discarding knowledge.

> **Profile = loop shape · overlays = cross-cutting proof · harness = project mechanics · contract = project truth · native `/goal` = persistence**

## Required inputs

Identify:

1. Approved Goal Contract, stable Goal ID, and revision.
2. Lifecycle state, priority, dependencies, parent/related goals, and portfolio path when applicable.
3. Primary execution profile or custom-loop definition.
4. Assurance overlays.
5. Project harness or authoritative setup/run/verify sources.
6. Progress, archive, history, library-version, branch/worktree, and authority information.

If the outcome, evidence, protected behavior, lifecycle, or durable paths are materially unresolved, stop before production edits and use `shape-goal`.

## Native-goal boundary

This skill supplies execution discipline; it does not replace native `/goal`.

- **Inside an active `/goal`:** execute one contract and continue across turns.
- **Outside an active `/goal`:** validate the contract and return a copy-ready native command.

One native goal session should execute one dependency-safe leaf contract. Parallel project goals require isolated sessions/worktrees, non-overlapping ownership, and explicit coordination.

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use its selected execution profile, assurance overlays, and project harness. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. At checkpoints, detect material goal drift instead of silently expanding scope. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve reusable state and leave a restartable handoff.
```

## 1. Orient from actual state

Read applicable repository instructions, contract and sources, architecture, plans, portfolio, prior goal archives, progress/handoffs, project harness, native scripts/CI/tests, runtime entry points, Git status/diff/branch/HEAD/worktrees, and relevant history.

Protect uncommitted, user-authored, and unrelated work. Never obtain a clean tree by discarding it.

## 2. Reconcile before trusting

Resolve documentation, plan, code, test, runtime, portfolio, and Git contradictions using:

1. Explicit authority in repository instructions or contract
2. Later approved decisions over drafts
3. Current executable evidence over unsupported status claims
4. Owner escalation when materially different outcomes remain plausible

A stale checklist is not proof that work remains; existing code is not proof that a requirement passes.

## 3. Validate lifecycle and isolation

Proceed only when:

- The contract is Approved or Active and names one outcome.
- Goal ID, revision, profile/custom loop, overlays, state, and archive paths are defined.
- Dependencies are satisfied or explicitly handled.
- Scope, verifiers, protected behavior, authority, review triggers, and exits are clear.
- The branch/worktree is compatible with the active portfolio entry.
- No different active goal, shared mutable resource, or unrelated work will be overwritten.

A contract may strengthen a profile or overlay, but profiles and overlays may not weaken the contract or expand authority.

## 4. Load the execution pattern

Read [references/loop-profiles.md](references/loop-profiles.md).

- Apply one primary preset when selected.
- For **Custom Contract-Driven**, require an explicit iteration unit, primary verifier, keep-or-revert rule, review strategy, and stop condition.
- Borrow a narrow technique from another profile only when it improves evidence without changing the outcome.

Read [references/assurance-overlays.md](references/assurance-overlays.md) and apply each selected overlay as additional acceptance, review, and authority obligations.

## 5. Reuse the project harness

Use the repository's verified setup, run, reset, and check commands. Do not rediscover them every goal.

When current sources are absent, contradictory, or repeatedly rediscovered:

1. Verify the commands and supported environments.
2. Update an existing authoritative document or create `docs/agent/PROJECT_HARNESS.md` from [templates/project-harness-template.md](templates/project-harness-template.md).
3. Link to canonical scripts rather than copying them.
4. Mark unverified assumptions and freshness triggers.

A stale harness is a hypothesis, not authority.

## 6. Establish the verified baseline

Record branch/SHA/worktree, preserved changes, exact native checks and results, known pre-existing failures, acceptance status, dependencies, no-progress count, and the next highest-priority unblocked gap.

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
9. **Record** evidence, attempts, reusable discoveries, portfolio-relevant changes, and next action.
10. **Repeat** without asking what comes next when contract and evidence answer it.

Do not stop at planning, scaffolding, documentation, analysis, or test creation while production implementation required by the contract remains.

## 8. Run the goal-fit gate at checkpoints

Check whether the approved contract still represents the user's current need.

Continue without interruption when new information is merely an implementation detail or clarification.

Pause and use `shape-goal` when any of these is material:

- A different observable outcome is requested
- Priority changes affect which goal should run
- Scope, acceptance evidence, protected behavior, authority, or stop conditions must change
- A new incident or external event should interrupt the current goal
- The goal should split, merge, pause, resume, cancel, or supersede
- The primary profile or required overlays no longer match the dominant risk

Do not silently expand scope. Preserve progress before switching.

## 9. Surface evidence for the evaluator

After each checkpoint, surface concise command/workflow results, acceptance-status changes, regressions checked, review status, overlays exercised, no-progress count, remaining gap, goal-fit result, and state path.

The evaluator may not inspect files or run tools independently. “Implemented,” task counts, code inspection, or a weakened verifier are not completion evidence.

## 10. Review independently where it matters

Use fresh review or isolated subagents for high-blast-radius, security, authorization, migration, concurrency, reliability, architecture, compliance, or subjective UX changes when practical. Provide contract, diff, evidence, and relevant overlays—not the implementer's persuasive narrative.

Treat findings as hypotheses until reproduced or otherwise verified.

## 11. Detect stalls and circular work

Progress requires at least one of:

- New verified evidence
- Reduced reproducible failure
- Changed testable hypothesis
- Closed acceptance gap
- Newly proven blocker or approval boundary
- Reusable verifier, fixture, diagnostic, or harness improvement that materially advances the next cycle

After two consecutive no-progress cycles, stop as Stalled, preserve state, and leave a restartable handoff. Do not repeat unchanged deterministic failures.

## 12. Respect authority boundaries

Unless explicitly authorized, require approval before merge, push, tag, publish, deploy, release, production mutation, destructive data/schema/infrastructure/branch actions, credential/billing/account changes, or removal of recovery paths.

Autonomous continuation never implies broader authority.

## 13. Promote durable knowledge

Move verified recurring knowledge to regression tests, approved docs/ADRs, runbooks, project harness, fixtures, scripts, benchmarks, or residual-risk records. Do not permanently document speculation or duplicate authoritative material.

## 14. Preserve lifecycle state and closeout

- **Paused** is non-terminal: persist progress, resume condition, branch/SHA, and portfolio state.
- **Achieved, Cancelled, Superseded, Blocked, Approval required, Budget exhausted, and Stalled** receive terminal closeout packets when the repository treats the run as closed.

At closeout:

1. Snapshot `CONTRACT.md`, `PROGRESS.md`, and `RESULT.md` under the archive path.
2. Update history and portfolio.
3. Link reusable outputs and related goals.
4. Record library version and contract revision.
5. Exclude secrets, private data, raw production dumps, exploit-enabling evidence, and unnecessary logs.

Closed evidence is immutable. Later work gets a new Goal ID or approved revision and links back.

## 15. Finish with evidence

Declare success only when every acceptance item passes, protected behavior and baseline are preserved, required overlay and broader gates pass, important changes are reviewed, durable state and knowledge are current, the closeout packet is complete, and the working tree has no unexplained agent-created changes.

Close with:

- **Outcome:** Achieved / Paused / Cancelled / Superseded / Blocked / Approval required / Budget exhausted / Stalled
- **Goal ID / revision / portfolio state**
- **Acceptance and overlay evidence**
- **Delivered behavior and regression status**
- **Reusable outputs and harness updates**
- **Residual risk**
- **State and archive paths**
- **Next action:** only when not achieved
