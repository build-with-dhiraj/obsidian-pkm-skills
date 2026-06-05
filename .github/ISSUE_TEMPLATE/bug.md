---
name: Bug report
about: Report a bug or unexpected behavior in any of the three skills
title: "[BUG] "
labels: bug
assignees: ''
---

## Which skill

- [ ] `obsidian-graph-auditor`
- [ ] `obsidian-brain-eval`
- [ ] `obsidian-orphan-killer`

## What happened

A clear, one-paragraph description of the bug.

## What you expected

A one-paragraph description of what you expected to happen.

## Reproducer

The exact command you ran, e.g.:

```bash
obsidian-graph-audit --vault /path/to/your/vault
# or
obsidian-brain-eval score --vault /path/to/vault --gold gold.jsonl --backend naive
# or
obsidian-orphan-killer <mode> --vault /path/to/your/vault --dry-run
```

If possible, attach a minimal reproducer vault (10-30 notes) that demonstrates the issue.

## Environment

- Skill `--version` output:
- OS and version:
- Python version:
- Vault size (notes / edges, approximate):

## Safety bug? (orphan-killer only)

If a body byte was modified, a non-existent hub was written, an already-stamped note was rewritten without `--force`, a denylisted hub name was minted, or the audit TSV disagrees with what was written: add the `safety` label — we triage those as release blockers.

## Logs / output

```
[paste the full output here]
```
