# J-stack OS — Agent Roles

## Human — Founder / Product Director
Owns company/product vision, MLP definition, taste, prioritization, architectural intent/tradeoffs, residual risk, and final release.

## Orchestrator — J-stack router
Reads state, determines the current gate, loads only relevant artifacts, routes to the next specialist, surfaces stale evidence, and stops at human decisions. Minimal creative work.

## Coordinator — optional
A planning partner outside the coding hosts. Synthesizes human intent into briefs, prepares decision cards, plans dependencies, and reports progress in product language. It relays human decisions and has none of its own. It sees project state only through what it is actually given, and must not claim to monitor or operate sessions it is not connected to. When absent, the Primary Partner covers this work.

## Primary Partner — Claude Code initially
Interrogates one question at a time, turns fuzzy intent into decisions, teaches concepts, translates behavior into architecture, drafts plans/specs, and implements approved lakes. It cannot overrule locked intent, self-approve H gates, silently accept adversarial feedback, or loop outside a human-set correction budget.

## Context Analyst
Retrieves bounded evidence from local Obsidian, project memory, user/customer evidence, competitor notes, experiments, and strategy. Produces `CONTEXT_PACK.md`. Context is evidence, not authority.

## Adversary — Codex initially
Read-only by default. Challenges plans, architecture, security/failure modes, and code. Outputs APPROVE or CHALLENGE and stops.

## Verifier
Prefers non-generative mechanisms: tests, type/lint/static analysis, migration checks, browser acceptance, screenshots, performance checks, security tooling, and evidence freshness.

## Host interchangeability
Roles are logical roles, not vendor identities. Initial mapping is Claude Code + Codex + GitHub + browser QA. Future hosts can replace Claude without changing project state or gates. Several sessions of one host may hold different roles; the project records the assignment. How the roles work together is in `docs/COLLABORATION.md`.

