# QA / Regression / UAT

**Use when:** The actual product surface and realistic user workflows must pass defined acceptance gates.

```text
/goal Make [PRODUCT OR SCOPE] pass [ACCEPTANCE FLOWS AND GATES]. First discover the real entry points, supported environments, repository-native run and test commands, requirements, and current Git and baseline state. Build a concise risk-based matrix of required user workflows, APIs and data paths, negative and edge cases, and supported configurations. Exercise the actual product from clean realistic state and capture exact failures and evidence. Verify each failure before fixing it; then make the smallest root-cause production fix, add automated regression coverage where practical, rerun the failed scenario, and rerun affected broader gates. Never weaken tests, skip required flows, or declare success from unit tests alone when integration, E2E, or UAT is applicable. Preserve unrelated and uncommitted work and update existing progress or handoff state. Finish only after a clean end-to-end run shows every required item passing with surfaced evidence and no new regressions. Stop for missing credentials, hardware, lawful access, approval, [BUDGET], or two no-progress cycles; leave exact reproduction evidence and the next action. No production or destructive action without explicit approval.
```

**Why it works:** It tests the product rather than merely the implementation units. The clean-state rerun and full workflow matrix prevent one fixed scenario from concealing adjacent regressions.
