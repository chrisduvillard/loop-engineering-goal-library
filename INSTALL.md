# Install, Verify, Update, and Package

The library contains two portable Agent Skills:

- `shape-goal` — discovers missing goal inputs, asks only material decisions, and approves a Goal Contract.
- `goal-engine` — executes the approved contract inside native `/goal`.

## Prerequisites

- Node.js **22.20.0 or newer** for the pinned `skills` CLI used by this repository.
- Python **3.9 or newer** only when running repository validation or package scripts; CI uses Python 3.12.
- A current Codex and/or Claude Code installation with Agent Skills support.

Check Node before installation:

```bash
node --version
```

## Recommended: global Codex + Claude Code install

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' \
  --global \
  --agent codex \
  --agent claude-code \
  --yes
```

The CLI normally keeps a canonical copy and links supported agents to it.

## Verify

```bash
npx -y skills@latest list --global --agent codex --agent claude-code
```

You should see:

```text
shape-goal
goal-engine
```

Then open a repository and verify one direct invocation:

| Host | Command |
|---|---|
| Claude Code | `/shape-goal Continue this project` |
| Codex CLI / IDE | `$shape-goal Continue this project` |

To test zero-friction routing, open any file under [`goals/`](goals/) and paste its first `/goal` command unchanged. It should enter shaping before production execution.

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

3. Restart the host and run the direct invocation test again.
4. Inspect `CLAUDE_CONFIG_DIR` or `CODEX_HOME` when a custom configuration directory is used.

Do not maintain divergent manual copies unless necessary; record the installed library version in each Goal Contract.

## Project-local install

Use this when the exact skills should be scoped to one repository:

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' \
  --agent codex \
  --agent claude-code \
  --yes
```

Project-local is the CLI default. Global and local installs can coexist, but avoid unintentionally divergent copies.

## Update

```bash
npx -y skills@latest update shape-goal goal-engine --global --yes
```

Verify again afterward. Goal Contracts record the library version or source commit for reproducibility.

## Clean reinstall

Rerun the recommended `add` command. Inspect paths with `skills list` before deleting anything manually.

## Use without installing

```bash
npx -y skills@latest use \
  chrisduvillard/loop-engineering-goal-library \
  --skill shape-goal \
  --agent claude-code
```

Temporary use is useful for evaluation. Global install is the smoothest everyday path.

## Manual installation

Copy each complete skill directory:

```text
skills/shape-goal/
skills/goal-engine/
```

Typical user locations include:

```text
~/.agents/skills/
~/.claude/skills/
```

Keep the directory intact so references, templates, host metadata, and `SKILL.md` travel together.

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

Individual ZIPs place `SKILL.md` at archive root. The bundle preserves both skill directories.

## Validate a checkout

```bash
python3 scripts/sync_goal_docs.py --check
python3 scripts/validate_repository.py
python3 scripts/package_skills.py
npx -y skills@1.5.23 add . --list
```
