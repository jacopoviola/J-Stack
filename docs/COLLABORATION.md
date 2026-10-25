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

Use this structure for substantive coordinator replies and work assignments. The first body paragraph is at most **200 characters**, excluding its heading: plain, respectful language understandable without technical background, explaining the outcome and immediate work. Detailed technical references belong in the session prompts or linked evidence. Short in-progress updates and direct factual answers may stay short; do not manufacture a multi-session assignment to fill a template.

```markdown
# Overall to do
<Plain-language outcome and immediate work; maximum 200 characters.>

## Session reference and prompt

SESSION A (model: <verified identifier, or unverified/proposed>):
<Existing task reference and what changed, plus a complete copyable prompt when a new instruction is actually needed; otherwise No new assignment.>

SESSION B (model: <verified identifier, or unverified/proposed>):
<Existing task reference and what changed, plus a complete copyable prompt when a new instruction is actually needed; otherwise No new assignment.>

CODEX (model: <verified identifier, or unverified/proposed>):
<Exact candidate/review scope and required evidence; otherwise No new assignment.>

## Paste back here
<Only the result needed for the coordinator's next decision: outcome, exact refs, evidence/review links, unresolved findings and any decision. Default: Nothing.>

### Founder ask
Nothing.
<Replace only when a genuine input/decision is required: direct question, recommendation, exact scope, needed-before point and consequence of waiting.>
```

Keep one combined session section; state which assignments can run in parallel and which depend on another result. Name actual roles/owners and task refs instead of transferring a branch from a default label. Do not imply a drafted prompt was sent or a session was started. Where a connected route is available and authorized, coordinate directly rather than make the founder relay routine steps. Request only missing results; never ask the founder to paste credentials, tokens, key material or raw sensitive logs.

Report actual configured model identifiers only when verified. If unavailable, say `unverified`; label a recommendation `proposed`, not running. Choose models for task complexity, tools and authorized availability; do not invent a best-model ranking or automatically switch/pay for a fallback. Preserve reviewer independence and pass current sources, exact refs, evidence and open questions when handing off or switching models. Default `Nothing` does not suppress a real reserved approval or missing input.

This supersedes the earlier Outcome/Flow/Status/Decision/Next presentation order; those facts are retained inside the concise result and session handoff, not added as competing headings.

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

## Two-way verification

**Two-way review — required for consequential changes.** Review consequential changes in both directions. Trace approved promises to executed evidence, and trace implemented permissions, state changes, side effects and recovery behavior back to their governing requirements. Independently challenge the expected results and tests. Verify the combined candidate across component boundaries. Report missing, unjustified or contradictory behavior before acceptance.

Use the existing packet, test matrix, review and evidence records. Check consequential behavior and required enabling infrastructure, not every variable or trivial function. Derive expected outcomes from the approved contract rather than mirroring the implementation; a passing mock or builder-written assertion cannot establish its own correctness. Integration checks cover relevant version mismatches, retries, concurrency and partial failure. Preserve valid unchanged evidence and existing review/correction limits; this creates no new lifecycle gate or mandatory full-system review for routine changes.

## Complexity and simplicity trigger

If the system becomes difficult to explain, delivery risks getting stuck, production code becomes hard to reason about, the UX gains effort/controls beyond the approved simple journey, or activities/packages/tools grow sharply relative to the approved plan, require a **bounded source-based review before expanding the affected path further**. State the observed signal, affected outcome and smallest decision to resolve; do not wait for a numerical complexity score.

Select the relevant top-down, bottom-up, integration, product-roadmap, company-safe belief/MOAT or UX review. Retrieve the governing documents and use the existing direction/recovery record; do not commission every review on every trigger. Work backward from the approved customer outcome, identify missing versus unnecessary complexity, and recommend the smallest coherent simplification. Keep the customer surface minimalist without hiding consequential failure, permissions or uncertainty. The founder retains control of consequential UX; proposed changes to locked behavior follow the existing approval/amendment route.

Pause only dependent unsafe or unapproved expansion. Continue independent authorized work, preserve scheduled safety/cleanup tasks, budgets and exhausted correction limits. Review is not authority to rewrite canon, add infrastructure, or restart a stopped repair loop. Report a concise result and ask the founder only for a consequential choice that remains after the authorized analysis.

## Delivery speed, review and stopping

Reuse applicable decisions and unchanged valid evidence. Continue routine work within existing authority without another permission question. Report review findings and correct them inside the actual human-set scope and convergence budget; the reviewer does not silently edit or self-approve. Repeated related findings require a root-cause inventory and the smallest coherent recovery, not another layer of tooling. A stop condition pauses the affected path while independent authorized work continues.

Verify requirements and interfaces, refusal/retry/recovery behavior, and integration proportional to risk. Required CI and independent review still run. Target no unresolved acceptance-blocking defects; no process promises zero bugs. Preserve limitations and residual decisions. Do not weaken a requirement, test or evidence claim to obtain PASS, and do not add ceremonial review cycles when no changed risk warrants them.

When only future dates, missing credentials or reserved decisions remain, record the blocker, owner and resumption condition, then end the turn. Do not create continuation loops, raise their cap or cancel scheduled safety/cleanup tasks. Use supported session controls for a built-in goal loop; do not invent a custom hook fix for an absent hook.

## Persistent context and output

At session start/resumption load this contract and the project's agent entrypoints, current refs/state and applicable decisions. Update the project's working agreement and durable decision record when explicit human instructions change the method. A chat memory, summary, repository file or instruction cannot guarantee that every future session has already loaded it; entrypoint retrieval is mandatory. Missing access or stale policy is disclosed before dependent consequential work.

Explain product outcome → roadmap stage → milestone promise → connected packages → concrete action. Keep updates short: delivered/verified, current critical dependency, ready parallel work, then any exact human decision needed and its deadline. Ask directly when/why input is needed; batch related prepared choices with recommendations. Do not end with an unexplained 'the next step is yours'. Never claim to have sent a handoff or started a remote session without actually doing so.

