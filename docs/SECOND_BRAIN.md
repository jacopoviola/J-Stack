# J-stack OS — Obsidian Second-Brain Integration

The second brain is a local Obsidian vault. J-stack retrieves context selectively rather than loading the whole vault.

Global config: `~/.jstack/config.json`.

Set the vault:

```bash
jstack-config set obsidian_vault_path "/path/to/vault"
```

Before consequential product, scope, architecture, stack, or roadmap decisions, search for evidence relevant to the **specific current decision**:

```bash
jstack-context "specific decision or question"
```

The helper performs cheap local lexical retrieval over Markdown. The AI then reads only the most relevant files and builds `.jstack/CONTEXT_PACK.md`.

Do not dump the full vault into context, treat old notes as current truth without dates, let notes override the current human direction, or invent missing evidence.
