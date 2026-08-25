<div align="center">

# Loop Engineering `/goal` Library

### Reusable autonomous coding loops for mature, brownfield repositories

**Portable across OpenAI Codex and Anthropic Claude Code**

</div>

---

This repository contains a compact, evidence-driven toolkit for long-running AI coding-agent work. It is optimized for existing codebases where the agent must understand the real repository state, reconcile stale plans and documentation, preserve existing behavior, make reversible production changes, verify results with native checks, and continue autonomously until a measurable target is reached.

Research was checked against current sources on **August 25, 2026**.

## Core operating model

```text
Orient → Reconcile → Select → Change → Verify → Review → Record → Repeat
```

The loop optimizes for the **verified repository state**, not for the amount of code produced or the number of tasks marked complete.

## Golden set

| Loop | Use it for |
|---|---|
| [Brownfield Continue / Finish](goals/01-brownfield-continue-finish.md) | Safely continue an existing project until a defined target is complete |
| [PRD / Spec Compliance](goals/02-prd-spec-compliance.md) | Reconcile implementation with documented requirements and close every verified gap |
| [Next Milestone](goals/03-next-milestone.md) | Deliver the next coherent dependency-safe milestone without scope sprawl |
| [Deep Audit + Remediation](goals/04-deep-audit-remediation.md) | Discover, verify, prioritize, and repair important defects or risks |
| [QA / Regression / UAT](goals/05-qa-regression-uat.md) | Exercise the actual product and realistic workflows until acceptance gates pass |
| [Safe Refactor / Modernization](goals/06-safe-refactor-modernization.md) | Improve internals while proving behavioral equivalence and retaining rollback paths |
| [Release Readiness](goals/07-release-readiness.md) | Remove release blockers without performing the release itself |

## Start here

For most established repositories, use the [Best Universal Brownfield Goal](templates/universal-brownfield-goal.md):

```text
/goal Bring this existing project to [TARGET]...
```

When the repository already has reliable instructions, plans, progress files, and native checks, use the [Ultra-Short Default Goal](templates/ultra-short-default-goal.md).

## Repository contents

```text
.
├── README.md
├── FULL_REPORT.md
├── GOAL_LIBRARY.md
├── QUICK_REFERENCE.md
├── SOURCES.md
├── goals/
│   ├── 01-brownfield-continue-finish.md
│   ├── 02-prd-spec-compliance.md
│   ├── 03-next-milestone.md
│   ├── 04-deep-audit-remediation.md
│   ├── 05-qa-regression-uat.md
│   ├── 06-safe-refactor-modernization.md
│   └── 07-release-readiness.md
└── templates/
    ├── universal-brownfield-goal.md
    ├── ultra-short-default-goal.md
    └── brownfield-safety-kernel.md
```

- [`FULL_REPORT.md`](FULL_REPORT.md) contains the complete research report and recommendations.
- [`GOAL_LIBRARY.md`](GOAL_LIBRARY.md) keeps all seven core loops in one copy-ready file.
- [`QUICK_REFERENCE.md`](QUICK_REFERENCE.md) contains the golden set, universal goal, ultra-short goal, safety kernel, specialization guidance, and vague-task conversion checklist.
- [`SOURCES.md`](SOURCES.md) lists the primary authoritative and practitioner sources.

## Design principles

Every loop is designed to:

- Establish the repository's actual state before changing anything.
- Reconcile documentation, plans, code, tests, runtime behavior, and Git history.
- Protect user work, local modifications, unrelated code, and existing behavior.
- Prefer small, coherent, reversible production changes.
- Discover and use repository-native verification commands.
- Verify findings before fixing them and add regression protection afterward.
- Surface acceptance evidence before claiming completion.
- Persist useful progress and handoff state between iterations.
- Detect circular work, exhausted budgets, and no-progress cycles.
- Stop at human approval and irreversible-action boundaries.

## Codex and Claude Code portability

The goals deliberately avoid relying on vendor-specific controls, model names, test frameworks, package managers, or subagent commands. They describe the repository operation and evidence contract in ordinary language, allowing each tool to execute it with its own native goal machinery.

`/goal` is best for **condition-driven autonomous work**. Time-driven polling, such as repeatedly checking CI or an external job, should use the platform's recurring or scheduled-loop mechanism instead.

## Specialized work

Bug fixing, security, reliability, performance, UI/UX, technical debt, and documentation synchronization usually do not need separate permanent loops. Start with one of the seven core patterns and specialize its scope, verifier, severity bar, benchmark, risk matrix, or acceptance rubric.

## License

No license has been added. Public visibility alone does not grant reuse rights; choose and add a license deliberately if you want others to modify or redistribute the material.
