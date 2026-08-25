---
name: shape-goal
description: Turn vague or changing project needs into an evidence-backed Goal Contract and managed goal portfolio, select an execution profile plus assurance overlays, preserve prior goals, and produce a copy-ready native /goal command backed by goal-engine. Use before /goal when the target, priority, scope, evidence, lifecycle transition, or best execution pattern is unclear.
compatibility: Portable Agent Skills host. Reads repository evidence and writes planning/state artifacts; production implementation is intentionally out of scope.
metadata:
  author: chrisduvillard
  version: "0.2.0"
  source: "github.com/chrisduvillard/loop-engineering-goal-library"
---

# Shape Goal

Compile rough or changing intent into a safe execution contract. **Shape and manage the work; do not implement production changes.**

```text
project needs → goal portfolio → approved contract → native /goal + goal-engine
```

A useful target has this form:

> **[Observable outcome]** is true for **[scope]**, proven by **[acceptance evidence]**, while **[protected behavior]** remains intact.

## Invocation patterns

These are natural-language modes, not a rigid parser:

| Need | Claude Code | Codex CLI / IDE |
|---|---|---|
| Continue or shape the next goal | `/shape-goal Continue this project` | `$shape-goal Continue this project` |
| Add a new goal | `/shape-goal New goal: [INTENT]` | `$shape-goal New goal: [INTENT]` |
| Change the current goal | `/shape-goal Change current goal: [NEW NEED]` | `$shape-goal Change current goal: [NEW NEED]` |
| Review priorities | `/shape-goal Review the goal portfolio and recommend what should run next` | `$shape-goal Review the goal portfolio and recommend what should run next` |
| Resume prior work | `/shape-goal Resume [GOAL ID]` | `$shape-goal Resume [GOAL ID]` |

## Required outputs

Produce:

1. A lifecycle decision for every affected existing goal.
2. One stable Goal ID for each new goal.
3. One approved Goal Contract revision for the next executable goal.
4. A portfolio disposition and path when multiple non-closed goals exist.
5. One primary execution profile or an explicit custom profile.
6. Zero or more assurance overlays.
7. One reusable project-harness path or a justified decision that existing repository instructions are sufficient.
8. Durable progress and archive paths.
9. One short skill-backed native `/goal` command.
10. One standalone fallback when `goal-engine` may not be installed.

## 1. Orient before asking

Read the applicable repository evidence first:

- Agent and repository instructions
- Specifications, PRDs, architecture docs, ADRs, and domain vocabulary
- Approved plans, milestones, issues, progress files, goal portfolio, prior archives, and handoffs
- Native scripts, tests, CI, release gates, runtime entry points, and project harness
- Git status, diff, branch, worktrees, and relevant history

Reconcile contradictions by explicit authority, recency, and executable evidence. Protect uncommitted and unrelated work.

**Facts are the agent's job; decisions are the user's.** Never ask for something the repository, tools, history, or runtime evidence can answer.

## 2. Treat the project as a portfolio of goals

A project may have many candidate, ready, active, paused, blocked, and closed goals over time.

Use the repository's existing tracker when it can represent priority, dependencies, state, contract, and progress. Otherwise use [templates/goal-portfolio-template.md](templates/goal-portfolio-template.md) at `docs/goals/PORTFOLIO.md` once more than one non-closed goal exists.

Rules:

- One native `/goal` session or worktree executes one dependency-safe leaf Goal Contract.
- Multiple project goals may run in parallel only in isolated branches/worktrees with non-overlapping ownership and explicit dependency handling.
- The portfolio orders and relates goals; it does not replace their contracts.
- A parent goal may coordinate child goals, but should not become an unbounded mega-goal.
- Priority changes update the portfolio, not the meaning of an approved contract.

## 3. Classify the lifecycle transition

Do not silently absorb a new request into the active goal. Classify it:

- **Clarify** — wording or evidence reference changes without changing semantics. Keep Goal ID; record revision.
- **Amend** — same observable outcome, but material scope, verifier, protection, authority, or stop condition changes. Pause execution, obtain approval, increment revision.
- **Reprioritize** — portfolio order changes; contracts remain unchanged.
- **Pause / Resume** — preserve progress, next action, branch/SHA, and resume condition.
- **Supersede** — a different outcome replaces the prior goal. Archive the prior goal as Superseded and create a new Goal ID.
- **Split** — one goal is too broad. Create child goals and select one dependency-safe leaf to execute.
- **Merge** — combine only when outcomes, evidence, and authority genuinely align; otherwise keep goals separate.
- **Cancel** — archive the goal as Cancelled with the reason and reusable evidence.
- **Close** — archive a terminal outcome and update history.

Keep the same Goal ID only when the observable outcome remains the same.

## 4. Classify ambiguity

### One target is strongly supported

Draft the contract and recommend its priority directly.

### Several materially different targets are plausible

