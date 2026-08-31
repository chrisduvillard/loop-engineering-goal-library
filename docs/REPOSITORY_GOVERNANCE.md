# Repository governance

## Required branch settings

Configure the default branch to require the `Validate library` checks, reject
force pushes, require pull requests, and require review for changes to
`.github/`, `scripts/`, `skills/`, `tests/`, `VERSION`, and release controls.
`CODEOWNERS` identifies those surfaces. Solo maintainers may use an emergency
bypass only when the reason and follow-up review are recorded.

## Release policy

Release only from a reviewed version tag. The tag, `VERSION`, README, skill
metadata, changelog, ZIP filenames, checksums, and source commit must agree.
Attach all reference-closed packages and `SHA256SUMS`. Record tested host, Skills
CLI, Python, Node, and operating-system versions.

## Supply-chain policy

Pin GitHub Actions by full commit SHA, install dependencies from lockfiles, keep
workflow permissions minimal, prohibit unreviewed executable downloads, and
rerun package closure and archive integrity checks before release.

## Production readiness

The project is beta until the live host matrix in `HOST_ACCEPTANCE_MATRIX.md`
passes. A repository-green build is necessary but not sufficient evidence of
native-host behavior.
