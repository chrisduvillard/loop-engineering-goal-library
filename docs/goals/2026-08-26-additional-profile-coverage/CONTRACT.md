# Goal Contract: Additional profile coverage

**Goal ID:** `2026-08-26-additional-profile-coverage`
**Revision:** 1
**State:** Approved
**Profile:** PRD / Spec Compliance
**Shaping history:** `SHAPING.md`
**Approval shaping round:** R1

## Outcome

Review the complete profile taxonomy and add only reusable Goal profiles whose iteration, verifier, failure mode, and stopping logic are materially distinct from the existing catalog.

## In scope

- Profile-gap review
- Five new profile guides
- `shape-goal` input specifications
- `goal-engine` execution rules
- Routing distinctions
- Catalog, generated docs, README, quick reference, versioning, sources, validation, and packages

## Out of scope

- Technology-specific profiles
- Duplicate combinations of existing profiles and overlays
- Licensing, publishing a release, deployment, or external-system changes

## Acceptance evidence

- 29 catalog entries with sequential IDs and valid categories
- Each new profile exposes interactive-first commands plus two safe advanced preflights
- Every advanced `/goal` remains within 4,000 characters
- Profile inputs and execution rules exist for all five additions
- Generated collections and README remain synchronized
- Repository validation, append-only history tests, Agent Skills discovery, and deterministic packaging pass
- Pull-request and final `main` CI pass

## Protected behavior

- `shape-goal` remains the main interactive entry point
- The one-question turn barrier remains intact
- `goal-engine` never interviews the user during autonomous execution
- Existing 24 profile links, IDs, contracts, overlays, archives, and packaging remain compatible
