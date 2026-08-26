# Contributing

Changes should make the library safer, easier to run unchanged, easier to verify, more adaptive, or more reusable—not merely longer.

## Canonical sources

- Goal identity and category metadata: `goals/catalog.json`
- Individual launchers and fallbacks: `goals/*.md`
- Shared shaping and input discovery: `skills/shape-goal/`
- Shared execution behavior: `skills/goal-engine/`
- Cross-cutting proof: `skills/goal-engine/references/assurance-overlays.md`

Do not hand-edit generated catalog sections or collection files. Regenerate with:

```bash
python3 scripts/sync_goal_docs.py --write
```

Generated outputs:

- `GOAL_LIBRARY.md`
- `SPECIALIST_LOOPS.md`
- `QUALITY_GOALS.md`
- `goals/README.md`
- The goal catalog section in `README.md`

## Zero-friction launcher invariant

The first `/goal` command in every canonical goal file must:

- Run unchanged
- Contain no repository-specific placeholder
- Name both `shape-goal` and `goal-engine`
- Require repository and connected-source search before user questions
- Ask only unresolved material owner decisions
- Preserve exact safe questions and answers in append-only `SHAPING.md`, with deeper rounds and superseding corrections
- Classify repository visibility and redact or securely reference confidential/restricted answers
- Stay within the portable 4,000-character native-goal condition limit
- Forbid production edits before contract approval
- State that shaping is not completion
- Require passing acceptance evidence and reusable closeout

The second command is a self-contained no-placeholder fallback.

## Adding or changing a profile

A new profile is justified only when the work has a distinct:

- Iteration unit
- Primary verifier
- Failure mode
- Keep-or-revert decision
- Stopping logic

Do not add a profile merely for a technology or framework.

When adding a profile:

1. Add it to `goals/catalog.json`.
2. Add the canonical goal file.
3. Add profile inputs to `skills/shape-goal/references/profile-inputs.md`.
4. Add execution rules to `skills/goal-engine/references/loop-profiles.md`.
5. Update relevant overlays and examples.
6. Regenerate collections.
7. Update version, changelog, validator, and README wording as needed.

Use a dedicated quality profile when that concern is the primary outcome. Use an assurance overlay when it is secondary.

## Changing input resolution

Preserve these rules:

- Search all available authoritative evidence before asking.
- Facts are the agent's responsibility; decisions are the user's.
- Ask one material decision at a time with evidence and a recommendation.
- Do not ask the same question again without materially new evidence.
- Do not auto-default product direction, acceptance thresholds, risk acceptance, destructive authority, or legal/compliance conclusions.
- Do not allow shaping to satisfy the enclosing native goal.

## Versioned changes

When behavior changes:

1. Update `VERSION`.
2. Update both skills' `metadata.version`.
3. Add a `CHANGELOG.md` entry.
4. Explain compatibility and migration effects.
5. Update examples and validators when schemas change.

Do not add a license, tag, release, or permanent published artifact without owner approval.

## Validate locally

```bash
python3 scripts/sync_goal_launchers.py --write
python3 scripts/sync_goal_launchers.py --check
python3 scripts/sync_goal_docs.py --write
python3 scripts/sync_goal_docs.py --check
python3 scripts/validate_repository.py
python3 scripts/package_skills.py
npx -y skills@1.5.23 add . --list
```

Generated ZIPs belong in `dist/` and are ignored by Git.

## Strong proposals include

- The friction or failure mode
- Evidence that it recurs often enough to justify complexity
- The smallest coherent change
- A verifier or worked example
- Compatibility and migration notes
- Whether it affects shaping, lifecycle, execution, overlays, harness, catalog, or standalone mode

## Sensitive data

Never commit credentials, private user data, production dumps, exploit-enabling evidence, or unnecessary large logs. Use synthetic examples, concise extracts, checksums, and approved stable references.
