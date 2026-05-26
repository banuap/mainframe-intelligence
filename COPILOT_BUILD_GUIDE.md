# GitHub Copilot Build Guide

## How to use Copilot for this project

Use GitHub Copilot Chat from VS Code. Always start prompts with `@workspace` so Copilot reads the repository context.

Before asking Copilot to generate code, make sure these files exist:

- `AGENTS.md`
- `README.md`
- `TEAM_BUILD_AND_DEPLOYMENT_GUIDE.md`
- `requirements.txt`
- `app/db/schema.sql`
- `app/main.py`

## Recommended Copilot workflow

1. Create or pick a GitHub Issue.
2. Create a feature branch.
3. Open VS Code at the repo root.
4. Ask Copilot Chat to inspect the repo.
5. Ask Copilot to implement only that issue.
6. Run tests.
7. Review generated code manually.
8. Commit and push.
9. Open a Pull Request.

## Branch workflow

```bash
git checkout develop
git pull
git checkout -b feature/postgres-ontology-repository