# J-stack OS — Production-Credible MLP Standard

The target is deliberately between a disposable MVP and a scale-up platform.

Default architecture should plausibly support a solo-founder path to approximately $20k MRR and meaningful production traffic without a foundational rewrite. Exact load targets are set per product during SYSTEM.

A competent technical reviewer should see:
- requirements translated into explicit architecture choices;
- a boring/simple stack where sufficient;
- clear reasons for non-boring components;
- strong auth/data/billing/secrets boundaries;
- migration discipline;
- deterministic tests for critical paths;
- observability and actionable errors;
- appropriate backup/recovery;
- cost/scaling assumptions and thresholds;
- low accidental coupling;
- no unnecessary microservices/distributed systems;
- reproducible deployment;
- explicit technical debt rather than surprises.

A J-stack MLP should not knowingly ship fake core functionality, critical placeholder flows, unaudited destructive migrations, obvious auth/authz flaws, critical paths with no tests, or demo-only architecture when normal growth is expected.

It also should not prematurely require Kubernetes, microservices, Kafka, multi-region infrastructure, or custom infrastructure when mature managed services are sufficient.
