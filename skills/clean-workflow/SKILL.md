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

## Coordinate the task workflow

Choose and load the relevant bundled skill automatically from the user's intent;
do not require the user to name each skill or repeat authorization already given.
Keep the project's Git and delivery conventions throughout the task.

| Request | Workflow |
| --- | --- |
| Build, fix, or refactor | Use [Clean Coding](../clean-coding/SKILL.md), including its verification and final examination. |
| Review code, a diff, or a PR | Use [Clean Code Review](../clean-code-review/SKILL.md). Inspect and validate existing feedback before adding findings; report or publish within the authorized scope. Do not implement fixes or resolve threads. |
| Address existing review feedback | Use [Clean Coding](../clean-coding/SKILL.md) and [Code review handling](references/code-review.md). Validate feedback, implement necessary corrections, verify remote fixes, reply to each addressed thread, and resolve eligible threads. |
| Review and fix, or another explicitly combined request | Use Clean Code Review to validate existing feedback and identify new issues, then Clean Coding for the authorized corrections, followed by a bounded Clean Code Review verification of the final changes. |

Carry the reviewed commit, relevant finding/thread links, validation evidence,
user constraints, and unresolved questions between stages. Recheck the current
head before relying on earlier findings. Do not change speculative or unsupported
feedback into implementation requirements. Keep blocked or disputed items visible.

For combined work, avoid publishing an intermediate finding as though it remains
unfixed after implementation. The final report distinguishes verified fixes,
remaining findings, and validation gaps. Reuse existing review threads and replies;
do not duplicate findings or post repetitive stage summaries. Thread-specific
replies required by the feedback-handling workflow are not optional summaries.

Advance through authorized stages without asking again. Honor read-only,
chat-only, no-push, no-comment, and no-resolution limits. A review-only request
never becomes a fix request automatically. Coordination does not grant permission
to approve, merge, release, or deploy; use the applicable authorization rules.

The two specialized skills also work independently. They do not require the
original source skills, and this coordination does not require separate agents.

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
- [Clean Labels](references/clean-labels.md) — use GHLT for template setup and migration
- [Code review handling](references/code-review.md)

When a request involves one of these areas, read the relevant reference before
acting. If repository instructions are stricter, follow the stricter rule.

## Completion

Before reporting completion, inspect the final diff, run relevant validation,
and state any check that could not be verified. When addressing existing review
feedback, verify the change and any authorized reply or thread resolution.
Report actions outside the authorized scope as pending rather than performing
them or claiming they are complete.
