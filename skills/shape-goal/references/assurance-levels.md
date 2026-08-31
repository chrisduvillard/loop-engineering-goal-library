# Assurance levels

## Lite

Use for small, reversible, low-risk changes. Require one concise contract, one
executable verifier, one evidence receipt, and mutation-mode enforcement. A
lease is optional when no concurrent work exists.

## Standard

Use for normal repository work. Require adaptive shaping, an approved contract,
canonical state, a lease for mutation, acceptance evidence, regression checks,
protected-work review, and closeout validation.

## High

Use for security, privacy, compliance, production infrastructure, destructive
migration, high blast radius, or costly irreversible work. Add a complete
assumption register, explicit rollback evidence, resource locks, an independent
held-out verifier, anti-cheat checks, forced compaction/resume testing, and a
complete archive.

The shaper recommends a level from risk and evidence. The user may raise or
lower it explicitly, but lowering High assurance must be recorded as an
accepted residual risk.
