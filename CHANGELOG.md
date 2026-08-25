# Changelog

All notable changes to this library are recorded here.

The project follows semantic versioning while it is field-tested. Versions below `1.0.0` may refine contracts and workflow details, but changes should remain documented and migration-friendly.

## [Unreleased]

- Reserved for changes after the current release.

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

- Global installation is now the recommended default for reuse across projects.
- Completed, blocked, stalled, and budget-exhausted goals now produce a reusable closeout archive.
- Skill metadata records the library source and version for reproducibility.

### Known pre-release validation

- Skill discovery and packaging are tested automatically.
- Full end-to-end field UAT in live Codex and Claude Code `/goal` sessions remains a tracked pre-`1.0.0` milestone.
