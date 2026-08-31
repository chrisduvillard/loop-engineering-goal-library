# Install, Verify, Update, and Package

The library contains two portable Agent Skills:

- `shape-goal` — the main interactive command; discovers missing inputs, asks one material decision at a time, and approves a Goal Contract.
- `goal-engine` — executes the approved contract inside a later native `/goal`.

## Prerequisites

- Node.js **22.20.0 or newer** for the pinned Skills CLI used by repository validation.
- Python **3.9 or newer** only when running the repository's validation or packaging scripts; CI uses Python 3.12.
- A current Codex and/or Claude Code installation with Agent Skills support.

```bash
node --version
```

## Recommended global install

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' \
  --global \
  --agent codex \
  --agent claude-code \
  --yes
```

## Verify

```bash
npx -y skills@latest list --global --agent codex --agent claude-code
```

You should see:

```text
shape-goal
goal-engine
```

Then open a repository and invoke the main skill **without an active `/goal`**:

| Host | Command |
|---|---|
| Claude Code | `/shape-goal Continue this project` |
| Codex CLI / IDE | `$shape-goal Continue this project` |

The skill should ask at most one owner question, save it, and end the turn so you can answer normally. After the Goal Contract is approved, it returns the execution `/goal` command.

## If shaping is already trapped inside `/goal`

When the interface shows **Pursuing goal** while a shaping question is waiting:

- Codex: run `/goal pause` or `/goal clear`, then `$shape-goal Resume goal-id`.
- Claude Code: run `/goal clear`, then `/shape-goal Resume goal-id`.

The saved `SHAPING.md` lets the interview resume without losing earlier questions or answers.

## Discovery troubleshooting

If `skills list` shows both skills but one host cannot invoke them:

1. Verify the host-specific locations exist:

   ```text
   Codex:       ~/.agents/skills/shape-goal and ~/.agents/skills/goal-engine
   Claude Code: ~/.claude/skills/shape-goal and ~/.claude/skills/goal-engine
   ```

2. Rerun the install with `--copy` when symlinks are unsupported or not followed:

   ```bash
   npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
     --skill '*' --global --agent codex --agent claude-code --copy --yes
   ```

3. Restart the host and run the direct invocation again.
4. Inspect `CLAUDE_CONFIG_DIR` or `CODEX_HOME` when a custom configuration directory is used.

Avoid divergent manual copies when possible. Goal Contracts record the installed library version or source commit.

## Project-local install

Use this when the exact skill version should be scoped to one repository:

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' \
  --agent codex \
  --agent claude-code \
  --yes
```

## Update

```bash
npx -y skills@latest update shape-goal goal-engine --global --yes
```

Restart Codex or Claude Code, then verify again afterward.

If the update command fails or does not repair a changed local install, rerun the global install command above. Reinstalling fetches the current repository version and is the safest repair path.

## Use without installing

```bash
npx -y skills@latest use \
  chrisduvillard/loop-engineering-goal-library \
  --skill shape-goal \
  --agent claude-code
```

Temporary use is useful for evaluation. Global installation is the smoothest everyday path.

## Manual installation

Copy each complete directory:

```text
skills/shape-goal/
skills/goal-engine/
```

Typical user locations:

```text
~/.agents/skills/
~/.claude/skills/
```

Keep each directory intact so references, templates, host metadata, and `SKILL.md` travel together.

## Build deterministic ZIP packages

```bash
python3 scripts/package_skills.py
```

Outputs:

```text
shape-goal-<version>.zip
goal-engine-<version>.zip
loop-engineering-skills-<version>.zip
SHA256SUMS
```

## Validate a checkout

```bash
python3 scripts/sync_goal_launchers.py --check
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

## Package integrity in 0.12.0

Each standalone ZIP now contains every skill-local reference it requires. The
packager rejects local Markdown references that escape the archive or resolve to
a missing member. Prefer the combined bundle when installing both phases, and
verify `SHA256SUMS` before extraction.

Claude Code can also discover the repository as a plugin through
`.claude-plugin/plugin.json`. Codex continues to use the documented Agent Skills
installation path.
