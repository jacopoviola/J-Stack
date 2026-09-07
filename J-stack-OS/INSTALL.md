# Install J-stack OS on macOS

Recommended filesystem location: `~/J-stack-OS` (brand name: **J-stack OS**).

```bash
# after downloading/unzipping
mv /path/to/J-stack-OS ~/J-stack-OS
cd ~/J-stack-OS
./setup.sh --host claude

# make helper commands visible if needed
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# optional checks
jstack-doctor

# configure local Obsidian second brain
jstack-config set obsidian_vault_path "/absolute/path/to/your/ObsidianVault"

# initialize a product repo
cd /path/to/project
jstack-init

# start cockpit
claude
```

Then say: **“Use J-stack. Where are we?”**

To also expose the same host-neutral skill tree to Codex:

```bash
cd ~/J-stack-OS
./setup.sh --host both
```

J-stack does not require the project to use Railway. The SYSTEM gate chooses the stack per project after requirements are understood.
