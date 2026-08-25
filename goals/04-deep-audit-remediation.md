# Deep Audit + Remediation

**Use when:** The codebase needs evidence-based discovery and repair of important defects or risks.

```text
/goal Deeply audit and remediate [SCOPE] against [RUBRIC AND SEVERITY BAR]. Establish the verified baseline and actual Git state; read applicable instructions, architecture, requirements, tests, CI, incidents, and prior audits. Inspect code, configuration, dependencies, data paths, and real behavior; use focused read-only reviewers or subagents where useful. Treat every scanner or reviewer claim as a hypothesis: reproduce or otherwise prove impact before changing code. Rank verified findings by severity, confidence, and blast radius. For each finding, fix the root cause with the smallest reversible production change, add regression protection, run repository-native targeted and affected broader checks, and independently review important fixes. Keep only verified improvements; do not perform speculative cleanup or weaken gates. Update existing progress or handoff state. Finish only when no verified in-scope finding at or above [SEVERITY BAR] remains and [FINAL GATES] pass with surfaced evidence. Stop for an approval or external blocker, [BUDGET], or two full passes with no new actionable evidence; record residual risks, untested areas, and the next safe action. No destructive or external-system action without explicit approval.
```

**Why it works:** It separates discovery from proof and proof from remediation, reducing false-positive churn. The severity bar and two-pass saturation rule give the otherwise open-ended audit an objective finish.
