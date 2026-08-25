---
name: shape-goal
description: Turn a vague project request, continuation request, issue, PRD, or milestone into an evidence-backed Goal Contract, select the right execution profile, and produce a copy-ready native /goal command backed by the goal-engine skill. Use before /goal when the target, scope, acceptance evidence, protected behavior, or best loop is unclear.
---

# Shape Goal

Compile rough intent into a safe execution contract. **Shape the work; do not implement production changes.**

A useful target has this form:

> **[Observable outcome]** is true for **[scope]**, proven by **[acceptance evidence]**, while **[protected behavior]** remains intact.

This skill and `goal-engine` have different jobs:

```text
shape-goal  → decide and persist what done means
goal-engine → execute that approved contract safely
native /goal → keep the execution alive and evaluate its finish condition
```

## Invocation

- **Claude Code:** `/shape-goal Continue this project`
- **Codex CLI or IDE:** `$shape-goal Continue this project`
- **Other Agent Skills hosts:** explicitly select or mention the `shape-goal` skill

## Required outputs

Produce all five:

1. One approved **Goal Contract**.
2. One selected **execution profile** from the loop library.
3. One short, skill-backed native `/goal` command.
4. One standalone `/goal` fallback when the user may not have `goal-engine` installed.
5. The path or issue where the contract was persisted.

## 1. Orient before asking

Read the applicable repository evidence first:

- Agent and repository instructions
- Specifications, PRDs, architecture docs, ADRs, and domain vocabulary
- Approved plans, milestones, issues, progress files, and handoffs
- Native scripts, tests, CI, release gates, and runtime entry points
- Git status, diff, branch, and relevant history

Establish the actual current state and reconcile contradictions by explicit authority, recency, and executable evidence. Protect uncommitted and unrelated work.

**Facts are the agent's job; decisions are the user's.** Never ask for something the repository, tools, documentation, or runtime evidence can answer.

## 2. Classify the ambiguity

Choose one path:

### A. One target is strongly supported

Draft the Goal Contract directly. Explain the evidence in a few lines and ask for one approval before persisting it.

### B. Several materially different targets are plausible

Present at most three candidate outcomes. For each, state:

- Supporting repository evidence
- Expected value
- In-scope surface
- Main trade-off or exclusion
- Likely acceptance evidence

Recommend one. Ask the user to resolve **one decision at a time** only when the alternatives lead to materially different products, scope, compatibility, or authority.

### C. The destination itself is still foggy

Do not manufacture a target to unlock autonomous work. Recommend a broader wayfinding or discovery session first when users, promised outcome, or product direction remain undecided.

A native `/goal` is premature when no stable destination or observable verifier exists.

## 3. Resolve only material decisions

Ask only questions whose answers could materially change:

- The product outcome
- In-scope or out-of-scope boundaries
- Acceptance evidence
- Protected behavior or compatibility
- Authority or irreversible-action boundaries

For each question:

- Ask one decision at a time.
- Provide a recommended answer and why.
- Use concrete scenarios when wording is vague.
- Surface conflicts with existing code or documents.
- Avoid debating reversible implementation details the executing agent can safely choose later.

Use `grill-with-docs`, the repository's domain workflow, or ADR process when terminology and hard-to-reverse design decisions need deeper alignment. Use wayfinding when the effort is too large or foggy to reduce to one contract. Goal shaping is narrower: it defines the **next executable outcome**.

## 4. Build the Goal Contract

Use [goal-contract-template.md](goal-contract-template.md). Keep it concise and include:

- One observable outcome
- Why this target is next
- One primary execution profile
- In-scope and out-of-scope boundaries
- Acceptance evidence and exact verifiers where known
- Protected behavior and compatibility constraints
- Baseline and known exceptions
- Approval and irreversible-action boundaries
- Success, blocker, budget, and stalled-loop exits
- Authoritative sources and the durable progress-state location

A target is not ready when it is merely:

- A task list
- A proposed implementation mechanism
- An aspiration such as “improve the project”
- A full open-ended backlog
- A proxy metric that can pass while the real user outcome still fails

## 5. Select the execution profile

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

## 6. Apply the readiness gate

The Goal Contract is ready only when:

- It names one outcome rather than unrelated work.
- A fresh agent can tell what is in and out of scope.
- Completion can be demonstrated by commands, workflows, measurements, or observable artifacts.
- Existing behavior and user work that must survive are named.
- No unresolved owner decision could lead to materially different implementations.
- Stop and escalation conditions are explicit.
- Success cannot be claimed solely from an agent assertion.
- The selected profile matches the target's dominant risk model.

## 7. Persist without creating competing state

After approval:

1. Update the existing authoritative issue, milestone, PRD, plan, or goal artifact when one exists.
2. Otherwise create `GOAL.md` at the repository root from the template.
3. Link rather than duplicate detailed requirements.
4. Mark the contract `Approved` and record the current branch/SHA when useful.
5. Name the existing progress/handoff artifact, or designate `GOAL_PROGRESS.md` when none exists.

If the user requested a read-only session, return the contract in the conversation without writing.

## 8. Render the native `/goal`

Prefer the short skill-backed command:

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the execution profile named in the contract. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; leave a restartable handoff.
```

This command is intentionally small. The contract carries project-specific truth; `goal-engine` carries reusable execution discipline; the host's native `/goal` carries persistence and evaluation.

Also provide the matching standalone command from the repository's goal library when `goal-engine` may not be installed. Do not duplicate the entire standalone prompt into the Goal Contract.

## 9. End with a launch packet

```text
Approved target: [ONE SENTENCE]
Contract: [PATH OR ISSUE]
Execution profile: [NAME]
Progress state: [PATH OR ISSUE]
Run with goal-engine: [COPY-READY /goal]
Standalone fallback: [LINK OR COPY-READY /goal]
Open owner decisions: None / [SHORT LIST]
```

Do not claim execution has begun merely because the contract and command are ready. Native `/goal` activation is the boundary between shaping and autonomous implementation.
