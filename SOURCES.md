# Sources

Research and implementation references checked on **August 25, 2026**. Primary vendor documentation is prioritized.

## OpenAI Codex and Agent Skills

- [Follow a goal](https://learn.chatgpt.com/use-cases/follow-goals)
- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Code migrations](https://developers.openai.com/codex/use-cases/code-migrations)
- [Iterate on difficult problems](https://developers.openai.com/codex/use-cases/iterate-on-difficult-problems)

OpenAI documents `/goal` as one durable objective with a verifiable stopping condition, protected scope, named evidence, checkpoints, and progress state. Codex can activate skills explicitly or implicitly from their descriptions; this library's launchers name both skills and also ship OpenAI host metadata.

## Anthropic Claude Code

- [Goals](https://code.claude.com/docs/en/goal)
- [Skills](https://code.claude.com/docs/en/skills)
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)

Claude Code's `/goal` evaluator judges evidence surfaced in the conversation and does not independently run tools. Claude can invoke skills automatically unless invocation is restricted. This informs the explicit shaping-to-execution handoff and evidence-surfacing rules.

## Open Agent Skills ecosystem

- [Agent Skills standard](https://agentskills.io/)
- [Vercel Labs `skills` CLI](https://github.com/vercel-labs/skills)
- [`skills` CLI documentation](https://www.skills.sh/docs/cli)

The repository uses portable `SKILL.md` directories with references, templates, scripts, and optional host metadata.

## Goal shaping and product-definition patterns

- [Matt Pocock: `grill-with-docs`](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)
- [Matt Pocock: `wayfinder`](https://github.com/mattpocock/skills/tree/main/skills/engineering/wayfinder)
- [Matt Pocock: `to-prd`](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-prd)

These informed repository-first fact finding, one-decision-at-a-time interviews, and durable planning artifacts. `shape-goal` is narrower: it resolves the exact executable contract and evidence required before autonomous implementation.

## Loop engineering

- [Forward Future Loop Library](https://signals.forwardfuture.com/loop-library/#top)
- [Forward Future loop learning guide](https://signals.forwardfuture.com/loop-library/learn/)
- [Addy Osmani: Loop Engineering](https://addyosmani.com/blog/loop-engineering/)

These informed the core model: objective + check + bounded iteration + durable state + objective exits.

## Current implementation interpretation

The zero-friction launcher is a deliberate two-phase meta-goal:

1. Shape and approve the exact repository-specific contract.
2. Execute that contract to passing evidence.

This is offered for convenience because the user requested commands that run unchanged. The stricter two-step path remains available and aligns directly with vendor guidance to define “done” before activating the long-running goal.

## Citation note

Vendor behavior can change. Re-check official documentation before relying on command syntax, evaluator behavior, invocation policy, install locations, feature flags, or permission boundaries.
