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
   contribution docs, remote URL, and agent instructions for the project's
   established workflow.
3. Treat Clean Workflow as active by default when the canonical Git remote
   owner is `wgtechlabs` or `warengonzaga`, unless explicit repository
   instructions opt out or require a different convention.
4. Treat Clean Workflow as active when the project explicitly references any
   of these conventions or repositories: Clean Workflow, Clean Commit, Clean
   Flow, or Clean Labels. Search repository instructions, contribution docs,
   workflow files, and recent commits for those references.
5. Treat Clean Workflow as active when the user requests it, even in an
   external project, unless that would violate the target project's explicit
   contribution rules.
6. Enter contribution-preservation mode when working in a fork, preparing an
   upstream contribution, opening a PR against another project's repository,
   maintaining a dependency, or working in an unrelated external repository.
7. In contribution-preservation mode, follow the host project's instructions
   and established conventions for commit messages, branches, PR titles,
   labels, changelogs, and releases. Do not apply Clean Commit, Clean Flow, or
   Clean Labels just because this skill is installed.
8. If signals conflict or adoption is unclear, ask before changing commit,
   branch, PR-title, or label conventions. Ordinary code changes can continue
   under the project's existing rules.

Do not rewrite existing history or rename existing branches and labels merely
to make another project conform to Clean Workflow.

## Choose the task workflow

- For implementation, bug fixes, or refactoring, read [Clean Development](../clean-development/SKILL.md).
- For reviewing a diff or pull request, read [Clean Code Review](../clean-code-review/SKILL.md).
- For addressing existing review feedback, read [Code review handling](references/code-review.md) and use Clean Development when a code change is needed.

Load only the workflow relevant to the requested task. The two skills also work independently and do not require the original source skills. Keep the Git and delivery conventions below when using this entrypoint. A review-only request does not authorize fixes or thread resolution.

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
and state any check that could not be verified. When addressing existing review
feedback, verify the change and any authorized reply or thread resolution.
Report actions outside the authorized scope as pending rather than performing
them or claiming they are complete.
