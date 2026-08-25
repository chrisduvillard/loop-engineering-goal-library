# Goal Engine: Execution Profiles

Execution profiles are **control-loop presets**, not project types and not an exhaustive taxonomy. The Goal Contract always wins on outcome, scope, acceptance evidence, protected behavior, authority, and stop conditions.

Choose one primary preset when it matches the dominant execution shape. Add cross-cutting proof through [assurance-overlays.md](assurance-overlays.md), not by creating a profile for every quality concern.

## 1. Brownfield Continue / Finish

**Use for:** An approved outcome, partial implementation, or unfinished milestone.

- Reconstruct the real current state before selecting work.
- Choose the highest-priority unblocked gap in dependency order.
- Do not stop at planning or tests while required production behavior remains.
- Finish when every in-scope gap is closed and the contract's acceptance evidence passes.

## 2. PRD / Spec Compliance

**Use for:** Closing every verified gap against an authoritative requirement set.

- Maintain a requirement-to-evidence map with Pass, Fail, Blocked, and Not applicable states.
- Distinguish implementation gaps from contradictory requirements that need an owner decision.
- Never weaken a requirement or verifier to make it pass.
- Finish when every in-scope requirement is evidenced and the final gates pass.

## 3. Next Milestone

**Use for:** Delivering one coherent, dependency-safe increment from a larger roadmap.

- Select the highest-priority milestone that can be completed end to end.
- Define its acceptance evidence before editing.
- Avoid unrelated backlog work and opportunistic modernization.
- Finish the selected milestone, not the entire roadmap.

## 4. Deep Audit + Remediation

**Use for:** Evidence-based discovery and repair of important defects or risks.

- Treat scanner, reviewer, and subagent findings as hypotheses until verified.
- Rank verified findings by severity, confidence, and blast radius.
- Fix root causes, add regression protection, and rerun affected broader gates.
- Finish after no verified finding at or above the severity bar remains and a final pass finds no new actionable evidence.

## 5. QA / Regression / UAT

**Use for:** Making actual product surfaces and realistic workflows pass.

- Build a risk-based matrix of required flows, negative cases, data paths, configurations, and environments.
- Exercise the real product from clean, realistic state.
- Rerun the exact failed scenario after each fix, then affected broader gates.
- Finish only after a clean end-to-end pass of every required acceptance flow.

## 6. Safe Refactor / Modernization

**Use for:** Changing internals while preserving external behavior and contracts.

- Map consumers, APIs, formats, configuration, deployment assumptions, and hidden compatibility constraints.
- Capture baseline behavior and add characterization coverage where protection is weak.
- Change one structural seam at a time and preserve a fallback or rollback path.
- Finish when the target structure is reached and before/after evidence proves equivalence except for approved changes.

## 7. Release Readiness

**Use for:** Removing release blockers without performing the release.

- Turn repository-defined release criteria into a checklist and capture their baseline.
- Work highest-risk blockers first and rerun production-like full gates at checkpoints.
- Verify artifacts, configuration, migrations, operational docs, and rollback instructions together.
- Finish at release-ready; never tag, publish, deploy, or alter production without contract authority.

## 8. Incident Recovery / Stabilization

**Use for:** Restoring a degraded system, preserving evidence, and preventing recurrence.

- Separate containment, recovery, root-cause proof, and prevention.
- Prefer reversible mitigations until the failure mechanism is understood.
- Preserve logs, timelines, metrics, and reproductions needed for diagnosis.
- Finish only when health is verified, root cause is evidenced, regression protection exists, and follow-up state is recorded.

## 9. Dependency / Framework Upgrade

**Use for:** Staged upgrades with compatibility and rollback evidence.

- Inventory direct and transitive dependencies, supported versions, official migration guidance, and ecosystem constraints.
- Establish compatibility gates before changing versions.
- Upgrade in coherent stages; inspect lockfiles and generated changes.
- Finish when supported configurations pass, scoped deprecations are handled, and recovery is documented.

## 10. Data Migration / Integrity

**Use for:** Schema, format, backfill, or data movement where correctness and recovery matter.

- Define invariants, reconciliation, idempotency, mixed-version behavior, and rollback before mutation.
- Test representative data, interruption, retry, and partial-failure scenarios.
- Separate preparation, migration, verification, cutover, and destructive cleanup.
- Finish when reconciliation proves integrity and required rollback/cutover evidence passes.

## 11. Branch Rescue / Integration

**Use for:** Recovering valuable work from stale, divergent, or oversized branches.

- Pin source and target SHAs and protect recovery refs.
- Decompose the branch into coherent behavioral slices.
- Compare each slice with newer target behavior and choose the least risky transfer method.
- Finish when selected value is integrated and verified, rejected work is explained, and recovery remains possible.

## Custom Contract-Driven

**Use for:** A measurable engineering outcome whose dominant loop does not fit a preset.

The contract must define:

- One bounded unit of iteration
- One primary verifier or stable evaluation rubric
- A keep-or-revert decision
- Review and regression obligations
- Objective success, blocker, budget, and stall exits

A custom profile is a safe fallback, not permission for vague work. If the same custom pattern recurs across several goals or projects, propose a new preset with field evidence.

## Combining profiles and overlays

Use one primary profile. A secondary profile may contribute a narrow technique—for example QA matrices during an upgrade or data reconciliation during release readiness.

Use assurance overlays for security, reliability, performance, UX/accessibility, data governance, compatibility, operability, documentation, or compliance concerns.

Do not combine profiles merely to appear comprehensive. If two profiles imply materially different outcomes, return to `shape-goal` and split or clarify the contract.
