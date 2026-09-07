---
name: jstack-architecture
version: 1.0.0
description: Behavior-first conceptual architecture, tech-stack decision, teach-back, and one independent adversarial review.
allowed-tools: [Bash, Read, Grep, Glob, Write, Edit, AskUserQuestion]
---
# System Gate
Prerequisites: vision + experience PASS.

## Rule zero
The human owns WHY + WHAT inside architecture too. Never begin by asking them to choose technologies.

## A — Behavioral interrogation
Ask one question at a time about ownership/permissions, concurrency, latency, background work, persistence/history, failure tolerance, recovery, integrations, privacy/security, traffic/data, cost sensitivity, and operator constraints.
For each relevant concept, teach: PROBLEM → CONCEPT → OUR CHOICE → WHY → ALTERNATIVE.

## B — Conceptual architecture
Produce conceptual architecture, system map, data model, invariants, failure model, and scale assumptions in language the human can explain.

## C — Tech stack gate
Search before building. Compare 2–3 credible options on correctness, solo simplicity, reliability, appropriate $20k-MRR-class headroom, observability/security, incremental scaling, and accidental complexity. Railway is allowed to win; it is not mandated.

## D — Teach-back H gate
Ask the human to explain the system back. Clarify one consequential misunderstanding at a time. Do not lock until comprehension is sufficient.

## E — Adversarial A gate
Invoke the configured independent reviewer once, read-only. Attack security, concurrency, data semantics, migrations, failure paths, cost/scaling cliffs, and unnecessary complexity. It outputs APPROVE or CHALLENGE.
Triage AGREE / DISAGREE / NEEDS HUMAN CONTEXT. Do not modify files from critique until the human authorizes changes.

Ask one final question: lock SYSTEM? Only explicit human approval passes. Stop.
