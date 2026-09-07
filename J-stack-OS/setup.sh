#!/usr/bin/env bash
set -euo pipefail
HOST="claude"
if [[ "${1:-}" == "--host" ]]; then HOST="${2:-claude}"; shift 2 || true; fi
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
mkdir -p "$HOME/.jstack" "$HOME/.local/bin"
if [[ ! -f "$HOME/.jstack/config.json" ]]; then
 cp "$SCRIPT_DIR/config.example.json" "$HOME/.jstack/config.json"
 python3 - "$HOME/.jstack/config.json" "$SCRIPT_DIR" <<'PY'
import json,sys
p,home=sys.argv[1:]; d=json.load(open(p)); d['jstack_home']=home; open(p,'w').write(json.dumps(d,indent=2)+'\n')
PY
fi
link_bin(){ chmod +x "$1"; ln -sf "$1" "$HOME/.local/bin/$2"; }
link_bin "$SCRIPT_DIR/bin/jstack_init.py" jstack-init
link_bin "$SCRIPT_DIR/bin/jstack_status.py" jstack-status
link_bin "$SCRIPT_DIR/bin/jstack_config.py" jstack-config
link_bin "$SCRIPT_DIR/bin/jstack_context.py" jstack-context
link_bin "$SCRIPT_DIR/bin/jstack_evidence.py" jstack-evidence
link_bin "$SCRIPT_DIR/bin/jstack_gate.py" jstack-gate
link_bin "$SCRIPT_DIR/bin/jstack_doctor.py" jstack-doctor
case "$HOST" in
 claude) mkdir -p "$HOME/.claude/skills"; ln -sfn "$SCRIPT_DIR" "$HOME/.claude/skills/jstack";;
 codex) CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"; mkdir -p "$CODEX_HOME/skills"; ln -sfn "$SCRIPT_DIR" "$CODEX_HOME/skills/jstack";;
 both) mkdir -p "$HOME/.claude/skills"; ln -sfn "$SCRIPT_DIR" "$HOME/.claude/skills/jstack"; CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"; mkdir -p "$CODEX_HOME/skills"; ln -sfn "$SCRIPT_DIR" "$CODEX_HOME/skills/jstack";;
 *) echo "Unsupported automated host: $HOST. Use hosts/README.md."; exit 2;; esac
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then echo 'NOTE: add ~/.local/bin to PATH.'; fi
echo "Installed J-stack OS from: $SCRIPT_DIR"
echo "Host: $HOST"
if [[ -t 0 ]]; then read -r -p "Obsidian vault path (optional, Enter to skip): " VAULT || true; if [[ -n "${VAULT:-}" ]]; then "$HOME/.local/bin/jstack-config" set obsidian_vault_path "$VAULT"; fi; fi
echo "Next: cd into a Git project and run: jstack-init"
