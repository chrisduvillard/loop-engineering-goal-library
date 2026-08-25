# Contributing

Changes should make the library safer, easier to use, easier to verify, more adaptive, or easier to reuse—not merely longer.

## Canonical sources

- Edit individual standalone preset files under `goals/`.
- Do not hand-edit `GOAL_LIBRARY.md` or `SPECIALIST_LOOPS.md`.
- Regenerate them with:

```bash
python3 scripts/sync_goal_docs.py --write
```

- Shared execution behavior belongs in `skills/goal-engine/`.
- Target, portfolio, and lifecycle behavior belongs in `skills/shape-goal/`.
- Cross-cutting proof obligations belong in `skills/goal-engine/references/assurance-overlays.md`.
- Project-specific facts never belong in the reusable global skills.

## Versioned changes

When behavior changes:

1. Update `VERSION` according to semantic versioning.
2. Update both skills' `metadata.version`.
3. Add a `CHANGELOG.md` entry.
4. Explain migration or compatibility effects.
5. Update examples and validators when a state schema changes.

Do not add a license, release, tag, or publish permanent artifacts without owner approval.

## Validate locally

```bash
python3 scripts/sync_goal_docs.py --check
python3 scripts/validate_repository.py
python3 scripts/package_skills.py
npx -y skills@1.5.23 add . --list
```

Generated ZIPs belong in `dist/` and are ignored by Git.

## Strong proposals include

- The friction or failure mode being addressed
- Evidence that it occurs often enough to justify complexity
- The smallest coherent change
- A verifier or worked example
- Compatibility and migration notes
- Whether the change affects shaping, lifecycle, portfolio, execution, overlays, harness, a preset, or standalone mode

## Preset, overlay, and custom-loop rules

### Add or change an execution preset when

- The pattern has a distinct control loop, verifier, failure mode, and stopping logic.
- It recurs across multiple real goals or projects.
- It cannot be expressed cleanly as an existing preset plus assurance overlays and contract evidence.

Do not create presets for technologies, frameworks, or quality attributes alone.

### Add or change an assurance overlay when

- The concern cuts across multiple execution presets.
- It adds stable proof, review, or authority obligations.
- A project-specific overlay has recurred enough to justify global reuse.

### Use Custom Contract-Driven when

- The goal is measurable but no preset fits yet.
- The contract can define iteration unit, verifier, keep-or-revert rule, review strategy, and stop condition.

One unusual goal is not evidence for a new global preset.

## Goal portfolio changes

Preserve these invariants:

- One native `/goal` session/worktree executes one dependency-safe leaf contract.
- A different observable outcome gets a different Goal ID.
- Priority changes do not silently rewrite contracts.
- Closed results remain immutable and related goals link to them.
- Parallel goals require isolation and explicit shared-resource coordination.

## Project harness changes

The Project Harness should link to canonical commands and scripts, record only verified mechanics, include freshness triggers, and remain vendor-neutral. Do not duplicate the entire README, CI configuration, or task runner.

## Sensitive data

Never commit credentials, private user data, raw production dumps, unredacted exploit-enabling evidence, or unnecessary large logs. Use synthetic examples, concise extracts, checksums, and stable approved references.
