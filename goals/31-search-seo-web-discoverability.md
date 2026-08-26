# Search / SEO / Web Discoverability

**Use when:** A public website or web application must improve its technical search readiness, rendered metadata, structured data, crawl paths, internal links, and discoverable content quality.

**In simple terms:** Make public web content crawlable, understandable, fast, and internally connected without promising rankings.

## Recommended — interactive shaping

`shape-goal` is the main command. Run it **outside an active `/goal`** so you can answer each question normally.

| Host | Command |
|---|---|
| Claude Code | `/shape-goal Use the Search / SEO / Web Discoverability profile` |
| Codex CLI / IDE | `$shape-goal Use the Search / SEO / Web Discoverability profile` |

`shape-goal` searches first, asks one material question, saves the answer, and ends the turn. After you approve the Goal Contract, paste the exact `/goal` command it returns.

## Advanced — autonomous preflight

Use this only when an approved contract or authoritative artifact already resolves every owner decision. It must stop and return control instead of asking questions inside the active `/goal`.

```text
/goal Use the installed shape-goal and goal-engine skills to complete this repository's next Search / SEO / Web Discoverability objective. Inspect repository instructions, Git state and history, public routes and rendered pages, audience and search intent, canonical URLs, robots and sitemap rules, metadata, structured data, internal links, redirects and status codes, localization signals, performance, accessibility, analytics, prior audits, and available connected authoritative search sources. Continue inside this `/goal` only when an already-approved Goal Contract or authoritative artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to resume `shape-goal` outside `/goal`; do not ask the question or take another autonomous turn, and do not make production changes before approval. Once approved, use goal-engine to inventory the public surface and search intent, crawl representative routes, verify rendered HTML and status behavior, correct canonical, robots, sitemap, metadata, structured-data, internal-link, redirect, locale, performance, accessibility, and content-discoverability defects, and rerun the same crawler and page-quality gates across the approved route matrix. Apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved public route is reachable and returns the intended status; canonical, robots, sitemap, metadata, structured-data, locale, internal-link, performance, accessibility, and content gates pass; broken or misleading discovery paths are resolved; and the result is stated as technical readiness rather than an unsupported ranking guarantee. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

## Inputs the skills resolve

- Target audiences, search intent, public routes, content types, and supported environments
- Canonical URL, redirect, robots, sitemap, pagination, duplicate-content, and crawl-budget rules
- Rendered titles, descriptions, social metadata, structured data, headings, internal links, and content-quality rubric
- Locale or hreflang matrix, performance and accessibility budgets, crawler or validation tools, and ranking-claim boundaries

**Suggested assurance overlays:** Search & Discoverability, Performance & Cost, UX & Accessibility, Internationalization & Localization

`shape-goal` must search the repository and connected authoritative sources before asking. It asks only material unresolved decisions, one at a time with a recommendation. Execution starts only after explicit contract approval.

## Advanced — self-contained preflight

Use this only when the skills are unavailable and no owner interaction is expected. If a decision is missing, it must save one proposed question and stop instead of looping.

```text
/goal Determine, obtain explicit approval for, and complete this repository's next Search / SEO / Web Discoverability objective without requiring the user to prefill placeholders. Phase 1 — shape: inspect repository instructions, Git state/history, public routes and rendered pages, audience and search intent, canonical URLs, robots and sitemap rules, metadata, structured data, internal links, redirects and status codes, localization signals, performance, accessibility, analytics, prior audits, and available authoritative search sources. Search before asking. Continue inside this `/goal` only when an existing approved artifact resolves every owner decision. Otherwise create or resume `SHAPING.md`, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to reply outside `/goal` and continue shaping from the saved state; do not ask the question or take another autonomous turn. Do not edit production before approval. Phase 2 — execute: inventory the public surface and search intent, crawl representative routes, verify rendered HTML and status behavior, correct canonical, robots, sitemap, metadata, structured-data, internal-link, redirect, locale, performance, accessibility, and content-discoverability defects, and rerun the same crawler and page-quality gates across the approved route matrix. Make small coherent reversible changes; use repository-native checks; verify findings before fixing; add regression protection; review important diffs independently when practical; keep only changes that preserve or improve the verified baseline; and persist evidence, failed approaches, reusable outputs, and the next action. Finish only when every approved public route is reachable and returns the intended status; canonical, robots, sitemap, metadata, structured-data, locale, internal-link, performance, accessibility, and content gates pass; broken or misleading discovery paths are resolved; and the result is stated as technical readiness rather than an unsupported ranking guarantee. Stop for a genuine blocker, required approval, exhausted approved budget, material goal drift, or two consecutive no-progress cycles. At every terminal outcome, preserve a reusable closeout packet containing SHAPING.md, CONTRACT.md, final PROGRESS.md, and RESULT.md; update the portfolio and history, promote durable tests, documentation, ADRs, runbooks, fixtures, tooling, evaluations, or benchmarks, and never archive secrets or private data, including personal, customer, or confidential business information, production dumps, exploit-enabling evidence, or unnecessary large logs. Never perform destructive, deployment, release, credential, billing, legal, or external-system actions without explicit approval.
```

**Why it works:** It uses a repeatable crawl-and-render evidence loop, fixes the full discovery path rather than isolated tags, and explicitly separates technical readiness from search-ranking promises that the repository cannot prove.
