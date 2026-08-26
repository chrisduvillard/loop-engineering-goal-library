# Test Suite / CI Health

**Use when:** Automated tests and CI must become trustworthy, deterministic, appropriately fast, and consistent with local development.

**In simple terms:** Find flaky, misleading, slow, skipped, or environment-dependent checks and turn the test pipeline into reliable evidence.

## Recommended — interactive shaping

`shape-goal` is the main command. Run it **outside an active `/goal`** so you can answer each question normally.

| Host | Command |
|---|---|
| Claude Code | `/shape-goal Use the Test Suite / CI Health profile` |
| Codex CLI / IDE | `$shape-goal Use the Test Suite / CI Health profile` |

`shape-goal` searches first, asks one material question, saves the answer, and ends the turn. After you approve the Goal Contract, paste the exact `/goal` command it returns.

## Advanced — autonomous preflight

Use this only when an approved contract or authoritative artifact already resolves every owner decision. It must stop and return control instead of asking questions inside the active `/goal`.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next Test Suite / CI Health objective. During shaping, load shape-goal's required-input specification for Test Suite / CI Health; exhaustively inspect repository instructions, Git state and history, test configuration, CI workflows, scripts, fixtures, reports, prior failures, supported environments, prior goal state, the project harness, and connected authoritative sources before asking the user. Resolve every material input from evidence where possible. Continue inside this `/goal` only when an already-approved Goal Contract or authoritative artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to resume `shape-goal` outside `/goal`; do not ask the question or take another autonomous turn, and do not make production changes before approval. Then hand off within this same goal to goal-engine to map the test and CI topology, reproduce flakes and false confidence, correct root causes, improve determinism, isolation, selection, diagnostics, runtime, and local/CI parity, and rerun representative and full gates; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes repeatedly under the defined environments, hidden skips and unexplained failures are resolved, and protected product behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

## Inputs the skills resolve

- Test and CI topology, ownership, supported environments, and required gates
- Current flake rate, failure classes, skipped/quarantined coverage, runtime, and feedback targets
- Reproduction protocol, representative workloads, fixtures, caches, services, and isolation boundaries
- Local/CI parity, retry policy, parallelism, diagnostics, coverage expectations, and completion evidence
- Common contract inputs: outcome, scope, exclusions, acceptance evidence, protected behavior, authority boundaries, budget, goal relationships, state paths, and closeout paths

**Suggested assurance overlays:** Reliability & Recovery, Documentation & Knowledge Transfer, Performance & Cost

`shape-goal` must search the repository and connected authoritative sources before asking. It asks only material unresolved decisions, one at a time with a recommendation. The active `/goal` is not complete when the contract is shaped; execution and passing evidence are still required.

## Advanced — self-contained preflight

Use this only when the skills are unavailable and no owner interaction is expected. If a decision is missing, it must save one proposed question and stop instead of looping.

```text
/goal Determine, obtain approval for, and complete this repository's next Test Suite / CI Health objective without requiring the user to prefill placeholders. Phase 1 — shape: establish the actual repository state from instructions, Git state/history, test configuration, CI workflows, scripts, fixtures, reports, supported environments, prior goals, runtime evidence, and available authoritative tools or connected sources. Build an input ledger for the target, scope, exclusions, acceptance evidence, protected behavior, authority boundaries, budget, and the profile-specific inputs described in this goal. Search before asking. Continue inside this `/goal` only when an existing approved artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to reply outside `/goal` and continue shaping from the saved state; do not ask the question or take another autonomous turn. Do not edit production before approval, and do not treat contract creation as completion. Phase 2 — execute: map the test and CI topology; reproduce flakes, false confidence, hidden skips, environment drift, poor isolation, and slow feedback; fix verified root causes; improve deterministic fixtures, diagnostics, selection, parallelism, caching, retries, and local/CI parity without weakening required gates; rerun focused checks repeatedly and then full clean-state CI-equivalent gates. Make small coherent reversible changes; use repository-native checks; add regression protection; review important diffs independently when practical; keep only changes that preserve or improve the verified baseline; and persist evidence, failed approaches, reusable outputs, and the next action. Finish only when every approved acceptance and assurance item passes repeatedly and protected product behavior remains intact. Stop for a genuine external blocker, required approval, exhausted approved budget, material goal drift, or two consecutive no-progress cycles. At every terminal outcome, preserve a reusable closeout packet containing SHAPING.md, CONTRACT.md, final PROGRESS.md, and RESULT.md under the repository's goal-history convention, update the portfolio/history, promote durable tests/docs/ADRs/runbooks/fixtures/tooling, and never archive secrets, private personal or confidential business data, production dumps, exploit-enabling evidence, or unnecessary large logs. Never perform destructive, deployment, release, credential, billing, or external-system actions without explicit approval.
```

**Why it works:** It treats the test system itself as a product with measurable trust, determinism, and feedback requirements, while preventing the easy but dangerous shortcut of weakening checks merely to make CI green.
