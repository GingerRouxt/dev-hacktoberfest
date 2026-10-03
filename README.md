# dev-hacktoberfest

A small public sandbox for testing [Tokate](https://tokate.dev/) contributions.
It contains a Python greeting CLI, real tests, and a draft-PR review workflow.
All example data is synthetic. This repository is separate from private projects.

## Run the demo

Requires Python 3.11+ and Bash for the verification script. There are no package
dependencies, accounts, environment variables or setup steps for the demo.

```bash
python3 hello.py
python3 hello.py Ada
```

The default response is `Hello, contributor!`; a name produces `Hello, Ada!`.

## Verify a change

```bash
bash scripts/verify.sh
```

This runs the unittest suite and checks the verification script's shell syntax.
The same command runs locally, in Tokate's sandbox, and in the GitHub Actions
job named `verify`. CI runs for main-branch pushes and pull requests, including
drafts, with read-only permissions and no repository secrets.

## Tokate setup

- Owner policy: [`.github/tokate.json`](.github/tokate.json).
- Allowed model and effort: `gpt-6.1-sol` / `high`.
- Runtime limit: 600 seconds for agent execution plus independent verification.
- Repository-command network access: disabled.
- Required GitHub check: `verify`.
- Agent guidance: [`AGENTS.md`](AGENTS.md).

An owner approves a specific issue for an assigned donor. Tokate uses that
donor's own GitHub and Codex/ChatGPT accounts, verifies the change, and opens a
draft PR. The owner reviews it; nothing merges automatically. A same-account
self-test demonstrates the mechanics, not a contribution from another person.
Do not infer live success from configuration or local tests alone: check the
actual PR, its receipt and the GitHub check results.

This is an integration sandbox, not a claim that its contributions qualify for
any external event or reward program.

## License

[MIT](LICENSE).
