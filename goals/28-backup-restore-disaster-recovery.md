# Backup / Restore / Disaster Recovery

**Use when:** Critical application state must be recoverable within approved recovery objectives, with backups and restore procedures proven by realistic drills.

**In simple terms:** Define what must survive, create trustworthy backups, restore them in a clean environment, and prove recovery meets the agreed targets.

## Recommended — interactive shaping

`shape-goal` is the main command. Run it **outside an active `/goal`** so you can answer each question normally.

| Host | Command |
|---|---|
| Claude Code | `/shape-goal Use the Backup / Restore / Disaster Recovery profile` |
| Codex CLI / IDE | `$shape-goal Use the Backup / Restore / Disaster Recovery profile` |

`shape-goal` searches first, asks one material question, saves the answer, and ends the turn. After you approve the Goal Contract, paste the exact `/goal` command it returns.

## Advanced — autonomous preflight

Use this only when an approved contract or authoritative artifact already resolves every owner decision. It must stop and return control instead of asking questions inside the active `/goal`.

```text
/goal Use the installed shape-goal and goal-engine skills to complete this repository's next Backup / Restore / Disaster Recovery objective. Inspect critical state and dependencies, backup jobs and artifacts, retention and immutability, encryption and key recovery, monitoring, restore scripts, environment definitions, runbooks, incident history, recovery objectives, and prior drill evidence plus repository instructions, Git state, prior goals, and the project harness. Continue inside this `/goal` only when an already-approved Goal Contract or authoritative artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to resume `shape-goal` outside `/goal`; do not ask the question or take another autonomous turn, and do not make production changes before approval. Once approved, use goal-engine to map recovery tiers, verify backup creation and monitoring, restore approved artifacts into an isolated clean environment, reconcile data and application behavior, exercise representative partial and full failure scenarios, measure recovery objectives, and improve automation and runbooks without performing destructive production tests. Apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when approved backups are current, protected, and observable; clean-room restores and required disaster drills succeed; integrity reconciliation passes; measured recovery point and time objectives meet the contract; and runbooks, ownership, residual risks, and production approval boundaries are current. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

## Inputs the skills resolve

- Critical systems, data, configuration, secrets or keys, dependencies, owners, and recovery tiers
- Recovery point and recovery time objectives, retention rules, and acceptable data loss or downtime
- Backup frequency, immutability, encryption, off-site or cross-region design, access, and key recovery
- Clean-room restore environment, integrity reconciliation, failover or failback, drill scope, and production authority

**Suggested assurance overlays:** Reliability & Recovery, Security & Privacy, Operability & Observability, Compliance & Auditability

`shape-goal` must search the repository and connected authoritative sources before asking. It asks only material unresolved decisions, one at a time with a recommendation. Execution starts only after explicit contract approval.

## Advanced — self-contained preflight

Use this only when the skills are unavailable and no owner interaction is expected. If a decision is missing, it must save one proposed question and stop instead of looping.

```text
/goal Determine, obtain explicit approval for, and complete this repository's next Backup / Restore / Disaster Recovery objective without requiring the user to prefill placeholders. Phase 1 — shape: inspect critical state and dependencies, backup jobs and artifacts, retention and immutability, encryption and key recovery, monitoring, restore scripts, environment definitions, runbooks, incident history, recovery objectives, and prior drill evidence plus repository instructions, Git state/history, prior goals, and available authoritative sources. Search before asking. Continue inside this `/goal` only when an existing approved artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to reply outside `/goal` and continue shaping from the saved state; do not ask the question or take another autonomous turn. Do not edit production before approval. Phase 2 — execute: map recovery tiers, verify backup creation and monitoring, restore approved artifacts into an isolated clean environment, reconcile data and application behavior, exercise representative partial and full failure scenarios, measure recovery objectives, and improve automation and runbooks without performing destructive production tests. Make small coherent reversible changes; use repository-native checks; verify findings before fixing; add regression protection; review important diffs independently when practical; keep only changes that preserve or improve the verified baseline; and persist evidence, failed approaches, reusable outputs, and the next action. Finish only when approved backups are current, protected, and observable; clean-room restores and required disaster drills succeed; integrity reconciliation passes; measured recovery point and time objectives meet the contract; and runbooks, ownership, residual risks, and production approval boundaries are current. Stop for a genuine blocker, required approval, exhausted approved budget, material goal drift, or two consecutive no-progress cycles. At every terminal outcome, preserve a reusable closeout packet containing SHAPING.md, CONTRACT.md, final PROGRESS.md, and RESULT.md; update the portfolio and history, promote durable tests, documentation, ADRs, runbooks, fixtures, tooling, evaluations, or benchmarks, and never archive secrets or private data, including personal, customer, or confidential business information, production dumps, exploit-enabling evidence, or unnecessary large logs. Never perform destructive, deployment, release, credential, billing, legal, or external-system actions without explicit approval.
```

**Why it works:** A backup is only useful when it can be restored. This loop makes clean-room recovery, integrity checks, measured RPO/RTO, and operational drills the completion evidence instead of trusting job-success messages.