Present at most three candidates with supporting evidence, expected value, dependencies, scope, trade-off, likely verifier, and recommendation. Ask one owner decision at a time only when alternatives create materially different outcomes.

### The destination is still foggy

Do not manufacture a target. Recommend wayfinding, product discovery, an experiment, or an ADR when no stable outcome or verifier exists.

## 5. Assign durable identity and relationships

Create a stable Goal ID:

```text
YYYY-MM-DD-short-kebab-slug
```

An issue or milestone ID may be used when already authoritative.

Record:

- Contract revision and lifecycle state
- Priority
- Parent and dependency Goal IDs
- Supersedes / superseded-by relationships
- Library version or source commit
- Contract, progress, portfolio, archive, and history paths
- Branch/worktree when active

## 6. Build the Goal Contract

Use [goal-contract-template.md](goal-contract-template.md). Include:

- One observable outcome and why it is next
- Scope and exclusions
- Acceptance evidence
- Protected behavior
- Baseline and known exceptions
- Primary profile or custom loop definition
- Assurance overlays
- Project-harness path
- Authority and stop boundaries
- Review triggers for goal drift
- Portfolio relationships and durable state paths

A target is not ready when it is a task list, implementation mechanism, vague aspiration, entire backlog, or proxy metric that can pass while the user outcome fails.

## 7. Select the execution pattern

Choose one primary preset from [../goal-engine/references/loop-profiles.md](../goal-engine/references/loop-profiles.md) when it matches the dominant control loop.

The eleven presets are **not project types and not a ceiling**. They cover common execution shapes. When none fits, select **Custom Contract-Driven** and define in the contract:

- Unit of iteration
- Primary verifier
- Keep-or-revert rule
- Review strategy
- Stop condition

Select relevant assurance overlays from [../goal-engine/references/assurance-overlays.md](../goal-engine/references/assurance-overlays.md). If two profiles imply different outcomes, split the goal rather than building a composite mega-goal.

## 8. Reuse or establish the project harness

Prefer existing verified commands and documentation. When setup, run, reset, or verification knowledge is repeatedly rediscovered or contradictory, use [../goal-engine/templates/project-harness-template.md](../goal-engine/templates/project-harness-template.md) to create or refresh `docs/agent/PROJECT_HARNESS.md`.

The harness stores project-specific mechanics once so later goals do not rediscover them. It must link to canonical scripts and remain vendor-neutral.

## 9. Apply the readiness gate

The next executable goal is ready only when:

- It has one stable Goal ID, revision, state, priority, and outcome.
- A fresh agent can tell what is in and out of scope.
- Completion has observable proof.
- Protected behavior and user work are named.
- Material owner decisions are resolved.
- Profile, overlays, harness, state, and archive paths are clear.
- Dependencies are satisfied or explicitly handled.
- Review and stopping conditions are explicit.
- No other active goal will be overwritten or accidentally entangled.

## 10. Persist without creating competing state

After approval:

1. Update an existing authoritative issue, milestone, PRD, plan, or goal artifact when possible.
2. Otherwise create or update `GOAL.md`.
3. Use `GOAL_PROGRESS.md` only when no suitable progress artifact exists.
4. Create or update a portfolio only when multiple non-closed goals need coordination.
5. Link rather than duplicate detailed requirements.
6. Preserve prior contract revisions and terminal closeout packets.
7. Record approvals and lifecycle transitions.

If the user requested read-only shaping, return the contract and launch packet without writing.

## 11. Render the native `/goal`

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use its selected execution profile, assurance overlays, and project harness. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. At checkpoints, detect material goal drift instead of silently expanding scope. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve reusable state and leave a restartable handoff.
```

Also provide the matching standalone preset. When **Custom Contract-Driven** is selected, use [templates/custom-contract-driven-goal.md](templates/custom-contract-driven-goal.md). Do not duplicate the entire standalone prompt into the contract.

## 12. End with a launch packet

```text
Lifecycle decision: [NEW / RESUME / AMEND / REPRIORITIZE / PAUSE / SUPERSEDE / SPLIT / MERGE / CANCEL / CLOSE]
Approved target: [ONE SENTENCE]
Goal ID / revision: [ID] / [REVISION]
Priority and dependencies: [PRIORITY] / [IDS OR NONE]
Contract: [PATH OR ISSUE]
Portfolio: [PATH / EXISTING TRACKER / NOT NEEDED]
Execution profile: [PRESET OR CUSTOM]
Assurance overlays: [LIST OR NONE]
Project harness: [PATH / EXISTING SOURCES]
Progress state: [PATH OR ISSUE]
Archive: [PATH]
Run with goal-engine: [COPY-READY /goal]
Standalone fallback: [LINK OR COPY-READY /goal]
Open owner decisions: None / [SHORT LIST]
```

Native `/goal` activation remains the boundary between shaping and autonomous implementation.
