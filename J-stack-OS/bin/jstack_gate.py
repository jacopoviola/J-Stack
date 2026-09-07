#!/usr/bin/env python3
import argparse,json,time
from pathlib import Path

def root():
    p=Path.cwd().resolve()
    while p!=p.parent and not (p/'.jstack'/'STATE.json').exists(): p=p.parent
    if not (p/'.jstack'/'STATE.json').exists(): raise SystemExit('No J-stack project. Run jstack-init.')
    return p

PASS_STATE={
 'vision':('VISION_LOCKED','experience'),
 'experience':('EXPERIENCE_LOCKED','architecture'),
 'system':('SYSTEM_LOCKED','premortem'),
 'premortem':('PREMORTEM_LOCKED','plan'),
 'plan':('PLAN_LOCKED','build'),
 'release':('SHIPPED','learn'),
}
DOWNSTREAM={
 'vision':['experience','system','premortem','plan','release'],
 'experience':['system','premortem','plan','release'],
 'system':['premortem','plan','release'],
 'premortem':['plan','release'],
 'plan':['release'],
 'release':[]
}

ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True)
pa=sub.add_parser('pass'); pa.add_argument('gate'); pa.add_argument('--human',action='store_true')
ho=sub.add_parser('hold'); ho.add_argument('gate'); ho.add_argument('--reason',default='Human decision required')
fa=sub.add_parser('fail'); fa.add_argument('gate'); fa.add_argument('--reason',default='Gate failed')
st=sub.add_parser('stale'); st.add_argument('gate'); st.add_argument('--reason',required=True)
ph=sub.add_parser('phase'); ph.add_argument('phase'); ph.add_argument('--next',dest='next_skill',default=None)
a=ap.parse_args(); r=root(); sp=r/'.jstack'/'STATE.json'; s=json.loads(sp.read_text())
if a.cmd=='phase':
    s['phase']=a.phase
    if a.next_skill: s['next_recommended_skill']=a.next_skill
    sp.write_text(json.dumps(s,indent=2)+'\n'); print('phase: '+a.phase); raise SystemExit
if a.gate not in s.get('gates',{}): raise SystemExit('Unknown gate: '+a.gate)
if a.cmd=='pass':
    if a.gate in PASS_STATE and not a.human: raise SystemExit('This gate requires --human.')
    s['gates'][a.gate]='PASS'; s.setdefault('locked_at',{})[a.gate]=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()); s['stale_reason']=None
    if a.gate in PASS_STATE:
        s['phase'],s['next_recommended_skill']=PASS_STATE[a.gate]
    s['human_approval_required']=False
elif a.cmd=='hold':
    s['gates'][a.gate]='HOLD'; s['stale_reason']=a.reason; s['human_approval_required']=True
elif a.cmd=='fail':
    s['gates'][a.gate]='FAIL'; s['stale_reason']=a.reason; s['human_approval_required']=False
else:
    s['gates'][a.gate]='STALE'; s['stale_reason']=a.reason; s['human_approval_required']=True
    for g in DOWNSTREAM.get(a.gate,[]):
        if s['gates'].get(g)=='PASS': s['gates'][g]='STALE'
sp.write_text(json.dumps(s,indent=2)+'\n'); print(f"{a.gate}: {s['gates'][a.gate]}")
