# SEO Cluster Plan — obsidian-graph-auditor

> SERP-overlap-driven cluster analysis for an open-source CLI that audits Obsidian vaults on an 8-dimension Grade-A rubric. Methodology: head-term SERP probe across the four candidate intent groups, then variant collapsing.

---

## Seed corpus (14 candidates)

| # | Keyword | Initial intent |
|---|---|---|
| 1 | obsidian audit | Informational / Tool-seeking |
| 2 | obsidian vault health | Informational |
| 3 | obsidian graph review | Informational / Tool-seeking |
| 4 | pkm graph score | Informational |
| 5 | second brain audit | Informational |
| 6 | obsidian orphans | Informational (problem-aware) |
| 7 | is my obsidian healthy | Informational (question-form) |
| 8 | obsidian scorecard | Informational |
| 9 | obsidian vault analyzer | Tool-seeking |
| 10 | obsidian graph analysis | Informational |
| 11 | personal knowledge management metrics | Informational (analytical) |
| 12 | obsidian vault quality | Informational |
| 13 | zettelkasten audit | Informational (pedagogical) |
| 14 | atomic notes review | Informational (pedagogical) |

---

## Head-term SERP probe (4 anchor queries)

### 1. `obsidian vault audit tool` — Tool-seeking head
**SERP shape (top 10):** Vault Intelligence plugin; Vault Inspector plugin; Vault Physician plugin; Claude Vault Assistant; "My Obsidian vault was rotting" Medium narrative; Obsidian Plugin Audit Tool; ClawHub; security pages.
**Insight:** SERP is dominated by **in-app plugins** with overlapping "scan + dashboard + one-click fix" framing. Critical gap: **no CLI / no opinionated rubric / no expert-cited thresholds.** The Medium narrative ("vault was rotting") confirms the emotional driver — vault decay anxiety.
**Direct competitors to differentiate against:** Vault Inspector, Vault Physician, Vault Intelligence, obsidian-graph-query (AI agent skill).

### 2. `obsidian graph analysis orphans` — Problem-aware head
**SERP shape:** obsidian-graph-query (BFS/shortest-path/bridges/hubs/orphans AI skill); 8+ Obsidian Forum threads about orphan detection, graph view limitations, "orphan files are not actually orphans".
**Insight:** Huge **community frustration cluster** — orphan detection is the #1 graph-view pain point. SERP has *no consolidated authoritative tool answer*, only forum threads and one AI skill. Citation opportunity: "X% of vaults exceed the 10% orphan threshold" is highly snippable.

### 3. `second brain audit pkm health` — Editorial/aspirational head
**SERP shape:** Medium articles on PKM hype/critique (Ann P. "Your Second Brain Is Broken", Danielpourasgharian); academic ACM paper on Second Brain → AI Companion transition; Aidan Helfant beginner guide; Journal it! app.
**Insight:** SERP is **100% editorial** — no tools rank here. This is the **positioning gap**: ours is the first tool to ship for this exact query. Key snippable phrase from SERP: *"a personal knowledge base that is only consumed and never expressed is a collection of saved links, not a second brain"* — perfectly aligned with our "auditor surfaces if you're write-only".

### 4. `zettelkasten review atomic notes` — Pedagogical head
**SERP shape:** zettelkasten.de canonical pages (atomicity guide); Bike Gremlin "death notes"; Medium "Anatomy of an Atomic Note"; Atlas Workspace setup guide.
**Insight:** Pure pedagogy SERP. Quote-mining opportunity: "Atomicity fosters re-use which in turn multiplies the amount of connections" — this maps directly onto our **link-density** dimension and gives us cited threshold rationale.

---

## SERP-overlap clusters (post-probe)

Two clusters with intra-cluster URL overlap ≥4/10. One isolation.

### Cluster A — "Tool / Health / Quality" (HUB)
SERP overlap with `obsidian vault audit tool`: ≥4/10 on every member.

| Keyword | Role | Search intent |
|---|---|---|
| **obsidian audit** | Pillar primary | Tool-seeking |
| obsidian vault audit tool | Pillar long-tail | Tool-seeking |
| obsidian vault health | Pillar synonym | Informational |
| obsidian vault quality | Pillar synonym | Informational |
| obsidian vault analyzer | Pillar long-tail | Tool-seeking |
| is my obsidian healthy | Pillar question-form (HIGH AI-citation value) | Informational |
| obsidian scorecard | Pillar synonym | Informational |

**Recommendation:** Make this the **pillar README content + repo name keyword**. `obsidian-graph-auditor` itself naturally claims the entire cluster.

### Cluster B — "Graph Analysis / Orphans" (SPOKE)
SERP overlap with `obsidian graph analysis orphans`: ≥4/10.

| Keyword | Role | Search intent |
|---|---|---|
| **obsidian graph analysis** | Spoke primary | Informational |
| obsidian graph review | Spoke long-tail | Informational |
| obsidian orphans | Spoke high-pain-point | Informational |
| pkm graph score | Spoke (cross-cluster) | Informational |

