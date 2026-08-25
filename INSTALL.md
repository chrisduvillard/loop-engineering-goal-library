# Install, Verify, Update, and Package

The library contains two Agent Skills:

- `shape-goal` — turns rough intent into an approved Goal Contract.
- `goal-engine` — executes that contract inside the host's native `/goal` loop.

## Recommended: install globally for Codex and Claude Code

Use a global install when you want the skills available in every repository:

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' \
  --global \
  --agent codex \
  --agent claude-code \
  --yes
```

The Agent Skills CLI uses a canonical copy and links it to supported agents by default, which keeps one source of truth across hosts.

## Verify the installation

```bash
npx -y skills@latest list --global --agent codex --agent claude-code
```

You should see both:

```text
shape-goal
goal-engine
```

Then verify invocation inside each host:

| Host | Shape an unclear project target |
|---|---|
| Claude Code | `/shape-goal Continue this project` |
| Codex CLI / IDE | `$shape-goal Continue this project` |

## Project-local installation

Use a project install when the exact skill version should be committed or shared only with one repository:

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' \
  --agent codex \
  --agent claude-code \
  --yes
```

Project-local is the CLI default. Global and project installs can coexist, but avoid keeping divergent copies unless that is intentional.

## Update

Update the globally installed skills:

```bash
npx -y skills@latest update shape-goal goal-engine --global --yes
```

Verify again after updating:

```bash
npx -y skills@latest list --global --agent codex --agent claude-code
```

When reproducibility matters, record the skill metadata version and source commit in the Goal Contract before execution.

## Clean reinstall fallback

If links or copies appear stale, rerun the recommended global `add` command. Review the paths printed by `skills list` before deleting anything manually.

## Use without installing

The Agent Skills CLI can render or launch one skill temporarily:

```bash
npx -y skills@latest use \
  chrisduvillard/loop-engineering-goal-library \
  --skill shape-goal \
  --agent claude-code
```

Use this for evaluation. Install globally for everyday work and durable reuse.

## Manual installation fallback

Clone or download the repository, then copy each complete skill directory:

```text
skills/shape-goal/
skills/goal-engine/
```

Typical global locations are:

```text
~/.codex/skills/
~/.claude/skills/
```

Keep each skill directory intact so its references, templates, and metadata travel with `SKILL.md`.

## Build reusable ZIP packages

From a repository checkout:

```bash
python3 scripts/package_skills.py
```

This creates deterministic packages under `dist/`:

```text
shape-goal-<version>.zip
goal-engine-<version>.zip
loop-engineering-skills-<version>.zip
SHA256SUMS
```

Individual ZIPs place `SKILL.md` at the archive root for upload-oriented hosts. The bundle preserves both `skills/<name>/` directories. GitHub Actions builds the same artifacts on every validated change.

## Validate a checkout

```bash
python3 scripts/validate_repository.py
python3 scripts/package_skills.py
npx -y skills@1.5.23 add . --list
```

The first command checks the repository contract. The second validates deterministic packaging. The third confirms that the Agent Skills CLI discovers both skills.
