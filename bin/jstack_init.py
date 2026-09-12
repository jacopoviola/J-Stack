#!/usr/bin/env python3
import json, os, shutil, sys
from pathlib import Path

CFG=Path.home()/'.jstack'/'config.json'
def home_path():
    if os.environ.get('JSTACK_HOME'):
        return Path(os.environ['JSTACK_HOME']).expanduser().resolve()
    if CFG.exists():
        try:
            value=json.loads(CFG.read_text()).get('jstack_home')
            if value: return Path(value).expanduser().resolve()
        except Exception: pass
    return (Path.home()/'J-stack-OS').resolve()

HOME=home_path(); TEMPLATE=HOME/'project-template'/'.jstack'; ROOT=Path.cwd().resolve(); DEST=ROOT/'.jstack'
if not TEMPLATE.exists(): print(f'J-stack template not found: {TEMPLATE}',file=sys.stderr); raise SystemExit(2)
if DEST.exists() and any(DEST.iterdir()): print(f'{DEST} already exists and is not empty. Refusing to overwrite.'); raise SystemExit(1)
shutil.copytree(TEMPLATE,DEST,dirs_exist_ok=True)
sp=DEST/'STATE.json'; s=json.loads(sp.read_text()); s['project_name']=ROOT.name; sp.write_text(json.dumps(s,indent=2)+'\n')
claude=ROOT/'CLAUDE.md'
block="\n<!-- JSTACK:START -->\n## J-stack OS\nThis project uses J-stack OS. Before consequential product/coding work, read `.jstack/STATE.json` and follow global J-stack router/operating principles. Ask one human decision question at a time. No autonomous loops. Preserve locked gates.\n<!-- JSTACK:END -->\n"
if claude.exists():
    txt=claude.read_text(errors='ignore')
    if '<!-- JSTACK:START -->' not in txt: claude.write_text(txt.rstrip()+'\n'+block)
else: claude.write_text('# Claude Project Instructions\n'+block)
print(f'Initialized J-stack project state at {DEST}')
print('Next: open Claude Code and say: Use J-stack. Where are we?')
