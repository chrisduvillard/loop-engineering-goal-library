# Codebase Onboarding / Knowledge Recovery

**Use when:** A mature, inherited, or poorly documented codebase must become understandable, runnable, and safe to change before major delivery work begins.

**In simple terms:** Turn an unfamiliar repository into a verified map that a new maintainer or agent can safely use.

## Recommended — interactive shaping

`shape-goal` is the main command. Run it **outside an active `/goal`** so you can answer each question normally.

| Host | Command |
|---|---|
| Claude Code | `/shape-goal Use the Codebase Onboarding / Knowledge Recovery profile` |
| Codex CLI / IDE | `$shape-goal Use the Codebase Onboarding / Knowledge Recovery profile` |

`shape-goal` searches first, asks one material question, saves the answer, and ends the turn. After you approve the Goal Contract, paste the exact `/goal` command it returns.

## Advanced — autonomous preflight

Use this only when an approved contract or authoritative artifact already resolves every owner decision. It must stop and return control instead of asking questions inside the active `/goal`.

```text
/goal Use the installed shape-goal and goal-engine skills to complete this repository's next Codebase Onboarding / Knowledge Recovery objective. Inspect repository instructions, Git history, architecture and ADRs, runtime entry points, critical user and data flows, ownership, setup and reset paths, tests and CI, operational runbooks, prior goals, and the project harness plus repository instructions, Git state, prior goals, and available connected authoritative sources. Continue inside this `/goal` only when an already-approved Goal Contract or authoritative artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to resume `shape-goal` outside `/goal`; do not ask the question or take another autonomous turn, and do not make production changes before approval. Once approved, use goal-engine to map the real architecture and ownership, trace representative user and data flows through code and runtime evidence, verify setup/run/reset/debug/test paths from clean state, reconcile stale or contradictory knowledge, and leave a reviewed Project Harness, architecture map, vocabulary, risk register, and handoff that a fresh maintainer can use without rediscovery. Apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when a fresh maintainer can reproduce the approved setup, critical journeys, verification commands, and architecture decisions from the durable artifacts; every important claim is linked to code or runtime evidence; unresolved uncertainty is explicitly recorded; and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

## Inputs the skills resolve

- Target maintainer or agent audience and the decisions they must be able to make
- Critical product journeys, runtime entry points, architecture boundaries, dependencies, and ownership
- Supported setup, run, reset, debug, and repository-native verification paths
- Required architecture map, Project Harness, vocabulary, risk register, freshness triggers, and maintainer-readiness evidence

**Suggested assurance overlays:** Documentation & Knowledge Transfer, Compatibility & Portability

`shape-goal` must search the repository and connected authoritative sources before asking. It asks only material unresolved decisions, one at a time with a recommendation. Execution starts only after explicit contract approval.

## Advanced — self-contained preflight

Use this only when the skills are unavailable and no owner interaction is expected. If a decision is missing, it must save one proposed question and stop instead of looping.

```text
/goal Determine, obtain explicit approval for, and complete this repository's next Codebase Onboarding / Knowledge Recovery objective without requiring the user to prefill placeholders. Phase 1 — shape: inspect repository instructions, Git history, architecture and ADRs, runtime entry points, critical user and data flows, ownership, setup and reset paths, tests and CI, operational runbooks, prior goals, and the project harness plus repository instructions, Git state/history, prior goals, and available authoritative sources. Search before asking. Continue inside this `/goal` only when an existing approved artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to reply outside `/goal` and continue shaping from the saved state; do not ask the question or take another autonomous turn. Do not edit production before approval. Phase 2 — execute: map the real architecture and ownership, trace representative user and data flows through code and runtime evidence, verify setup/run/reset/debug/test paths from clean state, reconcile stale or contradictory knowledge, and leave a reviewed Project Harness, architecture map, vocabulary, risk register, and handoff that a fresh maintainer can use without rediscovery. Make small coherent reversible changes; use repository-native checks; verify findings before fixing; add regression protection; review important diffs independently when practical; keep only changes that preserve or improve the verified baseline; and persist evidence, failed approaches, reusable outputs, and the next action. Finish only when a fresh maintainer can reproduce the approved setup, critical journeys, verification commands, and architecture decisions from the durable artifacts; every important claim is linked to code or runtime evidence; unresolved uncertainty is explicitly recorded; and protected behavior has not regressed. Stop for a genuine blocker, required approval, exhausted approved budget, material goal drift, or two consecutive no-progress cycles. At every terminal outcome, preserve a reusable closeout packet containing SHAPING.md, CONTRACT.md, final PROGRESS.md, and RESULT.md; update the portfolio and history, promote durable tests, documentation, ADRs, runbooks, fixtures, tooling, evaluations, or benchmarks, and never archive secrets or private data, including personal, customer, or confidential business information, production dumps, exploit-enabling evidence, or unnecessary large logs. Never perform destructive, deployment, release, credential, billing, legal, or external-system actions without explicit approval.
```

**Why it works:** It makes understanding a testable deliverable. Repository claims must be traced to code or runtime evidence, and the result becomes durable project infrastructure instead of another disposable audit note.
