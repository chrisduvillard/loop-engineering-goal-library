# Core `/goal` Library

These seven loops form the recommended permanent toolkit for long-running coding-agent work in mature repositories.

## Brownfield Continue / Finish

**Use when:** An existing project has plans, partial implementation, or an unfinished target and should advance autonomously.

```text
/goal Bring this existing repository to [TARGET]. First establish the actual state: read applicable repository instructions, specifications/PRDs, architecture, approved plans, progress/handoffs, native scripts/CI/tests, and Git status/diff/history. Reconcile stale or conflicting artifacts by authority, recency, and executable evidence; protect user, uncommitted, and unrelated work. Then repeat: select the highest-priority unblocked gap; verify it; make the smallest coherent reversible production change; run the repository-native relevant checks; review the diff; add regression coverage for fixed failures; keep only changes that preserve or improve the baseline; and update existing progress/handoff state with evidence and the next action. Continue autonomously—do not stop at planning, analysis, documentation, or tests while production work remains, and do not ask what to do next when the repository answers it. Finish only when every in-scope gap is closed and [ACCEPTANCE EVIDENCE] passes with results surfaced. Stop earlier only for a genuine external/owner-approval blocker, an exhausted [BUDGET], or two consecutive no-progress cycles; leave a restartable handoff. Never perform destructive, deployment, credential, release, or external-system actions without explicit approval.
```

**Why it works:** It starts from evidence rather than stale assumptions and gives the agent authority to choose the next safe task. Success, regression, stagnation, and approval boundaries are all explicit.

---

## PRD / Spec Compliance

**Use when:** A product, feature, or repository must be brought into full alignment with documented requirements.

```text
/goal Make [SCOPE] fully comply with [SPEC/PRD]. First reconcile the authoritative current requirements with actual code, runtime behavior, tests, documentation, CI, and Git history; maintain a concise requirement-to-evidence map and escalate only contradictions that require a product decision. In dependency and priority order, take each verified gap: reproduce or prove it, implement the smallest production fix, add or update acceptance and regression coverage, run repository-native targeted checks, then rerun affected broader gates. Preserve unrelated behavior and work; never mark a requirement complete from code inspection or an agent assertion alone, and never weaken a requirement or verifier to make it pass. Use an independent review for high-risk or ambiguous changes and verify its findings before fixing them. Update existing plan, progress, or handoff state. Finish only when every in-scope requirement is Pass with surfaced evidence and [FINAL GATES] pass. Stop as Blocked for a named external dependency or required owner decision, or stop at [BUDGET] or after two no-progress cycles; leave a restartable handoff. No irreversible or external-system action without explicit approval.
```

**Why it works:** The requirement map prevents forgotten or falsely completed items. It distinguishes a verified implementation gap from a contradiction that genuinely needs an owner decision.

---

## Next Milestone

**Use when:** The project has a larger roadmap but only the next coherent, dependency-safe increment should be completed.

```text
/goal Complete the next coherent unblocked milestone toward [OBJECTIVE]. Orient from the actual repository and reconcile applicable instructions, specifications, approved plans, progress/handoffs, tests, CI, and Git state; protect uncommitted and unrelated work. Select the highest-priority dependency-safe milestone that materially advances the objective and can be finished end-to-end without unnecessary scope expansion, then define its acceptance evidence before editing. Implement the required production behavior through small reversible changes, run repository-native relevant checks after each meaningful change, add regression coverage, review the diff, and update existing progress state. Do not substitute planning, scaffolding, documentation, or tests for required implementation. Finish when that milestone—not the entire backlog—meets its acceptance criteria and affected broader gates pass with surfaced evidence. Stop only for a genuine external or approval blocker, [BUDGET], or two consecutive no-progress cycles; leave a restartable handoff. No irreversible or external-system action without explicit approval.
```

**Why it works:** It constrains autonomy to one meaningful delivery unit without prescribing low-level tasks. The milestone’s evidence contract prevents both premature stopping and uncontrolled backlog expansion.

---

## Deep Audit + Remediation

**Use when:** The codebase needs evidence-based discovery and repair of important defects or risks.

```text
/goal Deeply audit and remediate [SCOPE] against [RUBRIC AND SEVERITY BAR]. Establish the verified baseline and actual Git state; read applicable instructions, architecture, requirements, tests, CI, incidents, and prior audits. Inspect code, configuration, dependencies, data paths, and real behavior; use focused read-only reviewers or subagents where useful. Treat every scanner or reviewer claim as a hypothesis: reproduce or otherwise prove impact before changing code. Rank verified findings by severity, confidence, and blast radius. For each finding, fix the root cause with the smallest reversible production change, add regression protection, run repository-native targeted and affected broader checks, and independently review important fixes. Keep only verified improvements; do not perform speculative cleanup or weaken gates. Update existing progress or handoff state. Finish only when no verified in-scope finding at or above [SEVERITY BAR] remains and [FINAL GATES] pass with surfaced evidence. Stop for an approval or external blocker, [BUDGET], or two full passes with no new actionable evidence; record residual risks, untested areas, and the next safe action. No destructive or external-system action without explicit approval.
```

