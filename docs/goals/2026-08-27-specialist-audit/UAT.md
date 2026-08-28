# UAT: Specialist codebase audit

## Metadata and generated documentation

- Changing `VERSION` and running the generator updates exactly one README Version badge.
- Repository validation rejects a badge that differs from `VERSION`.
- Profile counts remain derived from the canonical catalog.

## Dependency and maintenance behavior

- A different exact `skills` pin passes validation when `package.json` and `package-lock.json` agree.
- A mismatched root pin, package entry, tarball provenance, or integrity still fails.
- Dependabot covers both GitHub Actions and npm.

## Specialist reviewer workflow

- Six roles have non-overlapping primary concerns.
- Reviewers are read-only by default and do not share conclusions before independent review.
- Findings require evidence, reproduction, impact, remediation, and a verifier.
- Important fixes receive independent re-review.

## Deterministic state and archive contracts

- Question IDs are contiguous, at most one question is Proposed, and invalid status transitions fail.
- Answered questions require one saved answer and one normalized decision.
- Closed goal directories contain the required packet and appear exactly once in `docs/goals/INDEX.md`.
- The locked Skills CLI, npm provenance, Dependabot coverage, read-only workflow, immutable Action pins, and superseded-run cancellation are verified.

## Full regression

- Python compilation and all unit tests pass.
- Launcher and generated-document checks pass.
- Shaping histories remain append-only.
- Agent Skills discovery and deterministic packaging pass.
- Pull-request and merged-main CI pass on Linux, macOS, and Windows with Python 3.9 and 3.13.
