# Goal Engine: State, Evidence, and Reuse

Use the repository's existing plan, progress, issue, milestone, handoff, and history formats when they can represent the state below. Do **not** create a competing source of truth merely because templates exist.

When no suitable convention exists, use:

```text
GOAL.md
GOAL_PROGRESS.md
docs/goals/INDEX.md
docs/goals/<goal-id>/
├── CONTRACT.md
├── PROGRESS.md
└── RESULT.md
```

Templates:

- [../templates/goal-progress-template.md](../templates/goal-progress-template.md)
- [../templates/goal-result-template.md](../templates/goal-result-template.md)
- [../templates/goal-history-index-template.md](../templates/goal-history-index-template.md)

## Active-state rules

- `GOAL.md` or its authoritative equivalent holds the approved contract.
- `GOAL_PROGRESS.md` or the repository's existing state artifact holds mutable execution state.
- One active goal must not silently overwrite another.
- A closed or superseded goal must retain its own archive packet.
- Link to authoritative requirements instead of duplicating them.
- Record the library version/source commit so later readers can reproduce the workflow assumptions.

## Minimal progress state

The progress template records:

- Goal ID, contract, profile, library version, branch/SHA, and checkpoint
- Verified baseline and preserved working changes
- Acceptance ledger with exact verifiers
- Completed changes
- Failed or reverted approaches
- Contradictions, risks, blockers, and approvals
- No-progress count
- One next highest-priority unblocked action

Use only these acceptance statuses:

```text
Pass
Fail
Blocked
Not run
```

## Evidence quality

Prefer evidence in this order:

1. Deterministic repository-native commands with exact results
2. Reproduction or realistic runtime workflow
3. Integration, E2E, UAT, security, performance, or migration evidence
4. Reviewed diff tied to the contract
5. Stable rubric-based evaluation for subjective properties
6. Code inspection or agent judgment only as supporting context

An acceptance item is **Pass** only when its stated verifier has run successfully under the required conditions. “Implemented,” “reviewed,” or “looks correct” is not a verifier.

## Baseline discipline

- Record pre-existing failures before changing them.
- Do not hide regressions by redefining the baseline after edits.
- If a verifier must change because the requirement changed, obtain contract-required approval and explain the before/after semantics.
- A narrower targeted check may guide an iteration; the contract's broader final gates still determine completion.
- Preserve user-authored and unrelated working changes.

## Keep-or-revert rule

Keep a change only when it:

- Advances at least one contract acceptance item or removes a verified blocker
- Preserves protected behavior
- Does not introduce unexplained new failures
- Has a coherent, reviewable diff

Otherwise revert only the agent-authored slice when safe. Never discard unrelated or user-authored work.

## No-progress accounting

Count a serious cycle as progress only when it produces at least one of:

- New verified evidence
- A smaller reproducible failure
- A changed and testable hypothesis
- A closed acceptance gap
- A newly proven external blocker or approval boundary
- A reusable verifier, fixture, or diagnostic that materially improves the next cycle

Record no-progress cycles explicitly. Reset the count only when one of those outcomes occurs.

## Checkpoint update

At each meaningful checkpoint, surface and persist:

```text
Goal ID:
Profile:
Current gap:
Change made:
Verifier and result:
Acceptance items changed:
Regression status:
Review status:
Reusable discovery:
No-progress count:
Remaining highest-priority gap:
Blocker or approval needed:
State artifact:
```

## Durable-knowledge promotion

Before closeout, promote verified knowledge to its permanent home:

| Knowledge | Preferred home |
|---|---|
| Corrected failure | Regression test |
| Product or architecture decision | Approved document or ADR |
| Operational recovery or release procedure | Runbook |
| Stable benchmark or acceptance flow | Repository-owned script or test |
| Reusable fixture or specimen | Maintained test-data path |
| Important limitation | Product/architecture documentation or residual-risk record |

Do not promote speculative observations or duplicate material already stored authoritatively.

## Closeout archive

Archive every terminal outcome, not only success:

- **Achieved**
- **Blocked**
- **Approval required**
- **Budget exhausted**
- **Stalled**
- **Superseded**

The archive contains:

```text
CONTRACT.md  approved target and boundaries
PROGRESS.md  final ledger, evidence, attempts, blockers, and next action
RESULT.md    outcome, delivered behavior, reuse outputs, and residual risk
```

Update `docs/goals/INDEX.md` or the repository's existing history index with:

- Goal ID
- Close date
- Outcome
- Profile
- One-line target
- Result link
- Reusable outputs

Preserve history. Do not edit an old result to make later work appear part of the original goal; create a new Goal ID and link related goals.

## Sensitive-data guard

Never commit:

- Secrets, tokens, credentials, or private keys
- Private user data
- Raw production database dumps
- Unredacted security evidence that increases exploitability
- Large logs when a concise excerpt, checksum, or secure-system link is sufficient

When evidence must stay outside Git, record a stable approved reference and the minimum metadata needed to retrieve it lawfully.

## Result quality

A useful `RESULT.md` lets a fresh agent answer:

- What was supposed to become true?
- What actually happened?
- Which exact evidence supports the outcome?
- What behavior changed?
- What did not change?
- What failed or was reverted?
- What durable knowledge was promoted?
- What can be reused next time?
- What residual risk or next action remains?

A closeout packet is not a substitute for regression tests, ADRs, runbooks, or product documentation. It is the indexable evidence trail that links them together.
