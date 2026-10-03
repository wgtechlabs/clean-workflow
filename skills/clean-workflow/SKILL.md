---
name: clean-workflow
description: Coordinate issues and pull requests through implementation, bot-review waiting, code review, feedback fixes, conflict resolution, and verified PR readiness. Apply adopted Clean Workflow conventions while respecting the target project's rules and explicit review-only limits.
metadata:
  short-description: Take issues and PRs through the complete Clean Workflow
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

An explicit request to use Clean Workflow on a PR or to tackle an issue selects
the complete cycle by default. Load both [Clean Coding](../clean-coding/SKILL.md)
and [Clean Code Review](../clean-code-review/SKILL.md) yourself. The user does not
need to mention either separately. Read [PR and issue lifecycle](references/pr-lifecycle.md)
for the stage order, bot waiting, conflict handling, and completion gate.

Choose the scope from the user's request, not merely the presence of this skill:

| Request | Workflow |
| --- | --- |
| Use Clean Workflow on a PR, including a request to review it without a review-only limit | Inspect context → wait for active bots → Clean Code Review → Clean Coding for valid feedback and conflicts → verify final changes and remote readiness. |
| Use Clean Workflow to tackle an issue | Inspect the issue and linked work → Clean Coding → open or update the PR → enter the same PR cycle. |
| Explicit review-only, read-only, or no-edits request; standalone review of local code/diff | Use Clean Code Review within those limits. Do not implement fixes or resolve threads. |
| Build, fix, or refactor without a requested PR/issue cycle | Use Clean Coding, including its verification and final examination. |
| Address existing feedback without a requested full cycle | Use Clean Coding and [Code review handling](references/code-review.md). Validate, fix, verify, reply, and resolve within scope. |
| Review and fix local changes | Use Clean Code Review, then Clean Coding, then a bounded review of the final changes; do not invent a remote PR target. |

For the explicitly requested complete cycle, the task includes the necessary
branch changes, commits, push, PR creation/update, and feedback replies/resolutions
unless the user limits those actions. Installation, automatic convention detection,
or merely discussing a PR does not select that cycle or authorize publication.
Carry this task scope into each specialized skill; their standalone defaults do
not require another invocation or repeated permission for already authorized work.

Carry the reviewed commit, relevant finding/thread links, validation evidence,
user constraints, and unresolved questions between stages. Recheck the current
head before relying on earlier findings. Do not change speculative or unsupported
feedback into implementation requirements. Keep blocked or disputed items visible.

For combined work, avoid publishing an intermediate finding as though it remains
unfixed after implementation. The final report distinguishes verified fixes,
remaining findings, and validation gaps. Reuse existing review threads and replies;
do not duplicate findings or post repetitive stage summaries. Thread-specific
replies required by the feedback-handling workflow are not optional summaries.

Advance through authorized stages without asking again. Ask only when a missing
decision materially changes the result or safe conflict resolution needs the
user's intent; continue independent work meanwhile. Honor draft-only, read-only,
chat-only, no-push, no-comment, and no-resolution limits. A review-only request
never becomes a fix request automatically. Approval, merge, release, deployment,
and bypassing repository protections require separate authorization.

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
For a complete PR/issue cycle, apply the lifecycle's remote readiness gate to the
latest head and base; local fixes or a completed review alone are not completion.
Report actions outside the authorized scope as pending rather than performing
them or claiming they are complete.
