# RAG (Retrieval-Augmented Generation)

A pattern for grounding LLM answers in a document collection. At query time, relevant chunks are retrieved and injected into the prompt; the LLM generates an answer using that context. Nothing accumulates between queries — each call is stateless.

---

## How It Works

1. **Ingest**: Documents are chunked, embedded into vectors, and stored in a vector index.
2. **Retrieve**: At query time, the user's question is embedded and nearest-neighbor chunks are retrieved from the index.
3. **Generate**: Retrieved chunks are injected into the LLM's context window alongside the question.
4. **Discard**: The retrieval result is ephemeral — not stored or updated.

## RAG vs Fine-Tuning

| Dimension | RAG | Fine-Tuning |
|-----------|-----|-------------|
| Knowledge update | Add docs to index, no retraining | Retrain or re-fine-tune |
| Latency | Higher (retrieval step) | Lower (no retrieval) |
| Explainability | High — sources are explicit | Low — knowledge is baked in |
| Cost | Index storage + embedding calls | Training compute |
| Best for | Dynamic, large, or proprietary corpora | Fixed style/behavior/domain |

## RAG vs Long Context

| Dimension | RAG | Long Context |
|-----------|-----|-------------|
| Scale | Millions of documents | Fits in context window |
| Precision | Retrieval quality-dependent | Full document available |
| Cost | Embedding + retrieval | Token cost scales with context |
| Best for | Large knowledge bases | Few documents, high recall needed |

## Common Failure Modes (interview-ready)

- **Retrieval miss**: The right chunk isn't returned — fix with better chunking strategy, hybrid search (BM25 + semantic), or re-ranker.
- **Context overflow**: Too many chunks retrieved, signal drowned out — fix with top-k tuning and re-ranking.
- **Chunk boundary problems**: Answers straddle two chunks — fix with overlapping chunks or parent-document retrieval.
- **Hallucination despite retrieval**: Model ignores retrieved context — fix with stricter system prompts or citation enforcement.
- **Stale index**: Index not updated as source docs change — fix with incremental ingestion pipeline.

## Evaluation Dimensions

| Metric | What it measures |
|--------|-----------------|
| Context precision | Are retrieved chunks relevant? |
| Context recall | Are all relevant chunks retrieved? |
| Answer faithfulness | Does the answer stay grounded in retrieved context? |
| Answer relevancy | Does the answer actually address the question? |

Use frameworks like **RAGAS** or **LLM-as-judge** to score these in a CI/CD eval loop.

## Key Paper

[RAG — Lewis et al. (2020)](https://arxiv.org/abs/2005.11401) — the original paper. Required reading in Phase 6 of the roadmap.

## Related

- [ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) — production RAG project examples
- [links.md Phase 6](../links.md) — production RAG articles (17 Advanced RAG Techniques, Zero-Waste Agentic RAG)
