# Frontend UI / UX / Accessibility

**Use when:** A frontend surface must become coherent, usable, responsive, accessible, and visually polished without regressing behavior.

**In simple terms:** Improve the real interface through browser-based user journeys, visual evidence, and accessibility checks.

## Recommended — interactive shaping

`shape-goal` is the main command. Run it **outside an active `/goal`** so you can answer each question normally.

| Host | Command |
|---|---|
| Claude Code | `/shape-goal Use the Frontend UI / UX / Accessibility profile` |
| Codex CLI / IDE | `$shape-goal Use the Frontend UI / UX / Accessibility profile` |

`shape-goal` searches first, asks one material question, saves the answer, and ends the turn. After you approve the Goal Contract, paste the exact `/goal` command it returns.

## Advanced — autonomous preflight

Use this only when an approved contract or authoritative artifact already resolves every owner decision. It must stop and return control instead of asking questions inside the active `/goal`.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next Frontend UI / UX / Accessibility objective. During shaping, load shape-goal's required-input specification for Frontend UI / UX / Accessibility; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible. Continue inside this `/goal` only when an already-approved Goal Contract or authoritative artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to resume `shape-goal` outside `/goal`; do not ask the question or take another autonomous turn, and do not make production changes before approval. Then hand off within this same goal to goal-engine to inventory screens and states, reconcile design references and system patterns, test real interactions across supported viewports, and iterate on verified usability and visual gaps; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

## Inputs the skills resolve

- Target screens, journeys, and user groups
- Design references, brand rules, and design system
- Supported browsers, devices, viewports, themes, and input modes
- Visual, interaction, accessibility, content-state, and performance acceptance evidence
- Common contract inputs: outcome, scope, exclusions, acceptance evidence, protected behavior, authority boundaries, budget, goal relationships, state paths, and closeout paths.

**Suggested assurance overlays:** UX & Accessibility, Performance & Cost, Compatibility & Portability

`shape-goal` must search the repository and connected authoritative sources before asking. It asks only material unresolved decisions, one at a time with a recommendation. The active `/goal` is not complete when the contract is shaped; execution and passing evidence are still required.

## Advanced — self-contained preflight

Use this only when the skills are unavailable and no owner interaction is expected. If a decision is missing, it must save one proposed question and stop instead of looping.

```text
/goal Determine, obtain approval for, and complete this repository's next Frontend UI / UX / Accessibility objective without requiring the user to prefill placeholders. Phase 1 — shape: establish the actual repository state from instructions, Git state/history, requirements, architecture, plans, prior goals, tests/CI, runtime behavior, and available authoritative tools or connected sources. Build an input ledger for the target, scope, exclusions, acceptance evidence, protected behavior, authority boundaries, budget, and the profile-specific inputs described in this goal. Search before asking. Continue inside this `/goal` only when an existing approved artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to reply outside `/goal` and continue shaping from the saved state; do not ask the question or take another autonomous turn. Do not edit production before approval, and do not treat contract creation as completion. Phase 2 — execute: inventory screens and states, reconcile design references and system patterns, test real interactions across supported viewports, and iterate on verified usability and visual gaps. In particular, exercise real browser flows and all important states; use screenshots/visual comparison plus functional checks; verify keyboard, focus, semantics, contrast, responsive behavior, loading/error/empty states. Make small coherent reversible changes; use repository-native checks; verify findings before fixing; add regression protection; review important diffs independently when practical; keep only changes that preserve or improve the verified baseline; and persist progress, failed approaches, evidence, reusable outputs, and the next action. Finish only when every approved acceptance and assurance item passes with surfaced evidence and protected behavior remains intact. Stop for a genuine external blocker, required approval, exhausted approved budget, material goal drift, or two consecutive no-progress cycles. At every terminal outcome, preserve a reusable closeout packet containing SHAPING.md, CONTRACT.md, final PROGRESS.md, and RESULT.md under the repository's goal-history convention, update the portfolio/history, promote durable tests/docs/ADRs/runbooks/fixtures/tooling, and never archive secrets or private data, including personal, customer, or confidential business information, production dumps, exploit-enabling evidence, or unnecessary large logs. Never perform destructive, deployment, release, credential, billing, or external-system actions without explicit approval.
```

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.
