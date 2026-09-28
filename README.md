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

Both specialized skills are also available in their own repositories:
[Clean Coding](https://github.com/wgtechlabs/clean-coding) and
[Clean Code Review](https://github.com/wgtechlabs/clean-code-review). Their source
lineage is documented in each skill; no upstream skill installation is required.
They still need the repository access and tools relevant to the task.

Clean Code Review reports in chat unless the user or applicable repository
instructions authorize publication. Approval requires its own authorization;
permission to comment alone is insufficient. Existing authorization is reused.

Agents that support the Agent Skills format can load the desired folder under
`skills/` directly. Load `clean-workflow` alongside a specialized skill when
WG Tech Labs Git and delivery conventions are also wanted.

## Clean repositories

The WG Tech Labs Clean family covers development, review, and delivery conventions:

| Repository | Purpose |
| --- | --- |
| [Clean Workflow](https://github.com/wgtechlabs/clean-workflow) | Combine the conventions and route tasks to the relevant workflow. |
| [Clean Coding](https://github.com/wgtechlabs/clean-coding) | Standalone plugin for the `clean-development` skill: implementation, fixes, refactoring, and verification. |
| [Clean Code Review](https://github.com/wgtechlabs/clean-code-review) | Standalone plugin for evidence-backed code and pull-request reviews. |
| [Clean Commit](https://github.com/wgtechlabs/clean-commit) | Consistent commit-message conventions. |
| [Clean Flow](https://github.com/wgtechlabs/clean-flow) | Branch and promotion conventions: ship through `dev`, keep `main` stable. |
| [Clean Labels](https://github.com/wgtechlabs/clean-labels) | Consistent repository label categories and descriptions. |

## Tools used

These tools support the relevant workflow steps; they are not all required for
every task. The development and review skills use the target project's existing
build, lint, test, and runtime tools.

| Tool or project | Role |
| --- | --- |
| [Git](https://git-scm.com/) | Inspect changes and manage commits, branches, and merges. |
| [GitHub CLI (`gh`)](https://github.com/cli/cli) | Work with GitHub pull requests, reviews, releases, and issue/PR label assignments. An available GitHub integration can cover supported operations. |
| [GitHub Labels Template (`ghlt`)](https://github.com/warengonzaga/github-labels-template) | Apply, migrate, and verify the Clean Labels template on a repository. Uses an authenticated GitHub CLI. |
| [Release Build Flow Action](https://github.com/wgtechlabs/release-build-flow-action) | Automate version calculation, changelog updates, tags, and GitHub Releases in the configured release workflow. |
| [Codex CLI](https://github.com/openai/codex) | Install the marketplace and plugin using the commands above. Other Agent Skills-compatible hosts can load the skill folders directly. |

### Clean Labels with GHLT

```bash
npm install -g github-labels-template
ghlt list --repo owner/repo
ghlt apply --repo owner/repo
```

`apply` preserves existing labels by default. For an explicitly authorized
clean-slate migration, use `ghlt migrate -y --repo owner/repo`; this deletes
existing labels before applying the template. Verify the result with `ghlt list`.
Use `gh` or an available GitHub integration to assign labels to individual issues
and PRs. See [Clean Labels guidance](skills/clean-workflow/references/clean-labels.md)
for targeting and authorization rules.

## Contents

- `.agents/plugins/marketplace.json` — marketplace catalog for repository installation
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
