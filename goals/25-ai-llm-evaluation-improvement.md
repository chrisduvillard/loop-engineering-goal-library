# AI / LLM Evaluation & Improvement

**Use when:** An AI, agent, retrieval, ranking, or LLM-powered feature must improve under representative evaluations while controlling quality, safety, latency, and cost.

**In simple terms:** Build a trustworthy eval set, classify failures, test one change at a time, and keep only improvements that survive repeated runs.

## Recommended — interactive shaping

`shape-goal` is the main command. Run it **outside an active `/goal`** so you can answer each question normally.

| Host | Command |
|---|---|
| Claude Code | `/shape-goal Use the AI / LLM Evaluation & Improvement profile` |
| Codex CLI / IDE | `$shape-goal Use the AI / LLM Evaluation & Improvement profile` |

`shape-goal` searches first, asks one material question, saves the answer, and ends the turn. After you approve the Goal Contract, paste the exact `/goal` command it returns.

## Advanced — autonomous preflight

Use this only when an approved contract or authoritative artifact already resolves every owner decision. It must stop and return control instead of asking questions inside the active `/goal`.

```text
/goal Use the installed shape-goal and goal-engine skills to complete this repository's next AI / LLM Evaluation & Improvement objective. Inspect prompts, model and provider settings, tool and agent workflows, retrieval sources, eval datasets, graders, safety checks, traces, costs, latency, and prior experiment evidence plus repository instructions, Git state, prior goals, and the project harness. Continue inside this `/goal` only when an already-approved Goal Contract or authoritative artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to resume `shape-goal` outside `/goal`; do not ask the question or take another autonomous turn, and do not make production changes before approval. Once approved, use goal-engine to freeze a versioned evaluation protocol, capture a baseline and error taxonomy, test one prompt/model/retrieval/tool/workflow hypothesis at a time, repeat stochastic trials, compare quality plus guardrail floors, and keep only reproducible improvements with regression cases. Apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when the approved evaluation targets and all safety, grounding, latency, cost, and reliability floors pass on the fixed representative set, no test leakage or unexplained regression remains, and the winning configuration and evidence are versioned. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

## Inputs the skills resolve

- Target users, tasks, failure modes, and supported model/provider/tooling surfaces
- Versioned evaluation set, provenance, privacy, representative splits, and leakage or contamination controls
- Graders, rubrics, human-review boundaries, stochastic repetition, and calibration rules
- Baseline and target metrics plus grounding, safety, latency, cost, and reliability floors

**Suggested assurance overlays:** AI Quality & Safety, Security & Privacy, Performance & Cost, Data Integrity & Governance

`shape-goal` must search the repository and connected authoritative sources before asking. It asks only material unresolved decisions, one at a time with a recommendation. Execution starts only after explicit contract approval.

## Advanced — self-contained preflight

Use this only when the skills are unavailable and no owner interaction is expected. If a decision is missing, it must save one proposed question and stop instead of looping.

```text
/goal Determine, obtain explicit approval for, and complete this repository's next AI / LLM Evaluation & Improvement objective without requiring the user to prefill placeholders. Phase 1 — shape: inspect prompts, model and provider settings, tool and agent workflows, retrieval sources, eval datasets, graders, safety checks, traces, costs, latency, and prior experiment evidence plus repository instructions, Git state/history, prior goals, and available authoritative sources. Search before asking. Continue inside this `/goal` only when an existing approved artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to reply outside `/goal` and continue shaping from the saved state; do not ask the question or take another autonomous turn. Do not edit production before approval. Phase 2 — execute: freeze a versioned evaluation protocol, capture a baseline and error taxonomy, test one prompt/model/retrieval/tool/workflow hypothesis at a time, repeat stochastic trials, compare quality plus guardrail floors, and keep only reproducible improvements with regression cases. Make small coherent reversible changes; use repository-native checks; verify findings before fixing; add regression protection; review important diffs independently when practical; keep only changes that preserve or improve the verified baseline; and persist evidence, failed approaches, reusable outputs, and the next action. Finish only when the approved evaluation targets and all safety, grounding, latency, cost, and reliability floors pass on the fixed representative set, no test leakage or unexplained regression remains, and the winning configuration and evidence are versioned. Stop for a genuine blocker, required approval, exhausted approved budget, material goal drift, or two consecutive no-progress cycles. At every terminal outcome, preserve a reusable closeout packet containing SHAPING.md, CONTRACT.md, final PROGRESS.md, and RESULT.md; update the portfolio and history, promote durable tests, documentation, ADRs, runbooks, fixtures, tooling, evaluations, or benchmarks, and never archive secrets or private data, including personal, customer, or confidential business information, production dumps, exploit-enabling evidence, or unnecessary large logs. Never perform destructive, deployment, release, credential, billing, legal, or external-system actions without explicit approval.
```

**Why it works:** It treats nondeterministic AI behavior as an evaluation problem rather than a demo, so prompt, model, retrieval, and workflow changes are kept only when representative repeated evidence improves without breaking safety or operating constraints.
