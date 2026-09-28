---
name: clean-code-review
description: Review code changes or pull requests for concrete correctness, security, maintainability, and over-engineering issues, with accessibility and interaction checks when UI changes. Use for combined code reviews or pre-merge review; not feature implementation, broad redesign, or whole-repository audits unless requested.
---

# Clean Code Review

Produce a concise, evidence-backed review of the requested change. This skill synthesizes the useful review principles of Grilling, APEX, Thermo-Nuclear, Ponytail, Impeccable, and Make Interfaces Feel Better. It is self-contained: do not load or run all six workflows.

## Establish the review target

- Identify the requested PR, commit range, files, or working-tree changes. Inspect repository instructions and the actual diff; do not assume `HEAD~1` or discard uncommitted work. For a branch review, establish its intended base and merge base.
- Read surrounding code, relevant callers, contracts, and tests. Derive expected behavior from the task and repository evidence. Ask a focused question only if a missing product decision materially changes the review; do not start a planning interview.
- State scope and any missing evidence. Distinguish new or newly exposed defects from preexisting issues. Do not expand a diff review into a whole-repository rewrite.

## Apply relevant review lenses

### Correctness and evidence — APEX

Trace changed behavior through inputs, state transitions, side effects, and failures. Check applicable authorization and tenant boundaries, input validation, concurrency, retries and idempotency, data integrity, and migration compatibility. Choose lenses based on the diff rather than filling a checklist mechanically.

Use targeted tests or a minimal reproduction when they can resolve a suspected defect. Separate checks actually run from PR-reported checks. Passing tests are evidence for their covered cases, not proof that the whole change is correct. Investigate uncertainty before presenting it as a finding.

### Simplicity — Ponytail

Look for duplicated existing functionality, avoidable dependencies, dead flexibility, and speculative abstractions. Consider existing helpers, standard libraries, and native platform features before suggesting custom replacements. Verify semantic equivalence, platform support, and repository conventions before recommending deletion.

Fewer lines alone are not an improvement. A single caller or implementation does not by itself prove an abstraction is unnecessary. Never simplify away required validation, authorization, error handling, accessibility, observability, or meaningful tests. Omit invented line-savings estimates.

### Maintainability — Thermo-Nuclear

Find changes that scatter business rules, obscure invariants with casts or optionality, introduce tangled conditionals, duplicate canonical logic, or make related updates non-atomic. Prefer a concrete restructuring that removes concepts or branches while preserving behavior.

Large or growing files, including crossing 1,000 lines, are investigation signals, not automatic blockers. Flag a structural issue only when its maintenance or correctness cost is demonstrable. Recommend the smallest coherent remedy; distinguish optional refactoring from defects that need correction.

### UI quality — Impeccable and Make Interfaces Feel Better

Apply only when the change affects UI. Inspect relevant keyboard/focus behavior, labels and semantics, loading/empty/error/disabled states, narrow layouts, text scaling, touch interactions, and reduced-motion behavior. Check typography stability, borders, animation interruption, and visual consistency where they affect usability or the established design.

Respect the existing styling system and product direction. Do not invent requirements for dark mode, animation, new design tokens, or a preferred aesthetic. Do not recommend memoization, lazy loading, or rendering changes without a relevant behavioral or performance reason.

When runtime access is available and useful, inspect affected states and viewports in a bounded pass. A screenshot demonstrates appearance, not keyboard, touch, or functional correctness. Report exactly what was exercised and distinguish emulation from device testing. If runtime access is unavailable, keep source-supported findings and label visual or interaction behavior unverified.

## Validate and report

For every candidate, verify the exact location, triggering conditions, consequence, and supporting code or runtime evidence. Reject duplicates, style preferences, unsupported scenarios, and issues wholly outside scope. Keep unresolved questions separate from confirmed findings.

Present findings first, ordered by impact. Each finding contains:

- **[P0–P3] Short actionable title** and an exact file/line reference.
- The concrete trigger or violated contract, its consequence, and supporting evidence.
- The smallest safe remediation direction, with any material uncertainty stated explicitly.

Use P0 for an immediate critical failure, P1 for a major defect requiring prompt correction, P2 for a normal actionable issue, and P3 for minor nonblocking improvement. Do not inflate severity for aesthetics or a file-size threshold. Group repeated instances of one root cause. Do not manufacture findings or a quota.

