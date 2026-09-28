# Clean Commit

When Clean Commit is in scope, use one of these exact formats:

Do not impose this format on a project that uses Conventional Commits, a
repository-specific format, or another established convention. Follow that
project's format instead.

```text
<emoji> <type>: <description>
<emoji> <type> (<scope>): <description>
<emoji> <type>!: <description>
<emoji> <type>! (<scope>): <description>
```

Use the exact lowercase type and matching emoji:

| Emoji | Type | Use |
| --- | --- | --- |
| 📦 | `new` | New features, files, or capabilities |
| 🔧 | `update` | Existing-code changes and bug fixes |
| 🗑️ | `remove` | Removing code, features, or dependencies |
| 🔒 | `security` | Security fixes and hardening |
| ⚙️ | `setup` | Configuration, CI/CD, and tooling |
| ☕ | `chore` | Maintenance and housekeeping |
| 🧪 | `test` | Tests and test fixes |
| 📖 | `docs` | Documentation changes |
| 🚀 | `release` | Releases and release preparation |

Use present tense, start the description in lowercase, omit a final period,
and keep the message under 72 characters when practical.
