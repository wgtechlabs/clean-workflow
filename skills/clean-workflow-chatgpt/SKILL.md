---
name: clean-workflow-chatgpt
description: >-
  Coordinate software issues and pull requests using Clean Workflow conventions,
  implementation guidance, code review, feedback handling, and delivery checks.
  Use when the user requests Clean Workflow or works in an adopted project,
  especially in ChatGPT with connected GitHub or coding tools.
---

# Clean Workflow for ChatGPT

Use this skill for software-project work involving Git, GitHub, commits, branches, pull
requests, reviews, releases, labels, documentation, testing, or security when the
project or user has adopted the WG Tech Labs Clean Workflow.

The repository's instructions and the user's request remain authoritative. Apply this
workflow where it fits; do not force it onto unrelated work or override another
project's conventions.

## ChatGPT tool access

This skill supplies instructions only. It does not connect GitHub, grant repository
access, provide a shell, or add permissions. Inspect the current ChatGPT surface and use
only the GitHub or coding tools that are actually available. Use a connected GitHub app
for supported repository actions and an attached coding workspace for file edits and
local checks. If a needed capability is unavailable, explain the limit and provide only
the review, draft, or patch the available tools support. Tool access does not itself
authorize commits, pushes, comments, issue changes, or other external actions; follow
the user's request and repository rules.

## Convention detection

Before applying Clean Commit, Clean Flow, or Clean Labels, determine whether they are in
scope:

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

Do not rewrite existing history or rename existing branches and labels merely to make
another project conform to Clean Workflow.

## Coordinate the task workflow

An explicit request to use Clean Workflow on a PR or to tackle an issue selects the
complete cycle by default. Use the implementation, review, and lifecycle guidance in
this skill. The user does not need to invoke separate skills.

Choose the scope from the user's request, not merely the presence of this skill:

| Request | Workflow |
| --- | --- |
| Use Clean Workflow on a PR, without a review-only limit | Inspect context → wait for active bots → review → fix valid feedback and conflicts → verify final changes and remote readiness. |
| Use Clean Workflow to tackle an issue | Inspect the issue and linked work → implement → open or update the PR → enter the same PR cycle. |
| Explicit review-only, read-only, or no-edits request | Review within those limits. Do not implement fixes or resolve threads. |
| Build, fix, or refactor without a requested PR/issue cycle | Implement and verify the requested change; do not invent a remote PR target. |
| Address existing feedback without a requested full cycle | Validate the feedback, fix supported findings, verify, and reply or resolve only within the authorized scope. |
| Review and fix local changes | Review, implement valid fixes, then inspect the final diff; do not invent a remote PR target. |

A complete cycle includes the necessary branch changes, commits, pushes, PR creation or
updates, and authorized feedback replies or resolutions unless the user limits those
actions. Merely installing this skill, detecting conventions, or discussing a PR does
not authorize publication. Approval, merge, release, deployment, and bypassing
repository protections require separate authorization.

Carry the reviewed commit, relevant finding and thread links, validation evidence, user
constraints, and unresolved questions between stages. Recheck the current head before
relying on earlier findings. Do not turn speculative or unsupported feedback into
implementation requirements. Keep blocked or disputed items visible.

For combined work, avoid publishing an intermediate finding as though it remains unfixed
after implementation. The final report distinguishes verified fixes, remaining findings,
and validation gaps. Reuse existing review threads and replies; do not duplicate
findings or post repetitive stage summaries. Thread-specific replies required by the
feedback-handling workflow are not optional summaries.

Advance through authorized stages without asking again. Ask only when a missing decision
materially changes the result or safe conflict resolution needs the user's intent;
continue independent work meanwhile. Honor draft-only, read-only, chat-only, no-push,
no-comment, and no-resolution limits. A review-only request never becomes a fix request
automatically.

## Core workflow

- Inspect repository instructions, current branch, working-tree changes, and
  remote state before editing.
- Preserve unrelated user changes.
- Keep changes focused and production-ready.
- Use existing project tools and conventions before adding dependencies.
- Run the available lint, typecheck, test, build, and security checks that are
  relevant to the change.
- Never expose, log, or commit secrets.

## Implementation guidance

Before editing, read repository instructions, inspect current changes and affected code,
and trace relevant callers. Identify requested behavior, constraints, and observable
acceptance criteria. Preserve unrelated work. Check language, framework, and dependency
versions before relying on an API; consult version-appropriate primary documentation
when repository evidence is insufficient.

Choose the smallest complete approach: omit speculative work, reuse suitable code and
established patterns, prefer standard-library or native platform capabilities, and add
dependencies only when needed. Keep behavior in its canonical layer. Validate untrusted
input at boundaries, preserve useful error context, and make state ownership and side
effects clear. Re-plan when code or runtime evidence invalidates an assumption.

Run focused checks that cover the change, then inspect the final diff and relevant
callers. Report which checks ran and which could not be run. Passing tests support only
the cases they cover. Never expose, log, or commit secrets.

