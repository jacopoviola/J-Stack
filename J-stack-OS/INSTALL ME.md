# INSTALL ME — J-stack OS

Use this file as the setup instruction for **J-stack OS**.

If you are Claude Code, Claude Desktop/Cowork, Codex, or another coding agent with access to this folder, your job is to help me install and configure J-stack OS correctly on this Mac.

## What J-stack should look like

Global OS:

```text
~/J-stack-OS/
```

Per-project state:

```text
<project>/.jstack/
```

Primary setup:

- Claude Code = main cockpit
- Codex = adversarial reviewer
- GitHub = source control
- Browser-based QA
- Obsidian local vault = second brain

## Setup behavior

First, inspect the current machine and this folder before changing anything.

Check:

1. Whether this folder is already located at `~/J-stack-OS`.
2. Whether J-stack has already been installed for Claude and/or Codex.
3. Whether `$HOME/.local/bin` is already on `PATH`.
4. Whether the J-stack helper commands are available.
5. Whether an Obsidian vault path is already configured.
6. Whether the current product repo already contains `.jstack/`.

Do **not** reinstall or duplicate configuration unnecessarily.

If something requires my input, ask me **one question at a time**.

## Fresh installation

If J-stack has not yet been installed, guide me through or execute the equivalent of:

```bash
mv /path/to/unzipped/J-stack-OS ~/J-stack-OS
cd ~/J-stack-OS

./setup.sh --host both
```

Then make sure the helper commands are available:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Do not append the PATH line again if it is already present.

Run:

```bash
jstack-doctor
```

Explain any failures in plain English and help me resolve them before continuing.

## Connect my Obsidian second brain

If no vault has been configured, ask me for the **absolute path** to my local Obsidian vault.

Then configure it with:

```bash
jstack-config set obsidian_vault_path "/absolute/path/to/my/ObsidianVault"
```

Verify the path exists before saving it.

## Initialize J-stack inside a product repo

When I open a product repository that does not yet contain `.jstack/`, initialize it with:

```bash
cd /absolute/path/to/product-repo
jstack-init
```

Then verify that `.jstack/STATE.json` exists.

Do not initialize the global `~/J-stack-OS` folder as if it were a product unless I explicitly tell you to.

## After setup

Once installation and configuration are healthy, tell me that setup is complete and give me only the normal way to use J-stack:

> Open the product repo in Claude Code and say: **“Use J-stack. Where are we?”**

From then on, J-stack should read project state and guide me through the correct next phase.

I should not need to memorize terminal commands for normal usage.

## Important operating rules

- Do not run autonomous agent loops.
- Do not silently change product, architecture, data, security, cost, vendor, or UX decisions.
- Ask exactly one human decision question at a time.
- Explain technical concepts in product language.
- Prefer deterministic verification over model confidence.
- Treat Obsidian context as evidence, not authority.
- If setup is already correct, say so instead of reinstalling.
- If you cannot execute a required command from the current environment, give me the exact command to paste into macOS Terminal and explain where to run it.

## Success condition

Setup is complete only when:

- `~/J-stack-OS` exists;
- Claude host setup is installed;
- Codex host setup is installed or intentionally skipped by me;
- J-stack helper commands resolve;
- `jstack-doctor` passes or any remaining warnings are understood;
- my Obsidian vault is configured;
- the chosen product repo has `.jstack/STATE.json`.

Then stop setup and move me into normal J-stack usage.
