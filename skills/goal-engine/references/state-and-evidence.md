# Goal Engine: State, Evidence, Portfolio, Shaping, and Reuse

Use existing project trackers, plans, issues, milestones, progress files, decision logs, handoffs, runbooks, and history formats when they can represent the state below. Do **not** create competing sources of truth merely because templates exist.

Default simple mode:

```text
GOAL.md
GOAL_PROGRESS.md
docs/goals/INDEX.md
docs/goals/<goal-id>/
├── SHAPING.md
├── CONTRACT.md
├── PROGRESS.md
└── RESULT.md
```

When multiple non-closed goals need coordination and no suitable tracker exists, add:

```text
docs/goals/PORTFOLIO.md
```

Templates:

- [../templates/goal-progress-template.md](../templates/goal-progress-template.md)
- [../templates/goal-result-template.md](../templates/goal-result-template.md)
- [../templates/goal-history-index-template.md](../templates/goal-history-index-template.md)
- [../templates/shaping-history-template.md](../templates/shaping-history-template.md)
- [../templates/goal-portfolio-template.md](../templates/goal-portfolio-template.md)
- [../templates/project-harness-template.md](../templates/project-harness-template.md)

## State layers

- **Portfolio or existing tracker:** priorities, dependencies, lifecycle states, relationships, and review triggers across goals.
- **Shaping history:** append-only questions, answers, evidence, recommendations, corrections, deferred decisions, and shaping-round summaries.
- **Goal Contract:** one approved outcome, revision, evidence, protection, profile, overlays, authority, approval shaping round, and exits.
- **Progress state:** mutable baseline, ledger, attempts, blockers, no-progress count, and next action for one goal.
- **Project harness:** verified setup, run, reset, environment, and native-check mechanics reused across goals.
- **History index and archive:** immutable terminal evidence and reusable outputs.

## Active-state rules

- One native `/goal` session or worktree executes one dependency-safe leaf contract.
- Multiple active project goals require isolated branches/worktrees, non-overlapping ownership, and explicit coordination.
- One active goal must not silently overwrite, absorb, or redefine another.
- A paused goal retains shaping history, progress, and a resume condition.
- A closed, cancelled, or superseded goal retains its shaping and closeout packet.
- Link authoritative requirements instead of duplicating them.
- Record library version/source, contract revision, completed shaping rounds, and approval round.

## Shaping-history rules

- Create or resume `docs/goals/<goal-id>/SHAPING.md` as soon as the Goal ID exists, unless an existing authoritative decision log is used.
- Save every question actually asked and every answer that changes or confirms the contract.
- Use stable round/question IDs such as `R2-Q3`.
- Preserve the exact answer when safe and useful; redact sensitive material and use an approved secure reference when necessary.
- Never silently edit an earlier answer. Append a correction and mark the earlier decision superseded.
- Read prior rounds before asking; do not repeat a question without materially new evidence.
- A user may request repeated deepening rounds. Each round must add new decision value and end with a readiness summary.
- The approved contract names the shaping round that authorized execution.

## Goal lifecycle

Use these portfolio states:

```text
Candidate
Ready
Active
Paused
Blocked
Closed
```

Use these closed outcomes:

```text
Achieved
Cancelled
Superseded
Approval required
Budget exhausted
Stalled
Blocked
```

Priority changes do not change contract semantics. Keep the same Goal ID only while the observable outcome remains the same.

## Minimal progress state

Record Goal ID/revision, contract, shaping-history path and approval round, portfolio state, profile, overlays, harness, library version, branch/worktree/SHA, baseline, preserved changes, acceptance ledger, completed changes, failed/reverted approaches, contradictions, blockers, approvals, no-progress count, goal-fit result, and one next action.

Use only these acceptance statuses:

```text
Pass
Fail
Blocked
Not run
```

## Evidence quality

Prefer:

1. Deterministic repository-native commands with exact results
2. Reproduction or realistic runtime workflow
3. Integration, E2E, UAT, security, performance, migration, or overlay evidence
4. Reviewed diff tied to the contract
5. Stable rubric-based evaluation for subjective properties
6. Code inspection or agent judgment only as supporting context

