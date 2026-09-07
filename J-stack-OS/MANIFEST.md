# J-stack OS 0.1.0 — Manifest

## Core
- `SKILL.md` — router
- `AGENTS.md` — host-neutral contract
- `CLAUDE.md` — Claude Code adapter
- `OPERATING_PRINCIPLES.md` — invariants
- `core/state_machine.json` — finite workflow states
- `core/gates.json` — gate types and required artifacts
- `core/autonomy_boundary.md` — what AI may/may not decide alone

## User-facing skills
- vision
- experience
- architecture
- premortem
- plan
- build
- review
- qa
- release
- learn

## Internal roles
- context analyst
- adversary
- architecture teacher

## Local helpers
- `jstack-init` — bootstrap `.jstack/` in a repo
- `jstack-status` — show current phase/gates
- `jstack-config` — global config
- `jstack-context` — cheap local Obsidian retrieval
- `jstack-evidence` — content-bound test evidence
- `jstack-gate` — explicit gate/phase state changes
- `jstack-doctor` — environment check

## Project state
`project-template/.jstack/` contains the complete artifact skeleton copied into each initialized repo.
