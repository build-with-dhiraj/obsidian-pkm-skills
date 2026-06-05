# SERP-Backwards (SXO) Analysis — Top 3 Queries

> What page-types rank for our target queries, what they have in common, what they lack, and where we can claim the gap.

---

## Query 1: `obsidian vault audit tool`  (Cluster A pillar)

**Ranking page-types (top 10):**

| Type | Examples | Strengths | Weaknesses |
|---|---|---|---|
| In-app plugins | Vault Inspector, Vault Intelligence, Vault Physician | Native install, dashboards, one-click fix | Locked into Obsidian — no CLI, no CI integration, no scripting |
| Plugin-discovery pages | Obsidian Plugin Audit Tool, ClawHub | Curated listings | No opinionated *what-good-looks-like* rubric |
| Narrative blog posts | "My Obsidian vault was rotting" (Tej Narendra) | Emotional hook, real before/after | One author's anecdote, no shared methodology |
| Security / brand pages | obsidian.md/security | High DA | Not the user's intent |

**Page-type gap (claimable):**
- A **CLI tool**: nothing in the top 10 is a command-line tool. Pure positioning win.
- An **opinionated rubric**: every ranking tool surfaces "problems" generically (broken links, large files). None grades the vault on an expert-cited rubric. Pure differentiation win.
- A **before/after gate**: the narrative pieces show before/after as anecdote. We ship it as a reproducible *gate* (same vault, same script, same output).

**Recommended page-type for our README:** **Hybrid tool-page + opinionated-rubric authority page** with embedded scorecard, before/after table, and CLI install instructions. Word count ~2500.

---

## Query 2: `obsidian graph analysis orphans`  (Cluster B spoke)

**Ranking page-types (top 10):**

| Type | Examples | Strengths | Weaknesses |
|---|---|---|---|
| Forum threads | forum.obsidian.md (×8 threads about orphans) | Community trust, indexed long | Fragmented, no consolidated answer |
| AI agent skills | obsidian-graph-query (forum showcase) | Modern, AI-native framing | Forum thread, not a polished repo README |
| Twitter/X | Obsidian official announcement | Brand authority | Stale, just a feature changelog |

**Page-type gap (claimable):**
- A **consolidated answer page**: no single doc answers "how do I find and reduce orphans in my Obsidian vault?" with both *measurement* and *remediation*. We can be that page (`docs/GRAPH-ANALYSIS.md`).
- A **threshold rationale**: forum threads all complain but none cite "the right orphan rate should be <10%". We give that with citation (graph-theory + Konik PKM frameworks).

**Recommended page-type:** **Deep-link doc page** (`docs/GRAPH-ANALYSIS.md`) — 800-1200 words, scannable, with the specific 10% threshold + 1 chart + 1 code-snippet. Linked from README under "obsidian orphans" anchor.

---

## Query 3: `second brain audit`  (Cluster C spoke — POSITIONING)

**Ranking page-types (top 10):**

| Type | Examples | Strengths | Weaknesses |
|---|---|---|---|
| Medium opinion pieces | Ann P. "Your Second Brain Is Broken", Danielpourasgharian | High emotional resonance | Critique with no remedy, no tool |
| Academic papers | ACM 2025 "PKM → Second Brain → AI Companion" | Authority | Inaccessible to practitioners |
| Beginner guides | Aidan Helfant, inkeybit | Approachable | No measurement, no audit lens |
| Vendor pages | Journal it!, Original Mac Guy | Trying to sell | Not authoritative |

**Page-type gap (claimable):**
- **The first actual TOOL ranking for this query.** SERP is 100% editorial — there is no software solution ranking. This is a high-leverage positioning play.
- **An authority page with cited thresholds.** `docs/RUBRIC.md` is built to be the citation-target. Pack with Matuschak / Ahrens / kepano / Konik / Paranyushkin so AI overviews quote it.

**Recommended page-type:** **Authority/rubric page** (`docs/RUBRIC.md`) — 1500-2000 words, expert-cited, with the 8 dimensions as scannable H2/H3 sections. This is the **brand-mention engine** for GEO/AI-overview citation.

---

## Cross-query patterns

1. **No CLI ranks anywhere.** All cluster-A tools are in-app plugins. CLI is a differentiator across all three queries.
2. **No tool ranks for "second brain audit".** Pure greenfield positioning.
3. **Cited thresholds win.** Every page that *cites* an authority (zettelkasten.de does this with Luhmann) earns authority; ours can do this with kepano, Matuschak, Konik, Paranyushkin (modularity 0.4-0.65), Milo.
4. **Before/after narratives perform.** The Medium "rotting vault" piece's structure is universally compelling. Steal the shape: "Day 1: orphans 32.2%, top-hub 31.4%. After: orphans 12.0%, top-hub 1.14%."
5. **Comparison tables get cited 156% more by AI** (per seo-geo skill): the `docs/COMPARISON.md` page is high-leverage GEO real estate.

---

## SXO-driven page architecture (final)

| Page | Target query/cluster | Word count | Role |
|---|---|---|---|
| `README.md` (H1+H2 stack) | Cluster A pillar | 2500 | Tool-page + opinionated-rubric pillar |
| `docs/RUBRIC.md` | Cluster C (positioning + GEO citation) | 1500-2000 | Authority page with cited thresholds |
| `docs/COMPARISON.md` | Cluster A commercial-leaning ("vault audit tool" comparison-seekers) | 1000 | Feature matrix vs Vault Inspector / Vault Physician / Vault Intelligence / obsidian-graph-query / kepano collection / obsidiantools |
| `docs/GRAPH-ANALYSIS.md` | Cluster B (orphans pain) | 800-1200 | Deep-link with the 10%-orphan threshold + 5%-hub-share rule |
| `SKILL.md` | Cross-CLI tool surface | 200 (frontmatter) + 800 (body) | Trigger-phrase-packed for in-CLI recommendation |
| `llms.txt` | All AI crawlers | 150 | Index for AI bots — what this repo is + key URLs |
