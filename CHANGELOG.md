# Changelog

All notable changes to this library are recorded here.

The project follows semantic versioning while it is field-tested. Versions below `1.0.0` may refine contracts and workflow details, but changes should remain documented and migration-friendly.

## [Unreleased]

- Reserved for changes after the current release.

## [0.10.0] - 2026-08-26

### Added

- A cross-platform adversarial and mutation test suite covering destructive paths, symlinks, case/Unicode archive collisions, malformed catalogs, Markdown corruption, shaping-history attacks, workflow injection, NUL text, and fail-closed CLI behavior.
- `docs/ROBUSTNESS_AUDIT.md`, mapping pre-mortem, first principles, inversion, red-team/blue-team, Socratic, constraint-removal, stakeholder, and analogical reasoning to executable controls.
- A lockfile-pinned Skills CLI development dependency and CI test matrix for Python 3.9 and 3.13 on Linux, macOS, and Windows.

### Changed

- Packaging now validates semantic versions, refuses dangerous or non-generated output directories, rejects symlinks and special files, prevents case/Unicode extraction collisions, validates ZIP manifests and modes, and publishes atomically.
- Goal generators now validate catalog schema and safe paths, require exactly two advanced commands, reject Markdown injection, replace generated sections literally, and write atomically.
- Shaping-history validation now checks new files even without a base ref, ignores fenced-code decoys, rejects duplicate/out-of-order/reordered IDs and approval rows, and retains allowed status/supersession updates.
- Repository validation now rejects symlinks, NUL text, unexpected workflows, malformed catalog crashes, and missing adversarial tests.
- Both skills now treat repository/external content as untrusted evidence, resist prompt injection, validate state paths, and stop on stale contract state or an ambiguous execution interpretation.

## [0.9.0] - 2026-08-26

### Added

- Adaptive shaping depth: question count is determined by material ambiguity and risk rather than a fixed minimum or maximum.
- A universal clarity matrix covering outcome, users and journey, scope, evidence, protected behavior, failure cases, data/compatibility, quality obligations, authority, ownership, and profile-specific inputs.
- An answer-quality gate that classifies replies as Clear, Clear with conditions, Partial, Ambiguous, Conflicting, or Deferred / Blocked.
- A risk-weighted assumption register and explicit prohibition on hidden High-/Medium-impact assumptions at approval.
- Requirement-strength preservation for Must, Should, Preference, Optional, and Explicit non-goal statements.
- Bounded delegated judgment: “you decide” records criteria, limits, selection, and rationale instead of becoming blank authority.
- A clarity stress test with fresh-reader, counterexample, scenario, verifier, contradiction, traceability, and plain-English teach-back checks.
- A `Stress-test the current goal` command for users who want another challenge pass without losing prior questions or answers.
- Durable dogfood records under `docs/goals/2026-08-26-adaptive-question-clarity/`.

### Changed

- `shape-goal` now asks as few or as many atomic, non-duplicate questions as needed to produce one shared executable interpretation.
- Partial, ambiguous, conditional, or conflicting answers are clarified rather than silently normalized into agent assumptions.
- Goal Contracts and shaping histories now record shaping depth, materiality, confidence, assumption class, answer quality, interpretation confirmation, and clarity-review evidence.
- `goal-engine` stops as Approval required when approved contract wording later admits multiple material interpretations.
- README, quick reference, architecture, current implementation, roadmap, host metadata, validation, and packaged skills now describe and enforce the stronger clarity model.

## [0.8.0] - 2026-08-26

### Added

- **Codebase Onboarding / Knowledge Recovery** for verified architecture tracing, clean-state setup, maintainer readiness, Project Harness creation, and durable knowledge recovery.
- **Search / SEO / Web Discoverability** for rendered crawling, canonicalization, robots and sitemaps, metadata, structured data, internal links, locale signals, performance, and accessibility without unsupported ranking claims.
- **AI Quality & Safety**, **Internationalization & Localization**, and **Search & Discoverability** assurance overlays.
- A prominent README command for updating both installed skills to the latest repository version.

### Changed

