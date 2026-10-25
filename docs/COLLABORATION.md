# J-stack OS — Collaboration

How the roles in `docs/AGENT_ROLES.md` work together. Gates stay in `docs/GATES.md`, the escalation boundary in `core/autonomy_boundary.md`. This is the mandatory collaboration contract for every host and session using this framework. It adds no lifecycle gate and grants no project execution approval.

Adopted by explicit founder instruction on 25 October 2026, extending the J-stack Collaboration Charter v1.0 (8 October 2026). Which host or session holds which role, milestone packets, and vendor rules are project matters: record them in the project's `.jstack/`.

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

**Parallelize eligible work by default; do not serialize independent authorized packages.** At planning, resumption and a blocker, inspect the dependency graph. Start ready work concurrently where separate ownership, resources and interfaces make it safe. If an eligible package is left serial, record the concrete dependency, access, capacity, cost or collision reason. Do not create artificial work merely to keep agents busy.

Each package names its outcome, prerequisites, interface/input revision, owner, isolated branch/worktree or resource set, allowed effects, acceptance evidence and integration owner. One writer per branch/worktree; no shared mutable execution directory or uncoordinated schema/API edits. Coordinate shared contracts first, freeze the agreed interface, then implement independent parts concurrently. Reconcile current main and run required integration checks before combining the results.

Parallel BUILD follows the receiving project's approved lake/milestone concurrency. Where one active lake is required, parallelize packages within that lake and permitted preparation elsewhere. A prerequisite blocks its dependent action, not every other authorized package. This rule does not open another lake, waive a packet lock, add paid model/API usage, duplicate irreversible tests or expand an exhausted correction budget. Disclose unavailable execution access rather than claim another session is working.



## Whole-outcome assignments and system coherence

Give an engineer a complete bounded result: investigation, implementation, critical failure/recovery behavior, meaningful verification, documentation, independent review and corrections already covered by the task. The human should not relay routine engineering steps. Map each building block to the customer outcome, producer/consumer interfaces, dependencies and acceptance examples; preserve vertical delivery rather than disconnected component piles.

Separate the coordinator, architecture/readiness engineer, implementation engineer and independent reviewer. Several sessions may fill those roles; record actual assignments and explicit handoffs in the project. A default role never transfers another session's branch. The author is not the sole reviewer of consequential work.

Before a consequential instruction, retrieve current state, authority map, roadmap, packet, decisions and applicable company-published beliefs/moat method. Check the relevant sources, not every file indiscriminately. Distinguish founder-adopted operating doctrine from unadopted context and private personal material. Frame value now and strength tomorrow where the project's direction framework requires it; utility/security enablers need no invented moat. Never publish private beliefs or profiles into a public framework.

## Delivery speed, review and stopping

Reuse applicable decisions and unchanged valid evidence. Continue routine work within existing authority without another permission question. Report review findings and correct them inside the actual human-set scope and convergence budget; the reviewer does not silently edit or self-approve. Repeated related findings require a root-cause inventory and the smallest coherent recovery, not another layer of tooling. A stop condition pauses the affected path while independent authorized work continues.

Verify requirements and interfaces, refusal/retry/recovery behavior, and integration proportional to risk. Required CI and independent review still run. Target no unresolved acceptance-blocking defects; no process promises zero bugs. Preserve limitations and residual decisions. Do not weaken a requirement, test or evidence claim to obtain PASS, and do not add ceremonial review cycles when no changed risk warrants them.

When only future dates, missing credentials or reserved decisions remain, record the blocker, owner and resumption condition, then end the turn. Do not create continuation loops, raise their cap or cancel scheduled safety/cleanup tasks. Use supported session controls for a built-in goal loop; do not invent a custom hook fix for an absent hook.

## Persistent context and output

At session start/resumption load this contract and the project's agent entrypoints, current refs/state and applicable decisions. Update the project's working agreement and durable decision record when explicit human instructions change the method. A chat memory, summary, repository file or instruction cannot guarantee that every future session has already loaded it; entrypoint retrieval is mandatory. Missing access or stale policy is disclosed before dependent consequential work.

Explain product outcome → roadmap stage → milestone promise → connected packages → concrete action. Keep updates short: delivered/verified, current critical dependency, ready parallel work, then any exact human decision needed and its deadline. Ask directly when/why input is needed; batch related prepared choices with recommendations. Do not end with an unexplained 'the next step is yours'. Never claim to have sent a handoff or started a remote session without actually doing so.