**Why it works:** It separates discovery from proof and proof from remediation, reducing false-positive churn. The severity bar and two-pass saturation rule give the otherwise open-ended audit an objective finish.

---

## QA / Regression / UAT

**Use when:** The actual product surface and realistic user workflows must pass defined acceptance gates.

```text
/goal Make [PRODUCT OR SCOPE] pass [ACCEPTANCE FLOWS AND GATES]. First discover the real entry points, supported environments, repository-native run and test commands, requirements, and current Git and baseline state. Build a concise risk-based matrix of required user workflows, APIs and data paths, negative and edge cases, and supported configurations. Exercise the actual product from clean realistic state and capture exact failures and evidence. Verify each failure before fixing it; then make the smallest root-cause production fix, add automated regression coverage where practical, rerun the failed scenario, and rerun affected broader gates. Never weaken tests, skip required flows, or declare success from unit tests alone when integration, E2E, or UAT is applicable. Preserve unrelated and uncommitted work and update existing progress or handoff state. Finish only after a clean end-to-end run shows every required item passing with surfaced evidence and no new regressions. Stop for missing credentials, hardware, lawful access, approval, [BUDGET], or two no-progress cycles; leave exact reproduction evidence and the next action. No production or destructive action without explicit approval.
```

**Why it works:** It tests the product rather than merely the implementation units. The clean-state rerun and full workflow matrix prevent one fixed scenario from concealing adjacent regressions.

---

## Safe Refactor / Modernization

**Use when:** Architecture, dependencies, or internals should change while existing contracts remain stable.

```text
/goal Refactor or modernize [SCOPE] to [TARGET DESIGN] while preserving [BEHAVIOR AND CONTRACTS]. Orient from the actual repository and reconcile instructions, architecture, specifications, tests, CI, progress state, and Git history; protect uncommitted and unrelated work. Map consumers, public APIs, data formats, configuration, deployment assumptions, and hidden compatibility constraints. Capture a passing baseline and add characterization coverage for critical behavior that lacks protection. Define incremental seams and a fallback or rollback path, then make one coherent structural change at a time without unrelated feature expansion. After every change, run the same repository-native parity checks; at checkpoints run all affected broader gates, compare behavior and performance, and review the diff. Keep public and external contracts stable unless explicitly authorized, revert changes that worsen the verified state, independently review high-impact changes, and update existing progress or handoff artifacts. Finish only when the target structure is reached and before/after evidence proves equivalence except for explicitly named changes, all required gates pass, and any required rollback path is verified. Stop for an external decision, approval boundary, [BUDGET], or two no-progress cycles. No irreversible or external-system action without explicit approval.
```

**Why it works:** It makes behavioral equivalence a first-class result instead of assuming passing compilation proves safety. Incremental seams and fallback preservation prevent an all-or-nothing rewrite.

---

## Release Readiness

**Use when:** A version or milestone must converge on all repository-defined release gates without actually publishing it.

```text
/goal Bring [VERSION OR SCOPE] to release-ready—not released—under the repository-defined release criteria. Establish the actual state and reconcile release documentation, specifications, CI, Git history and working changes, open blockers, versioning and changelog, migrations, security, reliability and performance gates, deployment assumptions, and rollback instructions; protect unrelated and uncommitted work. Turn the actual release gates into a concise checklist and capture their baseline. Work the highest-risk unblocked failure first: verify it, make the smallest reversible production fix, add regression protection, run repository-native targeted checks, then rerun clean or production-like full gates at appropriate checkpoints. Use an independent final review and verify every finding; do not hide failures, weaken gates, or expand scope. Update release, progress, and handoff artifacts. Finish only when every required gate passes with surfaced evidence, no release-blocking finding remains, artifacts, documentation, configuration, migrations, and rollback instructions are consistent, and the working tree has no unexplained changes. Do not tag, publish, deploy, merge, push, or alter production without explicit approval. Stop for an external or approval blocker, [BUDGET], or two no-progress cycles; leave a restartable release handoff.
```

**Why it works:** It distinguishes preparing a release from executing irreversible release actions. The loop converges on the repository’s real gates instead of imposing a generic checklist.
