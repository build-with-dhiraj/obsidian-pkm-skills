---
name: Bug report
about: Report something the evaluator gets wrong
labels: bug
---

**What happened**

A clear description of the unexpected behavior.

**To reproduce**

The exact command you ran, e.g.:

```bash
obsidian-brain-eval score --vault /path/to/vault --gold gold.jsonl --backend naive
```

**Expected**

What you expected to see (e.g. "Recall@10 around 0.X with this gold-set", "no exception").

**Environment**

- `obsidian-brain-eval --version`:
- Python:
- OS:
- Backend (naive / lancedb / custom):

**Vault details**

- Approximate # of notes:
- Whether the vault uses `[[wikilinks]]`, frontmatter, both:
- Anything unusual (very large notes, non-Latin scripts, image-heavy):

**A minimal reproducer is hugely appreciated** - a 10-30 note vault + 2-3 gold records that surface the bug.
