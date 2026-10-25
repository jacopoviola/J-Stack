---
name: jstack
metadata:
  version: "1.0.0"
description: J-stack OS router. Read project state and route the next finite product-development action when asked to use J-stack, continue the build, explain where we are, or identify what is next.
allowed-tools: [Bash, Read, Grep, Glob, Write, Edit, AskUserQuestion]
---

# J-stack OS Router

You are the orchestration layer, not the main author.

## Start

1. Find the nearest project root containing `.git` or `.jstack`.
2. If `.jstack/STATE.json` does not exist, tell the user to run `jstack-init` or invoke the `vision` skill only after creating project state.
3. Read, in order:
   - global `OPERATING_PRINCIPLES.md`;
   - global `AGENTS.md` and `docs/COLLABORATION.md` as mandatory workflow rules;
   - project `.jstack/STATE.json`;
   - project authority map, agent entrypoints, adopted direction/belief/MOAT sources and current applicable decision record;
   - `.jstack/PROJECT_CHARTER.md` if present;
   - only the artifacts required for the current state.
4. Run `jstack-status` if available.

## Router behavior

- Prefer invoking the specialist skill. If the host cannot invoke nested skills, read `$JSTACK_HOME/skills/<specialist>/SKILL.md` (or the path from `~/.jstack/config.json`) and execute those instructions directly.
- Explain the product outcome, roadmap stage, milestone and current critical dependency before details. State current phase/gates/evidence and identify ready independent packages; start safe authorized work concurrently under the collaboration contract or name the actual blocker.
- If the user says “continue,” route to the next allowed specialist.
- If a human gate is pending, ask exactly one decision question through the relevant specialist.
- If an eval or adversarial gate failed, report findings and use the existing human-set correction budget where it actually applies. Stop the affected path at missing authority, a material contract conflict or the budget's convergence boundary; continue independent authorized work. Never infer an unlimited repair/retest loop.
- If only future dates, credentials or reserved decisions remain, record the blocker and resumption condition and end the turn without a continuation loop. Ask directly for any prepared decision that is needed.

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

