# QA / Regression / UAT

**Use when:** The actual product surface and realistic user workflows must pass defined acceptance gates.

## Recommended: skill-backed

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the QA / Regression / UAT profile. Exercise the real product from clean realistic state, verify failures before fixing them, and continue until every required flow and broader gate passes with surfaced evidence and no new regressions. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve a reusable closeout packet and leave exact restart evidence.
```

## Standalone fallback

```text
/goal Make [PRODUCT OR SCOPE] pass [ACCEPTANCE FLOWS AND GATES]. First discover the real entry points, supported environments, repository-native run and test commands, requirements, prior goal archives, and current Git and baseline state. Build a concise risk-based matrix of required user workflows, APIs and data paths, negative and edge cases, and supported configurations. Exercise the actual product from clean realistic state and capture exact failures and evidence. Verify each failure before fixing it; then make the smallest root-cause production fix, add automated regression coverage where practical, rerun the failed scenario, and rerun affected broader gates. Never weaken tests, skip required flows, or declare success from unit tests alone when integration, E2E, or UAT applies. Preserve unrelated and uncommitted work and update existing progress or handoff state. Finish only after a clean end-to-end run shows every required item passing with surfaced evidence and no new regressions. Stop for missing credentials, hardware, lawful access, approval, [BUDGET], or two no-progress cycles. At any terminal outcome, preserve a reusable closeout packet under the repository's goal-history convention (default `docs/goals/<goal-id>/`) containing `CONTRACT.md`, final `PROGRESS.md`, and `RESULT.md`; update the history index, promote verified reusable tests/docs/ADRs/runbooks/fixtures/tooling, and exclude secrets, private data, raw production dumps, and unnecessarily large logs. No production or destructive action without explicit approval.
```

**Why it works:** It tests actual product behavior, closes the failure-to-regression loop, and saves the acceptance matrix and reusable scenarios for future runs.
