#!/usr/bin/env python3
import argparse,hashlib,json,subprocess,time
from pathlib import Path
EXCLUDE_PREFIXES=('.git/','.jstack/')
def root():
    p=Path.cwd().resolve()
    while p!=p.parent and not (p/'.git').exists() and not (p/'.jstack').exists(): p=p.parent
    return p
def names(r):
    try:
        out=subprocess.check_output(['git','-C',str(r),'ls-files','-co','--exclude-standard','-z']); xs=[x for x in out.decode(errors='ignore').split('\0') if x]
    except Exception: xs=[str(p.relative_to(r)) for p in r.rglob('*') if p.is_file()]
    return sorted(x for x in xs if not any(x.startswith(e) for e in EXCLUDE_PREFIXES))
def fp(r):
    h=hashlib.sha256()
    for rel in names(r):
        p=r/rel
        if p.exists() and p.is_file():
            h.update(rel.encode()+b'\0')
            try: h.update(hashlib.sha256(p.read_bytes()).digest())
            except Exception: pass
    return h.hexdigest()
def ledger(r): return r/'.jstack'/'evidence.jsonl'
def records(r):
    if not ledger(r).exists(): return []
    out=[]
    for line in ledger(r).read_text(errors='ignore').splitlines():
        try: out.append(json.loads(line))
        except Exception: pass
    return out
ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True); sub.add_parser('fingerprint'); rn=sub.add_parser('run'); rn.add_argument('--label',required=True); rn.add_argument('command',nargs=argparse.REMAINDER); ck=sub.add_parser('check'); ck.add_argument('--label',required=True); a=ap.parse_args(); r=root(); current=fp(r)
if a.cmd=='fingerprint': print(current); raise SystemExit
if a.cmd=='run':
    cmd=a.command[1:] if a.command and a.command[0]=='--' else a.command
    if not cmd: raise SystemExit('Missing command after --')
    t=time.time(); proc=subprocess.run(cmd,cwd=r); rec={'ts':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'label':a.label,'fingerprint':fp(r),'command':cmd,'exit_code':proc.returncode,'duration_s':round(time.time()-t,3)}; ledger(r).parent.mkdir(parents=True,exist_ok=True)
    with ledger(r).open('a') as f: f.write(json.dumps(rec)+'\n')
    raise SystemExit(proc.returncode)
rs=[x for x in records(r) if x.get('label')==a.label]
if not rs: print('MISSING'); raise SystemExit(2)
rec=rs[-1]
if rec.get('exit_code')!=0: print('FAIL'); raise SystemExit(1)
if rec.get('fingerprint')!=current: print('STALE'); raise SystemExit(3)
print('FRESH')
