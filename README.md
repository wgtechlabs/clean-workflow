# Clean Workflow

An installable Codex plugin and AI-agent skill for WG Tech Labs project
workflow conventions.

It combines Clean Commit, Clean Flow, Clean Labels, code-review handling,
validation, and security-at-inception guidance. The workflow is extensible and
can grow to cover project setup, releases, documentation, and maintenance.

Clean Workflow is context-aware. It applies automatically to projects that
explicitly adopt these conventions, when the user requests them, or within WG
Tech Labs repositories that use them. For forks, upstream contributions, and
external projects, it enters contribution-preservation mode and respects the
target project's existing commit, branch, PR, changelog, release, and label
rules.

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
- `.github/workflows/release.yml` — automated versioning and releases

## Releases

Releases run from `main` through
[`release-build-flow-action`](https://github.com/wgtechlabs/release-build-flow-action).
The action derives the SemVer bump from Clean Commit history, updates
`CHANGELOG.md`, creates the version tag, and publishes the GitHub Release.

The workflow uses the repository's `GH_PAT` secret for release operations. The
first release falls back to `0.1.0`. The Codex plugin manifest currently keeps
its version in `.codex-plugin/plugin.json`; update that manifest in the release
change until the release action supports plugin manifests directly.

## License

MIT
