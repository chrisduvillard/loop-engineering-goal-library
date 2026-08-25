---
name: goal-engine
description: Execute an approved Goal Contract safely inside a native /goal loop for a mature repository. Use when a goal points to GOAL.md, an issue, PRD, milestone, or other approved contract and needs brownfield orientation, profile-specific execution, repository-native verification, regression protection, durable progress state, reusable closeout archives, and bounded autonomous continuation. Do not use to invent or materially redefine the target; use shape-goal first.
compatibility: Portable Agent Skills host with repository read/write tools. Native /goal support is required for durable continuation and host-side completion evaluation.
metadata:
  author: chrisduvillard
  version: "0.1.0"
  source: "github.com/chrisduvillard/loop-engineering-goal-library"
---

# Goal Engine

Execute an approved outcome without losing brownfield safety or the knowledge created along the way.

> **Skill = method · Goal Contract = project truth · native `/goal` = persistence · archive = reusable memory**

Do not reopen settled product decisions merely because implementation is difficult. Do not silently reinterpret the contract to make completion easier.

## Required inputs

Identify:

1. The approved Goal Contract path or authoritative issue/spec.
2. The stable Goal ID.
3. The execution profile named by the contract.
4. The repository's existing progress or handoff artifact.
5. The closeout archive and history-index paths.
6. The library version or source commit recorded by the contract.

If the outcome, scope, acceptance evidence, protected behavior, authority boundaries, stop conditions, or durable state paths are materially unresolved, stop before production edits and use `shape-goal`.

## Native-goal boundary

This skill supplies execution discipline; it does not replace the host's native `/goal` mechanism.