## Review guidance

Identify the requested PR, commit range, files, or working-tree change. Inspect
repository instructions and the actual diff; do not assume a base commit or discard
uncommitted work. Read surrounding code, callers, contracts, and tests. Keep the review
within scope and distinguish new defects from preexisting issues.

For a PR, inspect existing reviews, inline threads and replies, PR comments, and the
current head before adding findings. Validate claims against current code and evidence.
Compare findings by root cause and consequence; link valid existing findings instead of
repeating them. If access or pagination is incomplete, state the coverage gap and do not
claim the review is duplicate-free. Do not endorse speculative work, style preferences,
or unnecessary complexity as defects.

Trace changed behavior through inputs, state transitions, side effects, and failures.
Check authorization, input validation, concurrency, retries, data integrity, and
migrations when relevant. For UI changes, check accessibility and interaction behavior.
Use a focused test or minimal reproduction to resolve suspected defects when practical.
Make findings concise, actionable, and supported by a concrete file and line reference.

A review-only request never authorizes fixes. Do not post a review, comment, reply, or
resolve a thread without explicit user or applicable repository authorization. When
authorized, reply in an existing thread only when new evidence materially changes the
discussion, then resolve only after the change and reply are verified.

## PR and issue lifecycle

For an existing PR, establish the current head and base, state, linked issue, actual
diff, reviews, inline threads and replies, comments, checks, and reviewer requests.
Paginate relevant collections. Treat missing access or incomplete results as a coverage
gap. For an issue, inspect linked PRs and existing implementation before starting
duplicate work.

After opening a PR, entering an existing PR, or pushing changes, inspect configured
review bots and relevant check runs. Allow a short discovery interval (normally about 30
seconds) and refresh once for delayed startup. Wait only for observed or explicitly
expected bot work. Correlate results to the current head and run; old reviews do not
count as current. A green CI check does not prove that a separate review bot finished.
If expected work never appears, report it as unknown or blocked rather than assuming
completion.

For the complete cycle, review the current PR, validate feedback, implement supported
fixes, resolve conflicts within scope, run checks, and verify fixes on the remote head.
Reply to addressed review threads and resolve them only when authorized. Recheck newly
triggered bot reviews and inspect the final diff. Verify current checks and merge
requirements before reporting readiness. Keep findings, validation gaps, required human
approvals, and unknown mergeability visible. Do not approve, merge, release, deploy, or
bypass protections unless separately authorized.

## Git, branch, commit, and label conventions

Apply these rules only after convention detection confirms that Clean Workflow is in
scope. Follow explicit system, organization, repository, and user instructions first.
Clean Workflow applies by default to repositories whose canonical remote owner is
wgtechlabs or warengonzaga, unless repository instructions opt out or establish another
convention. It also applies when a project explicitly references Clean Workflow, Clean
Commit, Clean Flow, or Clean Labels, or when the user requests it. In forks, upstream
contributions, dependency maintenance, and unrelated external projects, preserve the
host project's conventions. If signals conflict or adoption is unclear, ask before
changing commit, branch, PR-title, or label conventions. Do not rewrite history or
rename existing branches or labels to impose this workflow.

When Clean Commit applies, use one of these formats:

<emoji> <type>: <description> <emoji> <type> (<scope>): <description> <emoji> <type>!:
<description> <emoji> <type>! (<scope>): <description>

Match emoji and lowercase type: 📦 new for new capabilities; 🔧 update for existing-code
changes and fixes; 🗑️ remove; 🔒 security; ⚙️ setup; ☕ chore; 🧪 test; 📖 docs; 🚀
release. Use present tense, begin the description in lowercase, omit a final period, and
keep it under 72 characters when practical. Do not impose this format on a repository
with another established convention.

When Clean Flow applies, create short-lived lowercase feature branches from dev and
target feature PRs at dev. Avoid direct commits to main and dev. Update the feature
branch against dev when needed. Promote stable dev to main with a regular merge commit.
Do not impose this model on a project using trunk-based development, GitHub Flow,
release branches, or another documented policy.

Use the repository's existing labels. Prefer the Clean Labels categories Type, Status,
Community, Resolution, and Area when they exist. Use GitHub Labels Template (GHLT) for
label-template setup and migration; inspect labels first. GHLT apply preserves existing
labels. Use its destructive migration only when the user explicitly authorizes a
clean-slate migration. Assign labels through GitHub CLI or an available GitHub
integration and verify the result.

## Completion

Before reporting completion, inspect the final diff, run relevant validation, and state
any check that could not be verified. When addressing existing review feedback, verify
the change and any authorized reply or thread resolution. For a complete PR/issue cycle,
apply the lifecycle's remote readiness gate to the latest head and base; local fixes or
a completed review alone are not completion. Report actions outside the authorized scope
as pending rather than performing them or claiming they are complete.