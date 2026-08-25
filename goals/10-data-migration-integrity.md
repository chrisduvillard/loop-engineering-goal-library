# Data Migration / Integrity

**Use when:** Stored data or schemas must change while preserving correctness, compatibility, recoverability, and auditability.

## Recommended: skill-backed

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Data Migration / Integrity profile. Define reconciliation, idempotency, restartability, mixed-version compatibility, and rollback before any destructive boundary, then continue through reversible phases until migration and reconciliation gates pass with no unexplained loss, duplication, or corruption. Stop for a contract-defined blocker, approval boundary, budget, or two no-progress cycles; preserve a reusable closeout packet.
```

## Standalone fallback

```text
/goal Migrate [DATA OR SCHEMA] from [SOURCE STATE] to [TARGET STATE] under [INTEGRITY AND COMPATIBILITY REQUIREMENTS]. First map the authoritative schema, readers and writers, invariants, volumes, retention/privacy constraints, migration history, prior goal archives, backup/restore path, repository-native checks, and actual Git/database state; preserve evidence and existing data. Define pre/post reconciliation queries, dry-run behavior, idempotency, restartability, mixed-version compatibility, and rollback before any destructive step. Implement in reversible phases—expand, backfill, verify, switch, then contract where applicable. Test on representative data; compare counts, checksums, relationships, and domain invariants; exercise interruption, retry, rollback, and old/new application combinations; add regression and migration coverage; and independently review high-risk steps. Never mutate production, delete data, or cross an irreversible boundary without explicit approval. Finish only when [MIGRATION GATES] and reconciliation checks pass with surfaced evidence, rollback/recovery is verified, and no unexplained loss, duplication, or corruption remains. Stop for missing access, unclear data ownership, approval/external blocker, [BUDGET], or two no-progress cycles; record exact resume state. At any terminal outcome, preserve a reusable closeout packet under the repository's goal-history convention (default `docs/goals/<goal-id>/`) containing `CONTRACT.md`, final `PROGRESS.md`, and `RESULT.md`; update the history index, promote verified reusable tests/docs/ADRs/runbooks/fixtures/tooling, and exclude secrets, private data, raw production dumps, and unnecessarily large logs.
```

**Why it works:** Data integrity and recoverability become explicit acceptance evidence, and the archived reconciliation plan makes future migrations safer.
