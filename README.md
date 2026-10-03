# Clean Workflow

An installable Codex plugin and AI-agent skills for WG Tech Labs project
workflow conventions.

It combines Clean Coding, Clean Code Review, Clean Commit, Clean Flow,
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

You can also invoke `$clean-coding` or `$clean-code-review` directly.

| Skill | Use |
| --- | --- |
| `clean-workflow` | Complete the issue/PR cycle and apply Git and delivery conventions |
| `clean-coding` | Implement, fix, or refactor with focused verification |
| `clean-code-review` | Review changes with evidence-backed findings |

For example: `$clean-workflow PR #42` or `$clean-workflow tackle issue #17`.
Either loads Clean Coding and Clean Code Review automatically. For a narrower
request, use `$clean-workflow review PR #42 only; do not edit or push` or invoke
`$clean-code-review review PR #42 without posting` directly.

Both specialized skills are also available in their own repositories:
[Clean Coding](https://github.com/wgtechlabs/clean-coding) and
[Clean Code Review](https://github.com/wgtechlabs/clean-code-review). Their source
lineage is documented in each skill; no upstream skill installation is required.
They still need the repository access and tools relevant to the task.

Clean Code Review reports in chat unless the user or applicable repository
instructions authorize publication. Approval requires its own authorization;
permission to comment alone is insufficient. Existing authorization is reused.

Agents that support the Agent Skills format can load the desired folder under
`skills/` directly. Invoke `clean-workflow` alone for coordinated work; the
specialized skills remain available for implementation-only or review-only tasks.

## Clean repositories

The WG Tech Labs Clean family covers development, review, and delivery conventions:

| Repository | Purpose |
| --- | --- |
| [Clean Workflow](https://github.com/wgtechlabs/clean-workflow) | Combine the conventions and route tasks to the relevant workflow. |
| [Clean Coding](https://github.com/wgtechlabs/clean-coding) | Standalone plugin for the `clean-coding` skill: implementation, fixes, refactoring, and verification. |
| [Clean Code Review](https://github.com/wgtechlabs/clean-code-review) | Standalone plugin for evidence-backed code and pull-request reviews. |
| [Clean Commit](https://github.com/wgtechlabs/clean-commit) | Consistent commit-message conventions. |
| [Clean Flow](https://github.com/wgtechlabs/clean-flow) | Branch and promotion conventions: ship through `dev`, keep `main` stable. |
| [Clean Labels](https://github.com/wgtechlabs/clean-labels) | Consistent repository label categories and descriptions. |

## Workflow coordination

An explicit Clean Workflow request on a PR selects the complete cycle by default:

1. Inspect the PR, linked issue, repository rules, current code, and existing feedback.
2. Detect and wait for active review/scanning bots, including Copilot and other providers.
3. Run Clean Code Review and validate human/bot findings without duplicating them.
4. Use Clean Coding to address valid findings together, resolve merge conflicts,
   verify the remote fixes, and reply to and resolve addressed review threads.
5. Check newly triggered bot work, review the final changes, and verify current
   checks and merge requirements before presenting the PR for a merge decision.

For an issue, Clean Coding first implements and verifies the requested behavior,
then opens or updates its PR and enters the same cycle. No separate skill mentions
are needed. See [PR and issue lifecycle](skills/clean-workflow/references/pr-lifecycle.md)
for bot discovery, bounded waiting, feedback rounds, and the readiness gate.

The complete cycle includes necessary commits, pushes, PR creation/update, and
feedback replies/resolutions unless the user limits them. Explicit review-only,
read-only, no-push, no-comment, no-resolution, and draft-only limits take precedence.
Installing the plugin or automatically detecting its conventions does not grant
that delivery scope. Approval, merge, release, and deployment remain separate actions.

The workflow reports stalled bots, missing evidence, unknown mergeability, and
required human approvals as pending or blocked. It does not claim readiness merely
because local tests pass or conflicts are cleared. The standalone skills remain
usable without this coordination layer.

## Skill ownership and updates

[Clean Coding](https://github.com/wgtechlabs/clean-coding) is the canonical source
for `clean-coding`.
[Clean Code Review](https://github.com/wgtechlabs/clean-code-review) is the canonical
source for `clean-code-review`. Make changes to those skills in their respective
repositories first, then update the copies bundled here from the upstream source.
Do not maintain independent edits to the bundled copies in Clean Workflow.

Clean Workflow owns task routing, Git and delivery conventions, and integration
of the two skills. The bundled copies keep plugin installation self-contained;
they are maintained dependencies, not separate authoritative implementations.

The `Sync upstream skills` workflow checks published stable releases daily at
00:00 UTC and supports manual dispatch. Drafts and prereleases are ignored.
When a release differs from [the recorded release](skills/upstream-releases.json),
it imports the entire skill directory from the release tag's exact commit and
opens or updates one PR against `dev`. It never pushes directly to `dev` or merges
automatically; review and merge the PR yourself. Repeated runs without a release
change produce no new changes. Repositories with no stable release keep their
existing bundled skill. A moved release tag fails the run for investigation.

The workflow becomes scheduled after it reaches the default branch. Enable
GitHub Actions to create pull requests in repository settings; it uses the
built-in `GITHUB_TOKEN` with contents and pull-request write permissions.
For a local check, run `python3 scripts/sync-skills.py` with authenticated `gh`
and Git available. This prepares local changes only. Review the diff before
submitting it. Initial pre-release provenance is retained in
[skills/UPSTREAM.md](skills/UPSTREAM.md).

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
- `skills/clean-coding/SKILL.md` — implementation and verification
- `skills/clean-code-review/SKILL.md` — review and authorized publication
- `skills/clean-workflow/references/` — detailed workflow conventions
- `.github/workflows/release.yml` — automated versioning and releases

## Releases

Releases run from `main` through
[`release-build-flow-action`](https://github.com/wgtechlabs/release-build-flow-action).
The action derives the SemVer bump from Clean Commit history, updates
`CHANGELOG.md`, creates the version tag, and publishes the GitHub Release.

The workflow uses the built-in `GITHUB_TOKEN` with `contents: write`; no PAT
secret is required. It plans a version, updates `.codex-plugin/plugin.json`, then
commits the manifest with the changelog before creating the tag and GitHub Release.
The initial release falls back to `0.1.0`. Release runs are serialized, and the
release action is pinned to an inspected commit. Branch rules must permit the
release commit. Sync generated changes from `main` back into `dev` after release.

## License

MIT
