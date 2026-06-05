---
name: Bug report
about: Report a bug or unexpected behavior
title: "[BUG] "
labels: bug
assignees: ''
---

## What happened

A clear, one-paragraph description of the bug.

## What you expected

A one-paragraph description of what you expected to happen.

## Is this a safety bug?

If any of the following happened, mark this issue with the `safety` label and we'll triage as a release blocker:

- A body byte was modified.
- A non-existent hub was written as a wikilink.
- A note already stamped with `resolved_at` / `anchored_at` / `clustered_at` was rewritten without `--force`.
- An LLM-named hub passed the guard list and wrote a denylisted name.
- The audit TSV claimed a decision that doesn't match what was actually written.

## Reproducer

```bash
obsidian-orphan-killer <mode> --vault /path/to/your/vault --dry-run
```

If possible, attach a minimal reproducer vault (10-30 notes) that demonstrates the issue.

## Environment

- `obsidian-orphan-killer --version` output:
- OS and version:
- Python version:
- Mode that triggered the bug (resolve / anchor / mint):
- Vault size (notes, approximate):
- Did the dry-run also show the bug, or only the live run?

## Logs / output

Paste the full stats output here:

```
[paste here]
```

If the bug is in the anchor or mint mode, paste the relevant rows from the audit TSV at `<vault>/orphan_killer_audit/<mode>.tsv`:

```
[paste here]
```
