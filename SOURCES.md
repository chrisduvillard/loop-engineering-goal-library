# Sources

Research checked on **August 25, 2026**. Primary sources were prioritized over secondary summaries.

## OpenAI Codex

- [Follow goals with `/goal`](https://developers.openai.com/codex/use-cases/follow-goals/)
- [Build skills for ChatGPT and Codex](https://developers.openai.com/codex/skills/)
- [Code migrations](https://developers.openai.com/codex/use-cases/code-migrations)
- [Iterate on difficult problems](https://developers.openai.com/codex/use-cases/iterate-on-difficult-problems)
- [Subagents](https://developers.openai.com/codex/agent-configuration/subagents)
- [Codex prompting and workflows](https://developers.openai.com/codex/prompting)

OpenAI defines skills as reusable workflows that package instructions, resources, and optional scripts, with progressive disclosure and explicit or implicit invocation. Codex uses `$skill-name` for explicit skill mentions in CLI and IDE contexts, while native `/goal` supplies durable continuation toward a verifiable stopping condition.

## Anthropic Claude Code

- [Claude Code goals](https://docs.anthropic.com/en/docs/claude-code/goal)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)

Claude Code exposes skills directly as `/skill-name` and can also load them automatically when relevant. Its native `/goal` adds a separate evaluator after every turn; that evaluator judges evidence surfaced in the conversation rather than independently reading files or running commands.

## Open Agent Skills ecosystem

- [Agent Skills open standard](https://agentskills.io/)
- [Vercel Labs `skills` CLI](https://github.com/vercel-labs/skills)
- [`skills` CLI documentation](https://www.skills.sh/docs/cli)

The repository uses standard `SKILL.md` frontmatter and keeps supporting references inside each skill directory so the skills remain portable across Codex, Claude Code, and other compatible hosts.

## Goal shaping and engineering workflows

- [Matt Pocock: `grill-with-docs`](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)
- [Matt Pocock: `wayfinder`](https://github.com/mattpocock/skills/tree/main/skills/engineering/wayfinder)
- [Matt Pocock: `to-prd`](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-prd)
- [Matt Pocock's skill architecture](https://github.com/mattpocock/skills)

`shape-goal` is an original workflow informed by these patterns. It differs from `grill-with-docs`: the latter sharpens domain language and durable design decisions, while `shape-goal` produces the narrower execution contract needed before an autonomous goal begins.

The split between `shape-goal` and `goal-engine` also follows a useful practitioner distinction: user-facing orchestration should remain separate from reusable execution discipline. The approved Goal Contract is the boundary between the two.

## Loop engineering libraries and practitioner work

- [Forward Future Loop Library](https://signals.forwardfuture.com/loop-library/#top)
- [Forward Future: Learn the loop pattern](https://signals.forwardfuture.com/loop-library/learn/)
- [Addy Osmani: Loop Engineering](https://addyosmani.com/blog/loop-engineering/)

## How the sources were used

- OpenAI and Anthropic documentation informed the separation between reusable skills and the native goal runtime, skill invocation differences, evidence requirements, evaluator behavior, state handling, and vendor portability.
- OpenAI migration, difficult-problem, and subagent guidance informed checkpointing, behavioral preservation, rollback, independent review, and parallel-agent boundaries.
- Anthropic's long-running-agent research informed durable repository state, incremental progress, generator/evaluator separation, and anti-premature-completion patterns.
- Matt Pocock's skills informed repository-first fact finding, owner-decision interviews, durable planning artifacts, and the distinction between deciding the destination and executing the route.
- Forward Future and Addy Osmani informed the general loop model: a durable objective combined with a check, bounded iteration, retained state, and objective exit conditions.

## Citation note

Documentation and product behavior can change. Re-check vendor documentation before relying on implementation-specific controls such as slash-command syntax, evaluator states, duration limits, feature flags, skill installation paths, invocation policy, or scheduled-loop behavior.
