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

## Full regression

- Python compilation and all unit tests pass.
- Launcher and generated-document checks pass.
- Shaping histories remain append-only.
- Agent Skills discovery and deterministic packaging pass.
- Pull-request and merged-main CI pass on Linux, macOS, and Windows with Python 3.9 and 3.13.
