# QA / Regression / UAT

**Use when:** The actual product surface and realistic user workflows must pass defined acceptance gates.

**In simple terms:** Exercise the real product until required workflows and regression gates pass.

## Recommended — interactive shaping

`shape-goal` is the main command. Run it **outside an active `/goal`** so you can answer each question normally.

| Host | Command |
|---|---|
| Claude Code | `/shape-goal Use the QA / Regression / UAT profile` |
| Codex CLI / IDE | `$shape-goal Use the QA / Regression / UAT profile` |

`shape-goal` searches first, asks one material question, saves the answer, and ends the turn. After you approve the Goal Contract, paste the exact `/goal` command it returns.

## Advanced — autonomous preflight

Use this only when an approved contract or authoritative artifact already resolves every owner decision. It must stop and return control instead of asking questions inside the active `/goal`.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next QA / Regression / UAT objective. During shaping, load shape-goal's required-input specification for QA / Regression / UAT; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible. Continue inside this `/goal` only when an already-approved Goal Contract or authoritative artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to resume `shape-goal` outside `/goal`; do not ask the question or take another autonomous turn, and do not make production changes before approval. Then hand off within this same goal to goal-engine to discover the real product surface, build a risk-based flow matrix, reproduce failures, fix root causes, and rerun clean end-to-end evidence; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

## Inputs the skills resolve

- Supported environments and product entry points
- Required user/API/data flows
- Test data, credentials, and lawful access
- Clean-state acceptance and broader gates
- Common contract inputs: outcome, scope, exclusions, acceptance evidence, protected behavior, authority boundaries, budget, goal relationships, state paths, and closeout paths.

**Suggested assurance overlays:** UX & Accessibility

`shape-goal` must search the repository and connected authoritative sources before asking. It asks only material unresolved decisions, one at a time with a recommendation. The active `/goal` is not complete when the contract is shaped; execution and passing evidence are still required.

## Advanced — self-contained preflight

Use this only when the skills are unavailable and no owner interaction is expected. If a decision is missing, it must save one proposed question and stop instead of looping.

```text
/goal Determine, obtain approval for, and complete this repository's next QA / Regression / UAT objective without requiring the user to prefill placeholders. Phase 1 — shape: establish the actual repository state from instructions, Git state/history, requirements, architecture, plans, prior goals, tests/CI, runtime behavior, and available authoritative tools or connected sources. Build an input ledger for the target, scope, exclusions, acceptance evidence, protected behavior, authority boundaries, budget, and the profile-specific inputs described in this goal. Search before asking. Continue inside this `/goal` only when an existing approved artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to reply outside `/goal` and continue shaping from the saved state; do not ask the question or take another autonomous turn. Do not edit production before approval, and do not treat contract creation as completion. Phase 2 — execute: discover the real product surface, build a risk-based flow matrix, reproduce failures, fix root causes, and rerun clean end-to-end evidence. In particular, test realistic workflows, not only units; verify failures before fixing; rerun exact failures and affected broader gates. Make small coherent reversible changes; use repository-native checks; verify findings before fixing; add regression protection; review important diffs independently when practical; keep only changes that preserve or improve the verified baseline; and persist progress, failed approaches, evidence, reusable outputs, and the next action. Finish only when every approved acceptance and assurance item passes with surfaced evidence and protected behavior remains intact. Stop for a genuine external blocker, required approval, exhausted approved budget, material goal drift, or two consecutive no-progress cycles. At every terminal outcome, preserve a reusable closeout packet containing SHAPING.md, CONTRACT.md, final PROGRESS.md, and RESULT.md under the repository's goal-history convention, update the portfolio/history, promote durable tests/docs/ADRs/runbooks/fixtures/tooling, and never archive secrets or private data, including personal, customer, or confidential business information, production dumps, exploit-enabling evidence, or unnecessary large logs. Never perform destructive, deployment, release, credential, billing, or external-system actions without explicit approval.
```

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.
