# Core `/goal` Library

> [!NOTE]
> Generated from the canonical files under [`goals/`](goals/). Edit those files, then run `python3 scripts/sync_goal_docs.py --write`.

Seven copy-ready skill-backed commands for most long-running work in mature repositories. Each linked profile also contains a self-contained standalone fallback.

---

## [Brownfield Continue / Finish](goals/01-brownfield-continue-finish.md)

**Use when:** An existing project has an approved outcome, partial implementation, or unfinished milestone and should advance autonomously.

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Brownfield Continue / Finish profile. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve a reusable closeout packet and leave a restartable handoff.
```

**Why it works:** It begins from an approved outcome and current evidence, gives the agent authority to choose the next safe action, and preserves both execution state and reusable closeout knowledge.

**Standalone fallback:** [Open the complete profile](goals/01-brownfield-continue-finish.md).

---

## [PRD / Spec Compliance](goals/02-prd-spec-compliance.md)

**Use when:** A product, feature, or repository must be brought into full alignment with documented requirements.

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the PRD / Spec Compliance profile. Continue until every in-scope requirement is Pass with surfaced evidence and the final gates succeed without protected-behavior regressions. Stop only for a contract-defined product decision, blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve a reusable closeout packet and leave a restartable handoff.
```

**Why it works:** The requirement map prevents forgotten or falsely completed items, while the closeout preserves the final compliance evidence and reusable regression protection.

**Standalone fallback:** [Open the complete profile](goals/02-prd-spec-compliance.md).

---

## [Next Milestone](goals/03-next-milestone.md)

**Use when:** The project has a larger roadmap but only the next coherent, dependency-safe increment should be completed.

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Next Milestone profile. Finish the selected milestone end-to-end without expanding into the wider backlog, and continue until its acceptance evidence and affected broader gates pass. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve a reusable closeout packet and leave a restartable handoff.
```

**Why it works:** It bounds autonomy to one useful delivery unit and retains a reusable record of what the milestone proved, changed, and taught.

**Standalone fallback:** [Open the complete profile](goals/03-next-milestone.md).

---

## [Deep Audit + Remediation](goals/04-deep-audit-remediation.md)

**Use when:** The codebase needs evidence-based discovery and repair of important defects or risks.

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Deep Audit + Remediation profile and its severity bar. Verify findings before changing code, remediate root causes, add regression protection, and continue until no verified in-scope finding at or above the bar remains and final gates pass. Stop only for a contract-defined blocker, approval boundary, budget, or two evidence-saturated passes; preserve a reusable closeout packet and leave a restartable handoff.
```

**Why it works:** It separates discovery, proof, and remediation, then preserves a reusable audit ledger instead of losing findings and failed hypotheses in chat.

**Standalone fallback:** [Open the complete profile](goals/04-deep-audit-remediation.md).

---

## [QA / Regression / UAT](goals/05-qa-regression-uat.md)

**Use when:** The actual product surface and realistic user workflows must pass defined acceptance gates.

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the QA / Regression / UAT profile. Exercise the real product from clean realistic state, verify failures before fixing them, and continue until every required flow and broader gate passes with surfaced evidence and no new regressions. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve a reusable closeout packet and leave exact restart evidence.
```

**Why it works:** It tests actual product behavior, closes the failure-to-regression loop, and saves the acceptance matrix and reusable scenarios for future runs.

**Standalone fallback:** [Open the complete profile](goals/05-qa-regression-uat.md).

---

## [Safe Refactor / Modernization](goals/06-safe-refactor-modernization.md)

**Use when:** Architecture, dependencies, or internals should change while existing contracts remain stable.

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Safe Refactor / Modernization profile. Work through incremental seams, compare against the captured baseline, retain rollback, and continue until the target structure is reached with behavioral-equivalence evidence and all gates passing. Stop only for a contract-defined decision, blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve a reusable closeout packet.
```

**Why it works:** Behavioral equivalence, incremental seams, rollback, and an archived parity record keep modernization falsifiable and reusable.

**Standalone fallback:** [Open the complete profile](goals/06-safe-refactor-modernization.md).

---

## [Release Readiness](goals/07-release-readiness.md)

**Use when:** A version or milestone must converge on all repository-defined release gates without actually publishing it.

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Release Readiness profile. Work the highest-risk verified blocker first and continue until every release gate passes, the repository and release artifacts agree, rollback instructions are verified, and the working tree has no unexplained changes. Do not release, tag, publish, merge, or deploy; preserve a reusable closeout packet.
```

**Why it works:** It distinguishes readiness from release authority and leaves a reusable release-evidence packet for the human release decision.

**Standalone fallback:** [Open the complete profile](goals/07-release-readiness.md).
