---
name: shape-goal
description: Turn a vague project request, continuation request, issue, PRD, or milestone into an evidence-backed Goal Contract, select the right execution profile, and produce a copy-ready native /goal command backed by the goal-engine skill. Use before /goal when the target, scope, acceptance evidence, protected behavior, durable state, or best loop is unclear.
compatibility: Portable Agent Skills host. Reads repository evidence and writes planning/state artifacts; production implementation is intentionally out of scope.
metadata:
  author: chrisduvillard
  version: "0.1.0"
  source: "github.com/chrisduvillard/loop-engineering-goal-library"
---

# Shape Goal

Compile rough intent into a safe, reusable execution contract. **Shape the work; do not implement production changes.**

A useful target has this form:

> **[Observable outcome]** is true for **[scope]**, proven by **[acceptance evidence]**, while **[protected behavior]** remains intact.

```text
shape-goal  → decide and persist what done means
goal-engine → execute that approved contract safely
native /goal → keep execution alive and evaluate its finish condition
```

## Invocation

- **Claude Code:** `/shape-goal Continue this project`
- **Codex CLI or IDE:** `$shape-goal Continue this project`
- **Other Agent Skills hosts:** explicitly select or mention `shape-goal`

## Required outputs

Produce all seven:

1. One stable **Goal ID**.
2. One approved **Goal Contract**.
3. One selected **execution profile**.
4. One durable **progress-state path**.
5. One durable **archive path** for the terminal closeout packet.
6. One short skill-backed native `/goal` command.
7. One standalone `/goal` fallback when `goal-engine` may not be installed.

## 1. Orient before asking

Read the applicable repository evidence first:

- Agent and repository instructions
- Specifications, PRDs, architecture docs, ADRs, and domain vocabulary
- Approved plans, milestones, issues, progress files, prior goal archives, and handoffs
- Native scripts, tests, CI, release gates, and runtime entry points
- Git status, diff, branch, and relevant history

Establish the actual current state and reconcile contradictions by explicit authority, recency, and executable evidence. Protect uncommitted and unrelated work.

**Facts are the agent's job; decisions are the user's.** Never ask for something the repository, tools, documentation, history, or runtime evidence can answer.

## 2. Respect the active-goal lifecycle

Before creating or replacing goal state:

1. Check whether `GOAL.md`, an issue, milestone, or other active Goal Contract already exists.
2. If it is the same goal, resume or update it without creating a duplicate source of truth.
3. If it is closed, ensure its closeout packet is archived before reusing the active path.
4. If it is still active and a different target is proposed, do not overwrite it. Ask whether to continue, pause, supersede, or close the existing goal.
5. When superseding, preserve the prior contract, status, evidence, and reason for supersession.

Use the repository's existing goal-history convention when one exists. Otherwise default to:

```text
GOAL.md
GOAL_PROGRESS.md
docs/goals/INDEX.md
docs/goals/<goal-id>/
```

## 3. Classify the ambiguity

Choose one path.

### A. One target is strongly supported

Draft the Goal Contract directly. Explain the evidence in a few lines and ask for one approval before persisting it.

### B. Several materially different targets are plausible

Present at most three candidate outcomes. For each, state:

- Supporting repository evidence
- Expected value
- In-scope surface
- Main trade-off or exclusion
- Likely acceptance evidence

Recommend one. Ask the user to resolve **one decision at a time** only when alternatives lead to materially different products, scope, compatibility, or authority.

### C. The destination itself is still foggy

Do not manufacture a target to unlock autonomous work. Recommend broader wayfinding or discovery when users, promised outcome, or product direction remain undecided.

A native `/goal` is premature when no stable destination or observable verifier exists.

## 4. Resolve only material decisions

Ask only questions whose answers could materially change:

- The product outcome
- In-scope or out-of-scope boundaries
- Acceptance evidence
- Protected behavior or compatibility
- Authority or irreversible-action boundaries
- Which durable artifact is authoritative

For each question:

- Ask one decision at a time.
- Provide a recommended answer and why.
- Use concrete scenarios when wording is vague.
- Surface conflicts with existing code or documents.
- Avoid debating reversible implementation details the executing agent can safely choose later.

Use `grill-with-docs`, a domain workflow, or an ADR process when terminology and hard-to-reverse design decisions need deeper alignment. Use wayfinding when the effort is too broad to reduce to one contract. Goal shaping defines the **next executable outcome**.

## 5. Assign durable identity and paths

