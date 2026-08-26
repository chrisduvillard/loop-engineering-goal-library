# Loop Engineering for AI Coding Agents

> [!IMPORTANT]
> This file is the **historical research foundation**, not the current copy-ready implementation. The live workflow, zero-friction launchers, shaping history, and profile catalog are maintained in [`README.md`](README.md), [`CURRENT_IMPLEMENTATION.md`](CURRENT_IMPLEMENTATION.md), and [`goals/`](goals/). Placeholder commands later in this report are preserved as research history.

*Research checked against current sources on August 25, 2026.*

## Executive conclusion

**Prompt engineering** improves an individual instruction. **Loop engineering** designs the control system around the agent:

```text
Fresh state → Select work → Make bounded change → Verify → Keep or revert
           → Review → Record state → Continue, stop, or escalate
```

Addy Osmani describes this as replacing yourself as the person repeatedly prompting the agent; Forward Future reduces the idea to “a task with a check.” The crucial additions are durable state, objective verification, retry and rollback rules, authority boundaries, and stopping logic. See [Addy Osmani's Loop Engineering](https://addyosmani.com/blog/loop-engineering/) and the [Forward Future Loop Library](https://signals.forwardfuture.com/loop-library/#top).

For brownfield development, the strongest general form is exactly:

> **Orient → Reconcile → Select → Change → Verify → Review → Record → Repeat**

The loop should optimize for the **verified repository state**, not merely finishing tasks or producing code.

---

# Research synthesis

## Codex and Claude Code `/goal`

### What they share

Both products use `/goal` for substantial work with a measurable completion condition. In each case, the condition also acts as the work directive, so the best goal combines:

- One outcome
- Important constraints and protected behavior
- A stated verification method
- An explicit stopping or escalation condition

Neither implementation grants additional permissions merely because a goal is active. Autonomous continuation and authority to deploy, delete, publish, access credentials, or modify external systems remain separate concerns. See [OpenAI's goal documentation](https://developers.openai.com/codex/use-cases/follow-goals/).

### OpenAI Codex

OpenAI presents `/goal` as a durable objective that remains attached to the active work until Codex considers the completion contract satisfied. Current controls include viewing, editing, pausing, resuming, and clearing the goal. OpenAI specifically recommends one objective, one stopping condition, named source files, verifiable commands or artifacts, checkpoints, and a short progress log. See [Follow goals with Codex](https://developers.openai.com/codex/use-cases/follow-goals/).

OpenAI’s guidance for migrations and refactors adds several brownfield-critical requirements: preserve behavior, work in controlled checkpoints, retain parity and rollback paths, run focused checks after each change, and avoid combining unrelated modernization with the requested work. See [Code migrations](https://developers.openai.com/codex/use-cases/code-migrations).

### Anthropic Claude Code

Claude Code’s implementation is more explicit about evaluation. After each turn, a separate small model evaluates the condition against evidence in the conversation and returns one of three results:

- Not yet met
- Met
- Impossible

The evaluator does **not** independently inspect files or execute commands. Therefore, the working agent must surface command results, test outcomes, measurements, and other evidence in the transcript. Claude also exposes duration, turn count, token consumption, and the evaluator’s latest reasoning. See [Claude Code goals](https://docs.anthropic.com/en/docs/claude-code/goal).

Claude supports time or turn bounds directly in the goal condition. It also detects a stalled pattern in which the agent repeatedly answers the evaluator without using tools or making progress, then returns control while leaving the goal available to resume.

### Claude `/loop` is different

Claude’s `/loop` is primarily **interval-driven**: the next invocation starts because time elapsed. `/goal` is **condition-driven**: the next turn starts because the previous turn did not satisfy the completion condition.

Use `/loop` for activities such as checking CI, watching a pull request, polling an external job, or periodically inspecting fresh inputs. Use `/goal` for implementing, fixing, migrating, auditing, or testing until a defined end state passes. Codex handles recurring time-driven work through separate scheduled-task functionality rather than the `/goal` primitive. See [Claude Code goals](https://docs.anthropic.com/en/docs/claude-code/goal).

### Portability rule

A portable goal should not depend on:

- Codex-specific pause or edit controls
- Claude-specific evaluator verdicts
- A particular model, subagent command, test framework, package manager, or stack
- Automatic approval or elevated permissions

It should describe the **repository operation and evidence contract** in ordinary language. Both tools can then execute it with their native machinery.

---

## The essential loop types

A mature coding workflow usually combines six primitives:

**Goal loop:** Continue closing known gaps until a defined acceptance state holds.

**Verification/evaluation loop:** Inspect the current result using a stable command, test, benchmark, runtime flow, or rubric. Do not change anything when the condition already passes.

**Retry loop:** Retry only when state changed or the failure was plausibly transient. Repeating an unchanged deterministic failure is not progress.

**Optimization loop:** Record a baseline, make one focused change, rerun the same evaluation under the same conditions, and retain the challenger only when it beats the current champion without violating must-pass gates.

**Audit loop:** Discover possible issues, but treat scanner, reviewer, and subagent output as hypotheses until reproduced or otherwise verified.

**Remediation loop:** Fix the verified root cause minimally, add regression protection, rerun the failing scenario, and then run the broader affected gates.

Deterministic checks should normally be primary. Rubric-based or model-based review is useful for qualities such as usability, visual design, readability, or architecture, but it should supplement rather than replace executable evidence. See [Iterate on difficult problems](https://developers.openai.com/codex/use-cases/iterate-on-difficult-problems).

---

## What counts as completion evidence

Strong evidence describes the resulting state, not merely the work performed:

- Exact command and exit/result
- Reproduction that no longer fails
- Passing unit, integration, contract, E2E, or UAT result
- Runtime logs, API responses, database state, screenshots, or generated artifacts
- Before/after benchmark under identical conditions
- Requirement-to-evidence traceability
- No new failures relative to the captured baseline
- Reviewed diff with unexplained changes resolved
- Tested rollback or retained fallback where applicable

For Claude in particular, this evidence must be surfaced in the conversation for the separate goal evaluator to see it. More generally, an agent saying “implemented,” “verified,” or “looks correct” is not acceptance evidence. See [Claude Code goals](https://docs.anthropic.com/en/docs/claude-code/goal).

---

## State management across iterations

The repository should remain the durable memory. Existing `PLAN`, `PROGRESS`, handoff, issue, checklist, or execution-plan artifacts should record at least:

```text
Objective and scope
Branch and current SHA
Baseline checks and known pre-existing failures
Completed changes and evidence
Failed or reverted approaches
Unresolved contradictions and risks
Current blockers
Next safest action
```

Do not create another competing state system when the repository already has one. Update the existing authoritative artifact. Anthropic’s long-running-agent experiments found that incremental work plus explicit handoff artifacts prevented later sessions from guessing or prematurely declaring completion; Addy makes the same point as “the agent forgets, the repo doesn’t.” OpenAI likewise recommends an external running log for long optimization loops. See [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).

---

## Independent review and subagents

Independent review is most valuable for:

- High-blast-radius changes
- Security and authorization paths
- Data migrations
- Concurrency and reliability changes
- Ambiguous requirements
- Subjective UI/UX evaluation
- Large or architecture-affecting diffs

A fresh reviewer should receive the relevant requirement, diff, and acceptance criteria—not the implementer’s full persuasive narrative. Its findings must still be verified before remediation. Anthropic found that separating generator and evaluator reduced overly positive self-assessment, while also noting that separate evaluation can be unnecessary overhead for simple, reliably verifiable work. See [Harness design for long-running applications](https://www.anthropic.com/engineering/harness-design-long-running-apps).

Parallel agents are safest for read-heavy discovery, independent reviews, isolated test investigation, or clearly separated workstreams. Concurrent writers should use separate worktrees or non-overlapping ownership; otherwise, coordination and merge conflicts can outweigh the speed gain. See [Codex subagents](https://developers.openai.com/codex/agent-configuration/subagents).

---

## Objective loop exits

Every loop should terminate in one of these states:

1. **Success:** All acceptance gates pass with surfaced evidence.
2. **No-op:** The target state already holds; evidence proves no change was needed.
3. **Blocked:** A named external dependency, credential, hardware resource, lawful-data requirement, or unavailable service prevents progress.
4. **Approval required:** Continuing would cross a product-decision or irreversible-action boundary.
5. **Exhausted:** The stated time, iteration, or cost budget is consumed.
6. **Stalled:** Two serious iterations produce neither new evidence nor measurable progress.

Blocked, exhausted, and stalled are valid stopping states—but they are not success. They should produce a restartable handoff. See [Forward Future's loop-learning guide](https://signals.forwardfuture.com/loop-library/learn/).

---

## Common failure modes

The most frequent failures are:

- **Vague objective:** “Improve everything” supplies no stable finish line.
- **One-shot overreach:** The agent changes too much, exhausts context, and leaves a partially coherent repository.
- **Stale-artifact obedience:** An old plan or checklist is trusted despite contradictory code, tests, or Git history.
- **Premature completion:** Some progress exists, so the agent assumes the whole objective is done.
- **Self-certification:** The implementer judges its own output without independent or executable evidence.
- **Verifier gaming:** Tests are weakened, skipped, narrowly optimized, or changed merely to make the result green.
- **Regression blindness:** The immediate test passes, but adjacent contracts or realistic flows fail.
- **Circular retrying:** The same command or approach is repeated without a changed hypothesis.
- **Context decay:** Later iterations forget what was tried, what remains, or why a decision was made.
- **Parallel collisions:** Multiple agents edit the same files or solve the same task.
- **Authority expansion:** An autonomous implementation goal drifts into deploy, publish, merge, destructive-data, credential, or production operations.

These are best countered by small changes, fixed checks, explicit state, independent review where warranted, full-gate checkpoints, rollback rules, and bounded no-progress exits. See [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).

---

## When `/goal` should not be used

Do not use an autonomous goal loop when:

- The task is one small, obvious change with one immediate check.
- The request is a loose collection of unrelated backlog items.
- The product direction or acceptance criteria have not been decided.
- No sufficiently stable verifier, rubric, or observable outcome exists.
- The next step is waiting for time or fresh external state; use scheduled polling instead.
- Every meaningful next action requires human judgment.
- The task mainly involves irreversible production, legal, financial, account, credential, or destructive operations.
- The likely benefit does not justify the iteration and token budget.

OpenAI explicitly advises against loose, unrelated goals, while Forward Future recommends a one-time task whenever one result does not need to determine the next action. See [OpenAI's goal documentation](https://developers.openai.com/codex/use-cases/follow-goals/).

---

# Core `/goal` library

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

---

# Are separate specialized loops worthwhile?

The seven loops above are sufficient as the permanent core.

| Area | Recommended treatment |
|---|---|
| Bug fixing | Use **Deep Audit + Remediation** scoped to one bug; use a normal task instead of `/goal` when it is a single reproduction/fix/check cycle. |
| Security | Use **Deep Audit + Remediation** with a security standard, severity threshold, read-only discovery, and stricter approval boundaries. |
| Reliability | Use **Deep Audit + Remediation** or **QA / Regression / UAT** with failure injection, recovery, idempotency, and observability gates. |
| Performance | Use **Safe Refactor / Modernization** with a fixed benchmark, stable environment, baseline, and champion/challenger keep-or-revert rule. |
| UI/UX | Use **QA / Regression / UAT** with real browser flows, screenshots, supported viewport matrix, accessibility checks, and an explicit design rubric. |
| Technical debt | Use **Safe Refactor / Modernization** with an objective structural target rather than “clean up the code.” |
| Documentation sync | Use **PRD / Spec Compliance** when documentation is authoritative; use **Release Readiness** for version, migration, operational, and release documentation. |

Security and performance sometimes deserve saved **configured variants**, but they do not require different core loop mechanics. Forward Future’s strongest specialized loops consistently reuse the same structure: capture baseline, make one bounded change, rerun the same verifier, keep only proven improvement, and stop on target, stagnation, budget, blocker, or approval. See the [Forward Future Loop Library](https://signals.forwardfuture.com/loop-library/).

---

# 1. Recommended Golden Set

Keep these seven permanently:

1. **Brownfield Continue / Finish** — default autonomous project loop.
2. **PRD / Spec Compliance** — requirements-driven convergence.
3. **Next Milestone** — bounded roadmap execution.
4. **Deep Audit + Remediation** — evidence-based discovery and repair.
5. **QA / Regression / UAT** — actual-product verification.
6. **Safe Refactor / Modernization** — behavior-preserving structural change.
7. **Release Readiness** — convergence on pre-release gates.

For Trading-Intel and AuraVoya, **Brownfield Continue / Finish** should be the everyday default. Switch to the more specialized loop when the objective is clearly spec compliance, product QA, architecture work, or release preparation.

---

# 2. Best Universal Brownfield `/goal`

```text
/goal Bring this existing project to [TARGET]. Before any persistent change, establish the actual state: read applicable repository instructions, specifications/PRDs, architecture, approved plans, progress/handoffs, native scripts/CI/tests, and Git status/diff/history. Reconcile contradictions by authority, recency, and executable evidence; protect user, uncommitted, and unrelated work. Derive concrete acceptance evidence from the target and repository. Then repeat: select the highest-priority unblocked gap; verify it; make the smallest coherent reversible production change; run the smallest relevant repository-native checks; review the diff; add regression coverage for fixed failures; and keep only changes that preserve or improve the baseline. At checkpoints run broader required gates and independently review important changes. Update existing progress or handoff artifacts with branch/SHA, changes, evidence, remaining gaps, blockers, and the next action. Continue autonomously; do not stop at planning, analysis, documentation, or tests while production work remains, and do not ask what to do next when repository evidence resolves it. Finish only when every in-scope gap is closed and all acceptance gates pass with evidence surfaced. Stop only for a genuine external or owner-approval blocker, an exhausted [BUDGET], or two consecutive cycles without new evidence or measurable progress; leave a restartable handoff. Never perform destructive, deployment, credential, release, merge, publish, or external-system actions without explicit approval.
```

This is the strongest general-purpose version because it handles:

- Repository orientation
- Stale or contradictory state
- Priority selection
- Production implementation
- Native verification
- Regression protection
- Independent review
- Durable handoff state
- Autonomous continuation
- Approval and stagnation boundaries

---

# 3. Ultra-Short Default `/goal`

Use this when the repository already has reliable instructions, plans, state files, and native checks:

```text
/goal Finish [TARGET] from the repository’s actual current state. Read and reconcile its instructions, plans/progress/handoffs, tests/CI, and Git state; protect unrelated and uncommitted work. Repeatedly take the highest-priority unblocked gap, make one small reversible production change, verify it with repository-native checks, add regression coverage, review the diff, and update existing progress state. Keep only changes that preserve or improve the baseline. Continue without asking what is next and do not stop at planning, tests, or documentation while implementation remains. Finish only when [ACCEPTANCE] passes with surfaced evidence; stop for a genuine approval/external blocker, exhausted budget, or two no-progress cycles and leave a restartable handoff. No irreversible or external action without approval.
```

---

# 4. Brownfield Safety Kernel

This is the minimum reusable paragraph that should appear in almost every brownfield loop:

```text
First establish the repository’s actual state from applicable instructions, requirements, plans/progress/handoffs, native checks, and Git status/diff/history. Reconcile stale or contradictory artifacts using authority, recency, and executable evidence; protect user, uncommitted, and unrelated work. Make small coherent reversible production changes, verify each with repository-native checks, add regression protection for fixed failures, review important diffs independently, and keep only changes that preserve or improve the baseline. Update existing state artifacts with evidence and the next action. Finish only on passing acceptance evidence; otherwise stop only for a genuine approval/external blocker, exhausted budget, or repeated no-progress, leaving a restartable handoff. Never perform irreversible or external-system actions without explicit approval.
```

The irreducible ideas are:

1. Orient from actual state.
2. Reconcile rather than blindly trust.
3. Protect existing work and behavior.
4. Change incrementally and reversibly.
5. Use native, stable verification.
6. Require evidence and regression protection.
7. Persist state and the next action.
8. Bound stagnation and authority.

---

# 5. Vague Task → Strong Loop

Convert an ordinary request using five questions:

1. **Outcome:** What observable state should be true?
2. **Scope:** Which surfaces are included, and what must remain unchanged?
3. **Verifier:** Which command, workflow, metric, or rubric proves success?
4. **Iteration:** What is one safe change, and when is it kept or reverted?
5. **Exit:** What counts as success, blocker, approval boundary, exhaustion, or stagnation?

Transform:

> Improve the project.

Into:

```text
/goal Improve [SCOPE] from its verified baseline until [MEASURABLE TARGET] passes under [VERIFIER]. Make one small reversible change per cycle, keep only changes that improve the result without regressing repository-native gates, and record the evidence and next action. Stop on target, genuine blocker or approval boundary, exhausted budget, or two no-progress cycles; preserve unrelated work and perform no irreversible action without approval.
```

The central rule is:

> **Never ask an autonomous agent to “make things better.” Give it a state to reach, a check that decides, a boundary it cannot cross, and a record that lets the next iteration continue safely.**
