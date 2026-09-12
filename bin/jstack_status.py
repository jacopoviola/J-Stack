#!/usr/bin/env python3
import json
from pathlib import Path

p=Path.cwd().resolve()
while p!=p.parent and not (p/'.jstack'/'STATE.json').exists(): p=p.parent
sp=p/'.jstack'/'STATE.json'
if not sp.exists(): print('No .jstack/STATE.json found. Run jstack-init.'); raise SystemExit(1)
s=json.loads(sp.read_text())

# gate types come from the J-stack install (core/gates.json), not from project state
GATES={}
try:
    GATES=json.loads((Path(__file__).resolve().parent.parent/'core'/'gates.json').read_text()).get('gates',{})
except Exception:
    pass

print(f"Project: {s.get('project_name')}\nPhase:   {s.get('phase')}\nLake:    {s.get('active_lake') or '-'}\nGates:")
for k,v in s.get('gates',{}).items():
    t=GATES.get(k,{}).get('type')
    print(f'  {k:12} {v}' + (f'   [{t}]' if t else ''))
if s.get('open_decisions'):
 print('Open decisions:'); [print('  - '+str(x)) for x in s['open_decisions']]
print(f"Next: {s.get('next_recommended_skill') or '-'}")

# Blocking gate = first gate in canonical order that is not PASS (matches router routing).
blocking=next((k for k,v in s.get('gates',{}).items() if v!='PASS'), None)
if blocking:
    t=GATES.get(blocking,{}).get('type','')
    st=s['gates'][blocking]
    if 'H' in t:
        print(f"Blocking gate: {blocking} ({st}) — type {t}: HUMAN APPROVAL REQUIRED TO PASS. AI cannot self-pass.")
    elif t:
        print(f"Blocking gate: {blocking} ({st}) — type {t}.")
    else:
        print(f"Blocking gate: {blocking} ({st}).")
else:
    print("Blocking gate: none — all gates PASS.")

# STATE flag: set True only by `jstack-gate hold` / `stale` (see docs/GATES.md).
# It means a decision is already posed and outstanding, NOT that the gate is human-gated.
print(f"Outstanding human decision (HOLD/STALE): {bool(s.get('human_approval_required'))}")
# `jstack-gate hold` also writes its reason into stale_reason; label it by the gate's
# actual status so a HOLD is not reported as a STALE.
if s.get('stale_reason'):
    st=s.get('gates',{}).get(blocking) if blocking else None
    print(('HOLD: ' if st=='HOLD' else 'STALE: ')+s['stale_reason'])
