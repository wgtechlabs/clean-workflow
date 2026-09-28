# Clean Workflow repository instructions

## Ownership

- `skills/clean-workflow/` contains the workflow routing and delivery conventions maintained here.
- `skills/clean-coding/` is a downstream copy of `skills/clean-coding/` in `wgtechlabs/clean-coding`.
- `skills/clean-code-review/` is a downstream copy of `skills/clean-code-review/` in `wgtechlabs/clean-code-review`.
- Make behavior changes to the two specialized skills in their canonical repositories first. Import upstream changes here; do not patch or fork the bundled skill content independently.
- Preserve source attribution, supporting files, and relative links when importing updates. Record the upstream revision and validate the resulting plugin before publishing.

Run `python3 scripts/sync-skills.py` to detect published stable releases and record imported tags and exact commits in `skills/upstream-releases.json`. Never sync unreleased main-branch commits. The scheduled workflow opens a PR against `dev`; it does not merge updates. Run `python3 scripts/test-sync-skills.py` after changing sync behavior.

## Delivery and validation

Read the relevant conventions under `skills/clean-workflow/references/` before Git or GitHub actions. Use feature branches from `dev`, PRs into `dev`, and regular merge commits for authorized `dev` to `main` promotion. Preserve unrelated changes.

Run `git diff --check`, check skill frontmatter and relative links, and validate plugin manifests for packaging changes. Distinguish format checks from installed-plugin and behavioral verification. Do not merge or publish without authorization.
