# Internationalization / Localization Readiness

**Use when:** A product must work correctly across approved languages, regions, scripts, reading directions, time zones, and local formats.

**In simple terms:** Find hard-coded locale assumptions, build a locale matrix, test translated and right-to-left experiences, and prove every supported locale works.

## Recommended — interactive shaping

`shape-goal` is the main command. Run it **outside an active `/goal`** so you can answer each question normally.

| Host | Command |
|---|---|
| Claude Code | `/shape-goal Use the Internationalization / Localization Readiness profile` |
| Codex CLI / IDE | `$shape-goal Use the Internationalization / Localization Readiness profile` |

`shape-goal` searches first, asks one material question, saves the answer, and ends the turn. After you approve the Goal Contract, paste the exact `/goal` command it returns.

## Advanced — autonomous preflight

Use this only when an approved contract or authoritative artifact already resolves every owner decision. It must stop and return control instead of asking questions inside the active `/goal`.

```text
/goal Use the installed shape-goal and goal-engine skills to complete this repository's next Internationalization / Localization Readiness objective. Inspect user-facing strings and content, locale detection and routing, translation resources, formatting and time-zone logic, pluralization, fonts, layouts, right-to-left behavior, accessibility, SEO, tests, screenshots, and translation ownership plus repository instructions, Git state, prior goals, and the project harness. Continue inside this `/goal` only when an already-approved Goal Contract or authoritative artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to resume `shape-goal` outside `/goal`; do not ask the question or take another autonomous turn, and do not make production changes before approval. Once approved, use goal-engine to create a supported locale matrix, remove hard-coded assumptions, centralize messages and local formatting, define fallbacks, run pseudo-localization and text-expansion checks, exercise right-to-left and locale-specific flows, and verify functional, visual, accessibility, and content evidence per locale. Apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved locale passes the defined functional, formatting, fallback, visual, accessibility, routing, and content gates; untranslated or unreviewed material is explicitly accounted for; and qualified human review is recorded wherever linguistic or legal judgment is required. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

## Inputs the skills resolve

- Supported locales, regions, scripts, fallback policy, and rollout order
- Translation source of truth, ownership, review workflow, and content or legal boundaries
- Dates, numbers, currency, units, time zones, pluralization, collation, names, and address rules
- RTL, text expansion, fonts, routing or SEO, accessibility, pseudo-localization, and per-locale UAT evidence

**Suggested assurance overlays:** Internationalization & Localization, UX & Accessibility, Compatibility & Portability, Documentation & Knowledge Transfer

`shape-goal` must search the repository and connected authoritative sources before asking. It asks only material unresolved decisions, one at a time with a recommendation. Execution starts only after explicit contract approval.

## Advanced — self-contained preflight

Use this only when the skills are unavailable and no owner interaction is expected. If a decision is missing, it must save one proposed question and stop instead of looping.

```text
/goal Determine, obtain explicit approval for, and complete this repository's next Internationalization / Localization Readiness objective without requiring the user to prefill placeholders. Phase 1 — shape: inspect user-facing strings and content, locale detection and routing, translation resources, formatting and time-zone logic, pluralization, fonts, layouts, right-to-left behavior, accessibility, SEO, tests, screenshots, and translation ownership plus repository instructions, Git state/history, prior goals, and available authoritative sources. Search before asking. Continue inside this `/goal` only when an existing approved artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to reply outside `/goal` and continue shaping from the saved state; do not ask the question or take another autonomous turn. Do not edit production before approval. Phase 2 — execute: create a supported locale matrix, remove hard-coded assumptions, centralize messages and local formatting, define fallbacks, run pseudo-localization and text-expansion checks, exercise right-to-left and locale-specific flows, and verify functional, visual, accessibility, and content evidence per locale. Make small coherent reversible changes; use repository-native checks; verify findings before fixing; add regression protection; review important diffs independently when practical; keep only changes that preserve or improve the verified baseline; and persist evidence, failed approaches, reusable outputs, and the next action. Finish only when every approved locale passes the defined functional, formatting, fallback, visual, accessibility, routing, and content gates; untranslated or unreviewed material is explicitly accounted for; and qualified human review is recorded wherever linguistic or legal judgment is required. Stop for a genuine blocker, required approval, exhausted approved budget, material goal drift, or two consecutive no-progress cycles. At every terminal outcome, preserve a reusable closeout packet containing SHAPING.md, CONTRACT.md, final PROGRESS.md, and RESULT.md; update the portfolio and history, promote durable tests, documentation, ADRs, runbooks, fixtures, tooling, evaluations, or benchmarks, and never archive secrets or private data, including personal, customer, or confidential business information, production dumps, exploit-enabling evidence, or unnecessary large logs. Never perform destructive, deployment, release, credential, billing, legal, or external-system actions without explicit approval.
```

**Why it works:** Localization quality depends on more than translated strings: the loop verifies data formats, directionality, layout expansion, fallbacks, routing, accessibility, and human language review as one supported-locale contract.
