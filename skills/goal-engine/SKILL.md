---
name: goal-engine
description: Execute an approved Goal Contract safely inside a native /goal loop for a mature repository. Use when a goal points to GOAL.md, an issue, PRD, milestone, or other approved contract and needs brownfield orientation, profile-specific execution, repository-native verification, regression protection, durable progress state, and bounded autonomous continuation. Do not use to invent or materially redefine the target; use shape-goal first.
---

# Goal Engine

Execute an approved outcome without losing brownfield safety.

> **Skill = method · Goal Contract = project-specific truth · `/goal` = persistence and evaluation**

Do not reopen settled product decisions merely because implementation is difficult. Do not silently reinterpret the contract to make completion easier.

## Required inputs

Identify:

1. The approved Goal Contract path or authoritative issue/spec.
2. The execution profile named by the contract.
3. The repository's existing progress or handoff artifact, when one exists.

If there is no approved contract, or if the outcome, scope, acceptance evidence, protected behavior, authority boundaries, or stop conditions are materially unresolved, stop before production edits and use the `shape-goal` skill.

## Native-goal boundary

This skill supplies execution discipline; it does not replace the host's native `/goal` mechanism.

- **Inside an active `/goal`:** execute the contract and continue across turns.
- **Outside an active `/goal`:** validate the contract and return the copy-ready command below. Do not pretend a normal turn has durable continuation or an independent completion evaluator.

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the execution profile named in the contract. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; leave a restartable handoff.
```

## 1. Orient from actual state

Before any persistent change, read the applicable:

- Repository and agent instructions
- Goal Contract and its authoritative sources
- Specifications, PRDs, architecture docs, ADRs, and domain vocabulary
- Approved plans, milestones, progress files, and handoffs
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

## 3. Validate the contract

Proceed only when all are true:

- The contract is approved and names one observable outcome.
- In-scope and out-of-scope boundaries are understandable to a fresh agent.
- Every acceptance item has an observable verifier or evidence form.
- Protected behavior and compatibility constraints are named.
- Authority and irreversible-action boundaries are explicit.
- Success, blocker, budget, and stalled exits are defined.
- The selected execution profile is compatible with the outcome.

Contract clauses override profile defaults. A profile may strengthen safety but may not weaken acceptance criteria or expand authority.

## 4. Load the execution profile

Read [references/loop-profiles.md](references/loop-profiles.md) and apply the profile selected by the contract. Use only one primary profile; borrow a secondary profile's verifier or review technique only when it materially improves evidence without expanding scope.

## 5. Establish the verified baseline

Discover the repository-native checks rather than assuming a language, framework, or package manager. Record:

- Current branch and SHA
- Working-tree changes that must be preserved
- Relevant checks and their exact results
- Known pre-existing failures and accepted exceptions
- Current acceptance-item status
- The next highest-priority unblocked gap

Use [references/state-and-evidence.md](references/state-and-evidence.md) when the repository lacks an established state format.

## 6. Run the brownfield loop

Repeat:

1. **Select** the highest-priority unblocked gap that advances the contract.
2. **Verify** that the gap is real before changing code.
3. **Change** the smallest coherent, reversible production slice.
4. **Check** it with the smallest relevant repository-native verifier.
5. **Protect** the fix with regression coverage when a failure was corrected.
6. **Review** the diff for scope drift, hidden contract changes, unrelated edits, and new risk.
7. **Broaden** verification at meaningful checkpoints: integration, E2E, UAT, security, performance, or release gates as applicable.
8. **Keep or revert** based on evidence; never retain a change that worsens the verified state without explicit approval.
9. **Record** evidence, failed or reverted approaches, remaining gaps, blockers, and the next action.
10. **Repeat** without asking what to do next when repository evidence and the contract answer it.

Do not stop at planning, scaffolding, documentation, analysis, or test creation while production implementation required by the contract remains.

## 7. Surface evidence for the evaluator

The native goal evaluator may only see the conversation, not the filesystem or commands independently. Surface concise evidence after each checkpoint:

- Command or workflow run
- Relevant exit status and result
- Acceptance items changed to Pass, Fail, Blocked, or Not run
- Regressions checked
- Diff or behavior reviewed
- Remaining gap and next action

Never claim completion from code inspection, task counts, an agent assertion, or a weakened verifier.

## 8. Review independently where it matters

Use a fresh reviewer or isolated subagent for high-blast-radius, security, authorization, migration, concurrency, reliability, architecture, or subjective UI/UX changes when practical. Give it the contract, relevant diff, and acceptance criteria—not the implementer's persuasive narrative.

Treat reviewer and scanner findings as hypotheses. Reproduce or otherwise verify them before remediation.

## 9. Detect stalls and circular work

A no-progress cycle is a serious iteration that produces none of:

- New verified evidence
- A reduced failing case
- A changed, testable hypothesis
- A closed acceptance gap
- A newly identified genuine blocker

Do not repeat an unchanged deterministic failure or retry the same approach without a reason state has changed. After two consecutive no-progress cycles, stop as **Stalled**, preserve evidence, and leave a restartable handoff. Stalled is not success.

## 10. Respect authority boundaries

The contract controls permission. Unless it explicitly authorizes the action, require approval before:

- Merge, push, tag, publish, deploy, release, or production mutation
- Destructive data, schema, infrastructure, or branch operations
- Credential, billing, account, secret, or external-system changes
- Irreversible migrations or removal of rollback paths

Autonomous continuation never implies broader authority.

## 11. Finish with evidence

Declare success only when:

- Every in-scope acceptance item passes with surfaced evidence.
- Protected behavior and the relevant baseline have not regressed.
- Required broader gates pass.
- Important changes have been reviewed and unexplained diffs resolved.
- Progress, handoff, release, or contract state is current.
- The working tree contains no unexplained changes created by the run.

Close with:

- **Outcome:** Achieved, Blocked, Approval required, Budget exhausted, or Stalled
- **Acceptance evidence:** concise item-by-item results
- **Changes:** production behavior delivered
- **Regression status:** checks and protected behavior
- **Residual risk:** bounded and explicit
- **State artifact:** updated path or issue
- **Next action:** only when not achieved
