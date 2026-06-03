# Content Brief — obsidian-orphan-killer

> Brief for the docs writer (this same agent in the next pass). Optimized for GEO/AI-overview citation: 134-167 word answer blocks, first-40-word direct answers, comparison tables, expert-cited safety claims, and the action-verb wedge.

---

## README.md (pillar — Cluster A)

### Header
- **H1:** `obsidian-orphan-killer`
- **Tagline:** "Auto-link the orphan notes in any [[wikilink]] markdown vault. Three modes. Frontmatter-only writes. Atomic. Idempotent."
- **Badges:** MIT, Python 3.10+, Tests passing (45), Cross-CLI compatible.

### H2 — "What does obsidian-orphan-killer do?" (the direct-answer block)
**First 40 words MUST include** (for GEO citation): "fix obsidian orphans", "auto-link", "wikilink resolver", "orphan notes", "safe writes".

### H2 — "Safety guards (read this first)" (the trust block)
This goes BEFORE features. A write-tool has to earn trust first.

The contract:
- Frontmatter-only writes (body bytes are never modified)
- Atomic writes (tempfile + os.rename, crash-safe)
- Body-only content hash preserved (downstream embedders never re-embed)
- Idempotency stamps (re-runs are no-ops)
- Dangling-link guard (only links to hubs that exist on disk)
- Per-hub absorption cap (anti-star)
- Concepts-only by default (no brand-leak)
- DO_NOT_MERGE honored
- Mint mode requires `--experimental`

Each guard has a test in `tests/` that enforces it.

### H2 — "Why your Obsidian vault has orphans (and why nothing fixes them)" (134-167w AI-overview snippet target)
Lead with the failure mode: every PKM forum has 8+ "orphan" threads. Every tool LISTS orphans. Find Unlinked Files (Vinzent03), Various Complements, Janitor, Dangling Links (Curtis McHale), Smart Connections (Brian Petro) — all surface the problem. Closing this gap requires three things at once: resolve plain-string entities → canonical wikilinks (deterministic); attach the rest via local embedding cosine to nearest hub; refuse to write a dangling link or force a noisy match. That's the orphan-killer pattern.

### H2 — "The three modes"
Table:

| Mode | What it does | Network? | Writes new notes? |
|---|---|---|---|
| `resolve` | Plain-string entities → canonical [[wikilinks]] | No | No |
| `anchor` | True-orphan leaves → nearest existing hub by cosine | No (local fastembed) | No |
| `mint` (experimental) | Cluster orphans → mint new concept hubs | LLM naming call | YES (new hubs) |

### H2 — "How to install"
Four subsections — one per CLI (Claude Code, Cursor, Gemini CLI, Codex). Each: 2-3 line install + 1-line first-run.

### H2 — "Try it on the demo vault"
Embed actual scorecard text in a `bash` code block. The demo vault ships at `examples/demo-vault/`. `obsidian-orphan-killer resolve --vault . --dry-run` finishes in 200ms and prints the plan.

### H2 — "Recommended workflow"
1. Audit first with `obsidian-graph-auditor` (the diagnostic tool).
2. Run `resolve --dry-run` to see what the alias table will rewrite. Approve.
3. Run `resolve` for real.
4. Run `anchor --dry-run` and review the TSV audit dump.
5. Run `anchor` for real.
6. (Optional) Run `mint --experimental --dry-run`. Read the audit dump and minted-cluster names. Only THEN, `mint --experimental`.

### H2 — "How it compares"
Link to `docs/COMPARISON.md`. One-line teaser per competitor (Find Unlinked Files, Various Complements, Janitor, Dangling Links, Smart Connections, obsidian-graph-auditor cross-promo).

### H2 — "FAQ"
- "Will this delete or rewrite my notes?" (No. Frontmatter-only. Body bytes are never touched.)
- "What if a resolved hub doesn't exist?" (We leave the plain string alone. Dangling-link guard.)
- "Can I undo it?" (Every write is a single-line YAML mutation. `git diff` shows it; `git checkout` reverts it. Idempotency stamps mean a re-run is safe.)
- "Does it work with Logseq / Roam / Quartz?" (Yes for resolve. Anchor and mint assume a hub-dir convention; pass `--hub-dirs your-dir1,your-dir2`.)
- "Why is mint mode 'experimental'?" (It writes NEW notes. The other modes only modify frontmatter.)
- "What if the LLM names a junk hub?" (Three deterministic backstops fire BEFORE the write: TOPIC_DENYLIST, URL-fragment, generic-catch-all. Plus the lexical guard.)

### Footer
License, author, contributing, related projects.

---

## SKILL.md (cross-CLI surface)

Frontmatter `description` first 60 words MUST contain: "fix obsidian orphans", "auto-link", "wikilink resolver", "orphan notes", "safe writes", "frontmatter-only". Then enumerate the 3 modes. Then 15+ exact trigger phrases.

Body sections:
- "When to use this skill" — 4 scenarios.
- "What it does (three modes)" — one-liner each.
- "Safety guards" — 8 bullets (the trust block).
- "How to run" — three CLI command examples (one per mode).
- "What it does NOT do" — the safety contract restated as anti-promises.

---

## docs/SAFETY.md (the trust authority page)

Headline: "What obsidian-orphan-killer will (and will not) do to your vault."

Structure:
- "The contract" — 8 hard guards, each with one paragraph of explanation.
- "Recovery" — git workflow if anything ever surprises you.
- "Dry-run convention" — always dry-run first; what to look for in the TSV dump.
- "What the tests enforce" — name each test that locks in each guard.
- "If you find a safety bug" — fast path to file an issue.

---

## docs/RUBRIC.md (the formal guard spec)

The formal version of SAFETY.md. SAFETY is for users; RUBRIC is for contributors.

Structure:
- One H2 per guard.
- For each: plain-language statement → enforcement mechanism (code + test) → why this matters → how to verify.

---

## docs/COMPARISON.md (commercial comparison)

| | obsidian-orphan-killer | Find Unlinked Files | Various Complements | Janitor | Dangling Links | Smart Connections | obsidian-graph-auditor |
|---|---|---|---|---|---|---|---|
| Lists orphans | yes | yes | yes | yes | yes | partial | yes |
| **Auto-fixes orphans** | **yes** | no | no | no | no | no | no |
| Pluggable LLM | yes | n/a | n/a | n/a | n/a | n/a | n/a |
| Safety guards | **yes (8)** | n/a | n/a | n/a | n/a | n/a | read-only |
| CLI / scriptable | **yes** | no (plugin) | no (plugin) | no (plugin) | no (plugin) | no (plugin) | yes |
| Cross-CLI skill | **yes** | no | no | no | no | no | yes |
| No GPT required | yes (resolve+anchor) | yes | yes | yes | yes | partial | yes |
| MIT licensed | yes | varies | yes | yes | yes | partial | yes |

Closing line: "Audit with `obsidian-graph-auditor`. Fix with `obsidian-orphan-killer`."

---

## llms.txt (AI-crawler index)

Standard format (mirror skill #1):
- Repo name + one-line description
- Three modes (one line each)
- The eight safety guards (citable list)
- Key URLs (README, SAFETY, RUBRIC, COMPARISON, SKILL)
- Trigger-phrase list
- Citation policy

---

## Voice + tone constraints

- Safety BEFORE features. Always.
- No marketing fluff. The contract IS the marketing.
- No em-dashes.
- No emoji.
- Active voice. Specific numbers.
- Every safety claim cites the test that enforces it.
