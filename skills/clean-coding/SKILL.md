---
name: clean-coding
description: Implement features, fix bugs, refactor code, and complete scoped engineering changes with minimal complexity and evidence-backed verification. Use when the user asks to build, add, fix, implement, change software, or address code-review feedback; not for review-only requests, general explanations, or non-coding tasks.
---

# Clean Coding

Deliver the requested engineering outcome using the smallest complete implementation that satisfies it. This is a self-contained synthesis of Grilling, APEX, Impeccable, Make Interfaces Feel Better, Thermo-Nuclear, and Ponytail. Apply the relevant principles below; invoking this skill does not require running all six source workflows.

## Understand before changing

Read the request, applicable repository instructions, current working-tree changes, and affected code. Trace the actual flow and relevant callers before choosing a fix. Preserve unrelated work.

Identify the requested behavior, constraints, exclusions, and observable acceptance criteria. For a bug, distinguish the reported symptom from its root cause and inspect sibling callers before changing shared behavior.

Resolve facts from the environment yourself. Ask only about missing decisions that materially change the outcome. For an ambiguous feature, group independent questions with recommended answers; ask dependent questions after their prerequisites are settled. Reuse decisions already supplied. A clear request can proceed directly; do not turn an isolated fix into a planning interview.

## Choose the smallest complete approach

Use Ponytail's decision order after understanding the task:

1. Omit speculative work that the requested outcome does not require.
2. Reuse suitable code, types, and patterns already in the repository.
3. Prefer a standard-library capability.
4. Prefer an appropriate native platform feature.
5. Reuse an already-installed dependency when it fits.
6. Otherwise write the minimum clear code that meets the requirements.

Check behavioral fit before substituting a simpler option. Minimal code must still cover explicitly requested behavior, validation at trust boundaries, data-loss prevention, security, and accessibility. Do not substitute an incomplete version for the user's requested feature. Prefer fewer concepts over clever one-liners or merely fewer lines.

For substantial work, state a short implementation plan tied to acceptance criteria and verification. For a small, clear change, act directly. Avoid speculative abstractions, dependencies, configuration, or scaffolding for hypothetical future needs.

## Implement and integrate

Follow Analyze → Plan → Execute → eXamine, scaled to the task. Put behavior in the canonical layer, reuse established conventions, and fix root causes where affected callers converge. Keep changes cohesive; do not scatter guards across callers when the shared contract needs correction.

Re-plan when code or runtime evidence invalidates an assumption. Keep deferred work and incomplete criteria visible during longer tasks. When delegation is separately authorized and useful, bound each independent subtask by objective, allowed files, excluded scope, and completion evidence; inspect returned changes before integrating them.

## Address code-review feedback

When asked to address PR review feedback, handle implementation and thread
follow-through together. Honor explicit draft-only, no-push, no-comment, or
no-resolution limits. A review-only request does not activate this workflow.

1. Fetch the current remote head, reviews, inline comments, replies, and thread
   status. Paginate the feedback and identify the requested scope. Validate each
   relevant comment against current code and tests before changing anything.
   Do not blindly implement speculative, unnecessary, duplicate, or already-fixed
   suggestions. Group fixes by root cause while tracking every addressed thread.
2. Implement the smallest necessary correction and run relevant checks. If the
   fix already exists, verify it instead of changing the code again. For disputed
   or unsupported feedback, explain the evidence in that comment's thread and
   leave it unresolved when a material disagreement or decision remains.
3. Deliver the fix to the PR branch when authorized and verify that the current
   remote code contains it. If publication is outside scope or blocked, report
   the fix as local/pending; do not claim the PR feedback is fully addressed.
4. **Always reply directly to each addressed review comment or thread.** State
   what changed (or where the existing fix was verified), link the commit or
   relevant code, and report the checks actually run and any limitations. A
   top-level PR comment or chat summary is not a substitute for this reply. Read
   existing replies first and reuse an equivalent verified reply instead of
   duplicating it. For feedback without a thread/reply facility, use the host's
   closest supported response location, link the original comment, and disclose
   that limitation.
5. Read back the reply, then resolve that specific thread only after its concern
   is addressed in the remote code and validation supports the fix. An authorized
   request to address review feedback includes these replies and resolutions
   unless the user limits that scope. Never resolve first or dismiss another
   review. Leave unresolved concerns and blocked actions visible.
