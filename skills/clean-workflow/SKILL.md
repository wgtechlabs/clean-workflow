---
name: clean-workflow
description: Apply WG Tech Labs Clean Workflow conventions when a project or user adopts them; otherwise respect the target project's existing workflow.
metadata:
  short-description: Apply the WG Tech Labs Clean Workflow
---

# Clean Workflow

Use this skill for software-project work involving Git, GitHub, commits,
branches, pull requests, reviews, releases, labels, documentation, testing,
or security when the project or user has adopted the WG Tech Labs Clean
Workflow.

The repository's instructions and the user's request remain authoritative.
Apply this workflow where it fits; do not force it onto unrelated work or
override another project's conventions.

## Convention detection

Before applying Clean Commit, Clean Flow, or Clean Labels, determine whether
they are in scope:

1. Follow explicit system, repository, organization, and user instructions.
2. Inspect existing commits, branch names, pull-request conventions, labels,
   contribution docs, and agent instructions for the project's established
   workflow.
3. Treat Clean Workflow as active when the project explicitly references it,
   the user requests it, or the repository is a WG Tech Labs project that uses
   these conventions.
4. Enter contribution-preservation mode when working in a fork, preparing an
   upstream contribution, opening a PR against another project's repository,
   maintaining a dependency, or working in an unrelated external repository.
5. In contribution-preservation mode, follow the host project's instructions
   and established conventions for commit messages, branches, PR titles,
   labels, changelogs, and releases. Do not apply Clean Commit, Clean Flow, or
   Clean Labels just because this skill is installed.
6. If signals conflict or adoption is unclear, ask before changing commit,
   branch, PR-title, or label conventions. Ordinary code changes can continue
   under the project's existing rules.

Do not rewrite existing history or rename existing branches and labels merely
to make another project conform to Clean Workflow.

## Core workflow

- Inspect repository instructions, current branch, working-tree changes, and
  remote state before editing.
- Preserve unrelated user changes.
- Keep changes focused and production-ready.
- Use existing project tools and conventions before adding dependencies.
- Run the available lint, typecheck, test, build, and security checks that are
  relevant to the change.
- Never expose, log, or commit secrets.

## Git and GitHub conventions

Apply the following references only after convention detection confirms that
Clean Workflow is in scope:

Follow the detailed rules in these references:

- [Clean Commit](references/clean-commit.md)
- [Clean Flow](references/clean-flow.md)
- [Clean Labels](references/clean-labels.md)
- [Code review handling](references/code-review.md)

When a request involves one of these areas, read the relevant reference before
acting. If repository instructions are stricter, follow the stricter rule.

## Completion

Before reporting completion, inspect the final diff, run relevant validation,
and state any check that could not be verified. For review work, do not call an
item complete until the supported change, review reply, and resolution state
have all been verified.