End with a brief validation note: checks run and results, coverage limits, and unresolved material questions. If no confirmed issues remain, say “No actionable findings in the reviewed scope” and disclose the verification limits; do not equate a lean diff with release readiness. Keep optional polish separate from blocking defects. Use inline comments when the host supports them and they help locate actionable findings.

Keep source files unchanged unless the user requests fixes. Apply only the authorized scope, preserve unrelated changes, and rerun affected checks.

## Publish PR reviews when authorized

Publish only when the user or applicable repository instructions authorize posting reviews. Installing or invoking this skill alone does not grant that permission. Reuse authorization already supplied; otherwise report in chat. Honor read-only and no-posting requests. A no-approval request still permits comments when posting is separately authorized. The steps below apply only within that authorization.

- When required changes remain, post one concise PR comment containing the confirmed findings, exact file/line links, reviewed commit, and validation limits. Do not submit a formal REQUEST_CHANGES review unless the user requests it.
- When no required changes remain, use the approval flow below; its review note is the published result, so do not add a duplicate comment. If approval is not authorized, unavailable, or inappropriate, post a comment explaining the conclusion and limitation when commenting is authorized; otherwise report in chat.
- If the review cannot be completed, post a clearly labeled partial review with verified findings and missing evidence; do not imply a clean result.
- Before posting, recheck the current head and review any new changes affecting the conclusions. Inspect existing comments and reviews to avoid duplicating the same result for the same commit; link an existing matching report instead.
- Verify the posted comment or review and link it in the final response. If publishing fails or the result is uncertain, report the precise limitation and inspect remote state before retrying.
- For targets without a PR, report the result in chat.

## Approve completed PR reviews when authorized

Submit an approval only when the user or applicable repository instructions authorize approval and the completed review finds no required changes remaining. Permission to post comments alone does not authorize approval. Reuse existing authorization for initial and follow-up reviews. Honor read-only and no-approval requests.

- Complete the requested review and inspect existing review feedback. Verify relevant unresolved findings against the current code; a resolved thread or author claim alone is not proof of a fix. Do not invent new suggestions to prolong a review. Optional nonblocking polish does not prevent approval.
- Approve only when the evidence supports the conclusion. Do not treat an incomplete review, exhausted time, missing essential evidence, or an unresolved material question as a clean result. Disclose nonblocking validation limits in the approval note.
- Immediately before submitting, confirm the PR is open and ready for review and its current head matches the reviewed commit. If it changed, review the new changes and rerun affected checks first. Bind the approval to the reviewed commit when the API supports it.
- Submit an APPROVE review with a short note explaining why: no required changes remain, or the earlier findings are verified fixed. Mention relevant checks and material validation limits without overstating coverage. Do not duplicate an existing approval by the same account for the same commit.
- Verify the submitted review and link it in the final response. If approval is unavailable, rejected, or cannot be verified, report the precise blocker without claiming success or retrying an uncertain submission blindly.

Authorization to review or approve does not extend to other delivery actions. Do not merge, deploy, dismiss another review, resolve other reviewers' threads, or submit formal change requests without separate user authorization.

## Source lineage

Adapted from `focused-code-review`. Workflow inspiration: [My 5 Must-Have Skills to Code with AI](https://codelynx.dev/posts/best-skills-to-code-with-ai) by Melvynx, with Ponytail as an additional source. The source skills do not need to be installed.

Adapted principles, not full workflow dependencies:
- [Grilling](https://github.com/mattpocock/skills): resolve material ambiguity using evidence.
- [APEX](https://github.com/melvynx/aiblueprint): validate behavior and substantiate findings.
- [Thermo-Nuclear](https://github.com/cursor/plugins): assess structural complexity and maintainability.
- [Ponytail](https://github.com/DietrichGebert/ponytail): question unnecessary code and reuse existing capabilities.
- [Impeccable](https://github.com/pbakaus/impeccable): inspect relevant UI accessibility and responsiveness.
- [Make Interfaces Feel Better](https://github.com/jakubkrehel/make-interfaces-feel-better): inspect interaction details within the existing design.
