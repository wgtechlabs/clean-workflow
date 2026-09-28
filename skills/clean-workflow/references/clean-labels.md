# Clean Labels

## Manage the repository label template

Use [GitHub Labels Template (GHLT)](https://github.com/warengonzaga/github-labels-template)
for Clean Labels setup and migration. Do not recreate its template with custom
scripts or individual GitHub API calls.

- Check `ghlt --version` and `gh auth status` before use. If GHLT is missing and
  installation is authorized, install it with `npm install -g github-labels-template`.
- Confirm the target repository and pass `--repo owner/repo` explicitly, especially
  when working across multiple repositories.
- Inspect current labels with `ghlt list --repo owner/repo`.
- For authorized template setup that preserves existing labels, run
  `ghlt apply --repo owner/repo`. Existing labels are skipped by default; use
  `--force` only when updating their template values is intended.
- For an explicitly requested clean-slate migration, run
  `ghlt migrate -y --repo owner/repo`. This deletes all existing labels before
  applying the template and can remove label assignments from issues and PRs.
  Do not infer migration permission from a request to label a PR or adopt the
  workflow. Reuse explicit migration authorization already supplied.
- Verify the result with `ghlt list --repo owner/repo`. Report failures or partial
  results; do not blindly repeat a destructive migration after an uncertain result.

## Assign labels to issues and pull requests

GHLT manages repository label definitions. Use GitHub CLI issue/PR commands or an
available GitHub integration to assign existing labels to individual items, then
read back the item to verify its labels.

Apply only labels that already exist in the target repository unless the user
explicitly asks to create labels. Prefer the Clean Labels categories:

- `Type`: what the work is (`bug`, `enhancement`, `documentation`, `refactor`,
  `performance`, `security`)
- `Status`: where it is in the workflow (`blocked`, `needs triage`, `ready`)
- `Community`: who it is for (`good first issue`, `help wanted`,
  `maintainer only`)
- `Resolution`: why an item was closed (`duplicate`, `invalid`, `wontfix`)
- `Area`: which software layer it affects (`core`, `interface`, `data`, `infra`,
  `testing`)

Labels should be consistent, scannable, and limited to the repository's
existing vocabulary.
