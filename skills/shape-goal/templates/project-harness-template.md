# Project Harness

Use an existing README, `AGENTS.md`, `CLAUDE.md`, Makefile, task runner, CI configuration, runbook, or project skill when it already provides the verified information below. Create `docs/agent/PROJECT_HARNESS.md` only when setup, run, or verification knowledge is repeatedly rediscovered or materially ambiguous.

**Project:** [NAME]
**Owner:** [OWNER]
**Status:** Draft / Verified / Stale
**Last verified:** [DATE]
**Verified on:** [OS / RUNTIME / HARDWARE]
**Authoritative sources:** [PATHS]

## Prerequisites

- [RUNTIME / TOOLCHAIN / SERVICE / HARDWARE]
- [REQUIRED ACCESS WITHOUT SECRETS]

## Setup

```bash
[REPRODUCIBLE INSTALL OR BOOTSTRAP COMMANDS]
```

## Run

| Surface | Command | Expected signal | Stop/cleanup |
|---|---|---|---|
| [APP / API / WORKER / CLI] | `[COMMAND]` | [HEALTH/OUTPUT] | `[COMMAND]` |

## Repository-native verification

| Gate | Command or workflow | Scope | Expected result |
|---|---|---|---|
| Unit | `[COMMAND]` | [SCOPE] | [RESULT] |
| Integration | `[COMMAND]` | [SCOPE] | [RESULT] |
| Build/type/lint | `[COMMAND]` | [SCOPE] | [RESULT] |
| E2E/UAT | `[COMMAND OR FLOW]` | [SCOPE] | [RESULT] |

## Realistic workflows

1. [USER OR OPERATOR FLOW]
2. [EXPECTED OBSERVABLE RESULT]
3. [CLEANUP OR RESET]

## Clean state and reset

```bash
[SAFE RESET / FIXTURE / DATABASE / CACHE COMMANDS]
```

State what must never be deleted or reset automatically.

## Supported environments

| Environment | Supported | Notes |
|---|---|---|
| [OS / RUNTIME / BROWSER / DEVICE] | Yes / No / Partial | [NOTES] |

## Data, credentials, and external systems

- Required data: [FIXTURE / SYNTHETIC / APPROVED SOURCE]
- Credential handling: [REFERENCE ONLY; NEVER STORE SECRET VALUES]
- External-system boundaries: [READ/WRITE/AUTHORITY]
- Production mutation: [PROHIBITED OR APPROVAL RULE]

## Known baseline issues

- [FLAKY TEST / PRE-EXISTING FAILURE / ENVIRONMENT LIMITATION]

## Evidence capture

- Record exact command, exit/result, environment, and relevant artifact.
- Prefer concise extracts, checksums, screenshots, or secure references over raw large logs.
- Never store secrets, private data, raw production dumps, or exploit-enabling material.

## Freshness triggers

Re-verify this harness when any of these changes:

- Toolchain, dependency, runtime, or supported platform
- Setup, build, run, test, deployment, or recovery workflow
- Required services, environment variables, fixtures, or credentials
- Entry points, architecture boundaries, or CI gates

A stale harness is evidence to investigate, not an instruction to follow blindly.
