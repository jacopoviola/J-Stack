---
name: jstack-premortem
version: 1.0.0
description: Pre-build failure analysis and preventive roadmap for expensive bottlenecks.
allowed-tools: [Bash, Read, Grep, Glob, Write, Edit, AskUserQuestion]
---
# Premortem Gate
Prerequisite: system PASS.
Read locked architecture and context. Identify risks across security/auth, data, concurrency, migrations, third parties, payments, observability, backup/recovery, cost, scale, design/architecture contradictions, deployment and rollback. For each specify severity, likelihood, detection, prevention, contingency, residual risk, and trigger. Classify as MUST solve before build / design now implement in lake / monitor and defer / consciously accept. Ask one consequential question at a time. Ask to lock PREMORTEM. Stop.
