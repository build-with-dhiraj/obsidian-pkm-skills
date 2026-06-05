---
name: Feature request
about: Suggest a new feature, rubric dimension, backend, or mode
title: "[FEATURE] "
labels: enhancement
assignees: ''
---

## Which skill

- [ ] `obsidian-graph-auditor`
- [ ] `obsidian-brain-eval`
- [ ] `obsidian-orphan-killer`
- [ ] cross-cutting / the suite as a whole

## What you want

A clear, one-paragraph description of the feature.

## Why it matters

What user problem does this solve? Concrete is better than abstract — "I run this on a 5,000-note vault and X is too slow" beats "could be faster".

## Proposed approach

If you have one. Optional.

## If this is a new graph-auditor rubric dimension

1. Is it **purely structural** (computable from the graph alone, no LLM)?
2. What's the **literature backing** for the threshold? Cite at least one source.
3. Is it **independent** of the existing 8 dimensions?
4. What's the **concrete fix path** when the dimension grades poorly?

## If this is a new orphan-killer mode or guard

1. Is it a **fundamentally different remediation strategy**, not a parameter tweak?
2. Does it **respect every existing safety guard** (frontmatter-only, atomic, idempotent, dangling-link guard, per-hub cap)?
3. Does it have a **dry-run path with an audit TSV**?
4. Should it be **gated behind `--experimental`**?

## If this is a new brain-eval backend or metric

1. What retrieval system would you plug in (link it)?
2. What gap in the current `naive` / `lancedb` backends does it fill?

See the relevant skill's `CONTRIBUTING.md` for the rationale behind these constraints.
