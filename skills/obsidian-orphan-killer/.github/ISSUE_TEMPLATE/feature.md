---
name: Feature request
about: Suggest a new mode, guard, or quality-of-life improvement
title: "[FEATURE] "
labels: enhancement
assignees: ''
---

## What you want

A clear, one-paragraph description of the feature.

## Why it matters

What user problem does this solve? Concrete is better than abstract — "I run this on a 5,000-note vault and X is too slow" beats "could be faster".

## Proposed approach

If you have one. Optional.

## If this is a new mode

Please address:

1. Is it a **fundamentally different remediation strategy**, not a parameter tweak on an existing mode?
2. Does it **respect every existing safety guard** (frontmatter-only, atomic, idempotent, dangling-link guard, per-hub cap)?
3. Does it have a **dry-run path with an audit TSV**?
4. Should it be **gated behind `--experimental`** (does it write new notes)?
5. What **failure mode** does it address that `resolve` / `anchor` / `mint` don't already cover?

See `CONTRIBUTING.md` for the rationale behind these constraints.

## If this is a new safety guard

Please address:

1. What **real-world failure mode** does it prevent? Cite an example.
2. How is it **enforced in code** (mechanism)?
3. What **test** locks it in?
4. Does it belong in `resolve`, `anchor`, `mint`, or all three?

PRs welcome. The bar for new guards is LOW.
