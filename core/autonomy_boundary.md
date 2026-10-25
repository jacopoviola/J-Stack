# Autonomy Boundary

The builder MAY decide without escalation:
- local variable/function names;
- internal file organization when interfaces do not change;
- straightforward library usage already approved by the stack;
- refactors that preserve behavior and contracts;
- test implementation details;
- minor optimizations with no user/system semantic impact.

The builder MUST HOLD and ask before changing:
- product behavior or scope;
- UX flow or locked visual behavior;
- architecture intent or system boundaries;
- persistence/data semantics or ownership;
- auth/authz/privacy/security posture;
- payments/billing;
- public API/schema contracts;
- external vendors/dependencies with meaningful lock-in or cost;
- destructive migrations;
- material operating cost;
- scaling assumptions;
- production release strategy;
- anything marked NON-NEGOTIABLE.

