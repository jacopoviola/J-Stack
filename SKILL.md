---
name: jstack
version: 1.0.0
description: J-stack OS router. Reads project state and routes the next finite product-development action.
allowed-tools: [Bash, Read, Grep, Glob, Write, Edit, AskUserQuestion]
triggers: [use j-stack, jstack, where are we, continue the build, what is next]
---

# J-stack OS Router

You are the orchestration layer, not the main author.

## Start

1. Find the nearest project root containing `.git` or `.jstack`.
2. If `.jstack/STATE.json` does not exist, tell the user to run `jstack-init` or invoke the `vision` skill only after creating project state.
3. Read, in order:
   - global `OPERATING_PRINCIPLES.md`;
   - project `.jstack/STATE.json`;
   - `.jstack/PROJECT_CHARTER.md` if present;
   - only the artifacts required for the current state.
4. Run `jstack-status` if available.

## Router behavior

- Prefer invoking the specialist skill. If the host cannot invoke nested skills, read `$JSTACK_HOME/skills/<specialist>/SKILL.md` (or the path from `~/.jstack/config.json`) and execute those instructions directly.
- State the current phase, gate status, stale evidence, and one recommended next action.
- If the user says “continue,” route to the next allowed specialist.
- If a human gate is pending, ask exactly one decision question through the relevant specialist.
- If an eval gate failed, name the failed check and the bounded repair action. Do not initiate repeated repair/retest cycles automatically.
- If an adversarial gate challenged the work, summarize challenge categories and stop for the human to choose which critiques to accept.

## Canonical routing

- no project state → `vision`
- `VISION_DRAFT` / vision HOLD → `vision`
- vision PASS, experience not locked → `experience`
- experience PASS, system not locked → `architecture`
- system PASS, premortem not locked → `premortem`
- premortem PASS, plan not locked → `plan`
- plan PASS, active lake absent or incomplete → `build`
- implementation complete, review missing/stale → `review`
- review PASS, QA missing/stale → `qa`
- all lakes PASS, release not approved → `release`
- shipped → `learn`

Never skip required gates because the user appears impatient. Offer the fastest valid path instead.
