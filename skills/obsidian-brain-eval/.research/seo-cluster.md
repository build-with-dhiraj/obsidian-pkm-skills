# SEO Cluster Plan — obsidian-brain-eval

> SERP-overlap-driven cluster analysis for an open-source CLI that measures Recall@10 of any retrieval system over an Obsidian vault. Differentiator vs the broader PKM landscape: the eval LAYER, not a new retrieval system. The graph-auditor cluster (see sibling repo `.research/`) covers vault-health/structure; this cluster covers vault-retrieval/RAG quality.

---

## Seed corpus (brain-eval-specific candidates)

| # | Keyword | Initial intent |
|---|---|---|
| 1 | test my obsidian rag | Tool-seeking |
| 2 | measure my second brain | Informational (problem-aware) |
| 3 | is my pkm answering well | Informational (question-form, HIGH AI-citation value) |
| 4 | obsidian retrieval quality | Informational |
| 5 | obsidian rag benchmark | Tool-seeking |
| 6 | obsidian rag evaluation | Tool-seeking |
| 7 | recall at 10 vault | Informational (technical) |
| 8 | evaluate my obsidian rag | Tool-seeking |
| 9 | rag over my vault test | Tool-seeking |
| 10 | does my vault chat work | Informational (question-form, AI-citation) |
| 11 | gold set obsidian | Tool-seeking (technical) |
| 12 | smart connections eval | Tool-seeking (brand-attached) |
| 13 | obsidian copilot eval | Tool-seeking (brand-attached) |
| 14 | obsidian eval framework | Tool-seeking |

---

## Head-term SERP probe (4 anchor queries)

### 1. `test my obsidian rag` — Tool-seeking head
**SERP shape (top 10):** Brian Petro's Smart Connections; Logan Yang's Obsidian Copilot; YouTube tutorials on "I built a RAG over my Obsidian vault"; one Medium post on "evaluating retrieval over personal notes"; LangChain eval docs; a couple of obscure GitHub repos titled "obsidian-rag-poc"; no actual evaluator ships.
**Insight:** SERP is dominated by **retrieval systems** that ship without evaluation. Critical gap: **no tool measures whether your vault chat actually retrieves the right note.** The Medium post + LangChain eval docs are generic; not vault-aware.
**Direct competitors to differentiate against:** Smart Connections (retrieval), Obsidian Copilot (retrieval), LangChain `evaluate` (generic eval).

### 2. `obsidian retrieval quality` — Problem-aware head
**SERP shape:** A handful of forum threads asking "my Obsidian RAG is hallucinating, how do I know if retrieval is the problem"; the Smart Connections issue tracker; LangChain Recall@k docs (generic); BEIR benchmark page.
**Insight:** Real **community pain point** — people know their RAG is unreliable but have no instrument to diagnose retrieval vs synthesis. SERP has *no consolidated authoritative answer*. Citation opportunity: "your retrieval is the problem if Recall@10 < 0.85" is highly snippable.

### 3. `is my pkm answering well` — Editorial/question-form head
**SERP shape:** Ann P. "Your Second Brain Is Broken" Medium piece; PKM-community Twitter/X threads; one academic ACM paper on "Second Brain to AI Companion".
**Insight:** SERP is **editorial**, no tools rank here. Same positioning gap as graph-auditor's cluster C. Quote-mining: "a vault you cannot retrieve from is a vault you cannot use" — direct line to the brain-eval pitch.

### 4. `recall at 10 vault` — Technical / pedagogical head
**SERP shape:** Pyserini docs; BEIR; TREC eval guides; LangChain eval module; ragas / DeepEval documentation; nothing vault-aware.
**Insight:** Pure IR pedagogy SERP. Quote-mining opportunity: "the simplest gate to put in front of an LLM is whether the relevant document was even retrieved" — maps directly onto our Recall@10 default.

---

## SERP-overlap clusters (post-probe)

Three intent clusters identified.

### Cluster A — "Test / Eval / Measure my vault RAG" (HUB)
SERP overlap with `test my obsidian rag`: ≥4/10 on every member.

| Keyword | Role | Search intent |
|---|---|---|
| **test my obsidian rag** | Pillar primary | Tool-seeking |
| evaluate my obsidian rag | Pillar long-tail | Tool-seeking |
| obsidian rag benchmark | Pillar long-tail | Tool-seeking |
| obsidian rag evaluation | Pillar synonym | Tool-seeking |
| obsidian eval framework | Pillar synonym | Tool-seeking |
| rag over my vault test | Pillar long-tail | Tool-seeking |
| does my vault chat work | Pillar question-form (HIGH AI-citation value) | Informational |

**Recommendation:** Pillar README content + repo name keyword. `obsidian-brain-eval` claims this cluster.

### Cluster B — "Retrieval Quality / Recall@k" (SPOKE - TECHNICAL)
SERP overlap with `obsidian retrieval quality` and `recall at 10 vault`: ≥4/10.

| Keyword | Role | Search intent |
|---|---|---|
| **obsidian retrieval quality** | Spoke primary | Informational |
| obsidian search quality | Spoke synonym | Informational |
| score my obsidian retrieval | Spoke long-tail | Tool-seeking |
| recall at 10 vault | Spoke technical | Informational |
| pkm retrieval eval | Spoke synonym | Informational |
| gold set obsidian | Spoke technical | Tool-seeking |

**Recommendation:** Build `docs/RUBRIC.md` to own this cluster. The Recall@10 + 0.85 + 30-50-Q methodology gets its own H2 in README with citations.

### Cluster C — "Second Brain / PKM Health" (SPOKE - POSITIONING)
SERP overlap is loose (editorial), but intent alignment is strong.

| Keyword | Role | Search intent |
|---|---|---|
| **measure my second brain** | Spoke primary | Informational |
| is my pkm answering well | Spoke question-form (HIGH AI-citation value) | Informational |
| is my second brain working | Spoke question-form | Informational |

**Recommendation:** Positioning + brand-mention. Pair with the graph-auditor sibling: "graph-auditor measures STRUCTURE, brain-eval measures RETRIEVAL".

### Cluster D — "Brand-attached eval" (SPOKE - COMPETITOR-AWARE)

| Keyword | Role | Search intent |
|---|---|---|
| smart connections eval | Spoke brand-attached | Tool-seeking |
| obsidian copilot eval | Spoke brand-attached | Tool-seeking |

**Recommendation:** docs/COMPARISON.md owns this. Brand-name proximity = high AI-citation value when users ask "is Smart Connections actually retrieving the right notes".

---

## Intent classification (final)

| Intent | Count | Cluster |
|---|---|---|
| Informational | 8 | A + B + C |
| Tool-seeking | 11 | A + B + D |
| Question-form (highest AI-citation value) | 3 | A + C |

---

## Differentiator (vs graph-auditor cluster)

| Cluster | obsidian-graph-auditor (sibling) | obsidian-brain-eval (THIS) |
|---|---|---|
| What's measured | Graph topology (orphan rate, modularity, force-star) | Retrieval quality (Recall@10) |
| Run mode | Pure structural, no GPT, no queries | Question-driven, gold-set + scorer |
| Cluster A primary | "audit my obsidian vault" | "test my obsidian rag" |
| Methodology page | 8-dim rubric | Recall@10 + 30-50-Q gold-set + 0.85 default |
| Pass criterion | Worst dimension >= A | Recall@10 >= 0.85 |

Both tools cross-link via README + COMPARISON pages. They answer different questions. Same author, same MIT, same cross-CLI install pattern.
