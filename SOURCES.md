# Sources

Research checked on **August 25, 2026**. Primary sources were prioritized over secondary summaries.

## OpenAI Codex

- [Follow goals with `/goal`](https://developers.openai.com/codex/use-cases/follow-goals/)
- [Build skills for ChatGPT and Codex](https://developers.openai.com/codex/skills/)
- [Code migrations](https://developers.openai.com/codex/use-cases/code-migrations)
- [Iterate on difficult problems](https://developers.openai.com/codex/use-cases/iterate-on-difficult-problems)
- [Subagents](https://developers.openai.com/codex/agent-configuration/subagents)
- [Codex prompting and workflows](https://developers.openai.com/codex/prompting)

OpenAI defines skills as reusable workflows that package instructions, resources, and optional scripts. Native `/goal` supplies durable continuation toward a verifiable stopping condition, while isolated agents or worktrees are the safer pattern for independent parallel work.

## Anthropic Claude Code

- [Claude Code goals](https://code.claude.com/docs/en/goal)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code extension overview](https://code.claude.com/docs/en/features-overview)
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)

Claude Code exposes skills as `/skill-name` and can load them automatically when relevant. Its current goal documentation states that one goal can be active per session and that a separate evaluator checks evidence surfaced in the conversation rather than independently reading files or running commands. This supports the library's one-contract-per-session rule and repository-level goal portfolio.

Claude's skill documentation also describes saving verified project run/verify knowledge into project-specific skills rather than rediscovering setup repeatedly. The library's vendor-neutral Project Harness applies the same reuse principle while remaining readable by Codex and other Agent Skills hosts.

## Open Agent Skills ecosystem

- [Agent Skills open standard](https://agentskills.io/)
- [Vercel Labs `skills` CLI](https://github.com/vercel-labs/skills)
- [`skills` CLI documentation](https://www.skills.sh/docs/cli)

The repository uses standard `SKILL.md` frontmatter and keeps supporting references and templates inside each skill directory so they remain portable across Codex, Claude Code, and other compatible hosts.

## Goal shaping and engineering workflows

- [Matt Pocock: `grill-with-docs`](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)
- [Matt Pocock: `wayfinder`](https://github.com/mattpocock/skills/tree/main/skills/engineering/wayfinder)
- [Matt Pocock: `to-prd`](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-prd)
- [Matt Pocock's skill architecture](https://github.com/mattpocock/skills)

`shape-goal` is an original workflow informed by these patterns. It differs from `grill-with-docs`: the latter sharpens domain language and durable design decisions, while `shape-goal` produces and manages the narrower execution contracts needed before autonomous goals begin.

## Loop engineering libraries and practitioner work

- [Forward Future Loop Library](https://signals.forwardfuture.com/loop-library/#top)
- [Forward Future: Learn the loop pattern](https://signals.forwardfuture.com/loop-library/learn/)
- [Addy Osmani: Loop Engineering](https://addyosmani.com/blog/loop-engineering/)

## How the sources were used

- OpenAI and Anthropic documentation informed the separation between reusable skills and native goal runtimes, skill invocation, evaluator visibility, state handling, and vendor portability.
- The one-goal-per-session model informed the split between a project-level portfolio and a single executable Goal Contract per session/worktree.
- OpenAI migration, difficult-problem, and subagent guidance informed checkpointing, rollback, independent review, and parallel-work boundaries.
- Anthropic's long-running-agent research informed durable state, incremental progress, generator/evaluator separation, and anti-premature-completion patterns.
- Claude's reusable run/verify skill pattern informed the Project Harness principle: verify project mechanics once, then reuse them.
- Matt Pocock's skills informed repository-first fact finding, owner-decision interviews, durable planning artifacts, and the distinction between deciding the destination and executing the route.
- Forward Future and Addy Osmani informed the general loop model: a durable objective combined with a check, bounded iteration, retained state, and objective exits.

## Citation note

Documentation and product behavior can change. Re-check vendor documentation before relying on implementation-specific controls such as slash-command syntax, evaluator states, duration limits, feature flags, skill installation paths, invocation policy, or scheduled-loop behavior.
