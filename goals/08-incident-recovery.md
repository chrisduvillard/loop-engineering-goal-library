# Incident Recovery / Stabilization

**Use when:** A severe regression or production-like incident must be contained, diagnosed, and recovered without compounding the damage.

```text
/goal Stabilize and recover [SYSTEM OR SCOPE] from [INCIDENT OR FAILURE] to [RECOVERY TARGET]. First preserve evidence and establish the actual state from incident reports, logs, metrics, traces, recent deploys/config/data changes, repository instructions/runbooks, native tests/CI, and Git status/history; protect unrelated work and do not alter production or external systems without explicit approval. Separate containment, restoration, root cause, and prevention. Reproduce or otherwise verify the failure, map its blast radius, and identify the safest reversible mitigation. Then iterate: test one evidence-backed hypothesis, make the smallest reversible change, run repository-native targeted checks and realistic recovery scenarios, compare health with the pre-incident baseline, and keep only proven improvements. Add regression and observability coverage, independently review high-risk fixes, and record the timeline, evidence, decisions, and residual risk. Finish only when [RECOVERY GATES] pass, the failure is no longer reproducible under the defined conditions, and rollback/recovery is verified. Stop for an approval or external blocker, unresolved safety uncertainty, [BUDGET], or two no-progress cycles; leave an actionable incident handoff.
```

**Why it works:** It prevents the common mistake of mixing emergency containment with speculative cleanup. Recovery, root cause, and prevention each require their own evidence before the incident can be considered closed.
