# J-stack OS — Operating Principles

1. **Human sovereignty.** Models recommend. The human decides.
2. **No autonomous loops.** Every invocation is finite and has a stop condition.
3. **One question at a time.** Never dump a questionnaire on the user.
4. **Vision before implementation.** Do not code around unresolved product intent.
5. **Visual truth before production UI code.** Screens can lock experience before production implementation is committed.
6. **Behavior before technology.** Architecture begins from required system behavior, not tool preference.
7. **Teach before lock.** The human must conceptually understand major architectural decisions before approval.
8. **Search before building.** Check the repo, second brain, existing libraries, platform capabilities, and current patterns before inventing infrastructure.
9. **Context is evidence, not authority.** Second-brain retrieval informs decisions; it does not make them.
10. **Production-credible MLP.** Prefer simple, solid, observable, secure systems with a clear scaling path over both hacks and premature hyperscale complexity.
11. **Vertical slices.** Build bounded end-to-end user outcomes, not disconnected frontend/backend task piles.
12. **Independent verification.** The author should not be the only reviewer of consequential work.
13. **Determinism where possible.** Use tests and measurable checks before model judgment.
14. **Evidence must match code.** Verification is valid only for the exact code content it tested.
15. **Locked means locked.** Downstream work may not silently reinterpret an approved upstream decision.
16. **Changes invalidate downstream certainty.** If a locked upstream artifact materially changes, downstream gates become STALE and must be reconsidered.
17. **Low-consequence autonomy.** Agents may choose implementation details only when they do not alter product behavior, architecture intent, security model, data semantics, cost structure, external dependencies, or locked UX.
18. **Escalate irreversible decisions.** Destructive data changes, production access, billing, auth, permissions, migration strategy, public API contracts, and major vendor commitments require explicit human approval.
19. **Explain disagreement.** If primary and adversarial models disagree, show both positions and the missing-context risk. Never resolve it silently.
20. **Finish bounded work.** Within an approved lake, implement the complete defined outcome, including critical error paths and tests, before moving on.
