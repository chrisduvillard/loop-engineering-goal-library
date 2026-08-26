# Shape Goal: Durable Shaping History

Every question actually asked during goal shaping, and every answer that changes or confirms the Goal Contract, is durable project knowledge. Preserve it instead of leaving it only in chat.

## Default location

Use an existing authoritative decision log when it already preserves the fields below. Otherwise create:

```text
docs/goals/<goal-id>/SHAPING.md
```

Create the file as soon as the Goal ID exists. Keep it for active, paused, superseded, cancelled, blocked, and achieved goals. The Goal Contract, portfolio, progress state, result, and history index should link to it.

## Append-only rule

Treat the shaping history as an append-only decision record.

- Never silently rewrite or delete an earlier question or answer.
- When the user changes an answer, append a correction and mark the earlier decision as superseded.
- When new evidence changes the recommendation, record the new evidence and the resulting revision.
- Preserve unanswered, deferred, and declined questions with their status.
- Do not copy the full chat transcript; preserve the structured questions, answers, evidence, recommendations, and contract impact.

Use stable identifiers:

```text
R1       initial shaping round
R1-Q1    first question in round 1
R2-Q3    third question in deepening round 2
```

## What to record for every question

Record immediately after the answer:

- Round and question ID
- Decision lens and unresolved issue
- Why the question was necessary
- Repository or connected evidence considered
- Recommended answer and trade-off
- The exact question asked
- The user's answer, verbatim when safe and useful
- Normalized decision used by the contract
- Contract sections affected
- Status: Answered, Deferred, Declined, or Superseded
- Any prior question or decision superseded

If an answer contains secrets, credentials, private personal data, raw production data, or exploit-enabling detail, store a redacted decision summary and an approved secure reference rather than the sensitive text.

## Standard and deepening rounds

### Standard shaping round

Resolve the minimum material decisions required for a safe, verifiable Goal Contract. Search repository evidence first and ask one decision at a time.

### Deepening round

Run when the user asks to go deeper, challenges the proposed contract, is not satisfied with the target, or requests another batch of questions.

Before asking anything:

1. Read every previous shaping round and the current contract.
2. Build a gap map of weak assumptions, untested evidence, unresolved trade-offs, and potentially hidden scope.
3. Select the highest-value unexplored lens.
4. Do not repeat a prior question unless materially new evidence changes it.

Useful lenses include:

- Desired outcome and user value
- Target users, journeys, and non-goals
- Scope boundaries and dependencies
- Acceptance evidence and failure cases
- Compatibility and migration expectations
- UI, UX, content, and accessibility decisions
- Data semantics, privacy, and security boundaries
- Reliability, recovery, and operational behavior
- Performance, cost, and resource budgets
- Maintainability, ownership, and long-term support
- Authority, irreversible actions, and risk acceptance

A round is a sequence of one-at-a-time questions, not a large questionnaire. At the end of each round, summarize new decisions, contract revisions, remaining uncertainty, and readiness.

## Repeatable deepening

The user may request additional rounds repeatedly:

- **Claude Code:** `/shape-goal Deepen the current goal`
- **Codex CLI / IDE:** `$shape-goal Deepen the current goal`
- Equivalent natural language: `Run another shaping round for <goal-id>`

Each round must add new decision value. Stop a round when the contract is ready, the remaining uncertainty is immaterial, a genuine owner/external blocker exists, or the user pauses shaping.

At round close, offer the lifecycle result:

```text
Approve this contract
Run another deeper shaping round
Pause shaping and preserve the current state
```

Do not begin production execution until the approved contract references the shaping round that authorized it.

## Contract and closeout linkage

The Goal Contract records:

- Shaping-history path
- Number and IDs of completed rounds
- Last shaping round
- Approval round
- Open or deferred decisions

At terminal closeout, preserve the shaping record with the other goal evidence:

```text
docs/goals/<goal-id>/
├── SHAPING.md
├── CONTRACT.md
├── PROGRESS.md
└── RESULT.md
```

The closeout result should link important decisions rather than duplicating the full history.
