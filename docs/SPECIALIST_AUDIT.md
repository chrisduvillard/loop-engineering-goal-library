# Specialist Codebase Audit

This audit is intentionally split into independent review tracks so each one can challenge the repository from a different angle.

## Review tracks

1. **Decision-state integrity** — shaping questions, answers, approvals, lifecycle transitions, and resume behavior.
2. **Agent-control semantics** — interaction boundaries, approved-contract handoff, goal drift, authority, and concurrency.
3. **Security and path safety** — prompt injection, filesystem boundaries, packaging, generated files, and supply-chain controls.
4. **CI and portability** — supported Python versions, operating systems, deterministic checks, dependency updates, and failure diagnostics.
5. **Documentation and maintainability** — user friction, duplicated sources, goal catalog routing, archive completeness, and future contributor safety.

## Review method

Each track reviews the same repository state independently, records hypotheses before accepting findings, and requires executable evidence for any remediation. Findings are consolidated only after the specialist checks disagree or agree for explicit reasons.

## Status

Audit in progress on `codex/specialist-audit`. Final findings, fixes, verification evidence, residual risks, and reusable outputs will be recorded here before merge.
