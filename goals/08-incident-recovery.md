# Incident Recovery / Stabilization

**Use when:** A severe regression or production-like incident must be contained, diagnosed, and recovered without compounding the damage.

## Recommended: skill-backed

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Incident Recovery / Stabilization profile. Preserve evidence; separate containment, restoration, root cause, and prevention; and continue until recovery gates pass, the failure is no longer reproducible under defined conditions, and rollback/recovery is verified. Stop for unresolved safety uncertainty or a contract-defined blocker, approval boundary, budget, or two no-progress cycles; preserve a reusable closeout packet.
```

## Standalone fallback

```text
/goal Stabilize and recover [SYSTEM OR SCOPE] from [INCIDENT OR FAILURE] to [RECOVERY TARGET]. First preserve evidence and establish the actual state from incident reports, logs, metrics, traces, recent deploys/config/data changes, repository instructions/runbooks, native tests/CI, prior goal archives, and Git status/history; protect unrelated work and do not alter production or external systems without explicit approval. Separate containment, restoration, root cause, and prevention. Reproduce or otherwise verify the failure, map its blast radius, and identify the safest reversible mitigation. Then iterate: test one evidence-backed hypothesis, make the smallest reversible change, run repository-native targeted checks and realistic recovery scenarios, compare health with the pre-incident baseline, and keep only proven improvements. Add regression and observability coverage, independently review high-risk fixes, and record the timeline, evidence, decisions, and residual risk. Finish only when [RECOVERY GATES] pass, the failure is no longer reproducible under the defined conditions, and rollback/recovery is verified. Stop for an approval or external blocker, unresolved safety uncertainty, [BUDGET], or two no-progress cycles. At any terminal outcome, preserve a reusable closeout packet under the repository's goal-history convention (default `docs/goals/<goal-id>/`) containing `CONTRACT.md`, final `PROGRESS.md`, and `RESULT.md`; update the history index, promote verified reusable tests/docs/ADRs/runbooks/fixtures/tooling, and exclude secrets, private data, raw production dumps, and unnecessarily large logs. No production or destructive action without explicit approval.
```

**Why it works:** It prevents emergency work from becoming speculative cleanup and retains the incident timeline, proof, and prevention assets for the next response.
