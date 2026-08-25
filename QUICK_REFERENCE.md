# Quick Reference

## Global install

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' \
  --global \
  --agent codex \
  --agent claude-code \
  --yes
```

Verify:

```bash
npx -y skills@latest list --global --agent codex --agent claude-code
```

## The 30-second workflow

| Step | Claude Code | Codex CLI / IDE |
|---|---|---|
| Shape an unclear target | `/shape-goal Continue this project` | `$shape-goal Continue this project` |
| Execute | Use the native `/goal` command below | Use the native `/goal` command below |

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use the selected execution profile. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve a reusable closeout packet and leave a restartable handoff.
```

```text
Rough intent → shape-goal → Goal Contract → /goal + goal-engine → Evidence → Archive
```

## What is the target?

A target is not a task breakdown. It is either a verifiable outcome or a pointer to an approved Goal Contract, issue, PRD, milestone, or acceptance checklist.

```text
[Observable outcome] is true for [scope], proven by [acceptance evidence], while [protected behavior] remains intact.
```

Use `shape-goal` when the outcome, scope, evidence, protected behavior, authority, or archive path is not settled.

## Active state

Use the repository's existing authoritative artifacts when they work. Otherwise:

```text
GOAL.md
GOAL_PROGRESS.md
```

One active goal must not silently overwrite another.

## Close and preserve

At every terminal outcome, snapshot:

```text
docs/goals/<goal-id>/
├── CONTRACT.md
├── PROGRESS.md
└── RESULT.md
```

Update `docs/goals/INDEX.md`. Promote verified reusable knowledge:

| Discovery | Permanent home |
|---|---|
| Corrected failure | Regression test |
| Product or architecture decision | Approved docs or ADR |
| Operational procedure | Runbook |
| Stable workflow or benchmark | Test or repository script |
| Reusable specimen | Maintained fixture |

Never commit secrets, credentials, private data, raw production dumps, or unnecessary large logs.

## Ultra-short default

When `goal-engine` is installed and `GOAL.md` is already approved:

```text
/goal Follow goal-engine to complete GOAL.md. Stop only when every acceptance item passes with surfaced evidence, or when a contract-defined blocker, approval boundary, budget, or two-cycle stall applies; preserve a reusable closeout packet and leave a restartable handoff.
```

## Choose a profile

| Work | Profile |
|---|---|
| Continue an existing project | Brownfield Continue / Finish |
| Close a PRD or specification | PRD / Spec Compliance |
| Deliver one roadmap increment | Next Milestone |
| Discover and repair important issues | Deep Audit + Remediation |
| Exercise real product workflows | QA / Regression / UAT |
| Change internals without changing behavior | Safe Refactor / Modernization |
| Remove pre-release blockers | Release Readiness |
| Recover from a severe failure | Incident Recovery / Stabilization |
| Upgrade an ecosystem dependency | Dependency / Framework Upgrade |
| Transform schemas or stored data | Data Migration / Integrity |
| Recover work from a divergent branch | Branch Rescue / Integration |

Use one primary profile. Split or reshape the contract when profiles imply different outcomes.

## Update

```bash
npx -y skills@latest update shape-goal goal-engine --global --yes
```

## Standalone fallback

No installed skills:

- [`GOAL_LIBRARY.md`](GOAL_LIBRARY.md) — seven copy-ready skill-backed commands
- [`SPECIALIST_LOOPS.md`](SPECIALIST_LOOPS.md) — four specialist commands
- [`goals/`](goals/) — complete standalone prompts
- [`templates/universal-brownfield-goal.md`](templates/universal-brownfield-goal.md) — universal form

## Brownfield Safety Kernel

```text
Establish the actual repository state before editing; reconcile instructions, requirements, plans, code, tests, runtime behavior, prior goal archives, and Git history; protect user and unrelated work. Make small reversible production changes, verify each with repository-native checks, add regression protection, review important diffs, keep only changes that preserve or improve the baseline, and persist evidence plus the next action. Finish only on passing acceptance evidence; stop on a genuine blocker, approval boundary, budget, or repeated no-progress. Preserve a reusable closeout packet and never perform irreversible or external-system actions without explicit approval.
```
