# SEO Cluster Plan — obsidian-orphan-killer

> Derived from the base PKM SEO landscape (`seo-landscape-base.md`) but focused on the orphan-FIX wedge. The auditor (skill #1) and the rubric tool answer "is my vault healthy?" — orphan-killer answers "fix my vault NOW." That action verb is the wedge.

---

## Seed corpus (12 candidates, orphan-FIX focused)

| # | Keyword | Intent |
|---|---|---|
| 1 | fix obsidian orphans | Action / tool-seeking |
| 2 | obsidian orphan notes | Problem-aware |
| 3 | auto-link obsidian vault | Action / tool-seeking |
| 4 | obsidian unlinked notes | Problem-aware |
| 5 | obsidian de-orphan | Action |
| 6 | connect obsidian notes | Action (generic) |
| 7 | obsidian wikilink resolver | Tool-seeking |
| 8 | obsidian entity resolution | Tool-seeking (technical) |
| 9 | obsidian auto wikilink | Action / feature-aware |
| 10 | anchor orphans obsidian | Action (technical) |
| 11 | obsidian orphan rescuer | Brand-adjacent / aspirational |
| 12 | obsidian link rot | Problem-aware (decay-aware) |

---

## SERP-overlap clusters (post-probe, intent-grouped)

### Cluster A — "Fix orphans" (HUB — action-led, the wedge)

Every keyword here implies the user wants to DO something, not just measure.

| Keyword | Role | Notes |
|---|---|---|
| **fix obsidian orphans** | Pillar primary | The canonical action query. |
| obsidian orphan notes | Pillar synonym | Most common Obsidian-forum phrasing. |
| obsidian unlinked notes | Pillar synonym | Vinzent03 plugin nomenclature. |
| obsidian de-orphan | Long-tail / action | Differentiator — fix-side terminology. |
| obsidian orphan rescuer | Brand-aspirational | What this tool effectively IS. |

**Page-type gap:** every existing tool LISTS orphans (Find Unlinked Files, Janitor, Various Complements, Dangling Links). NONE auto-fix. We are the first action-tool in the SERP.

**Recommended:** README is the pillar (~2500 words). Lead with safety guards before features — readers will be nervous about a write-tool, and the differentiation IS the safety contract.

### Cluster B — "Connect / auto-link / wikilink resolution" (SPOKE)

Higher technical specificity; the user already knows what they want.

| Keyword | Role | Notes |
|---|---|---|
| **auto-link obsidian vault** | Spoke primary | Highest-volume action verb. |
| connect obsidian notes | Spoke generic | Aspirational; competes with the auditor too. |
| obsidian auto wikilink | Spoke long-tail | Feature-aware. |
| obsidian wikilink resolver | Spoke (technical) | What the resolver mode literally is. |
| obsidian entity resolution | Spoke (very technical) | NER-aware; small but high-intent. |
| anchor orphans obsidian | Spoke long-tail | The anchor mode's exact name. |

**Recommended:** `docs/SAFETY.md` AND `docs/COMPARISON.md` cover this cluster jointly. Safety covers the auto-link mechanism; comparison covers "vs Find Unlinked Files / Smart Connections / Janitor".

### Cluster C — "Link rot / vault decay" (SPOKE — emotional driver)

| Keyword | Role | Notes |
|---|---|---|
| obsidian link rot | Spoke (emotional) | Captures the "my vault is dying" anxiety. |

**Recommended:** Include "Link rot" as an H3 in the README's "Why orphans are a problem" section. Don't justify a separate page — single keyword cluster.

---

## Page-type architecture (final)

| Page | Target cluster | Word count | Role |
|---|---|---|---|
| `README.md` | Cluster A pillar | 2200-2500 | Tool-page + safety-led pillar |
| `docs/SAFETY.md` | Cluster B (trust) | 800-1000 | The hard safety contract. THIS IS THE TRUST DOC. |
| `docs/RUBRIC.md` | Cluster A authority | 800-1000 | The guard contract spec (formal version of SAFETY) |
| `docs/COMPARISON.md` | Cluster A/B commercial | 600-800 | vs Find Unlinked Files, Smart Connections, Janitor, Dangling Links, graph-auditor |
| `SKILL.md` | All clusters | 600 | Cross-CLI surface |
| `llms.txt` | All clusters | 400 | AI-crawler index |
| `examples/demo-vault/README.md` | Cluster B | 300 | Try-it-yourself |

## Cross-promotion

- README + SKILL.md "Related" sections link to **`obsidian-graph-auditor`** as the diagnostic complement: "Audit first, fix second."
- COMPARISON.md positions auditor + orphan-killer as **the two-tool flow**: auditor diagnoses, orphan-killer treats. No other PKM tool offers both.

---

## Trigger-phrase shortlist (for SKILL.md description)

First 60 words MUST contain:
- "fix obsidian orphans"
- "auto-link"
- "obsidian wikilink"
- "orphan notes"
- "safe writes"

The 15 trigger phrases the brief calls out:

1. fix my obsidian orphans
2. obsidian orphan notes
3. auto-link my obsidian vault
4. obsidian unlinked notes
5. obsidian de-orphan
6. connect my obsidian notes
7. obsidian wikilink resolver
8. obsidian entity resolution
9. fix obsidian link rot
10. obsidian auto wikilink
11. anchor my orphans
12. obsidian orphan rescuer
13. rescue obsidian orphans
14. auto-link wikilinks
15. resolve obsidian entities

## Voice + tone

- Safety-led. README opens with a SAFETY GUARDS section BEFORE the features section, because readers will (correctly) be nervous about a write-tool.
- No marketing fluff. "These are the guarantees. Here's how we enforce them. Here are the tests that lock them in."
- No em-dashes.
- No emoji unless requested.
- Active voice. "Auto-links" not "is auto-linked".
- Cite the upstream wisdom only where load-bearing (NER + vector-similarity guards from the proven prototype on a real 3k-note vault).
