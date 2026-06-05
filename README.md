# obsidian-pkm-skills

> **Placeholder README — full documentation is added by the Technical Writer in Phase 2.**

A suite of three Claude / Cursor / Gemini CLI skills for keeping an Obsidian (or any `[[wikilink]]` markdown) vault healthy. Audit it, evaluate its retrieval quality, and fix its orphans — three independently installable, pure-Python tools maintained in one monorepo.

| Skill | PyPI package | What it does |
|---|---|---|
| [`obsidian-graph-auditor`](skills/obsidian-graph-auditor/) | `obsidian-graph-auditor` | Score a vault on an 8-dimension Grade-A rubric (read-only, no API keys). |
| [`obsidian-brain-eval`](skills/obsidian-brain-eval/) | `obsidian-brain-eval` | Measure Recall@10 of any retrieval system over the vault. |
| [`obsidian-orphan-killer`](skills/obsidian-orphan-killer/) | `obsidian-orphan-killer` | Auto-link orphan notes (frontmatter-only, atomic, idempotent writes). |

Each skill is self-contained under `skills/<name>/` with its own `SKILL.md`, Python package, tests, docs, and examples.

## Repository layout

```
obsidian-pkm-skills/
├── .claude-plugin/        # plugin + marketplace manifests (skills install)
├── .github/workflows/     # test, lint-skills, publish-pypi
└── skills/
    ├── obsidian-graph-auditor/
    ├── obsidian-brain-eval/
    └── obsidian-orphan-killer/
```

## Status

Phase 1 (scaffold, CI, publish pipeline) is complete. Prose documentation (full README, contributing guide, per-skill cross-links) lands in Phase 2.

## License

MIT © Dhiraj Singh Pawar — see [LICENSE](LICENSE).
