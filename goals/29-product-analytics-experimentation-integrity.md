# Product Analytics / Experimentation Integrity

**Use when:** Product events, funnels, metrics, dashboards, or controlled experiments must become trustworthy enough to support decisions without misleading attribution.

**In simple terms:** Define the events and metrics, verify collection end to end, test experiment assignment, and prove the numbers mean what the team thinks they mean.

## Recommended — interactive shaping

`shape-goal` is the main command. Run it **outside an active `/goal`** so you can answer each question normally.

| Host | Command |
|---|---|
| Claude Code | `/shape-goal Use the Product Analytics / Experimentation Integrity profile` |
| Codex CLI / IDE | `$shape-goal Use the Product Analytics / Experimentation Integrity profile` |

`shape-goal` searches first, asks one material question, saves the answer, and ends the turn. After you approve the Goal Contract, paste the exact `/goal` command it returns.

## Advanced — autonomous preflight

Use this only when an approved contract or authoritative artifact already resolves every owner decision. It must stop and return control instead of asking questions inside the active `/goal`.

```text
/goal Use the installed shape-goal and goal-engine skills to complete this repository's next Product Analytics / Experimentation Integrity objective. Inspect metric definitions, event schemas and producers, identity and consent logic, collection and transport, warehouse transformations, dashboards, experiment assignment and exposure, joins, loss and duplication, sample-ratio checks, analysis code, and prior decision records plus repository instructions, Git state, prior goals, and the project harness. Continue inside this `/goal` only when an already-approved Goal Contract or authoritative artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to resume `shape-goal` outside `/goal`; do not ask the question or take another autonomous turn, and do not make production changes before approval. Once approved, use goal-engine to map decisions to versioned metrics and event contracts, instrument or correct the smallest verified gaps, trace representative events end to end, reconcile counts and identities, test experiment assignment and exposure, detect sample-ratio or telemetry-loss problems, validate dashboards and guardrails, and document what conclusions the evidence can and cannot support. Apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when the approved events, metrics, funnels, dashboards, and experiment checks reconcile within defined thresholds; identity, consent, privacy, assignment, exposure, sample-ratio, guardrail, and lineage gates pass; and qualified owners can reproduce the analysis without unsupported causal claims. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

## Inputs the skills resolve

- Decision questions, metric definitions, primary outcomes, guardrails, owners, and acceptable interpretation boundaries
- Event taxonomy, schemas, identity and session rules, consent, privacy, retention, and source-to-report lineage
- Missing, late, duplicate, reordered, or joined-event behavior plus reconciliation and monitoring thresholds
- Experiment unit, randomization, exposure, assignment persistence, sample-ratio checks, analysis window, power or stopping policy, and qualified decision owner

**Suggested assurance overlays:** Data Integrity & Governance, Security & Privacy, Compliance & Auditability, Documentation & Knowledge Transfer

`shape-goal` must search the repository and connected authoritative sources before asking. It asks only material unresolved decisions, one at a time with a recommendation. Execution starts only after explicit contract approval.

## Advanced — self-contained preflight

Use this only when the skills are unavailable and no owner interaction is expected. If a decision is missing, it must save one proposed question and stop instead of looping.

```text
/goal Determine, obtain explicit approval for, and complete this repository's next Product Analytics / Experimentation Integrity objective without requiring the user to prefill placeholders. Phase 1 — shape: inspect metric definitions, event schemas and producers, identity and consent logic, collection and transport, warehouse transformations, dashboards, experiment assignment and exposure, joins, loss and duplication, sample-ratio checks, analysis code, and prior decision records plus repository instructions, Git state/history, prior goals, and available authoritative sources. Search before asking. Continue inside this `/goal` only when an existing approved artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to reply outside `/goal` and continue shaping from the saved state; do not ask the question or take another autonomous turn. Do not edit production before approval. Phase 2 — execute: map decisions to versioned metrics and event contracts, instrument or correct the smallest verified gaps, trace representative events end to end, reconcile counts and identities, test experiment assignment and exposure, detect sample-ratio or telemetry-loss problems, validate dashboards and guardrails, and document what conclusions the evidence can and cannot support. Make small coherent reversible changes; use repository-native checks; verify findings before fixing; add regression protection; review important diffs independently when practical; keep only changes that preserve or improve the verified baseline; and persist evidence, failed approaches, reusable outputs, and the next action. Finish only when the approved events, metrics, funnels, dashboards, and experiment checks reconcile within defined thresholds; identity, consent, privacy, assignment, exposure, sample-ratio, guardrail, and lineage gates pass; and qualified owners can reproduce the analysis without unsupported causal claims. Stop for a genuine blocker, required approval, exhausted approved budget, material goal drift, or two consecutive no-progress cycles. At every terminal outcome, preserve a reusable closeout packet containing SHAPING.md, CONTRACT.md, final PROGRESS.md, and RESULT.md; update the portfolio and history, promote durable tests, documentation, ADRs, runbooks, fixtures, tooling, evaluations, or benchmarks, and never archive secrets or private data, including personal, customer, or confidential business information, production dumps, exploit-enabling evidence, or unnecessary large logs. Never perform destructive, deployment, release, credential, billing, legal, or external-system actions without explicit approval.
```

**Why it works:** Analytics can be technically present yet decision-dangerous. This loop ties every metric to a decision, verifies the full event and experiment path, and blocks conclusions when assignment, telemetry, identity, or interpretation evidence is not trustworthy.
