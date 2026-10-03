# AGENTS.md

## Purpose and layout

This is a public, dependency-free Python sandbox for testing Tokate contributions.
`hello.py` contains the greeting function and CLI; `tests/test_hello.py` exercises
both. `scripts/verify.sh` is the shared verification entry point.

## Commands

Run from the repository root with Python 3.11+ and Bash:

```bash
python3 hello.py Ada
bash scripts/verify.sh
```

No package installation, network access, credentials, database or service is
needed. Use Python's standard library and `unittest`. Match existing four-space
indentation, small functions and Markdown documentation.

## Making changes

- Read the approved issue, relevant implementation and existing tests first.
- Preserve existing edits. Make focused changes and reuse existing functions.
- Add behavior tests for the requested feature or regression; keep existing
  checks meaningful and do not bypass failing tests.
- Update usage documentation when behavior changes. Run the shared checks and
  report the actual commands, results and unresolved limitations.
- Use temporary fixtures and synthetic data. Never copy private project code,
  local configuration, credentials, logs or personal information into this repo.
- During a donor run, work only in the checkout and leave edits uncommitted.
  Do not push, publish, merge, contact people, spawn agents, install tools or
  change permissions. Tokate owns the separate draft-PR publication step.
- Do not change `.github/tokate.json`, `.github/tokate-pr.md`, approvals or
  `.github/workflows/` from a donor task. Owner policy and required checks are
  review boundaries, not obstacles to work around.

## Tokate policy

The repository accepts `gpt-6.1-sol` with `high` effort and a 600-second maximum.
Repository-command network access is disabled. Verification runs
`bash scripts/verify.sh` and requires the GitHub check named `verify`.
Retain the generated PR template placeholders and human review before merging.
Do not start another Tokate run or retry inference automatically inside a task.
