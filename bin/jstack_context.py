#!/usr/bin/env python3
"""Cheap local Markdown retrieval for an Obsidian vault."""
import json,re,sys
from pathlib import Path
from collections import Counter
CFG=Path.home()/'.jstack'/'config.json'; TOKEN=re.compile(r"[A-Za-zÀ-ÿ0-9_\-]{3,}")
def toks(s): return [x.lower() for x in TOKEN.findall(s)]
def excerpt(text,terms,width=700):
 lo=text.lower(); pos=min([lo.find(t) for t in terms if lo.find(t)>=0] or [0]); start=max(0,pos-width//3); return ' '.join(text[start:start+width].split())
q=' '.join(sys.argv[1:]).strip()
if not q: print('Usage: jstack-context "decision/query"',file=sys.stderr); raise SystemExit(2)
cfg=json.loads(CFG.read_text()) if CFG.exists() else {}; vault_path=cfg.get('obsidian_vault_path')
if not isinstance(vault_path,str) or not vault_path.strip(): print('Configure vault: jstack-config set obsidian_vault_path "/path/to/vault"',file=sys.stderr); raise SystemExit(1)
vault=Path(vault_path).expanduser()
if not vault.is_dir(): print('Configure vault: jstack-config set obsidian_vault_path "/path/to/vault"',file=sys.stderr); raise SystemExit(1)
terms=toks(q); results=[]
for path in vault.rglob('*.md'):
 if any(part.startswith('.') for part in path.relative_to(vault).parts): continue
 try: text=path.read_text(errors='ignore')
 except Exception: continue
 c=Counter(toks(text[:120000])); title=toks(path.stem); score=sum(3*title.count(t)+min(c[t],20) for t in terms)
 if len(terms)>1 and all(t in c or t in title for t in terms): score+=8
 if score>0: results.append((score,path,text))
results.sort(key=lambda x:x[0],reverse=True)
for i,(score,path,text) in enumerate(results[:12],1): print(f'[{i}] score={score:.1f} {path}\n    {excerpt(text,terms)}\n')
if not results: print('No lexical matches found. Try fewer/more concrete terms.')