- **Inside an active `/goal`:** execute the contract and continue across turns.
- **Outside an active `/goal`:** validate the contract and return the copy-ready command below. Do not pretend a normal turn has durable continuation or an independent completion evaluator.

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the execution profile named in the contract. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve a reusable closeout packet and leave a restartable handoff.
```

## 1. Orient from actual state

Before any persistent change, read the applicable:

- Repository and agent instructions
- Goal Contract and its authoritative sources
- Specifications, PRDs, architecture docs, ADRs, and domain vocabulary
- Approved plans, milestones, progress files, prior goal archives, and handoffs
- Native scripts, tests, CI, release gates, and runtime entry points
- Git status, diff, branch, HEAD, and relevant history

Protect uncommitted, user-authored, and unrelated work. Never discard or overwrite changes merely to obtain a clean tree.

## 2. Reconcile before trusting

Documentation, plans, tests, code, runtime behavior, and Git history may disagree. Record material contradictions and reconcile them using:

1. Explicit authority in repository instructions or the Goal Contract
2. Later approved decisions over older drafts
3. Current executable evidence over unsupported status claims
4. Owner escalation when materially different product outcomes remain plausible

A stale checklist is not proof that work remains. Existing code is not proof that a requirement is satisfied.

## 3. Validate the contract and lifecycle

Proceed only when all are true:

- The contract is approved and names one observable outcome.
- It has a stable Goal ID.
- In-scope and out-of-scope boundaries are understandable to a fresh agent.
- Every acceptance item has an observable verifier or evidence form.
- Protected behavior and compatibility constraints are named.
- Authority and irreversible-action boundaries are explicit.
- Success, blocker, budget, and stalled exits are defined.
- The selected execution profile is compatible with the outcome.
- Progress and archive paths are defined.
- No different active goal would be overwritten.

Contract clauses override profile defaults. A profile may strengthen safety but may not weaken acceptance criteria or expand authority.

## 4. Load the execution profile

Read [references/loop-profiles.md](references/loop-profiles.md) and apply the profile selected by the contract. Use only one primary profile; borrow a secondary profile's verifier or review technique only when it materially improves evidence without expanding scope.

## 5. Establish the verified baseline

Discover repository-native checks rather than assuming a language, framework, or package manager. Record:

- Current branch and SHA
- Working-tree changes that must be preserved
- Relevant checks and their exact results
- Known pre-existing failures and accepted exceptions
- Current acceptance-item status
- The next highest-priority unblocked gap

Use [references/state-and-evidence.md](references/state-and-evidence.md) when the repository lacks an established state format. Its templates are:

- [templates/goal-progress-template.md](templates/goal-progress-template.md)
- [templates/goal-result-template.md](templates/goal-result-template.md)
- [templates/goal-history-index-template.md](templates/goal-history-index-template.md)

## 6. Initialize durable state safely

Use the repository's existing plan, issue, progress, handoff, and history system when it can represent the contract.

Otherwise:

```text
GOAL.md
GOAL_PROGRESS.md
docs/goals/INDEX.md
docs/goals/<goal-id>/
```

Rules:

- Never create a second active progress source when one already exists.
- Never overwrite another active goal.
- Preserve the exact baseline before edits.
- Record library version/source, Goal ID, contract, profile, branch/SHA, no-progress count, and next action.
- Keep secrets, credentials, private user data, raw production dumps, and oversized logs out of committed state.

## 7. Run the brownfield loop

Repeat:

1. **Select** the highest-priority unblocked gap that advances the contract.
2. **Verify** that the gap is real before changing code.
3. **Change** the smallest coherent, reversible production slice.
4. **Check** it with the smallest relevant repository-native verifier.
5. **Protect** the fix with regression coverage when a failure was corrected.
6. **Review** the diff for scope drift, hidden contract changes, unrelated edits, and new risk.
7. **Broaden** verification at meaningful checkpoints: integration, E2E, UAT, security, performance, migration, or release gates as applicable.
8. **Keep or revert** based on evidence; never retain a change that worsens the verified state without explicit approval.
9. **Record** evidence, failed or reverted approaches, remaining gaps, blockers, reusable discoveries, and the next action.
10. **Repeat** without asking what to do next when repository evidence and the contract answer it.

Do not stop at planning, scaffolding, documentation, analysis, or test creation while production implementation required by the contract remains.

## 8. Surface evidence for the evaluator

The native goal evaluator may only see the conversation, not the filesystem or commands independently. Surface concise evidence after each checkpoint:

- Command or workflow run
- Relevant exit status and result
- Acceptance items changed to Pass, Fail, Blocked, or Not run
- Regressions checked
- Diff or behavior reviewed
- No-progress count
- Remaining gap and next action
- State artifact updated

Never claim completion from code inspection, task counts, an agent assertion, or a weakened verifier.

## 9. Review independently where it matters

Use a fresh reviewer or isolated subagent for high-blast-radius, security, authorization, migration, concurrency, reliability, architecture, or subjective UI/UX changes when practical. Give it the contract, relevant diff, and acceptance criteria—not the implementer's persuasive narrative.

Treat reviewer and scanner findings as hypotheses. Reproduce or otherwise verify them before remediation.

## 10. Detect stalls and circular work

A no-progress cycle is a serious iteration that produces none of:

- New verified evidence
- A reduced failing case
- A changed, testable hypothesis
- A closed acceptance gap
- A newly identified genuine blocker
- A reusable diagnostic, fixture, or verifier that materially improves the next cycle

Do not repeat an unchanged deterministic failure or retry the same approach without a reason state has changed. After two consecutive no-progress cycles, stop as **Stalled**, preserve evidence, and leave a restartable handoff. Stalled is not success.

## 11. Respect authority boundaries

The contract controls permission. Unless it explicitly authorizes the action, require approval before:

- Merge, push, tag, publish, deploy, release, or production mutation
- Destructive data, schema, infrastructure, or branch operations
- Credential, billing, account, secret, or external-system changes
- Irreversible migrations or removal of rollback paths

Autonomous continuation never implies broader authority.

## 12. Promote durable knowledge

Before closeout, move reusable knowledge out of transient chat and into the correct repository-owned location:

- Corrected failures → regression tests
- Stable product or architecture decisions → approved docs or ADRs
- Operational procedures → runbooks
- Reusable fixtures, commands, scripts, or benchmarks → maintained repository paths
- Important limitations → documented residual risk

Do not turn every observation into permanent documentation. Promote only knowledge that is verified, likely to recur, and useful to a future maintainer or agent.

## 13. Preserve the closeout packet

At every terminal outcome—Achieved, Blocked, Approval required, Budget exhausted, or Stalled:

1. Snapshot the approved contract as `CONTRACT.md`.
2. Snapshot the final progress state as `PROGRESS.md`.
3. Create `RESULT.md` from the result template.
4. Store them under the contract's archive path.
5. Update the repository's existing goal-history index or `docs/goals/INDEX.md`.
6. Link reusable tests, ADRs, runbooks, fixtures, commands, and tooling.
7. Record the exact library version or source commit.
8. Exclude secrets, private data, raw production dumps, and unnecessary logs.

Preserve history rather than rewriting a prior result. If the goal was superseded, archive the superseded contract and link to its replacement.

## 14. Finish with evidence

Declare success only when:

- Every in-scope acceptance item passes with surfaced evidence.
- Protected behavior and the relevant baseline have not regressed.
- Required broader gates pass.
- Important changes have been reviewed and unexplained diffs resolved.
- Progress, handoff, release, and contract state are current.
- Durable knowledge has been promoted where appropriate.
- The closeout packet and history index are complete.
- The working tree contains no unexplained changes created by the run.

Close with:

- **Outcome:** Achieved, Blocked, Approval required, Budget exhausted, or Stalled
- **Acceptance evidence:** concise item-by-item results
- **Changes:** production behavior delivered
- **Regression status:** checks and protected behavior
- **Reusable outputs:** tests, docs, ADRs, fixtures, commands, or tooling
- **Residual risk:** bounded and explicit
- **State artifact:** updated path or issue
- **Archive:** closeout packet path
- **Next action:** only when not achieved
