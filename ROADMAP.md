# Roadmap

The repository should add abstractions only when they remove more field friction than they create.

## Implemented in `0.4.0`

- Twenty-two zero-friction profile launchers with no required placeholder replacement.
- Two-phase bootstrap: exhaustive goal shaping and approval followed by execution inside the same native `/goal`.
- Profile-specific input definitions and a search-before-asking decision protocol.
- Dedicated frontend, documentation, security, reliability, API, observability, developer-experience, data-quality, and audit-readiness profiles.
- Machine-readable goal catalog and generated README/catalog collections.
- OpenAI skill host metadata.
- Immutable GitHub Action pins and stronger launcher validation.
- A real repository closeout packet documenting the deep review.

## Before `1.0.0`

- Run the same zero-friction launcher through a complete live Codex `/goal` session.
- Run a comparable launcher through Claude Code `/goal`, including at least one owner question during shaping.
- Verify that neither evaluator treats Goal Contract creation as completion.
- Compare skill retention, compaction, evidence visibility, pause/resume, and handoff quality.
- Field-test Frontend UI / UX / Accessibility and Documentation Synchronization profiles on real mature projects.
- Test a priority change and supersession in a multi-goal portfolio.
- Test two isolated parallel goals in separate worktrees.
- Test global install, update, reinstall, ZIP upload, and OpenAI host metadata on macOS.
- Choose an explicit repository and skill license. **Recommended:** MIT for maximum reuse with attribution.
- Create a tagged release with permanent packaged skill ZIPs and checksums.

## Evidence-gated candidates

### Deterministic `goalctl` helper

A small CLI could initialize contracts, validate input ledgers, update portfolios, switch active pointers, and archive closeouts. Add only after field use identifies repetitive deterministic steps that are safer to automate than leave to agents.

### Goal history search and portfolio summarization

Add when several real archived goals make manual navigation inconvenient.

### Project-specific profile packs

A repository or organization may need its own profiles or overlays. Prefer project skills that reference this library rather than expanding the global catalog from one local use case.

### New global profile

Add only when the same Custom Contract-Driven pattern recurs across multiple real projects and has a distinct iteration unit, verifier, failure mode, keep-or-revert decision, and stopping logic.

### Claude Code plugin and OpenAI plugin packaging

Consider namespaced plugin releases after field testing, versioning, and licensing are settled.

## Not planned

- A custom replacement for native `/goal`.
- A monolithic project goal that absorbs unrelated work.
- Hidden auto-approval of product direction, destructive actions, legal conclusions, or risk acceptance.
- A proprietary state database when repository artifacts or existing trackers are sufficient.
- Automatic deployment, release, destructive migration, security testing outside scope, or credential authority.
