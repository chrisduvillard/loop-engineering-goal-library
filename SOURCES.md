# Sources

Research and implementation references checked on **August 26, 2026**. Primary vendor documentation is prioritized.

## OpenAI Codex and Agent Skills

- [Follow a goal](https://learn.chatgpt.com/use-cases/follow-goals)
- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Code migrations](https://developers.openai.com/codex/use-cases/code-migrations)
- [Iterate on difficult problems](https://developers.openai.com/codex/use-cases/iterate-on-difficult-problems)

OpenAI describes `/goal` as a durable objective for work with a known completion contract, validation loop, and room for autonomous progress. Goal runs can be paused, resumed, or cleared, but their purpose is to continue without requiring the user to steer every turn. This supports shaping the contract first and starting `/goal` only after approval.

## Anthropic Claude Code

- [Goals](https://code.claude.com/docs/en/goal)
- [Skills](https://code.claude.com/docs/en/skills)
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)

Claude Code documents `/goal` as condition-driven: when the condition is not met, another turn begins automatically instead of returning control. Its evaluator judges evidence surfaced in the conversation and does not independently run tools. This makes native `/goal` a strong execution primitive but a poor default container for a human interview that must pause for each answer.

## Open Agent Skills ecosystem

- [Agent Skills standard](https://agentskills.io/)
- [Vercel Labs `skills` CLI](https://github.com/vercel-labs/skills)
- [`skills` CLI documentation](https://www.skills.sh/docs/cli)

The repository uses portable `SKILL.md` directories with references, templates, scripts, and optional host metadata.

## Goal shaping and product-definition patterns

- [Matt Pocock: `grill-with-docs`](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)
- [Matt Pocock: `wayfinder`](https://github.com/mattpocock/skills/tree/main/skills/engineering/wayfinder)
- [Matt Pocock: `to-prd`](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-prd)

These informed repository-first fact finding, one-decision-at-a-time interviews, durable planning artifacts, and deeper non-duplicate questioning. `shape-goal` is narrower: it resolves one executable contract and its acceptance evidence before autonomous implementation.

## Loop engineering

- [Forward Future Loop Library](https://signals.forwardfuture.com/loop-library/#top)
- [Forward Future loop learning guide](https://signals.forwardfuture.com/loop-library/learn/)
- [Addy Osmani: Loop Engineering](https://addyosmani.com/blog/loop-engineering/)

These informed the core model: objective + check + bounded iteration + durable state + objective exits.

## Profile-specific primary references

- [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [W3C Internationalization resources](https://www.w3.org/International/)
- [RFC 9745: Deprecation HTTP Response Header Field](https://www.rfc-editor.org/info/rfc9745/)
- [RFC 8594: Sunset HTTP Header Field](https://www.rfc-editor.org/info/rfc8594/)
- [NIST SP 1339: OT Backup Quick Start Guide](https://csrc.nist.gov/pubs/sp/1339/final)
- [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/)
- [Microsoft Research: Diagnosing Sample Ratio Mismatch in Online Controlled Experiments](https://www.microsoft.com/en-us/research/publication/diagnosing-sample-ratio-mismatch-in-online-controlled-experiments-a-taxonomy-and-rules-of-thumb-for-practitioners/)

These sources informed the distinctive verification mechanics of the new profiles: repeated stochastic evals, locale-aware checks, staged deprecation and sunset, tested restoration, and trustworthy event and experiment evidence.

## Current implementation interpretation

The recommended workflow is deliberately two-stage:

1. Run `shape-goal` in an ordinary interactive conversation. It asks one question and returns control.
2. After explicit approval, start a new native `/goal` using `goal-engine` and the approved contract.

Advanced combined preflights remain available when no owner interaction is expected. At the first unresolved owner decision they stop as **Approval required** instead of asking and continuing autonomously.

## Citation note

Vendor behavior can change. Re-check official documentation before relying on command syntax, evaluator behavior, invocation policy, install locations, feature flags, or permission boundaries.
