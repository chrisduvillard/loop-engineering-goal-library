# Assurance and mutation modes

## Mutation modes

- `read_only`: inspect, execute non-mutating checks, and report. Tracked source
  changes are forbidden.
- `propose_patch`: design a patch or remediation plan without applying it to the
  repository.
- `apply_verified_fixes`: modify the repository within the approved contract and
  prove the result.

Review, audit, assess, inspect, and evaluate requests default to `read_only`.
Words such as fix, implement, repair, and remediate may select
`apply_verified_fixes`, but only when the user's authorization is explicit.

## Assurance levels

- Lite for small reversible changes.
- Standard for ordinary brownfield engineering.
- High for security, compliance, production infrastructure, destructive
  migration, high blast radius, or costly irreversible work.

Mutation mode controls what may change. Assurance level controls how much proof
and independence are required. They are orthogonal contract fields.