- The catalog now contains 31 profiles: 7 core, 9 specialist, and 15 product/quality profiles.
- The README uses color-coded workflow badges, emoji section markers, callouts, code blocks, tables, and collapsed catalogs while remaining short and plain.
- Installation guidance documents restart and safe reinstall behavior after updates.
- Validation covers the expanded catalog, 12 overlay names, README update path, and this repository's final review record.

## [0.7.0] - 2026-08-26

### Added

- **AI / LLM Evaluation & Improvement** for versioned representative evals, stochastic repetition, error taxonomies, graders, leakage controls, and quality/safety/latency/cost trade-offs.
- **Deprecation / Legacy Sunset** for consumer discovery, migration tooling, adoption evidence, compatibility windows, staged removal, and rollback.
- **Internationalization / Localization Readiness** for locale matrices, local formats, pseudo-localization, RTL, text expansion, accessibility, and qualified linguistic review.
- **Backup / Restore / Disaster Recovery** for backup integrity, clean-room restoration, reconciliation, recovery-objective measurement, and realistic drills.
- **Product Analytics / Experimentation Integrity** for event contracts, identity and consent, lineage, experiment assignment, exposure, sample-ratio checks, and reproducible interpretation.
- Routing distinctions that prevent the new profiles from replacing existing profiles or overlays when their verifier is only secondary.
- A durable profile-gap review record under `docs/goals/2026-08-26-additional-profile-coverage/`.

### Changed

- The catalog now contains 29 profiles: 7 core, 8 specialist, and 14 product/quality profiles.
- README catalogs, generated collections, quick reference, current implementation, roadmap, validator, and packaged skill metadata now reflect version `0.7.0`.

## [0.6.0] - 2026-08-26

### Changed

- `shape-goal` is now the explicit main entry point and runs interactively outside native `/goal`.
- Shaping and autonomous execution are separate phases: the user answers questions normally, approves the Goal Contract, and then starts the generated `/goal` command.
- `shape-goal` now enforces a question barrier: save one question, ask it, and end the turn immediately with no further tools or background work.
- `goal-engine` never interviews the user while autonomous execution is active. Material drift stops as Approval required and returns to interactive shaping.
- Every profile file now begins with host-specific `shape-goal` commands and demotes combined `/goal` launchers to advanced autonomous preflights.
- Advanced preflights stop at the first unresolved owner decision rather than asking and continuing inside `/goal`.
- README and generated profile collections are shorter, clearer, and centered on the interactive-first workflow.

### Added

- Active-goal rescue instructions for Codex and Claude Code.
- Validation for interactive start commands, question-stop behavior, and advanced preflight boundaries.

### Compatibility

Existing approved Goal Contracts remain valid. Users who previously started shaping through a combined `/goal` should pause or clear that goal, resume with `shape-goal`, approve the contract, and then start a new execution `/goal`.

## [0.5.0] - 2026-08-26

### Added

- **Test Suite / CI Health** for flakiness, hidden skips, false confidence, isolation, runtime, diagnostics, and local/CI parity.
- **Infrastructure / Deployment Readiness** for infrastructure-as-code, environment parity, artifacts, deployment stages, health checks, observability, and rollback without unauthorized production mutation.
- Shared launcher synchronization with a portable 4,000-character native-goal limit.
- Append-only shaping-history diff validation across pull requests and direct pushes.
- Repository-visibility and information-classification rules for confidential shaping answers.
- Current Node/Python prerequisites and host-specific discovery troubleshooting.

### Changed

- All self-contained fallbacks now preserve `SHAPING.md`, exact safe questions and answers, recommendations, normalized decisions, corrections, and repeatable deeper rounds.
- Compaction-critical safety and handoff invariants now appear near the top of both skills.
- `shape-goal` renders the actual persisted contract reference instead of always assuming `GOAL.md`.
- The shaping template now includes Blocked state and a durable approval-question record.
- The historical research report is clearly separated from the live implementation.
- The library now contains 24 zero-friction goal profiles: 7 core, 6 specialist, and 11 product/quality profiles.

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
