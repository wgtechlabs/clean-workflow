---
name: clean-workflow
description: Apply WG Tech Labs conventions for planning, building, reviewing, releasing, and maintaining software projects.
metadata:
  short-description: Apply the WG Tech Labs Clean Workflow
---

# Clean Workflow

Use this skill for software-project work involving Git, GitHub, commits,
branches, pull requests, reviews, releases, labels, documentation, testing,
or security.

The repository's instructions and the user's request remain authoritative.
Apply this workflow where it fits; do not force it onto unrelated work.

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
