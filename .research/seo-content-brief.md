# Content Brief — obsidian-brain-eval

> GEO-optimized brief for README.md + SKILL.md + docs/* + llms.txt. Built on the SERP-cluster analysis in seo-cluster.md.

---

## README.md (the pillar — Cluster A)

### Header
- **H1:** `obsidian-brain-eval`
- **Tagline:** "Test your Obsidian RAG. Measure your second brain. Score any retrieval backend on Recall@10 against a gold-set generated from your own vault. Default target 0.85. Works in Claude Code, Cursor, Gemini CLI, and Codex."
- **Badges:** PyPI placeholder, MIT, Python 3.10+, Tests passing, Cross-CLI.

### H2 — "What is obsidian-brain-eval?" (direct-answer block)
**First 40 words MUST include** (for GEO citation):
- "test obsidian rag"
- "measure second brain"
- "Recall@10"
- "gold-set"
- "retrieval quality"

Target length: 80-100 words. Then bulleted "What it does" list.

### H2 — "Why your Obsidian RAG needs a Recall@10 gate" (134-167 word answer block — AI-overview snippet target)
- Open with the failure-mode hook: "Most chat-with-my-vault setups are anecdotal."
- Cite the SERP gap: "no tool measures whether your vault chat actually surfaces the right note."
- Walk the two failure modes: retrieval failure vs synthesis failure. Recall@10 isolates them.
- Question-form hooks (snippable): "Is my Obsidian RAG actually working?", "What's my Recall@10?", "Does Smart Connections retrieve the right notes?"
- Close with: "The gate has to pass before answer-side investment is worth it. This skill is the gate."

### H2 — "The methodology" (the citable table)
| Element | Default | Source |
|---|---|---|
| Metric | Recall@10 | BEIR, TREC |
| Pass threshold | >= 0.85 | LangChain/LlamaIndex prod-RAG eval |
| Gold-set size | 30-50 questions | Sakai 2014 |
| Generator | GPT-4.1 (configurable) | OpenAI |
| Backends | BM25 + LanceDB | Pyserini + bge-small |
| Relevance signal | source + frontmatter wikilinks | kepano |

### H2 — "Example output"
Embed actual scorecard text in a `bash` code block. Mention the demo vault.

### H2 — "How to install" (Cluster A long-tail capture)
Sub-H3 per CLI: Python/PyPI, Claude Code, Cursor, Gemini CLI, Codex.

### H2 — "Quickstart" (zero-config 30-second hook)
Run against the shipped `examples/demo-vault`. No GPT needed.

### H2 — "Real workflow on YOUR vault" (Cluster B technical capture)
Generate -> review gold-set -> score with naive -> score with lancedb -> CI gate.

### H2 — "CI gate" (operationalisation)
GitHub Actions YAML snippet. Exit-code semantics.

### H2 — "Pluggable retrieval backends" (Cluster D capture - "Smart Connections eval" etc.)
The Python protocol. 10-line custom backend example.

### H2 — "How it compares" (Cluster D + sibling cross-promotion)
Link to docs/COMPARISON.md. Quick-list:
- vs anecdotal vault chat
- vs Smart Connections
- vs Obsidian Copilot
- vs ragas / DeepEval / LangChain / LlamaIndex
- vs obsidian-graph-auditor (sibling)

### H2 — "FAQ" (question-form Cluster A + C capture)
- "Will this modify my vault?"
- "Does it require GPT?"
- "Does it work on Logseq, Foam, Quartz?"
- "What's the difference between brain-eval and graph-auditor?"
- "Can I use a non-OpenAI model for generate?"
- "Is the 0.85 threshold right for me?"
- "How much does it cost to run?"

### H2 — "Sources cited"
Bullet list. Link to docs/RUBRIC.md for full citations.

### H2 — "License" + "Related"

---

## SKILL.md (cross-CLI manifest)

### YAML frontmatter
- name: obsidian-brain-eval
- description: pack with the 19 trigger phrases from Cluster A + B + C + D, plus the sibling cross-promotion. Verbatim phrases users say, not paraphrases.
- license, author, homepage, version.

### H1 + tagline + "When to use this skill" (six numbered triggers)
1. Test their vault's RAG. (Cluster A)
2. Measure retrieval quality. (Cluster B)
3. Benchmark a retrieval system. (Cluster A + D)
4. Generate a gold-set. (Cluster B)
5. Establish a CI gate. (operationalisation)
6. Decide what to improve next. (diagnostic)

### "What it does" + "How to run" + "How to read the output" + "Install" + "Pluggable backends" + "What it does NOT do" + "Related"

---

## docs/RUBRIC.md (citable methodology)

- H2: What is Recall@k? — anchors Cluster B
- H2: Why Recall@k and not MRR/NDCG? — secondary technical capture
- H2: Why 0.85? — high-citability defended threshold
- H2: How the gold-set is built — Cluster B technical
- H2: Why 30-50 questions? — anchors Cluster B with Sakai 2014 citation
- H2: Why the source note must be in the candidate folder
- H2: Why we don't measure answer quality — positioning vs ragas/DeepEval
- H2: What "PASS" and "BELOW TARGET" mean
- H2: References — full citations

---

## docs/COMPARISON.md (Cluster D capture)

Feature matrix vs:
- Anecdotal vault chat
- Smart Connections (Brian Petro) — brand-attached, Cluster D primary
- Obsidian Copilot (Logan Yang) — brand-attached, Cluster D secondary
- Generic RAG eval (ragas / DeepEval / LangChain evaluate / LlamaIndex RagEvaluator)
- obsidian-graph-auditor (sibling cross-promotion)

Each gets a "When to use" block + a "Trade-off" line. Reasonable-workflow numbered list at the bottom.

---

## llms.txt (AI-crawler manifest)

- What it measures (Recall@k, rank distribution, PASS/FAIL)
- What it generates (JSONL gold-set)
- Default thresholds + sizing (Recall@10 >= 0.85, 30-50 Qs)
- Backends shipped (naive + lancedb + custom)
- Sources cited
- Important pages (README, SKILL, RUBRIC, COMPARISON)
- Common queries (full Cluster A + B + C + D list, 19 phrases)
- License + citation policy

---

## Cross-cluster keyword densities target

| Cluster | README mentions | SKILL.md mentions | docs mentions |
|---|---|---|---|
| A (test/eval/measure rag) | 12+ | 8+ | 4+ |
| B (retrieval quality / recall@10) | 8+ | 5+ | 12+ (RUBRIC) |
| C (second brain / pkm) | 4+ | 3+ | 2+ |
| D (smart connections / copilot eval) | 3+ | 2+ | 8+ (COMPARISON) |
| Cross-CLI (Claude Code, Cursor, Gemini, Codex) | 14+ | 5+ | n/a |
