# J-stack OS — Collaboration

How the roles in `docs/AGENT_ROLES.md` work together. Gates stay in `docs/GATES.md`, the escalation boundary in `core/autonomy_boundary.md`. This file adds no gate and grants no approval.

Derived from the J-stack Collaboration Charter v1.0 (8 October 2026). Which host or session holds which role, milestone packets, and vendor rules are project matters: record them in the project's `.jstack/`.

## Authority

- Only an explicit human decision is a decision. A recommendation, a drafted approval, an agent's interpretation, or a builder-recorded deviation is not one.
- Reuse an approval within its stated scope without asking again. Never extend it by analogy to a new vendor, environment, cost, feature, or security tradeoff.
- Keep approved requirements, proposals, assumptions, observations, and open decisions distinct. Repeating an assumption in several artifacts does not approve it.
- Records preserve traceability; they cannot manufacture authorization.
- Disclose missing access, attachments, or session visibility. Never replace them with a claim of verification.

## Decision rights

| Decision | Owner | Gate |
|---|---|---|
| Product promise, workflow, UX, business rule, scope | Human | H |
| Vendor or architecture-significant component | Human | H |
| Routine implementation inside approved scope | Builder | none; `core/autonomy_boundary.md` |
| Whether a candidate meets the technical contract | Adversary + Verifier | A + E |
| Change to a locked artifact or acceptance criterion | Human | reopen the gate; downstream goes STALE |
| Lake acceptance, release | Human | H |
| Merge, provisioning, deploy, paid activity, external submission | Whoever holds that authorization | verify scope, environment, and candidate immediately before acting |

Architecture-significant means it affects authentication, cryptography, persistent data, queues, external interfaces, recurring cost, or operating responsibility. Open source is not automatically routine.

## Claims

Never infer one claim from another.

| Claim | Established by |
|---|---|
| Proposal review APPROVE | A gate on a frozen plan or spec; says the proposal is coherent, nothing about code |
| Technical PASS | E + A gates on one code fingerprint, within stated limits |
| Human acceptance | H gate on a demonstrated result |
| Merged and verified | Target branch contains the change and post-merge checks ran |
| Lake closed | Every acceptance and closeout obligation recorded |
| Release ready | RELEASE gate |

These are distinctions, not an extra approval ladder. Follow the project's gate sequence and do not ask twice for the same scope.

## Evidence provenance

Every evidence record names the candidate (fingerprint or commit), environment, scope, result, and **executor**: builder, reviewer, CI, or reviewer-authored/builder-executed. The last is not reviewer-executed testing.

- A PASS covers only the bytes it tested. A change after review leaves the earlier verdict tied to its original scope.
- Keep failures, superseded results, and limits in the record.
- A local mock, a different host, or a related model is not proof for the selected production route.

## Decision cards

Interrogation stays one question at a time (`OPERATING_PRINCIPLES.md` 3). Decisions already prepared for one lake or milestone may be presented together, one card each. No card is approved by silence.

```text
Decision:
User/operator consequence:
Recommended choice and reason:
Meaningful alternative and tradeoff:
Evidence and uncertainty:
Needed before:
Exact scope of approval requested:
```

## Human update

Lead with the conclusion; omit empty sections; keep test totals, logs, and code detail in the lake record.

1. **Outcome** — what changed for a customer or operator.
2. **Flow** — what happens now, including the important failure path.
3. **Status** — built, reviewed, proven, still pending.
4. **Decision** — only when one is required, as a decision card.
5. **Next** — the next complete package.

## Handoff

For builder → reviewer and session → session.

```text
Goal and approved scope:
Baseline and exact candidate:
What changed and why:
Requirements and acceptance mapping:
Tests, results and execution provenance:
Known failures, limits and superseded evidence:
Decisions already approved / still open:
Reviewer task or next owner:
Allowed actions and stop conditions:
```

## Parallel sessions

Every package has one accountable owner. Every branch or worktree has one writer at a time; a session does not modify another's work without an explicit handoff. Parallel preparation is allowed; BUILD concurrency follows the project's plan.
