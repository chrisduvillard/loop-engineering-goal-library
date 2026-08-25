# PRD / Spec Compliance

**Use when:** A product, feature, or repository must be brought into full alignment with documented requirements.

```text
/goal Make [SCOPE] fully comply with [SPEC/PRD]. First reconcile the authoritative current requirements with actual code, runtime behavior, tests, documentation, CI, and Git history; maintain a concise requirement-to-evidence map and escalate only contradictions that require a product decision. In dependency and priority order, take each verified gap: reproduce or prove it, implement the smallest production fix, add or update acceptance and regression coverage, run repository-native targeted checks, then rerun affected broader gates. Preserve unrelated behavior and work; never mark a requirement complete from code inspection or an agent assertion alone, and never weaken a requirement or verifier to make it pass. Use an independent review for high-risk or ambiguous changes and verify its findings before fixing them. Update existing plan, progress, or handoff state. Finish only when every in-scope requirement is Pass with surfaced evidence and [FINAL GATES] pass. Stop as Blocked for a named external dependency or required owner decision, or stop at [BUDGET] or after two no-progress cycles; leave a restartable handoff. No irreversible or external-system action without explicit approval.
```

**Why it works:** The requirement map prevents forgotten or falsely completed items. It distinguishes a verified implementation gap from a contradiction that genuinely needs an owner decision.
