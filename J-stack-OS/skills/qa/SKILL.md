---
name: jstack-qa
version: 1.0.0
description: Bounded real-browser product QA against acceptance criteria; report-first, no automatic fix loop.
allowed-tools: [Bash, Read, Grep, Glob, Write, Edit, AskUserQuestion]
---
# QA Gate
Require fresh review evidence. Detect browser harness: project-configured → gstack browse if installed → Playwright → another explicit real-browser tool. If none, HOLD; never pretend visual QA happened. Run the active lake's browser acceptance plus consequential error/recovery states. Capture evidence. Compare with SCREEN_CONTRACTS/ACCEPTANCE. Save QA.md with fingerprint. Report-first; do not edit product code. Defects → HOLD and ask one question about bounded fixes. Objective PASS → ask human for lake acceptance. Stop.