Create a stable Goal ID:

```text
YYYY-MM-DD-short-kebab-slug
```

An issue or milestone ID may be used when it is already the durable identity.

Record:

- Library source and skill metadata version, or the exact source commit when known
- Contract path
- Progress-state path
- Archive path
- Existing goal-history index

When no stronger repository convention exists, use:

```text
Contract: GOAL.md
Progress: GOAL_PROGRESS.md
Archive: docs/goals/<goal-id>/
Index: docs/goals/INDEX.md
```

## 6. Build the Goal Contract

Use [goal-contract-template.md](goal-contract-template.md). Keep it concise and include:

- Stable Goal ID and library version/source
- One observable outcome
- Why this target is next
- One primary execution profile
- In-scope and out-of-scope boundaries
- Acceptance evidence and exact verifiers where known
- Protected behavior and compatibility constraints
- Baseline and known exceptions
- Approval and irreversible-action boundaries
- Success, blocker, budget, and stalled-loop exits
- Authoritative sources
- Progress, archive, and reusable-output paths

A target is not ready when it is merely:

- A task list
- A proposed implementation mechanism
- An aspiration such as “improve the project”
- A full open-ended backlog
- A proxy metric that can pass while the user outcome still fails

## 7. Select one execution profile

Choose one primary profile:

- **Brownfield Continue / Finish** — default continuation toward an approved outcome
- **PRD / Spec Compliance** — close documented requirement gaps
- **Next Milestone** — deliver one bounded roadmap increment
- **Deep Audit + Remediation** — discover, prove, and repair important findings
- **QA / Regression / UAT** — make real product workflows pass
- **Safe Refactor / Modernization** — change internals while proving equivalence
- **Release Readiness** — satisfy pre-release gates
- **Incident Recovery / Stabilization** — restore health, prove root cause, prevent recurrence
- **Dependency / Framework Upgrade** — stage ecosystem upgrades safely
- **Data Migration / Integrity** — preserve and reconcile data through change
- **Branch Rescue / Integration** — recover coherent value from divergent work

Use one primary profile even when secondary techniques are useful. If two profiles imply different outcomes, split or clarify the contract instead of creating a composite mega-goal.

## 8. Apply the readiness gate

The Goal Contract is ready only when:

- It has one stable Goal ID and one outcome.
- A fresh agent can tell what is in and out of scope.
- Completion can be demonstrated by commands, workflows, measurements, or observable artifacts.
- Existing behavior and user work that must survive are named.
- No unresolved owner decision could lead to materially different implementations.
- Stop and escalation conditions are explicit.
- Success cannot be claimed solely from an agent assertion.
- The selected profile matches the target's dominant risk model.
- Progress and archive paths are unambiguous.
- A prior active goal will not be overwritten or silently lost.

## 9. Persist without creating competing state

After approval:

1. Update the existing authoritative issue, milestone, PRD, plan, or goal artifact when one exists.
2. Otherwise create or update `GOAL.md` from the template.
3. Link rather than duplicate detailed requirements.
4. Mark the contract `Approved` and record the current branch/SHA when useful.
5. Name the existing progress/handoff artifact, or designate `GOAL_PROGRESS.md`.
6. Name the existing archive/index convention, or designate `docs/goals/<goal-id>/` and `docs/goals/INDEX.md`.
7. Never overwrite a different active goal without an explicit supersession decision.

If the user requested a read-only session, return the contract and launch packet without writing.

## 10. Render the native `/goal`

Prefer the short skill-backed command:

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the execution profile named in the contract. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve a reusable closeout packet and leave a restartable handoff.
```

The contract carries project-specific truth; `goal-engine` carries reusable execution discipline; the host's native `/goal` carries persistence and evaluation.

Also provide the matching standalone command from the goal library when `goal-engine` may not be installed. Do not duplicate the whole standalone prompt into the contract.

## 11. End with a launch packet

```text
Approved target: [ONE SENTENCE]
Goal ID: [ID]
Contract: [PATH OR ISSUE]
Execution profile: [NAME]
Progress state: [PATH OR ISSUE]
Archive: [PATH]
Library: [VERSION OR COMMIT]
Run with goal-engine: [COPY-READY /goal]
Standalone fallback: [LINK OR COPY-READY /goal]
Open owner decisions: None / [SHORT LIST]
```

Do not claim execution has begun merely because the contract and command are ready. Native `/goal` activation is the boundary between shaping and autonomous implementation.
