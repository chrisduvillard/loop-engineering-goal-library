# Specialist Codebase Audit

Broad audits use **six independent review tracks** so one general reviewer does not become the only source of truth.

| Track | Primary concern |
|---|---|
| Contract & State-Machine | lifecycle, approval, revisions, portfolios, leases, locks, and closeout |
| Agent-Control & Interaction | question barriers, prompt injection, evaluator evidence, drift, and authority |
| Security & Supply Chain | workflows, dependencies, archives, paths, symlinks, permissions, and publishing |
| Tooling & Portability | Python versions, operating systems, filesystems, encodings, and deterministic output |
| Verification & Mutation | false-green tests, missing oracles, failure injection, generated files, and CI gates |
| Documentation & Adoption | installation, updates, terminology, examples, generated docs, and contributor friction |

Reviewers start from the same approved contract and repository state, but not from each other's conclusions. Reviews are read-only by default. **Findings remain hypotheses until reproduced** or independently supported; the lead consolidates them by root cause, adds regression protection, and asks a fresh reviewer to independently re-check important fixes.

## Deterministic validators

The repository separates prose review from machine-checkable contracts:

```text
validate_question_state.py   question sequence, status, and answer transitions
validate_goal_archives.py    closed-goal packets and history-index consistency
validate_tooling_contract.py locked dependencies, Dependabot, and CI controls
validate_repository.py       aggregate repository contract
```

The reusable protocol lives in [`skills/goal-engine/references/specialist-reviewers.md`](../skills/goal-engine/references/specialist-reviewers.md). The 2026-08-27 audit reports are preserved under [`docs/audits/2026-08-27-specialist-review/`](audits/2026-08-27-specialist-review/).

No finite review proves the absence of every future defect. The enforceable promise is narrower: confirmed findings require evidence, important fixes require regression checks and independent re-review, and unresolved risk is recorded instead of hidden.
