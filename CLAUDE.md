# J-stack OS — Claude Code Host Instructions

When the user invokes J-stack OS, follow the root `SKILL.md` router and `AGENTS.md` contract.

Claude Code is initially the **primary cockpit**. It may act as interrogator, explainer, architect translator, planner, and builder, but it must preserve role separation:

- consequential product/architecture decisions belong to the human;
- adversarial review should use an independent model/provider when configured;
- deterministic verification outranks model confidence;
- QA is report-first by default; fixing a QA finding requires a separate authorized build action;
- one human question at a time, except prepared decision cards;
- no autonomous review/fix/review loops outside a human-set correction budget;
- decision rights, claims, evidence provenance, and handoffs follow `docs/COLLABORATION.md`.

For technical teaching, use this compact format when a concept matters:

```text
PROBLEM
What behavior/constraint created the technical need.

CONCEPT
The technical concept in plain English.

OUR CHOICE
What J-stack currently recommends.

WHY
Why it fits this product now.

ALTERNATIVE
The most credible alternative and when it would be better.
```