An acceptance item is Pass only when its verifier ran successfully under required conditions. “Implemented,” “reviewed,” or “looks correct” is not proof.

The shaping history is decision evidence, not implementation evidence. It proves what was decided and why; it does not prove production completion.

## Baseline discipline

- Record pre-existing failures before edits.
- Do not redefine the baseline after changes to hide regressions.
- Changing a verifier's semantics requires contract-defined approval and a new shaping entry.
- Targeted checks guide iterations; broader final gates determine completion.
- Preserve user-authored and unrelated work.

## Keep-or-revert rule

Keep a change only when it advances an acceptance item or verified blocker, preserves protected behavior, introduces no unexplained failure, and has a coherent reviewable diff. Otherwise revert only the agent-authored slice when safe.

## Goal-fit and no-progress accounting

At checkpoints record whether the current contract still fits the user's need.

Return to `shape-goal` and append a new shaping round when priority, outcome, scope, proof, protection, authority, profile, overlays, dependencies, lifecycle, or user satisfaction must materially change.

Count a serious cycle as progress only when it produces new verified evidence, a smaller reproduction, a changed testable hypothesis, a closed gap, a proven blocker/approval boundary, a materially useful shaping decision, or a reusable verifier/fixture/diagnostic/harness improvement that advances the next cycle.

Repeated questions or searches without new evidence or decisions are not progress.

## Checkpoint update

```text
Goal ID / revision / portfolio state:
Shaping history / approval round:
Profile and overlays:
Project harness:
Current gap:
Change made:
Verifier and result:
Acceptance items changed:
Regression and review status:
Goal-fit result:
Reusable discovery:
No-progress count:
Remaining highest-priority gap:
Blocker or approval needed:
State artifact:
```

## Durable-knowledge promotion

| Knowledge | Preferred home |
|---|---|
| Questions, answers, trade-offs, and corrections | Shaping history |
| Corrected failure | Regression test |
| Stable product or architecture decision | Approved document or ADR |
| Operational recovery or release procedure | Runbook |
| Stable setup/run/verification recipe | Project harness or project skill |
| Stable benchmark or acceptance flow | Repository-owned script or test |
| Reusable fixture or specimen | Maintained test-data path |
| Important limitation | Product/architecture documentation or residual-risk record |

Promote only verified, recurring knowledge. Do not duplicate canonical material or the full shaping interview.

## Closeout archive

Preserve `SHAPING.md` and archive terminal outcomes as `CONTRACT.md`, `PROGRESS.md`, and `RESULT.md`; update portfolio and history with Goal ID, revision, close date, outcome, profile, overlays, target, shaping link and round count, result link, related goals, and reusable outputs.

Paused goals are not terminal: preserve shaping history, progress, and resume condition without pretending they are complete.

Preserve history. Later work gets a new Goal ID or approved revision and links back.

## Sensitive-data guard

Never commit secrets, tokens, credentials, private keys, private user data, raw production dumps, unredacted exploit-enabling evidence, or large logs when a concise extract, checksum, redacted decision summary, or approved secure reference is sufficient.

## Result quality

A useful result lets a fresh agent answer what was intended, which shaping round approved it, what happened, which evidence supports it, what changed, what remained protected, what failed or was reverted, what goal followed or was superseded, what knowledge was promoted, and what residual risk or next action remains.

## Canonical runtime model

The canonical machine-readable files are:

- `.loop/active-goal.json`
- `.loop/goals/<goal-id>/contract.json`
- `.loop/goals/<goal-id>/progress.json`
- `.loop/leases/<goal-id>.json`

`GOAL.md` and `GOAL_PROGRESS.md` are generated views. They must include a source
hash and must not become competing writable state. Use `scripts/goalctl.py` to
validate and render them.

Lifecycle, run termination, and final outcome are distinct. A paused or blocked
goal is not closed. `Achieved` is valid only after every acceptance item is
`pass`, the declared verifier has succeeded, protected behavior has been
checked, and read-only mutation enforcement has passed when applicable.
