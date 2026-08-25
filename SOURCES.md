# Sources

Research checked on **August 25, 2026**. Primary sources were prioritized over secondary summaries.

## OpenAI Codex

- [Follow goals with `/goal`](https://developers.openai.com/codex/use-cases/follow-goals/)
- [Code migrations](https://developers.openai.com/codex/use-cases/code-migrations)
- [Iterate on difficult problems](https://developers.openai.com/codex/use-cases/iterate-on-difficult-problems)
- [Subagents](https://developers.openai.com/codex/agent-configuration/subagents)
- [Codex prompting and workflows](https://developers.openai.com/codex/prompting)

## Anthropic Claude Code

- [Claude Code goals](https://docs.anthropic.com/en/docs/claude-code/goal)
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)

## Loop engineering libraries and practitioner work

- [Forward Future Loop Library](https://signals.forwardfuture.com/loop-library/#top)
- [Forward Future: Learn the loop pattern](https://signals.forwardfuture.com/loop-library/learn/)
- [Addy Osmani: Loop Engineering](https://addyosmani.com/blog/loop-engineering/)

## How the sources were used

- OpenAI and Anthropic documentation informed the goal lifecycle, evidence requirements, autonomous continuation model, evaluator behavior, state handling, and vendor portability guidance.
- OpenAI migration, difficult-problem, and subagent guidance informed checkpointing, behavioral preservation, rollback, independent review, and parallel-agent boundaries.
- Anthropic’s long-running-agent research informed durable repository state, incremental progress, generator/evaluator separation, and anti-premature-completion patterns.
- Forward Future and Addy Osmani informed the general loop model: a durable objective combined with a check, bounded iteration, retained state, and objective exit conditions.

## Citation note

Documentation and product behavior can change. Re-check vendor documentation before relying on implementation-specific controls such as slash-command syntax, evaluator states, duration limits, feature flags, or scheduled-loop behavior.
