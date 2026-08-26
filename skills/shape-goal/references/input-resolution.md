# Shape Goal: Input Resolution Protocol

Use this protocol whenever the repository-specific target, scope, evidence, or boundaries are not already approved.

Read [shaping-history.md](shaping-history.md) and [question-quality.md](question-quality.md) before asking any user question.

> **Question barrier:** search first, save one question, ask it, and end the turn immediately. The user's next normal reply is the answer.

## The input ledger

Create a concise ledger before asking questions:

| Input | Status | Impact | Confidence | Assumption class | Evidence, decision, or question source |
|---|---|---|---|---|---|
| Outcome | Unresolved / Evidence / Safe default / Owner decision / N/A | High | Unknown | Unresolved | Source or `R1-Q1` |
| Users and journey boundary | ... | ... | ... | ... | ... |
| Scope and exclusions | ... | ... | ... | ... | ... |
| Acceptance evidence | ... | ... | ... | ... | ... |
| Protected behavior | ... | ... | ... | ... | ... |
| Failure and edge cases | ... | ... | ... | ... | ... |
| Data, compatibility, and dependencies | ... | ... | ... | ... | ... |
| Authority boundaries | ... | ... | ... | ... | ... |
| Ownership and reusable outputs | ... | ... | ... | ... | ... |
| Profile-specific inputs | ... | ... | ... | ... | ... |

Do not persist an approved contract while a material row remains unresolved. Link every owner-decision row to its saved question-and-answer ID. Resolve every applicable lens from the universal clarity matrix in [question-quality.md](question-quality.md); `Not applicable` requires a reason.

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

The shaping record is append-only. Corrections create a new decision entry and reference the prior one.

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

Before persisting a verbatim answer, determine repository visibility and whether the answer contains confidential business strategy, customer commitments, unreleased roadmap, commercial terms, or third-party restricted material. Store a redacted normalized decision plus an approved secure reference when repository storage is inappropriate.

## Safe defaults

Use a default without asking only when it is reversible, low-risk, consistent with repository conventions, and does not materially change product scope or authority. Record the default and why it is safe.

Record every assumption as Evidence-backed, Owner-approved, Safe reversible default, or Unresolved. Surface safe defaults before approval; High- and Medium-impact unresolved assumptions block readiness.

Never default:

- Product outcome when several materially different outcomes are plausible
- Removal of compatibility or protected behavior
- Destructive, production, credential, billing, release, legal, or external-system authority
- Acceptance thresholds that determine whether the user considers the work successful
- Risk acceptance, privacy policy, compliance interpretation, or irreversible migration choices

## Ask one material decision at a time

After searchable sources are exhausted:

1. Assign the next stable question ID, such as `R1-Q2`.
2. State the unresolved atomic decision and its impact.
3. Summarize the relevant evidence and conflict.
4. Present no more than three materially different options.
5. Recommend one option, explain the trade-off, and state what changes based on the answer.
6. Save the exact proposed question in `SHAPING.md`.
7. Ask one direct question.
8. **End the turn immediately.** Do not call tools, continue research, ask another question, or begin background work.

When the user replies:

1. Treat the normal reply as the answer; never require a Steer message.
2. Append the exact safe answer to `SHAPING.md` immediately.
3. Classify answer quality as Clear, Clear with conditions, Partial, Ambiguous, Conflicting, or Deferred / Blocked.
4. Record only the faithful normalized decision, contract impact, confidence, assumption class, and any superseded answer.
5. When more than one material interpretation remains, save and ask one targeted clarification; never choose silently.
6. Update the input ledger and contract draft.
7. Continue only after the answer is safely persisted.

Questions should be concrete and easy to answer. Do not ask users to discover file paths, commands, implementation details, or repository facts that the agent can inspect.

For secrets, credentials, private personal data, confidential business/customer information, third-party restricted material, raw production data, or exploit-enabling detail, store a redacted decision summary and approved secure reference instead of the sensitive text.

## Adaptive, standard, deeper, and stress-test rounds

There is no minimum or maximum question count. Use Adaptive depth by default and escalate to Thorough or Exhaustive when impact, uncertainty, irreversibility, subjective judgment, or weak evidence requires it. The first round resolves the material decisions required for readiness—not an arbitrary quota.

When the user is not satisfied or requests another batch of questions, open a deepening round:

1. Read every prior question and answer.
2. Build a gap map for weak assumptions, hidden scope, missing failure cases, and fragile evidence.
3. Select the most valuable unexplored lens.
4. Ask one non-duplicate material question at a time through the question barrier.
5. Close the round with new decisions, contract changes, remaining uncertainty, and a readiness recommendation.

The user may request repeated rounds. Each round must add decision value; repeated questions without new evidence count as no progress. A **stress-test round** challenges the current draft with fresh-reader, counterexample, scenario, verifier, contradiction, traceability, assumption, and plain-English teach-back checks.

## Exhaustive, not circular

“Relentless” means continuing across interactive turns until every material input is resolved, not refusing to return control or repeating searches and questions.

Stop a shaping round when:

- The current contract is ready for approval
- A named external source, credential, lawful-access constraint, or unavailable decision owner blocks resolution
- The user declines or defers a material decision
- The approved shaping budget is exhausted
- The user pauses and the shaping history preserves the exact resume state

## Round close and approval gate

At the end of each round, surface:

- Round ID and questions answered
- Contract sections changed
- Remaining uncertainty or deferred decisions
- Selected shaping depth and recommended disposition
- Assumption register and clarity-stress-test result

Ask one disposition question and end the turn:

```text
Approve the current Goal Contract
Run another deeper shaping round
Pause shaping and preserve the current state
```

Approval is itself a shaping answer. Persist the user's explicit response and the approved contract revision before changing lifecycle state.

Before approval, surface a compact plain-English teach-back of outcome, scope, exclusions, evidence, protected behavior, profile, overlays, authority, budget, stop conditions, state paths, shaping depth, assumptions, clarity-test findings, and approval round.

## Execution handoff after approval

Interactive shaping finishes before native `/goal` execution begins.

1. Persist the approved Goal Contract and approval answer.
2. Render a copy-ready `/goal` command using the actual persisted contract path or authoritative issue/specification.
3. Save that command in the contract's launcher field.
4. Return it to the user.
5. Do not execute it automatically.

If an advanced autonomous preflight reaches an unresolved owner decision, save one proposed question and stop as **Approval required**. Do not ask the question while the active `/goal` continues; tell the user to resume `shape-goal` outside `/goal`.
