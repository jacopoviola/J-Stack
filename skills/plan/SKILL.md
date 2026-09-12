---
name: jstack-plan
version: 1.0.0
description: Convert locked intent into an executable vertical-slice development plan with acceptance and test contracts.
allowed-tools: [Bash, Read, Grep, Glob, Write, Edit, AskUserQuestion]
---
# Plan Gate
Prerequisites: vision, experience, system, premortem PASS.
Read all locked artifacts. Decompose MLP into bounded vertical lakes. For each define outcome, scope, dependencies, acceptance, data/permission implications, failure behavior, deterministic verification, browser QA, and human acceptance. Define global test matrix, observability, and release strategy. Keep lakes small enough for independent review; prefer bounded PRs over giant diffs. As a default review-context heuristic, target <~1,000 changed lines per independently reviewed change when practical, without destroying vertical-slice cohesion. Invoke one independent plan review. Triage findings without auto-revision. Ask to lock PLAN. Stop.
