# J-stack OS

**J-stack OS** is a finite, human-governed AI product-development operating system for a non-technical founder/PM who wants to own a software product from vision to production while becoming technically fluent in the process.

It is intentionally **not an autonomous coding loop**. Every meaningful stage ends at an explicit gate:

- **PASS** — advance to the next named state.
- **HOLD** — a human decision is required.
- **FAIL** — return to a named previous gate.

No agent may self-iterate indefinitely. No agent may silently change locked product intent, architecture intent, data semantics, security posture, external dependencies, cost structure, or UX behavior.

## Core mental model

**You own WHY + WHAT, including architectural intent.**

AI translates intent into technical options, explains consequences, implements approved decisions, and verifies what can be verified objectively. Independent models challenge plans and code. Deterministic systems test reality. You retain the final signature.

The system follows:

**VISION → EXPERIENCE → SYSTEM → PREMORTEM → PLAN → BUILD → VERIFY → RELEASE → LEARN**

The operating principle underneath it is:

> Human control decreases only as uncertainty decreases.

## Product quality target

J-stack optimizes for a **production-credible Minimal Lovable Product (MLP)**, not a disposable hackathon MVP and not premature hyperscale infrastructure.

The default target is a product that can plausibly sustain meaningful production traffic and a solo-founder path to roughly **$20k MRR** without a foundational rewrite. If a competent technical investor audited the system tomorrow, the goal is to show:

- a simple and well-reasoned architecture;
- explicit scaling assumptions and known boundaries;
- proper auth/authz and data semantics;
- tested critical paths;
- observable failures;
- sane deployment and migration discipline;
- documented major decisions;
- minimal accidental complexity;
- a clear path to scale through incremental changes rather than a rewrite.

## Quick start

```bash
cd ~/J-stack-OS
./setup.sh --host claude

cd /path/to/your/project
jstack-init
claude
```

Then say:

> `Use J-stack. Where are we?`

or invoke the router skill if your Claude Code installation exposes it as a slash command.

## Folder model

```text
~/J-stack-OS/          # Global operating system, skills, rules, scripts
project/.jstack/       # Project-specific state, decisions, specs, evidence
```

J-stack does not depend on conversation history for continuity. The project state lives in `.jstack/`.

## Primary roles

- **Founder / Product Director — Human:** final authority on product, taste, prioritization, architecture intent, tradeoffs, and release.
- **Primary Partner — Claude Code initially:** interrogator, architecture translator, planner, builder, explainer.
- **Adversary — Codex initially:** independent read-only challenge of plans/architecture/code. Recommends; never commands.
- **Context Analyst — host-neutral:** retrieves relevant evidence from the local Obsidian second brain and project memory.
- **Verifier — deterministic where possible:** tests, type checks, migrations, browser QA, screenshots, security checks, performance checks, evidence freshness.

Hosts are intentionally replaceable. The process is the product; Claude/Codex are adapters.

## One-question rule

Any skill that requires human reasoning MUST ask exactly **one decision question at a time** using this format:

```text
CONTEXT
Why this decision matters now.

QUESTION
One decision only.

RECOMMENDATION
The agent's recommended option and why.

OPTIONS
A. ...
B. ...
C. ...
D. Other / explain in my own words
```

The agent must wait for the answer before asking the next question. Decisions already prepared for one lake or milestone may instead be presented together as decision cards; see `docs/COLLABORATION.md`.

## Architecture-learning invariant

J-stack may not lock architecture until the human can explain the conceptual system back in plain language. The agent must ask about desired behavior and constraints before technologies.

Bad question:

> Redis or Kafka?

Good question:

> If a background job takes 90 seconds and the user closes the browser, must the job continue and the result still be available later?

The agent then translates the behavioral answer into technical options, teaches the relevant concept briefly, and asks for approval.

## No-loop rule

J-stack contains **no unbounded autonomous loops**.

A reviewer may review once per invocation. A verifier may run a bounded deterministic test suite. A fix requires an explicit human-authorized action. Re-review happens only after a human chooses to run it again, or inside a correction budget the human set in advance.

See `docs/WORKFLOW.md`, `docs/GATES.md`, `docs/AGENT_ROLES.md`, and `docs/COLLABORATION.md`.
