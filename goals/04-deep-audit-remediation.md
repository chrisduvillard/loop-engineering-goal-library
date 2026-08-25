# Deep Audit + Remediation

**Use when:** The codebase needs evidence-based discovery and repair of important defects or risks.

## Recommended: skill-backed

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Deep Audit + Remediation profile and its severity bar. Verify findings before changing code, remediate root causes, add regression protection, and continue until no verified in-scope finding at or above the bar remains and final gates pass. Stop only for a contract-defined blocker, approval boundary, budget, or two evidence-saturated passes; preserve a reusable closeout packet and leave a restartable handoff.
```

## Standalone fallback

```text
/goal Deeply audit and remediate [SCOPE] against [RUBRIC AND SEVERITY BAR]. Establish the verified baseline and actual Git state; read applicable instructions, architecture, requirements, tests, CI, incidents, prior audits, and prior goal archives. Inspect code, configuration, dependencies, data paths, and real behavior; use focused read-only reviewers or subagents where useful. Treat every scanner or reviewer claim as a hypothesis: reproduce or otherwise prove impact before changing code. Rank verified findings by severity, confidence, and blast radius. For each finding, fix the root cause with the smallest reversible production change, add regression protection, run repository-native targeted and affected broader checks, and independently review important fixes. Keep only verified improvements; do not perform speculative cleanup or weaken gates. Update existing progress or handoff state. Finish only when no verified in-scope finding at or above [SEVERITY BAR] remains and [FINAL GATES] pass with surfaced evidence. Stop for an approval or external blocker, [BUDGET], or two full passes with no new actionable evidence; record residual risks and untested areas. At any terminal outcome, preserve a reusable closeout packet under the repository's goal-history convention (default `docs/goals/<goal-id>/`) containing `CONTRACT.md`, final `PROGRESS.md`, and `RESULT.md`; update the history index, promote verified reusable tests/docs/ADRs/runbooks/fixtures/tooling, and exclude secrets, private data, raw production dumps, and unnecessarily large logs. No destructive or external-system action without explicit approval.
```

**Why it works:** It separates discovery, proof, and remediation, then preserves a reusable audit ledger instead of losing findings and failed hypotheses in chat.
