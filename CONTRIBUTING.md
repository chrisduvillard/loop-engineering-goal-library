# Contributing

Changes should make the library safer, easier to use, easier to verify, or easier to reuse—not merely longer.

## Canonical sources

- Edit individual profile files under `goals/`.
- Do not hand-edit `GOAL_LIBRARY.md` or `SPECIALIST_LOOPS.md`.
- Regenerate them with:

```bash
python3 scripts/sync_goal_docs.py --write
```

- Shared execution behavior belongs in `skills/goal-engine/`.
- Target-shaping behavior belongs in `skills/shape-goal/`.
- Project-specific facts never belong in the reusable skills.

## Versioned changes

When behavior changes:

1. Update `VERSION` according to semantic versioning.
2. Update both skills' `metadata.version`.
3. Add a `CHANGELOG.md` entry.
4. Explain any migration or compatibility effect.

Do not add a license, release, tag, or publish artifacts without owner approval.

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
- Evidence that it occurs or is likely enough to justify complexity
- The smallest coherent change
- A verifier or example
- Compatibility and migration notes
- Whether the change affects `shape-goal`, `goal-engine`, one profile, or standalone mode

## Profile changes

Keep one primary outcome per profile. A new profile is justified only when the work has a distinct risk model that cannot be expressed cleanly through an existing profile plus contract-specific acceptance evidence.

## Sensitive data

Never commit credentials, private user data, raw production dumps, or unredacted exploit evidence. Use synthetic examples and stable approved references.
