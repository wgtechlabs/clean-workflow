# Clean Workflow

An installable Codex plugin and AI-agent skill for WG Tech Labs project
workflow conventions.

It combines Clean Commit, Clean Flow, Clean Labels, code-review handling,
validation, and security-at-inception guidance. The workflow is extensible and
can grow to cover project setup, releases, documentation, and maintenance.

## Install for Codex

Add the repository as a plugin marketplace, then install the plugin:

```bash
codex plugin marketplace add wgtechlabs/clean-workflow
codex plugin add clean-workflow@clean-workflow
```

Restart Codex after installation, then invoke it explicitly with:

```text
$clean-workflow
```

Agents that support the Agent Skills format can also load the skill directly
from `skills/clean-workflow/`.

## Contents

- `.codex-plugin/plugin.json` — Codex plugin manifest
- `skills/clean-workflow/SKILL.md` — canonical skill entrypoint
- `skills/clean-workflow/references/` — detailed workflow conventions

## License

MIT
