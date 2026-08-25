# PRD / Spec Compliance

**Use when:** A product, feature, or repository must be brought into full alignment with documented requirements.

## Recommended: skill-backed

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the PRD / Spec Compliance profile. Continue until every in-scope requirement is Pass with surfaced evidence and the final gates succeed without protected-behavior regressions. Stop only for a contract-defined product decision, blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve a reusable closeout packet and leave a restartable handoff.
```

## Standalone fallback

```text
/goal Make [SCOPE] fully comply with [SPEC/PRD]. First reconcile the authoritative current requirements with actual code, runtime behavior, tests, documentation, CI, prior goal archives, and Git history; maintain a concise requirement-to-evidence map and escalate only contradictions that require a product decision. In dependency and priority order, take each verified gap: reproduce or prove it, implement the smallest production fix, add or update acceptance and regression coverage, run repository-native targeted checks, then rerun affected broader gates. Preserve unrelated behavior and work; never mark a requirement complete from code inspection or an agent assertion alone, and never weaken a requirement or verifier to make it pass. Use an independent review for high-risk or ambiguous changes and verify its findings before fixing them. Update existing plan, progress, or handoff state. Finish only when every in-scope requirement is Pass with surfaced evidence and [FINAL GATES] pass. Stop as Blocked for a named external dependency or required owner decision, or stop at [BUDGET] or after two no-progress cycles. At any terminal outcome, preserve a reusable closeout packet under the repository's goal-history convention (default `docs/goals/<goal-id>/`) containing `CONTRACT.md`, final `PROGRESS.md`, and `RESULT.md`; update the history index, promote verified reusable tests/docs/ADRs/runbooks/fixtures/tooling, and exclude secrets, private data, raw production dumps, and unnecessarily large logs. No irreversible or external-system action without explicit approval.
```

**Why it works:** The requirement map prevents forgotten or falsely completed items, while the closeout preserves the final compliance evidence and reusable regression protection.
