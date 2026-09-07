# J-stack OS — Gate Specification

## Gate semantics

- `PASS`: criteria satisfied; next state allowed.
- `HOLD`: human decision or missing evidence required.
- `FAIL`: objective criteria failed; return to a named previous action.
- `STALE`: prior evidence/approval no longer matches current upstream artifacts or code.
- `PENDING`: not yet evaluated.

## H — Human gate

AI cannot self-pass an H gate.

Required H gates:
1. Product Constitution / MLP definition
2. User experience lock
3. Conceptual architecture + tech stack lock
4. Premortem/residual-risk acceptance
5. Development plan lock
6. Each meaningful vertical lake acceptance
7. Production release

## E — Evaluation gate

Use when success can be measured objectively: test exits, schema/migration checks, browser acceptance, performance budgets, fresh evidence, etc. A model may interpret results, but may not turn a failed objective check into PASS based on confidence.

## A — Adversarial gate

An independent model reviews a frozen artifact or code snapshot **once per invocation**.

Output must be `APPROVE` or `CHALLENGE`.

For CHALLENGE include severity, exact concern, concrete failure scenario, evidence/reference, proposed mitigation, and confidence.

The primary model triages into AGREE / DISAGREE / NEEDS HUMAN CONTEXT. It may not revise automatically.

## Staleness

```text
VISION change
  → EXPERIENCE, SYSTEM, PREMORTEM, PLAN, affected LAKES, RELEASE stale

EXPERIENCE change
  → SYSTEM when behavior/data assumptions change; PLAN, affected LAKES, RELEASE stale

SYSTEM change
  → PREMORTEM, PLAN, affected LAKES, RELEASE stale

PREMORTEM preventive decision change
  → PLAN, affected LAKES, RELEASE stale

PLAN change
  → affected LAKES and RELEASE stale

CODE change
  → code-bound E/A/QA evidence stale
```

Cosmetic edits that do not alter meaning need not invalidate downstream gates; the agent must explain why before preserving PASS.

## Review scope budget

Default target: keep one independently reviewed change below roughly **1,000 changed lines** when practical. If a diff materially exceeds this, split it into coherent PRs/lakes before adversarial review unless splitting would destroy the ability to reason about the feature end-to-end. This is a review-context heuristic, not a product-scope limit.
