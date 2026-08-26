# Shape Goal: Durable Shaping History

Every question asked during goal shaping—and every answer that changes or confirms the Goal Contract—is durable project knowledge. Preserve it instead of leaving it only in chat.

## Default location

Use an existing authoritative decision log when it preserves the fields below. Otherwise create:

```text
docs/goals/<goal-id>/SHAPING.md
```

Create the file as soon as the Goal ID exists. Keep it for active, paused, superseded, cancelled, blocked, and achieved goals. The contract, portfolio, progress, result, and history index should link to it.

## Append-only rule

- Never silently rewrite or delete an earlier question or answer.
- When the user changes an answer, append a correction and mark the earlier decision superseded.
- When new evidence changes the recommendation, record the evidence and resulting revision.
- Preserve unanswered, deferred, and declined questions with their status.
- Preserve structured decisions rather than copying the entire chat transcript.

Use stable identifiers:

```text
R1       initial shaping round
R1-Q1    first question in round 1
R2-Q3    third question in deepening round 2
```

## The question barrier

A shaping question is an interactive turn boundary:

1. Search and prepare before asking.
2. Save the exact proposed question and its evidence/recommendation.
3. Ask one question.
4. End the turn immediately.
5. On the user's next normal reply, save the answer before continuing.

After asking, do not call tools, keep researching, start background work, ask another question, or continue an autonomous `/goal`. The user should never need to use Steer merely to answer.

## What to record for every question

Record:

- Round and question ID
- Decision lens and unresolved issue
- Why the question was necessary
- Repository or connected evidence considered
- Recommended answer and trade-off
- Exact question asked
- User answer, verbatim when safe and useful
- Normalized decision used by the contract
- Contract sections affected
- Status: Proposed, Answered, Deferred, Declined, or Superseded
- Any prior question or decision superseded

A proposed question is saved before the turn ends; the answer is appended on the next turn.

If an answer contains secrets, credentials, private personal data, confidential business/customer strategy, third-party restricted material, raw production data, or exploit-enabling detail, store a redacted decision summary and approved secure reference rather than the sensitive text.

## Repository visibility and data classification

Before committing a verbatim answer, determine whether the repository and shaping path are public, private, or externally shared. Public visibility is not consent to publish confidential decisions.

- Store verbatim answers only when their classification permits repository storage.
- For confidential strategy, customer commitments, unreleased roadmap, private commercial terms, or third-party restricted material, store a redacted normalized decision plus an approved secure reference.
- Record who can access the secure source and whether it is sufficient for a future authorized agent.
- Mark the contract Blocked when essential evidence cannot be referenced safely.

## Standard and deepening rounds

### Standard round

Resolve the minimum material decisions required for a safe, verifiable Goal Contract. Search first and ask one decision per turn.

### Deepening round

Run when the user asks to go deeper, challenges the contract, is not satisfied with the target, or requests another batch of questions.

Before asking:

1. Read every previous shaping round and current contract.
2. Build a gap map of weak assumptions, untested evidence, unresolved trade-offs, and hidden scope.
3. Select the highest-value unexplored lens.
4. Do not repeat a prior question unless materially new evidence changes it.

Useful lenses include:

- Desired outcome and user value
- Target users, journeys, and non-goals
- Scope boundaries and dependencies
- Acceptance evidence and failure cases
- Compatibility and migration expectations
- UI, UX, content, and accessibility
- Data semantics, privacy, and security
- Reliability, recovery, and operations
- Performance, cost, and resources
- Maintainability, ownership, and long-term support
- Authority, irreversible actions, and risk acceptance

A round is a sequence of one-question interactive turns, not a large questionnaire or a background loop.

## Repeatable deepening

The user may request additional rounds repeatedly:

- Claude Code: `/shape-goal Deepen the current goal`
- Codex CLI / IDE: `$shape-goal Deepen the current goal`
- Natural language: `Run another shaping round for goal-id`

Each round must add new decision value. Stop when the contract is ready, remaining uncertainty is immaterial, a genuine blocker exists, or the user pauses.

At round close, ask one disposition question and return control:

```text
Approve this contract
Run another deeper shaping round
Pause shaping and preserve the current state
```

Approval is itself recorded as a question and answer. Do not begin production execution until the contract references the approval round.

## Contract and closeout linkage

The Goal Contract records:

- Shaping-history path
- Completed round IDs
- Latest shaping round
- Approval round
- Open or deferred decisions
- Exact execution launcher returned after approval

At terminal closeout, preserve:

```text
docs/goals/<goal-id>/
├── SHAPING.md
├── CONTRACT.md
├── PROGRESS.md
└── RESULT.md
```

The result links important decisions instead of duplicating the full history.
