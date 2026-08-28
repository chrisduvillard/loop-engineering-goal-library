# Contributing

Changes should make the library safer, smoother, easier to verify, more adaptive, or more reusable—not merely longer.

## Canonical sources

- Goal identity and category metadata: `goals/catalog.json`
- Individual profile guidance and advanced preflights: `goals/*.md`
- Shared shaping behavior: `skills/shape-goal/`
- Shared execution behavior: `skills/goal-engine/`
- Cross-cutting proof: `skills/goal-engine/references/assurance-overlays.md`

Regenerate shared launcher clauses and catalogs with:

```bash
python3 scripts/sync_goal_launchers.py --write
python3 scripts/sync_goal_docs.py --write
```

Generated or synchronized outputs include:

- Interactive profile blocks in `goals/*.md`
- Advanced preflight boundaries in `goals/*.md`
- `GOAL_LIBRARY.md`
- `SPECIALIST_LOOPS.md`
- `QUALITY_GOALS.md`
- `goals/README.md`
- The goal catalog section in `README.md`

## Interactive-first invariant

Every canonical goal file must:

- Present `shape-goal` as the recommended start
- Provide both Claude Code and Codex invocation syntax
- Tell users to run shaping outside an active `/goal`
- Ask one material owner decision per turn
- End the turn immediately after asking
- Preserve safe questions and answers in append-only `SHAPING.md`
- Support deeper non-duplicate shaping rounds
- Require explicit contract approval

The two `/goal` commands are advanced autonomous preflights. They must:

- Run unchanged and contain no repository-specific placeholder
- Stay within the portable 4,000-character condition limit
- Continue only when an approved artifact already resolves every owner decision
- Save one proposed question and stop as **Approval required** when interaction is needed
- Never ask a question and continue looping inside `/goal`
- Forbid production changes before approval
- Require passing evidence, protected behavior, authority boundaries, and reusable closeout

## Adding or changing a profile

A new profile is justified only when the work has a distinct:

- Iteration unit
- Primary verifier
- Failure mode
- Keep-or-revert decision
- Stopping logic

Do not add a profile merely for a technology or framework.

When adding one:

1. Add it to `goals/catalog.json`.
2. Add the canonical goal file.
3. Add required inputs to `skills/shape-goal/references/profile-inputs.md`.
4. Add execution rules to `skills/goal-engine/references/loop-profiles.md`.
5. Update relevant overlays and examples.
6. Regenerate launcher clauses and collections.
7. Update version, changelog, validator, and README wording.

Use a dedicated quality profile when the concern is the primary outcome. Use an assurance overlay when it is secondary.

## Changing input resolution

Preserve these rules:

- Search authoritative evidence before asking.
- Facts are the agent's responsibility; decisions are the user's.
- Ask one material decision with evidence and a recommendation.
- Save the proposed question, ask it, and end the turn.
- Save the user's next reply before continuing.
- Do not ask the same question again without materially new evidence.
- Do not auto-default product direction, acceptance thresholds, risk acceptance, destructive authority, or legal/compliance conclusions.
- Do not start autonomous execution before explicit approval.

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
python3 scripts/validate_shaping_history_diff.py --self-test
python3 scripts/validate_question_state.py --self-test
python3 scripts/validate_goal_archives.py --self-test
python3 scripts/validate_tooling_contract.py --self-test
python3 scripts/validate_repository.py
python3 scripts/package_skills.py
npm ci --ignore-scripts
npx --no-install skills add . --list
```

Generated ZIPs belong in `dist/` and are ignored by Git.

## Strong proposals include

- The friction or failure mode
- Evidence that it recurs often enough to justify complexity
- The smallest coherent change
- A verifier or worked example
- Compatibility and migration notes
- Whether it affects shaping, lifecycle, execution, overlays, harness, catalog, or advanced mode

## Sensitive data

Never commit credentials, private user data, confidential business/customer information, production dumps, exploit-enabling evidence, or unnecessary large logs. Use synthetic examples, concise extracts, checksums, and approved stable references.
