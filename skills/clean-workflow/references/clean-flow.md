# Clean Flow

When Clean Flow is in scope, ship through `dev` and keep `main` stable.

Do not impose this branch model on a project that uses trunk-based development,
GitHub Flow, release branches, or another established model. Follow the target
repository's documented branch policy instead.

```text
main + dev + feature branches
feature/* -> squash merge -> dev -> merge commit -> main
```

- Create feature branches from `dev`.
- Target feature pull requests at `dev`.
- Use short-lived branches with lowercase descriptive names.
- Avoid direct commits to `main` and `dev`.
- Update or rebase a feature branch against `dev` before submitting when needed.
- Delete feature branches after merge when repository policy allows it.
- Promote stable `dev` to `main` with a regular merge commit.
- Use a meaningful `🚀 release:` title for `dev` to `main` pull requests.

Use prefixes such as `feature/`, `fix/`, `docs/`, `chore/`, `test/`, and
`refactor/`.
