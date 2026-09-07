---
name: jstack-release
version: 1.0.0
description: Production release gate with evidence freshness, migration, observability, rollback, and explicit human approval.
allowed-tools: [Bash, Read, Grep, Glob, Write, Edit, AskUserQuestion]
---
# Release Gate
Verify plan locked, all required lakes accepted, evidence fresh, no unresolved critical/high findings, migrations reviewed, secrets/environment correct, auth/billing relevant config checked, observability ready, backup/recovery and rollback appropriate. Run bounded preflight; deterministic failure is FAIL. Summarize impact/risk/rollback/cost/smoke plan. Ask one question: approve production release? Only explicit approval deploys. Deploy once, run bounded smoke checks, no self-healing redeploy loop. On PASS mark SHIPPED and stop.
