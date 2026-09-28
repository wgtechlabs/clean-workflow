# Clean Workflow

An installable Codex plugin and AI-agent skills for WG Tech Labs project
workflow conventions.

It combines Clean Development, Clean Code Review, Clean Commit, Clean Flow,
Clean Labels, code-review handling,
validation, and security-at-inception guidance. The workflow is extensible and
can grow to cover project setup, releases, documentation, and maintenance.

Clean Workflow is context-aware. It applies automatically to projects that
explicitly adopt these conventions, when the user requests them, or within WG
Tech Labs repositories that use them. For forks, upstream contributions, and
external projects, it enters contribution-preservation mode and respects the
target project's existing commit, branch, PR, changelog, release, and label
rules.

The default owner scope is `wgtechlabs/*` and `warengonzaga/*`. Projects in
that scope use Clean Workflow unless their explicit repository instructions say
otherwise. Projects outside that scope opt in when they reference Clean
Workflow, Clean Commit, Clean Flow, or Clean Labels.

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

You can also invoke `$clean-development` or `$clean-code-review` directly.

| Skill | Use |
| --- | --- |
| `clean-workflow` | Route the task and apply Git and delivery conventions |
| `clean-development` | Implement, fix, or refactor with focused verification |
| `clean-code-review` | Review changes with evidence-backed findings |

For example: `$clean-development fix the reported login bug` or
`$clean-code-review review PR #42 without posting`.

Both specialized skills are self-contained adaptations of the local
`focused-development` and `focused-code-review` skills. Their source lineage
is documented in each skill; no upstream skill installation is required.
They still need the repository access and tools relevant to the task.

Clean Code Review reports in chat unless the user or applicable repository
instructions authorize publication. Approval requires its own authorization;
permission to comment alone is insufficient. Existing authorization is reused.

Agents that support the Agent Skills format can load the desired folder under
`skills/` directly. Load `clean-workflow` alongside a specialized skill when
WG Tech Labs Git and delivery conventions are also wanted.

## Contents

- `.codex-plugin/plugin.json` — Codex plugin manifest
- `skills/clean-workflow/SKILL.md` — workflow entrypoint and task routing
- `skills/clean-development/SKILL.md` — implementation and verification
- `skills/clean-code-review/SKILL.md` — review and authorized publication
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
