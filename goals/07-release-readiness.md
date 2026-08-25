# Release Readiness

**Use when:** A version or milestone must converge on all repository-defined release gates without actually publishing it.

## Recommended: skill-backed

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Release Readiness profile. Work the highest-risk verified blocker first and continue until every release gate passes, the repository and release artifacts agree, rollback instructions are verified, and the working tree has no unexplained changes. Do not release, tag, publish, merge, or deploy; preserve a reusable closeout packet.
```

## Standalone fallback

```text
/goal Bring [VERSION OR SCOPE] to release-ready—not released—under the repository-defined release criteria. Establish the actual state and reconcile release documentation, specifications, CI, Git history and working changes, prior goal archives, open blockers, versioning and changelog, migrations, security, reliability and performance gates, deployment assumptions, and rollback instructions; protect unrelated and uncommitted work. Turn actual release gates into a concise checklist and capture their baseline. Work the highest-risk unblocked failure first: verify it, make the smallest reversible production fix, add regression protection, run repository-native targeted checks, then rerun clean or production-like full gates at appropriate checkpoints. Use an independent final review and verify every finding; do not hide failures, weaken gates, or expand scope. Update release, progress, and handoff artifacts. Finish only when every required gate passes with surfaced evidence, no release-blocking finding remains, artifacts, documentation, configuration, migrations, and rollback instructions are consistent, and the working tree has no unexplained changes. At any terminal outcome, preserve a reusable closeout packet under the repository's goal-history convention (default `docs/goals/<goal-id>/`) containing `CONTRACT.md`, final `PROGRESS.md`, and `RESULT.md`; update the history index, promote verified reusable tests/docs/ADRs/runbooks/fixtures/tooling, and exclude secrets, private data, raw production dumps, and unnecessarily large logs. Do not tag, publish, deploy, merge, push, or alter production without explicit approval. Stop for an external or approval blocker, [BUDGET], or two no-progress cycles.
```

**Why it works:** It distinguishes readiness from release authority and leaves a reusable release-evidence packet for the human release decision.