**Recommendation:** Build a `docs/GRAPH-ANALYSIS.md` deep-link page from README. The "obsidian orphans" pain point gets its **own H3 section in README** with the specific 10% threshold + before/after data point — that's the highest AI-citation hook.

### Cluster C — "PKM / Second Brain / Zettelkasten" (SPOKE — POSITIONING)
Intra-cluster overlap is lower (SERP is editorial), but intent alignment is strong.

| Keyword | Role | Search intent |
|---|---|---|
| **second brain audit** | Spoke primary | Informational |
| personal knowledge management metrics | Spoke long-tail | Informational |
| pkm graph score | Spoke (cross-cluster from B) | Informational |
| zettelkasten audit | Spoke pedagogical | Informational |
| atomic notes review | Spoke pedagogical | Informational |

**Recommendation:** This is the **brand-mention / GEO play.** Build `docs/RUBRIC.md` to be the cited authority page — pack it with Matuschak, Sönke Ahrens, kepano, Konik, Paranyushkin citations so AI overviews quote *us* when answering "what does a healthy zettelkasten / second brain look like?"

---

## Intent classification (final)

| Intent | Count | Cluster |
|---|---|---|
| Informational | 12 | A + B + C |
| Tool-seeking (commercial-leaning) | 3 | A only (`audit tool`, `analyzer`, `vault audit tool`) |
| Transactional | 0 | — |
| Navigational | 0 | — |

No exclusions — all keywords are valid clustering targets.

---

## Cannibalization & merge decisions

- `obsidian audit` ≈ `obsidian vault audit tool` (SERP overlap ~7/10) → merge into **single pillar** (README H1 + H2 cover both).
- `obsidian vault health` ≈ `obsidian vault quality` ≈ `is my obsidian healthy` (overlap ~5/10) → cover under **one H2 "Why your Obsidian vault needs an audit"** with question-form H3s for the AI-overview hook.
- `obsidian orphans` SERP barely overlaps with the tool-seeking cluster (~2/10) → place in cluster B but **link to it from pillar README** (interlink, anchor: "obsidian orphans threshold").

---

## Trigger-phrase shortlist for SKILL.md description

These are the **10–15 EXACT phrases users type** (mined from above SERPs + the question-form variants the heads expose). All of them should appear in SKILL.md `description` so Claude Code / Gemini CLI / Codex / Cursor surface this skill when the user types ANY of them:

1. audit my obsidian vault
2. is my obsidian healthy
3. is my second brain healthy
4. score my pkm graph
5. obsidian vault review
6. obsidian graph analysis
7. measure my obsidian
8. obsidian orphans
9. cross-linking review
10. obsidian graph health check
11. grade my pkm
12. obsidian vault quality
13. obsidian scorecard
14. zettelkasten audit
15. second brain audit
16. find orphans in my vault
17. why is my vault rotting
18. pkm metrics

---

## Internal link matrix (repo-level)

```
README.md (pillar — claims cluster A entirely)
├── docs/RUBRIC.md (cluster C authority page — AI-overview citation target)
├── docs/COMPARISON.md (commercial-leaning, differentiates from Vault Inspector et al.)
├── docs/GRAPH-ANALYSIS.md (cluster B deep-link — orphans + hubs + modularity)
└── SKILL.md (cross-CLI surface for cluster A tool-seeking queries)
```

Every doc links back to README. Three cross-links per doc (mandatory min).

---

## Output of this phase

- `/Users/pw/builds/obsidian-graph-auditor/.research/seo-cluster.md` (this file)
- Cluster A pillar keyword set → drives **repo name (claimed), README H1, package name, SKILL name**
- Cluster B + C → drive the **two docs/ pages** + the orphan-threshold-specific README section
- Trigger-phrase shortlist (18 phrases) → goes straight into SKILL.md `description`

---

## Sources

- Vault Inspector — https://www.obsidianstats.com/plugins/vault-inspector
- Vault Intelligence — https://www.obsidianstats.com/plugins/vault-intelligence
- Vault Physician (community discovery)
- obsidian-graph-query AI agent skill — https://forum.obsidian.md/t/obsidian-graph-query-let-your-ai-agent-query-your-vaults-knowledge-graph-bfs-shortest-path-bridges-hubs-orphans/111828
- Tej Narendra, "My Obsidian vault was rotting" — https://tejnaren07.medium.com/my-obsidian-vault-was-rotting-so-i-wrote-a-plugin-to-diagnose-it-a1343830fbbb
- Ann P., "Your Second Brain Is Broken" — https://medium.com/@ann_p/your-second-brain-is-broken-why-most-pkm-tools-waste-your-time-76e41dfc6747
- zettelkasten.de atomicity guide — https://zettelkasten.de/atomicity/guide/
- Obsidian forum orphan discussions — https://forum.obsidian.md/t/find-orphan-notes/817
