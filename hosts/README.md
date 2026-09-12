# Host Adapters

J-stack process is host-neutral. Initial mapping: Claude Code primary cockpit, Codex adversary, GitHub source control, detected real-browser QA.

`setup.sh --host claude` installs for Claude Code. `setup.sh --host codex` installs a host-neutral copy under `${CODEX_HOME:-~/.codex}/skills/jstack/`.

Kimi or another coding host can be added later by pointing it at `AGENTS.md`, `OPERATING_PRINCIPLES.md`, project `.jstack/STATE.json`, and the relevant skill.
