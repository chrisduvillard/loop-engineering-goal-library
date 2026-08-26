# Changelog

All notable changes to this library are recorded here.

The project follows semantic versioning while it is field-tested. Versions below `1.0.0` may refine contracts and workflow details, but changes should remain documented and migration-friendly.

## [Unreleased]

- Reserved for changes after the current release.

## [0.4.0] - 2026-08-25

### Added

- Zero-friction two-phase launchers for every goal: `shape-goal` resolves and approves missing inputs, then `goal-engine` executes the approved contract.
- A profile-specific input specification covering every goal and an exhaustive-but-bounded search-and-question protocol.
- Durable append-only shaping histories under `docs/goals/<goal-id>/SHAPING.md`.
- Stable shaping round and question identifiers, saved recommendations and answers, correction/supersession records, deferred-decision tracking, and approval-round linkage.
- Repeatable deepening rounds for users who want to challenge or refine a proposed Goal Contract without losing earlier answers.
- A shaping-history protocol, reusable template, and worked two-round example.
- Nine dedicated product and quality profiles:
  - Frontend UI / UX / Accessibility
  - Documentation Synchronization / Knowledge Transfer
  - Security / Privacy Hardening
  - Reliability / Resilience Hardening
  - API / Integration Contract Compatibility
  - Observability / Operability
  - Developer Experience / Tooling
  - Data Quality / Pipeline Assurance
  - Compliance / Audit Readiness
- A machine-readable `goals/catalog.json` and generated `goals/README.md`.
- `QUALITY_GOALS.md` for the product and quality profiles.
- OpenAI host metadata for both skills.
- A real closeout packet for this repository's final deep review.

### Changed

- All 22 recommended `/goal` commands run unchanged and contain no repository-specific placeholders.
- Every goal also has a self-contained no-placeholder fallback.
- `shape-goal` supports bootstrap mode inside an already-active native `/goal`, keeps an input ledger, searches before asking, saves every asked question and answer, supports repeated deeper rounds, and hands off without claiming completion.
- `goal-engine` reads the shaping decision trail, avoids reopening settled decisions without new evidence, and preserves `SHAPING.md` at pause and closeout.
- Goal Contracts record shaping-history path, completed rounds, last round, and approval round.
- Progress, result, history, README, quick reference, architecture, and state templates link the durable shaping record.
- Sensitive shaping answers are redacted and linked to approved secure evidence rather than committed verbatim.
- The README, catalog, generated libraries, and contribution guidance reflect the zero-friction workflow.
- CI validates launcher invariants, profile input coverage, shaping-history schemas, generated catalogs, host metadata, and immutable GitHub Action pins.
- GitHub Actions are pinned to full commit SHAs.
- A temporary write-enabled workflow used to assemble the review branch was removed before merge.

## [0.3.0] - 2026-08-25

### Added

- A complete README walkthrough from installation and goal shaping through native `/goal` execution, changing priorities, closeout, and reuse.
- A plain-English README guide covering every standalone goal and when to use it.
- **Measured Optimization / Benchmark** for fixed-protocol champion-versus-challenger improvement loops.
- **Technical Spike / Feasibility** for bounded technical investigation and Go / Conditional Go / No-Go decisions.

### Changed

- The library contains seven core and six specialist standalone goals, for thirteen presets total.
- `shape-goal`, Goal Contract templates, quick reference, architecture, and validation recognize all thirteen presets.
- The specialist library includes optimization and feasibility profiles.
- The worked example's follow-on performance goal uses the dedicated optimization profile.

## [0.2.0] - 2026-08-25

### Added

- Goal Portfolio support for candidate, ready, active, paused, blocked, and closed goals.
- Explicit lifecycle transitions: clarify, amend, reprioritize, pause, resume, supersede, split, merge, cancel, and close.
- Parent, dependency, priority, revision, and supersession relationships in Goal Contracts.
- Assurance overlays for security/privacy, reliability/recovery, performance/cost, UX/accessibility, data governance, compatibility, operability, documentation, and compliance.
- A `Custom Contract-Driven` fallback.
- A packaged standalone custom `/goal` fallback.
- A reusable project-harness template.
- A completed example portfolio.

### Changed

- The standalone goals are high-value control-loop presets rather than an exhaustive list of project types.
- `shape-goal` manages changing priorities and multiple goals without silently overwriting the active contract.
- `goal-engine` performs a goal-fit gate at checkpoints and pauses for reshaping when the user's need materially changes.
- One native `/goal` session or worktree is bound to one dependency-safe leaf contract.

## [0.1.0] - 2026-08-25

### Added

- Two portable Agent Skills: `shape-goal` and `goal-engine`.
- Seven core and four specialist execution profiles.
- Standalone `/goal` commands for environments without installed skills.
- Goal Contract, progress-state, closeout, and goal-history templates.
- Durable goal archival under `docs/goals/<goal-id>/`.
- Installation, update, packaging, and completed-cycle documentation.
- Deterministic ZIP packaging.
- Repository validation, Agent Skills CLI discovery checks, and packaged-artifact CI.

### Known pre-release validation

- Skill discovery and packaging are tested automatically.
- Full end-to-end field UAT in live Codex and Claude Code `/goal` sessions remains a tracked pre-`1.0.0` milestone.
