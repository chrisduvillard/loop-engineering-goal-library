# Install, Verify, Update, and Package

The library contains two portable Agent Skills:

- `shape-goal` — discovers missing goal inputs, asks only material decisions, and approves a Goal Contract.
- `goal-engine` — executes the approved contract inside native `/goal`.

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
