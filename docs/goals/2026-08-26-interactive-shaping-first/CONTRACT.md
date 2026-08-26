# Goal Contract: Interactive shaping first

**Goal ID:** `2026-08-26-interactive-shaping-first`  
**Revision:** 1  
**State:** Active  
**Priority:** P0  
**Library version:** `0.6.0`  
**Shaping history:** `SHAPING.md`  
**Completed shaping rounds:** R1  
**Approval shaping round:** R1  
**Execution profile:** PRD / Spec Compliance  
**Assurance overlays:** Documentation & Knowledge Transfer; Compatibility & Portability  
**Progress:** `PROGRESS.md`  
**Result:** `RESULT.md`

## Outcome

The library uses `shape-goal` as the clear interactive entry point, lets users answer shaping questions through ordinary replies without **Steer**, starts native `/goal` only after explicit approval, and explains this workflow through a short, polished, plain-English README.

## Why this is next

Live use exposed a mismatch between autonomous `/goal` continuation and human-in-the-loop questioning. The current workflow can continue working after it asks a question, forcing the user to steer an answer into an active goal.

## In scope

- Review the complete repository architecture, skills, launchers, generated documentation, validation, CI, packaging, and installation guidance.
- Make `shape-goal` the primary command and enforce a one-question-per-turn barrier.
- Prevent `goal-engine` and advanced preflights from interviewing the user inside active `/goal` execution.
- Update all 24 profile files to recommend interactive shaping first.
- Keep autonomous and self-contained preflights as clearly labelled advanced fallbacks.
- Dogfood the shaping, contract, progress, evidence, and closeout lifecycle on this repository.
- Replace the README with a concise, visually polished, plain-English guide.
- Validate, review, merge to `main`, and remove temporary branches and workflows.

## Out of scope

- Replacing native `/goal` implementations.
- Automatic pausing or clearing of a host goal when the host provides no portable programmatic control.
- Production deployment, release publication, tags, or license selection.
- Claiming full host-level UAT in Codex and Claude Code without running those external clients end to end.

## Acceptance evidence

1. `shape-goal` explicitly says to run outside active `/goal`, ask one material question, save it, end the turn immediately, and wait for the user's normal reply.
2. `goal-engine` explicitly forbids material owner questions during autonomous execution and stops as **Approval required** on goal drift.
3. All 24 profile files expose interactive `shape-goal` commands first; their advanced `/goal` preflights stop instead of asking when an owner decision is missing.
4. The README makes `shape-goal` the main command within the opening section, explains the no-Steer workflow, and keeps the profile catalog compact and collapsible.
5. Repository validation, launcher synchronization, generated-document synchronization, append-only history tests, Agent Skills discovery, packaging, and Markdown-link checks pass in CI.
6. This repository contains an honest dogfood shaping record, contract, progress log, UAT record, and closeout result for this change.
7. The reviewed pull request is merged to `main`; only `main` remains; temporary workflows are absent.

## Protected behavior

- Existing 24 execution profiles, profile names, categories, and advanced fallbacks remain available.
- Questions, answers, corrections, approvals, contracts, progress, and closeout evidence remain durable and append-only.
- Brownfield safety, repository-native verification, regression protection, authority boundaries, multi-goal lifecycle, overlays, harness reuse, and packaging remain intact.
- No confidential user or business information is added to this public repository.

## Authority boundaries

Authorized: repository documentation, skills, scripts, validators, examples, CI, branch, pull request, merge, and post-merge branch cleanup for this project.

Not authorized: tags, releases, deployments, production mutation, credentials, billing, destructive data operations, or license selection.

## Stop and escalation conditions

Stop as Blocked or Approval required if a material product decision remains unresolved, a required GitHub permission is unavailable, or validation cannot be completed. Stop as Stalled after two materially unchanged failed approaches. Do not claim achieved until the merge, final `main` validation, and branch cleanup are verified.
