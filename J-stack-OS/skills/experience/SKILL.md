---
name: jstack-experience
version: 1.1.0
description: Turn visual references and user flows into a complete visual prototype and locked experience contract before production implementation.
allowed-tools: [Bash, Read, Grep, Glob, Write, Edit, AskUserQuestion]
---
# Experience Gate
Prerequisite: vision PASS.

## A — Map intent
Read the locked Product Constitution/MLP, every supplied screenshot/mockup, and the user-flow description. Build USER_FLOWS, SCREEN_MAP, SCREEN_CONTRACTS, and STATE_MATRIX without backend architecture assumptions.

## B — Complete visual prototype
Using the chosen design-capable coding environment (Claude Code/design tooling initially), implement **all MLP screens and meaningful states** as an interactive visual prototype. Mock data and temporary wiring are allowed. Loading, empty, error, validation, permission, success, recovery, and responsive states must exist where meaningful.

Write `PROTOTYPE_CONTRACT.md` recording where the prototype lives, what is mocked, what is complete, and any deviations.

**Critical rule:** prototype frontend code is the visual/interaction source of truth but is not automatically canonical production code. Production implementation begins only after SYSTEM → PREMORTEM → PLAN lock.

## C — Visual verification
Use a real browser if available to compare the prototype with reference screenshots and screen contracts. Record deviations in `VISUAL_ACCEPTANCE.md`. Never claim visual verification from code inspection alone.

## D — Human lock
Ask exactly one product/design decision question at a time. Use second-brain evidence when it can materially change relevance/priority. Before lock, ensure every core MLP outcome maps to a complete flow and every flow has every required screen/state.

Ask one final question: lock EXPERIENCE? Only explicit human approval passes. Stop.
