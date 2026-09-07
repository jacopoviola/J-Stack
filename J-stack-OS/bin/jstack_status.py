#!/usr/bin/env python3
import json
from pathlib import Path
p=Path.cwd().resolve()
while p!=p.parent and not (p/'.jstack'/'STATE.json').exists(): p=p.parent
sp=p/'.jstack'/'STATE.json'
if not sp.exists(): print('No .jstack/STATE.json found. Run jstack-init.'); raise SystemExit(1)
s=json.loads(sp.read_text()); print(f"Project: {s.get('project_name')}\nPhase:   {s.get('phase')}\nLake:    {s.get('active_lake') or '-'}\nGates:")
for k,v in s.get('gates',{}).items(): print(f'  {k:12} {v}')
if s.get('open_decisions'):
 print('Open decisions:'); [print('  - '+str(x)) for x in s['open_decisions']]
print(f"Next: {s.get('next_recommended_skill') or '-'}\nHuman approval required: {bool(s.get('human_approval_required'))}")
if s.get('stale_reason'): print('STALE: '+s['stale_reason'])
