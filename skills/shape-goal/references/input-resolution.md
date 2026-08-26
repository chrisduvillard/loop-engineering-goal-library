# Shape Goal: Input Resolution Protocol

Use this protocol whenever a launcher is copied unchanged and the repository-specific target, scope, evidence, or boundaries are not already approved.

Read [shaping-history.md](shaping-history.md) before asking any user question.

## The input ledger

Create a concise ledger before asking questions:

| Input | Status | Evidence, decision, or question source |
|---|---|---|
| Outcome | Unresolved / Evidence / Safe default / Owner decision | [SOURCE OR R1-Q1] |
| Scope and exclusions | ... | ... |
| Acceptance evidence | ... | ... |
| Protected behavior | ... | ... |
| Authority boundaries | ... | ... |
| Profile-specific inputs | ... | ... |

Do not persist an approved contract while any material row is unresolved. Link every owner-decision row to its saved question-and-answer ID.

## Create or resume shaping history

Once a Goal ID exists, use an existing authoritative decision log when suitable; otherwise create:

```text
docs/goals/<goal-id>/SHAPING.md
```

Before asking:

1. Read all previous shaping rounds.
2. Read the current contract and input ledger.
3. Check whether the decision was already answered, deferred, declined, corrected, or superseded.
4. Ask again only when materially new evidence changes the choice.

The shaping record is append-only. Corrections create a new question/decision entry and reference the prior one.

## Search before asking

Search in this order, using every lawful source available to the host:

1. Repository and agent instructions
2. Current Git status, diff, branches/worktrees, and relevant history
3. Active Goal Contract, shaping history, portfolio, progress, handoffs, and prior closeout archives
4. Approved PRDs, specifications, issues, milestones, ADRs, architecture, design references, and domain vocabulary
5. Native scripts, CI, tests, fixtures, benchmarks, release gates, and package/task configuration
6. Runtime entry points, real product behavior, logs, screenshots, generated artifacts, and supported environments
7. Connected authoritative issue trackers, documentation systems, design files, incident systems, or data catalogs when available and permitted
8. Official external documentation when a changing dependency, platform, standard, or regulation is materially relevant

Triangulate important claims. A stale plan, checkbox, code presence, or one reviewer opinion is not sufficient evidence by itself.

## Visibility and information classification

Before persisting a verbatim answer, determine repository visibility and whether the answer contains confidential business strategy, customer commitments, unreleased roadmap, commercial terms, or third-party restricted material. Store a redacted normalized decision plus an approved secure reference when repository storage is not appropriate.

## Safe defaults

Use a default without asking only when it is reversible, low-risk, consistent with repository conventions, and does not materially change product scope or authority. Record the default and why it is safe.

Never default:

- The product outcome when several materially different outcomes are plausible
- Removal of compatibility or protected behavior
- Destructive, production, credential, billing, release, legal, or external-system authority
- Acceptance thresholds that determine whether the user considers the work successful
- Risk acceptance, privacy policy, compliance interpretation, or irreversible migration choices

## Ask one material decision at a time

After searchable sources are exhausted:

1. Assign the next stable round/question ID, such as `R1-Q2`.
2. State the unresolved decision.
3. Summarize the evidence and conflict.
4. Present no more than three materially different options.
5. Recommend one option and explain the trade-off.
6. Ask one direct question.
7. After the answer, append the exact question and the user's answer to `SHAPING.md` immediately.
8. Record a normalized decision, contract impact, and any superseded answer.
9. Update the input ledger and contract draft.
10. Do not ask the same question again unless new evidence materially changes it.

Questions should be concrete and easy to answer. Do not ask users to discover file paths, commands, implementation details, or repository facts that the agent can inspect.

Preserve the answer verbatim when safe and useful. For secrets, credentials, private personal data, confidential business/customer information, third-party restricted material, raw production data, or exploit-enabling detail, store a redacted decision summary and an approved secure reference instead.

## Standard and deeper rounds

The first round resolves the minimum material decisions required for readiness.

When the user is not satisfied or asks for another batch of questions, open a new deepening round:

1. Read every prior question and answer.
2. Build a gap map for weak assumptions, hidden scope, missing failure cases, and fragile evidence.
3. Select the most valuable unexplored lens.
4. Ask one non-duplicate material question at a time.
5. Close the round with new decisions, contract changes, remaining uncertainty, and a readiness recommendation.

The user may request repeated rounds. Each round must add decision value; repeated questions without new evidence count as no progress.

## Exhaustive, not circular

“Relentless” means continuing until every material input is resolved, not repeating searches or questions.

Stop a shaping round only when:

- The current contract is ready for approval
- A named external source, credential, lawful-access constraint, or unavailable decision owner blocks resolution
- The user declines or defers a material decision
- The approved shaping budget is exhausted
- The user pauses and the shaping history preserves the exact resume state

A shaping blocker is not successful completion of the enclosing `/goal`.

## Round close and approval gate

At the end of each round, surface:

- Round ID and questions answered
- Contract sections changed
- Remaining uncertainty or deferred decisions
- Recommended disposition

Offer:

```text
Approve the current Goal Contract
Run another deeper shaping round
Pause shaping and preserve the current state
```

Before production edits, surface a compact contract review:

- Outcome
- Scope and exclusions
- Acceptance evidence
- Protected behavior
- Primary profile and overlays
- Authority boundaries
- Budget and stop conditions
- State, shaping-history, and archive paths
- Approval shaping round

Ask for explicit approval unless the user has already approved an authoritative artifact containing the same semantics. After approval, persist the contract and hand off to `goal-engine`.

## Handoff inside a zero-friction `/goal`

When `shape-goal` was activated by a copied `/goal` launcher:

1. Surface the approved target, acceptance evidence, and approval shaping round in the conversation for the native evaluator.
2. State that shaping is complete but the enclosing goal is **not** complete.
3. Invoke or load `goal-engine`.
4. Continue execution against the approved contract.
5. Do not return terminal success until the contract's evidence passes.
