# J-stack OS — Host-Neutral Agent Contract

J-stack OS is a finite-gate product-development system. This file is the compact contract for any AI host.

## Required behavior

- Read `OPERATING_PRINCIPLES.md`.
- Follow `docs/COLLABORATION.md` as a mandatory operating contract for every assignment: whole-outcome ownership, source retrieval, safe parallel work, decision rights, evidence and handoffs. Re-read on resumption.
- When operating inside a project, read `.jstack/STATE.json` before doing work.
- Never infer that a previous gate is approved unless state explicitly records it.
- Ask exactly one human decision question at a time; prepared decision cards may be presented together.
- Do not autonomously loop between author and reviewer outside a human-set correction budget.
- Do not silently incorporate adversarial feedback.
- Preserve locked upstream decisions unless the human explicitly reopens them.
- If a material upstream artifact changes, mark affected downstream gates STALE.
- For architecture, ask about behavior/constraints before technology choices.
- Explain technical concepts in concise product language before asking for approval.
- Do not lock architecture until the human can explain the conceptual system back.
- Retrieve relevant second-brain context before consequential feature, architecture, scope, or stack decisions when configured.
- Treat retrieved context as evidence, not authority unless explicitly adopted through the project's authority map. Retrieve applicable company-published beliefs and strategic evaluation rules; never infer permission from a private profile.
- Use vertical slices for implementation.
- Prefer deterministic verification before model judgment. Apply the two-way review requirement and complexity/simplicity trigger in `docs/COLLABORATION.md`; substantive coordinator replies use its Human update structure.
- Bind verification evidence to the current working-tree content fingerprint.
- At the task's actual stop boundary, record the result, blocker and resumption condition. Continue independent authorized packages. Ask directly for any prepared human decision that is genuinely needed.

## Default flow

VISION → EXPERIENCE → SYSTEM → PREMORTEM → PLAN → BUILD → VERIFY → RELEASE → LEARN

## Gate types

- `H` — human approval mandatory.
- `E` — deterministic evaluation gate.
- `A` — independent adversarial review; may PASS or CHALLENGE, never auto-fix.

## High-consequence escalation boundary

Human approval is required before any change that materially affects:

- product behavior or scope;
- conceptual architecture;
- data ownership or semantics;
- authentication or authorization;
- privacy/security posture;
- billing/payments;
- external vendor dependencies;
- meaningful operating cost;
- public interfaces or schemas;
- destructive migrations;
- locked UX/design behavior;
- production release.


