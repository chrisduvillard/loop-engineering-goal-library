# Infrastructure / Deployment Readiness

**Use when:** Infrastructure, environment configuration, deployment automation, smoke checks, and rollback must be proven ready without silently changing production.

**In simple terms:** Verify that the system can be provisioned and deployed consistently, diagnosed after rollout, and safely rolled back before a human authorizes production change.

## Recommended — interactive shaping

`shape-goal` is the main command. Run it **outside an active `/goal`** so you can answer each question normally.

| Host | Command |
|---|---|
| Claude Code | `/shape-goal Use the Infrastructure / Deployment Readiness profile` |
| Codex CLI / IDE | `$shape-goal Use the Infrastructure / Deployment Readiness profile` |

`shape-goal` searches first, asks one material question, saves the answer, and ends the turn. After you approve the Goal Contract, paste the exact `/goal` command it returns.

## Advanced — autonomous preflight

Use this only when an approved contract or authoritative artifact already resolves every owner decision. It must stop and return control instead of asking questions inside the active `/goal`.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next Infrastructure / Deployment Readiness objective. During shaping, load shape-goal's required-input specification for Infrastructure / Deployment Readiness; exhaustively inspect repository instructions, Git state and history, infrastructure-as-code, environment and secret references, build artifacts, deployment workflows, health checks, runbooks, rollback paths, supported environments, prior incidents and goals, the project harness, and connected authoritative systems before asking the user. Resolve every material input from evidence where possible. Continue inside this `/goal` only when an already-approved Goal Contract or authoritative artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to resume `shape-goal` outside `/goal`; do not ask the question or take another autonomous turn, and do not make production changes before approval. Then hand off within this same goal to goal-engine to reconcile infrastructure and application assumptions, validate provisioning and configuration in approved non-production or simulated environments, verify artifact provenance, migrations, smoke and health gates, observability, failure handling, and rollback, and remove verified readiness blockers; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved readiness gate passes with surfaced evidence, environment differences and residual risks are documented, rollback remains viable, and no production deployment or mutation has occurred without explicit authority. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

## Inputs the skills resolve

- Target environments, infrastructure scope, ownership, dependencies, and environment-parity expectations
- Infrastructure-as-code, configuration, secret-reference, artifact, migration, and deployment-pipeline sources of truth
- Provisioning validation, smoke and health checks, observability, failure scenarios, and rollback evidence
- Production authority boundaries, maintenance windows, change approvals, residual-risk policy, and readiness criteria
- Common contract inputs: outcome, scope, exclusions, acceptance evidence, protected behavior, authority boundaries, budget, goal relationships, state paths, and closeout paths

**Suggested assurance overlays:** Reliability & Recovery, Operability & Observability, Security & Privacy, Compatibility & Portability

`shape-goal` must search the repository and connected authoritative sources before asking. It asks only material unresolved decisions, one at a time with a recommendation. The active `/goal` is not complete when the contract is shaped; execution and passing evidence are still required.

## Advanced — self-contained preflight

Use this only when the skills are unavailable and no owner interaction is expected. If a decision is missing, it must save one proposed question and stop instead of looping.

```text
/goal Determine, obtain approval for, and complete this repository's next Infrastructure / Deployment Readiness objective without requiring the user to prefill placeholders. Phase 1 — shape: establish the actual repository state from instructions, Git state/history, infrastructure-as-code, environment configuration and secret references, artifacts, deployment workflows, health checks, runbooks, rollback paths, supported environments, prior incidents and goals, and available authoritative tools or connected systems. Build an input ledger for the target, scope, exclusions, acceptance evidence, protected behavior, authority boundaries, budget, and the profile-specific inputs described in this goal. Search before asking. Continue inside this `/goal` only when an existing approved artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to reply outside `/goal` and continue shaping from the saved state; do not ask the question or take another autonomous turn. Do not edit production before approval, and do not treat contract creation as completion. Phase 2 — execute: reconcile infrastructure and application assumptions; validate provisioning, configuration, artifacts, migrations, deployment stages, smoke and health gates, observability, failure handling, and rollback in approved non-production, ephemeral, dry-run, or simulated environments; fix verified readiness blockers without broadening production authority. Make small coherent reversible changes; use repository-native checks; add regression protection; review high-blast-radius changes independently; keep only changes that preserve or improve the verified baseline; and persist evidence, failed approaches, reusable outputs, and the next action. Finish only when every approved acceptance and assurance item passes, environment differences and residual risks are explicit, rollback is viable, and protected behavior remains intact. Stop for a genuine external blocker, required approval, exhausted approved budget, material goal drift, or two consecutive no-progress cycles. At every terminal outcome, preserve a reusable closeout packet containing SHAPING.md, CONTRACT.md, final PROGRESS.md, and RESULT.md under the repository's goal-history convention, update the portfolio/history, promote durable tests/docs/ADRs/runbooks/fixtures/tooling, and never archive secrets, private personal or confidential business data, production dumps, exploit-enabling evidence, or unnecessary large logs. Never perform production provisioning, deployment, mutation, credential rotation, billing changes, publishing, release, or destructive infrastructure actions without explicit approval.
```

**Why it works:** It separates proving deployment readiness from exercising production authority, and it evaluates infrastructure, application artifacts, operations, and rollback as one coherent delivery surface.
