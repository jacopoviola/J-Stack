#!/usr/bin/env python3
import json, shutil
from pathlib import Path
cfg_path=Path.home()/'.jstack'/'config.json'
cfg=json.loads(cfg_path.read_text()) if cfg_path.exists() else {}
checks=[('git','required'),('python3','required'),('claude','primary cockpit'),('codex','adversary'),('gh','GitHub CLI'),('node','browser/test tooling'),('npx','Playwright fallback')]
print('J-stack doctor')
for cmd,why in checks:
    p=shutil.which(cmd); print(f"{'OK' if p else '--'} {cmd:10} {p or 'not found'} ({why})")
vault=Path(cfg.get('obsidian_vault_path','')).expanduser() if cfg.get('obsidian_vault_path') else None
print(f"{'OK' if vault and vault.exists() else '--'} Obsidian  {vault if vault else 'not configured'}")
print('Browser QA can also use gstack or another host browser harness if installed.')
