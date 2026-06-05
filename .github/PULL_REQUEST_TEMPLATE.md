<!-- Placeholder PR template — finalized by the Technical Writer in Phase 2. -->

## Which skill(s)

- [ ] `obsidian-graph-auditor`
- [ ] `obsidian-brain-eval`
- [ ] `obsidian-orphan-killer`
- [ ] repo-wide (CI, packaging, docs)

## What this changes

<!-- One or two sentences. -->

## Checklist

- [ ] Tests pass locally (`pip install -e "skills/<name>[dev]"` then `pytest` in that skill dir)
- [ ] Lint passes (`ruff check`)
- [ ] `SKILL.md` frontmatter still has valid `name` + `description` (the `lint-skills` workflow enforces this)
- [ ] CHANGELOG updated for the affected skill (if user-facing)
