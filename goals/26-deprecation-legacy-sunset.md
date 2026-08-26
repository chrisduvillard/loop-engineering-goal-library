# Deprecation / Legacy Sunset

**Use when:** A legacy API, feature, format, service, flag, dependency, or code path must be retired without abandoning active consumers or removing rollback too early.

**In simple terms:** Find who still depends on the old path, provide a safe migration, prove adoption, then remove it in controlled stages.

## Recommended — interactive shaping

`shape-goal` is the main command. Run it **outside an active `/goal`** so you can answer each question normally.

| Host | Command |
|---|---|
| Claude Code | `/shape-goal Use the Deprecation / Legacy Sunset profile` |
| Codex CLI / IDE | `$shape-goal Use the Deprecation / Legacy Sunset profile` |

`shape-goal` searches first, asks one material question, saves the answer, and ends the turn. After you approve the Goal Contract, paste the exact `/goal` command it returns.

## Advanced — autonomous preflight

Use this only when an approved contract or authoritative artifact already resolves every owner decision. It must stop and return control instead of asking questions inside the active `/goal`.

```text
/goal Use the installed shape-goal and goal-engine skills to complete this repository's next Deprecation / Legacy Sunset objective. Inspect the legacy surface and replacement, call sites and consumers, runtime usage and telemetry, compatibility promises, support policy, feature flags, migration tooling, documentation, data retention, and rollback paths plus repository instructions, Git state, prior goals, and the project harness. Continue inside this `/goal` only when an already-approved Goal Contract or authoritative artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to resume `shape-goal` outside `/goal`; do not ask the question or take another autonomous turn, and do not make production changes before approval. Once approved, use goal-engine to inventory consumers, make the replacement production-ready, add migration tooling and visible warnings, measure adoption and errors, migrate dependency-safe slices, and remove the legacy surface only after the approved usage and compatibility thresholds plus explicit breaking-change authority are satisfied. Apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when the replacement is proven, every supported consumer is migrated or explicitly accepted, usage and error thresholds meet the retirement policy, removal and cleanup gates pass, documentation is current, and rollback or recovery evidence remains until the approved sunset is complete. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

## Inputs the skills resolve

- Legacy surface, supported replacement, owners, and authoritative retirement reason
- Known and unknown consumers, usage evidence, compatibility window, and support commitments
- Migration tooling, warnings, documentation, telemetry, and adoption thresholds
- Removal authority, retention or archival needs, rollback path, and final cleanup evidence

**Suggested assurance overlays:** Compatibility & Portability, Documentation & Knowledge Transfer, Operability & Observability

`shape-goal` must search the repository and connected authoritative sources before asking. It asks only material unresolved decisions, one at a time with a recommendation. Execution starts only after explicit contract approval.

## Advanced — self-contained preflight

Use this only when the skills are unavailable and no owner interaction is expected. If a decision is missing, it must save one proposed question and stop instead of looping.

```text
/goal Determine, obtain explicit approval for, and complete this repository's next Deprecation / Legacy Sunset objective without requiring the user to prefill placeholders. Phase 1 — shape: inspect the legacy surface and replacement, call sites and consumers, runtime usage and telemetry, compatibility promises, support policy, feature flags, migration tooling, documentation, data retention, and rollback paths plus repository instructions, Git state/history, prior goals, and available authoritative sources. Search before asking. Continue inside this `/goal` only when an existing approved artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to reply outside `/goal` and continue shaping from the saved state; do not ask the question or take another autonomous turn. Do not edit production before approval. Phase 2 — execute: inventory consumers, make the replacement production-ready, add migration tooling and visible warnings, measure adoption and errors, migrate dependency-safe slices, and remove the legacy surface only after the approved usage and compatibility thresholds plus explicit breaking-change authority are satisfied. Make small coherent reversible changes; use repository-native checks; verify findings before fixing; add regression protection; review important diffs independently when practical; keep only changes that preserve or improve the verified baseline; and persist evidence, failed approaches, reusable outputs, and the next action. Finish only when the replacement is proven, every supported consumer is migrated or explicitly accepted, usage and error thresholds meet the retirement policy, removal and cleanup gates pass, documentation is current, and rollback or recovery evidence remains until the approved sunset is complete. Stop for a genuine blocker, required approval, exhausted approved budget, material goal drift, or two consecutive no-progress cycles. At every terminal outcome, preserve a reusable closeout packet containing SHAPING.md, CONTRACT.md, final PROGRESS.md, and RESULT.md; update the portfolio and history, promote durable tests, documentation, ADRs, runbooks, fixtures, tooling, evaluations, or benchmarks, and never archive secrets or private data, including personal, customer, or confidential business information, production dumps, exploit-enabling evidence, or unnecessary large logs. Never perform destructive, deployment, release, credential, billing, legal, or external-system actions without explicit approval.
```

**Why it works:** Retiring a legacy path is not a normal refactor: success depends on consumer discovery, migration adoption, staged warnings, compatibility windows, and evidence-backed removal rather than merely deleting old code.
