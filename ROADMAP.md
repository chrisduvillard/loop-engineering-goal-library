# Roadmap

The repository should add abstractions only when they remove more field friction than they create.

## Implemented in `0.2.0`

- Multiple-goal portfolio and priority/dependency tracking.
- Explicit goal transitions and contract revisions.
- One-contract-per-session/worktree isolation rules.
- Assurance overlays instead of dozens of domain-specific profiles.
- Custom Contract-Driven fallback.
- Reusable project harness.
- Goal-fit checks during execution.

## Before `1.0.0`

- Run a complete multi-goal brownfield portfolio through live Codex `/goal` sessions.
- Run comparable goals and a priority change through live Claude Code `/goal` sessions.
- Compare evaluator behavior, compaction, skill retention, evidence visibility, pause/resume, and supersession quality.
- Test two isolated parallel goals in separate worktrees without shared-state collisions.
- Test global install, update, reinstall, and ZIP upload paths on macOS.
- Choose an explicit repository and skill license. **Recommended:** MIT for maximum reuse with attribution.
- Create a tagged release with permanent packaged skill ZIPs and checksums.

## Evidence-gated candidates

### `goalctl` automation

A small CLI could initialize contracts, validate frontmatter, update portfolios, switch active pointers, and archive closeouts. Add only after live use identifies repetitive deterministic steps that are safer to automate than leave to agents.

### Goal-history search and portfolio summarization

Add when several real archived goals make manual navigation inconvenient.

### Project-harness generator

The current skills can create or refresh the harness. A dedicated generator is justified only if setup/run discovery repeatedly consumes substantial effort across projects.

### New execution preset

Add only when the same Custom Contract-Driven pattern recurs across multiple real projects and has a distinct verifier, failure mode, and stopping logic. Do not add profiles merely for technologies or quality attributes already handled by overlays.

### Claude Code plugin packaging

Consider a namespaced plugin release after the standalone Agent Skills workflow is field-tested and versioning/licensing are settled.

## Not planned

- A custom replacement for native `/goal`.
- One monolithic project goal that absorbs unrelated work.
- A proprietary state database when repository artifacts or existing trackers are sufficient.
- Automatic deployment, release, destructive migration, or credential authority.
