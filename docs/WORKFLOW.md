# J-stack OS — End-to-End Workflow

## 0. Boot / Project initialization

**Goal:** create durable project state independent of chat history.

Output: `.jstack/` project workspace and `STATE.json`.

Gate: none.

---

## 1. VISION

**Owner:** Human + Primary Partner  
**Gate:** H

Inputs:
- founder vision;
- company/product context;
- second-brain evidence where relevant;
- existing product/brand materials.

Outputs:
- `00_constitution/COMPANY_VISION.md`
- `00_constitution/PRODUCT_VISION.md`
- `00_constitution/BRAND_BOOK.md`
- `00_constitution/PRODUCT_PRINCIPLES.md`
- `00_constitution/DESIGN_PRINCIPLES.md`
- `00_constitution/NON_NEGOTIABLES.md`
- `00_constitution/ANTI_GOALS.md`
- `MLP_DEFINITION.md`

The Primary Partner interrogates one question at a time. It challenges framing, but cannot redefine the company direction without approval.

PASS when the human explicitly locks the Product Constitution and MLP definition.

---

## 2. EXPERIENCE

**Owner:** Human + Primary Partner / Design-capable host  
**Gate:** H

Inputs:
- locked Product Constitution;
- screenshots/mockups/prototypes;
- user-flow description;
- relevant user research / second-brain evidence.

Outputs:
- `01_experience/USER_FLOWS.md`
- `01_experience/SCREEN_MAP.md`
- `01_experience/SCREEN_CONTRACTS.md`
- `01_experience/STATE_MATRIX.md`
- `01_experience/EXPERIENCE_DECISIONS.md`
- screenshots/reference assets.

Must cover core flows plus loading, empty, error, permission, success, responsive, and recovery states where relevant. The EXPERIENCE phase includes a **complete interactive visual prototype of all MLP screens**, using mock data/temporary wiring where necessary, plus real-browser visual verification when a harness is available.

The visual prototype is the **experience source of truth**, not automatically canonical production code. Production implementation begins only after SYSTEM → PREMORTEM → PLAN lock.

PASS only after human experience approval.

---

## 3. SYSTEM

**Owner:** Human architectural intent + Primary Partner technical translation  
**Gates:** H + A

### 3A. Conceptual architecture

Ask behavioral questions about concurrency, failure tolerance, persistence, ownership/permissions, latency, background work, external integration behavior, security/privacy, traffic/revenue assumptions, and recovery.

Outputs:
- `02_system/CONCEPTUAL_ARCHITECTURE.md`
- `02_system/SYSTEM_MAP.md`
- `02_system/DATA_MODEL.md`
- `02_system/INVARIANTS.md`
- `02_system/FAILURE_MODEL.md`
- `02_system/SCALE_ASSUMPTIONS.md`

### 3B. Technical stack gate

Only after behavior is understood, compare credible stack options using fit to requirements, one-operator simplicity, failure surface, expected cost, scaling headroom, ecosystem maturity, lock-in, deployment ergonomics, auditability, and migration path.

Outputs:
- `02_system/TECH_STACK.md`
- ADRs under `02_system/ADR/`.

### Teach-back requirement

Before SYSTEM can PASS, ask the human to explain the architecture back in their own words. Clarify gaps until the explanation is conceptually correct.

### Adversarial review

Run one independent read-only architecture review. Output APPROVE or CHALLENGE. Do not revise automatically. Human chooses accepted critiques; primary model records rejected critiques with rationale.

PASS only after human architecture lock.

---

## 4. PREMORTEM

**Owner:** Primary Partner + Context Analyst + Adversary  
**Gate:** H

Check security/auth/authz, data-model traps, migrations, concurrency, background jobs, idempotency, payments, third-party outages, observability, backup/recovery, cost/scaling cliffs, design/technical contradictions, vendor lock-in, release/rollback, and relevant privacy/legal constraints.

Outputs:
- `03_premortem/RISKS.md`
- `03_premortem/BOTTLENECKS.md`
- `03_premortem/PREVENTIVE_DECISIONS.md`

PASS when the human accepts the preventive roadmap and residual risk.

---

## 5. PLAN

**Owner:** Primary Partner  
**Gates:** A + H

Outputs:
- `04_plan/PLAN.md`
- `04_plan/MLP_SCOPE.md`
- `04_plan/BUILD_ORDER.md`
- `04_plan/ACCEPTANCE_CRITERIA.md`
- `04_plan/TEST_MATRIX.md`
- `04_plan/OBSERVABILITY_PLAN.md`
- `04_plan/RELEASE_STRATEGY.md`

Plan MUST be decomposed into bounded vertical lakes. Every lake must deliver a user-observable or system-complete outcome with explicit acceptance criteria.

Run one independent plan challenge. Human decides which recommendations to accept.

PASS only on explicit human plan lock.

---

## 6. BUILD — one lake at a time

For each lake create:

```text
.jstack/05_lakes/LAKE-###-slug/
  SPEC.md
  ACCEPTANCE.md
  IMPLEMENTATION_NOTES.md
  DECISIONS.md
  REVIEW.md
  QA.md
  EVIDENCE.md
```

The accountable owner reads current state, applicable adopted direction/belief rules, the lake contract and relevant upstream interfaces. Split the complete outcome into dependency-linked packages and start independent authorized work concurrently under `docs/COLLABORATION.md`. One active lake does not require one active engineer. Future-milestone work remains preparation unless its BUILD is authorized by the receiving plan.

Own implementation, critical error/recovery paths, documentation, validation and a review-ready result. Corrections and re-review are allowed only within the existing human-set budget; no unapproved or unbounded loop. Hand the frozen candidate to VERIFY. A blocker pauses dependent work, while other ready authorized packages continue.

---

## 7. VERIFY

Verification is a sequence of finite gates, not a loop. Repair and re-review repeat only inside a human-set correction budget (`docs/GATES.md`).

### 7A. Deterministic checks — E
Compilation/type checking, lint, unit/integration/contract tests, migration validation, security/static checks, accessibility, performance, and critical-path coverage as applicable. Evidence is fingerprinted against current working-tree content.

### 7B. Independent code review — A
Reviewer is read-only by default. It produces PASS or CHALLENGE. No automatic fixes.

### 7C. Browser/product QA — E + human judgment
Use a real browser against the running application. Exercise acceptance and consequential error states. QA is report-first.

### 7D. Human lake acceptance — H
Human verifies that the implemented behavior remains the intended product. PASS freezes the lake unless explicitly reopened.

---

## 8. RELEASE

Required: all planned lakes accepted, fresh critical evidence, migrations reviewed, environment/secrets checked, production observability ready, backup/rollback appropriate to risk, docs current, no unresolved critical/high findings, and human approval.

Deploy once. Run bounded production smoke checks. No self-healing deployment loop.

---

## 9. LEARN

Capture user behavior, escaped defects, architecture assumptions, cost/performance surprises, product learnings, operational learnings, and new second-brain knowledge. Append history; do not rewrite it.