6. Refetch the thread and verify its reply and resolution state. Report links to
   addressed threads and any pending items. After an uncertain write, inspect
   remote state before retrying; tool limitations do not count as completion.

## Design and polish when UI is involved

Apply these principles during implementation, then polish the working interface:

- Let the user's brief and existing product identity guide the design. Refinement preserves the established direction; redesign follows the requested replacement direction.
- Match the surface's purpose: persuasive pages support a decision, operational UI supports task completion, reading surfaces support comprehension, and showcase surfaces let the work lead.
- Use the existing styling system. Establish hierarchy, readable typography, layout, responsive behavior, accessible semantics, and relevant interaction states before fine polish.
- Refine details where they matter: stable numeric widths, optical alignment, concentric nested corners, coherent borders and shadows, and icons consistent with text weight and state.
- Use interruptible transitions for interactive changes and specify animated properties. Avoid habitual animation on frequent interactions. Preserve reduced-motion behavior and a static feedback cue.
- Inspect relevant viewports and states in a bounded batch; fix the observed issues together and confirm the fixes. Capture screenshots for visual evidence when runtime tools are available. Do not keep polishing after the requested result is met.

Skip this section for changes without a UI surface.

## Verify the outcome

Discover actual validation commands from project instructions, package scripts, CI, and nearby tests. Choose checks that exercise changed behavior and its risk, rather than inventing a ritual command list.

For nontrivial logic or a bug regression, use the smallest meaningful runnable check that would fail if the behavior broke. Reuse existing test infrastructure. Avoid a new framework or suites that only mirror the implementation.

Run relevant static checks and tests, then exercise the real CLI, API, application, or other target surface when required to prove the acceptance criteria. Verify persistence through reload or authoritative read-back when persistence is part of the request. Screenshots prove appearance; exercise interactions separately.

Distinguish passed checks, introduced failures, demonstrated preexisting or unrelated failures, unavailable checks, and checks not run. Fix introduced failures and rerun checks invalidated by subsequent edits. Missing tools or services limit what can be claimed; they never count as a pass.

## Examine before finishing

Review the final diff for behavior and scope, then apply the useful Thermo-Nuclear and Ponytail questions:

- Can a clearer model remove branches, layers, or duplicated logic while preserving behavior?
- Are business rules in the right layer, or scattered through unrelated code?
- Do casts, optional fields, silent fallbacks, or wrappers obscure an invariant?
- Has a file become difficult to reason about, including growth past roughly 1,000 lines?
- Can related updates leave partial state, or does orchestration add unnecessary complexity?
- Did the implementation introduce speculative flexibility or reinvent an existing capability?

Investigate these signals in context. Prefer a concrete, scope-appropriate simplification over unrelated architectural churn. Preserve required checks and safeguards. Revalidate behavior after review fixes.

Finish with the implemented outcome, the checks actually run and their results, and any remaining material limitation or unmet criterion. Complete the authorized delivery actions and verify their result; implementation alone does not authorize additional publication or production changes.

## Source lineage

Adapted from `focused-development`. Workflow inspiration: [My 5 Must-Have Skills to Code with AI](https://codelynx.dev/posts/best-skills-to-code-with-ai) by Melvynx, with Ponytail as an additional source. The source skills do not need to be installed.

Extracted and adapted from the installed source skills; these links provide provenance, not mandatory runtime dependencies:

- [Grilling](https://github.com/mattpocock/skills): decision dependencies and fact-finding before questions.
- [APEX](https://github.com/melvynx/aiblueprint): acceptance criteria, scoped execution, validation classification, and runtime proof.
- [Impeccable](https://github.com/pbakaus/impeccable): brief-led design, surface purpose, and bounded visual verification.
- [Make Interfaces Feel Better](https://github.com/jakubkrehel/make-interfaces-feel-better): detail polish within the existing styling system.
- [Thermo-Nuclear](https://github.com/cursor/plugins): structural simplification, canonical ownership, and maintainability review.
- [Ponytail](https://github.com/DietrichGebert/ponytail): reuse-first implementation, root-cause fixes, and minimal code without sacrificing requirements.
