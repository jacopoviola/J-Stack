---
name: jstack-review
version: 1.0.0
description: Finite independent review of a code snapshot; deterministic checks first, adversarial review second, no auto-fix loop.
allowed-tools: [Bash, Read, Grep, Glob, Write, Edit, AskUserQuestion]
---
# Review Gate
Capture working-tree fingerprint. If the review diff is materially >~1,000 changed lines, HOLD first and recommend coherent splitting unless the change cannot be reasoned about correctly when split. Run deterministic test-matrix commands through `jstack-evidence run` where possible. If a required check fails, FAIL and stop; do not auto-fix. If deterministic checks pass, invoke an independent read-only code reviewer once. Reviewer outputs APPROVE or CHALLENGE with severity, scenario, evidence, confidence, and mitigation. Save REVIEW.md with fingerprint. Primary host may triage but not modify code in this invocation. CHALLENGE → HOLD and ask one question about a bounded fix set/rejection/investigation; if the lake SPEC records an unspent correction budget and every finding is inside it (`docs/GATES.md`), record the round and route to `build` instead. APPROVE → record PASS and stop. QA is separate.
