# Changelog

All notable changes to this library are recorded here.

The project follows semantic versioning while it is field-tested. Versions below `1.0.0` may refine contracts and workflow details, but changes should remain documented and migration-friendly.

## [Unreleased]

- Reserved for changes after the current release.

## [0.3.0] - 2026-08-25

### Added

- A complete README walkthrough from installation and goal shaping through native `/goal` execution, changing priorities, closeout, and reuse.
- A plain-English README guide covering every standalone goal and when to use it.
- **Measured Optimization / Benchmark** for fixed-protocol champion-versus-challenger improvement loops.
- **Technical Spike / Feasibility** for bounded technical investigation and Go / Conditional Go / No-Go decisions.

### Changed

- The library now contains seven core and six specialist standalone goals, for thirteen presets total.
- `shape-goal`, Goal Contract templates, quick reference, architecture, and validation now recognize all thirteen presets.
- The specialist library now includes optimization and feasibility profiles.
- The worked example's follow-on performance goal now uses the dedicated optimization profile.

## [0.2.0] - 2026-08-25

### Added

- Goal Portfolio support for candidate, ready, active, paused, blocked, and closed goals.
- Explicit lifecycle transitions: clarify, amend, reprioritize, pause, resume, supersede, split, merge, cancel, and close.
- Parent, dependency, priority, revision, and supersession relationships in Goal Contracts.
- Assurance overlays for security/privacy, reliability/recovery, performance/cost, UX/accessibility, data governance, compatibility, operability, documentation, and compliance.
- A `Custom Contract-Driven` fallback when none of the eleven presets fits.
- A packaged standalone custom `/goal` fallback for environments without installed skills.
- A reusable project-harness template for setup, run, reset, realistic workflow, and repository-native verification knowledge.
- A completed example portfolio showing one achieved goal and a different ready goal that follows it.

### Changed

- The eleven standalone goals are described as high-value control-loop presets rather than an exhaustive list of project types.
- `shape-goal` manages changing priorities and multiple goals without silently overwriting the active contract.
- `goal-engine` performs a goal-fit gate at checkpoints and pauses for reshaping when the user's need materially changes.
- One native `/goal` session or worktree is explicitly bound to one dependency-safe leaf contract; parallel goals require isolation and coordination.
- Progress, result, history, README, architecture, and quick-reference artifacts record profiles, overlays, portfolio state, harness reuse, and related goals.

## [0.1.0] - 2026-08-25

### Added

- Two portable Agent Skills: `shape-goal` and `goal-engine`.
- Seven core and four specialist execution profiles.
- Standalone `/goal` commands for environments without installed skills.
- Goal Contract, progress-state, closeout, and goal-history templates.
- Durable goal archival under `docs/goals/<goal-id>/`.
- Installation, update, packaging, and completed-cycle documentation.
- Deterministic ZIP packaging for reuse in Agent Skills hosts and ChatGPT uploads.
- Repository validation, Agent Skills CLI discovery checks, and packaged-artifact CI.

### Changed

- Global installation is the recommended default for reuse across projects.
- Completed, blocked, stalled, and budget-exhausted goals produce a reusable closeout archive.
- Skill metadata records the library source and version for reproducibility.

### Known pre-release validation

- Skill discovery and packaging are tested automatically.
- Full end-to-end field UAT in live Codex and Claude Code `/goal` sessions remains a tracked pre-`1.0.0` milestone.
