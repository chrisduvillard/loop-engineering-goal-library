# Shape Goal: Input Resolution Protocol

Use this protocol whenever a launcher is copied unchanged and the repository-specific target, scope, evidence, or boundaries are not already approved.

## The input ledger

Create a concise ledger before asking questions:

| Input | Status | Evidence or decision |
|---|---|---|
| Outcome | Unresolved / Evidence / Safe default / Owner decision | [SOURCE] |
| Scope and exclusions | ... | ... |
| Acceptance evidence | ... | ... |
| Protected behavior | ... | ... |
| Authority boundaries | ... | ... |
| Profile-specific inputs | ... | ... |

Do not persist an approved contract while any material row is unresolved.

## Search before asking

Search in this order, using every lawful source available to the host:

1. Repository and agent instructions
2. Current Git status, diff, branches/worktrees, and relevant history
3. Active Goal Contract, portfolio, progress, handoffs, and prior closeout archives
4. Approved PRDs, specifications, issues, milestones, ADRs, architecture, and domain vocabulary
5. Native scripts, CI, tests, fixtures, benchmarks, release gates, and package/task configuration
6. Runtime entry points, real product behavior, logs, screenshots, generated artifacts, and supported environments
7. Connected authoritative issue trackers, documentation systems, design files, incident systems, or data catalogs when available and permitted
8. Official external documentation when a changing dependency, platform, standard, or regulation is materially relevant

Triangulate important claims. A stale plan, a checkbox, code presence, or one reviewer opinion is not sufficient evidence by itself.

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

1. State the unresolved decision.
2. Summarize the evidence and conflict.
3. Present no more than three materially different options.
4. Recommend one option and explain the trade-off.
5. Ask one direct question.
6. Record the answer in the ledger and contract.
7. Do not ask the same question again unless new evidence materially changes it.

Questions should be concrete and easy to answer. Do not ask users to discover file paths, commands, implementation details, or repository facts that the agent can inspect.

## Exhaustive, not circular

“Relentless” means continuing until every material input is resolved, not repeating searches or questions.

Stop shaping only when:

- The contract is ready and explicitly approved
- A named external source, credential, lawful-access constraint, or unavailable decision owner blocks resolution
- The user declines to decide a material ambiguity
- The approved shaping budget is exhausted

A shaping blocker is not successful completion of the enclosing `/goal`.

## Approval gate

Before production edits, surface a compact contract review:

- Outcome
- Scope and exclusions
- Acceptance evidence
- Protected behavior
- Primary profile and overlays
- Authority boundaries
- Budget and stop conditions
- State and archive paths

Ask for explicit approval unless the user has already approved an authoritative artifact containing the same semantics. After approval, persist the contract and hand off to `goal-engine`.

## Handoff inside a zero-friction `/goal`

When `shape-goal` was activated by a copied `/goal` launcher:

1. Surface the approved target and acceptance evidence in the conversation for the native evaluator.
2. State that shaping is complete but the enclosing goal is **not** complete.
3. Invoke or load `goal-engine`.
4. Continue execution against the approved contract.
5. Do not return a terminal success outcome until the contract's evidence passes.
