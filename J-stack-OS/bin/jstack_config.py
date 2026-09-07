#!/usr/bin/env python3
import json, sys
from pathlib import Path
CFG=Path.home()/'.jstack'/'config.json'
def load(): return json.loads(CFG.read_text()) if CFG.exists() else {}
def save(d): CFG.parent.mkdir(parents=True,exist_ok=True); CFG.write_text(json.dumps(d,indent=2)+'\n')
a=sys.argv[1:]
if not a or a[0] in {'show','list'}: print(json.dumps(load(),indent=2)); raise SystemExit
if a[0]=='get' and len(a)==2: print(load().get(a[1],'')); raise SystemExit
if a[0]=='set' and len(a)>=3:
 d=load(); d[a[1]]=' '.join(a[2:]); save(d); print('set '+a[1]); raise SystemExit
print('Usage: jstack-config [show|get KEY|set KEY VALUE]',file=sys.stderr); raise SystemExit(2)
