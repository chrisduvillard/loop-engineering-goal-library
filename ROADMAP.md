# Roadmap

Add abstractions only when they remove more field friction than they create.

## Implemented through `0.10.0`

- `shape-goal` as the main interactive entry point.
- A strict question barrier: save one question, ask it, and return control immediately.
- Adaptive question depth with no fixed quota, an answer-quality gate, a risk-weighted assumption register, and a pre-approval clarity stress test.
- Separate interactive shaping and autonomous `/goal` execution.
- Thirty-one profiles with host-specific `shape-goal` start commands.
- Dedicated loops for AI/LLM evaluation, legacy retirement, internationalization/localization, backup and disaster recovery, trustworthy product analytics/experimentation, codebase onboarding, and search/SEO/web discoverability.
- Advanced autonomous preflights that stop as Approval required instead of interviewing inside `/goal`.
- Append-only shaping history, repeatable deeper rounds, explicit approval records, and information-classification rules.
- `goal-engine` brownfield execution with native verification, regression protection, drift detection, reusable closeout, and authority boundaries.
- Multi-goal portfolio, Project Harness, assurance overlays, generated catalogs, validation, and deterministic packaging.

## Before `1.0.0`

- Run the interactive-first flow through a complete live Codex session:
  1. invoke `$shape-goal`
  2. answer at least two questions without Steer
  3. approve the contract
  4. start the generated `/goal`
  5. complete and archive the result
- Run the comparable flow through Claude Code.
- Field-test adaptive questioning with a two-question low-risk goal and a many-question high-risk goal; verify that ambiguous answers trigger clarification rather than inference.
- Field-test the fresh-reader, counterexample, scenario, and plain-English teach-back gates with a subjective UI goal and an irreversible migration goal.
- Verify active-goal rescue from a deliberately misused autonomous preflight.
- Compare skill retention, compaction, evidence visibility, pause/resume, and handoff quality.
- Field-test Frontend UI / UX / Accessibility and Documentation Synchronization on mature projects.
- Field-test the seven `0.7.0`–`0.8.0` profiles on representative projects and promote no additional global profile without repeated evidence.
- Test a priority change and supersession in a multi-goal portfolio.
- Test two isolated parallel goals in separate worktrees.
- Test global install, update, reinstall, ZIP upload, and host metadata on macOS.
- Choose an explicit repository and skill license. **Recommended:** MIT.
- Create a tagged release with permanent packaged skill ZIPs and checksums.

## Evidence-gated candidates

### Deterministic `goalctl` helper

A small CLI could initialize contracts, validate input ledgers, update portfolios, switch active pointers, and archive closeouts. Add it only when field use identifies repetitive deterministic steps that are safer to automate than leave to agents.

### Goal history search and portfolio summary

Add when several real archived goals make manual navigation inconvenient.

### Project-specific profile packs

Prefer project or organization skills that reference this library rather than expanding the global catalog from one local use case.

### New global profile

Add only when the same Custom Contract-Driven pattern recurs across multiple real projects and has a distinct iteration unit, verifier, failure mode, keep-or-revert decision, and stopping logic.

### Plugin packaging

Consider namespaced Claude Code and OpenAI plugin releases after field testing, versioning, and licensing are settled.

## Not planned

- A custom replacement for native `/goal`.
- Interactive interviews inside an autonomous `/goal` loop.
- A monolithic project goal that absorbs unrelated work.
- Hidden auto-approval of product direction, destructive actions, legal conclusions, or risk acceptance.
- A proprietary state database when repository artifacts or existing trackers are sufficient.
- Automatic deployment, release, destructive migration, security testing outside scope, or credential authority.
