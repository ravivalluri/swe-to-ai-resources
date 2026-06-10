# Phase 6 — LLMs + AI Engineering

**Dates:** Jan 11 – Apr 18, 2027 (Weeks 47–60)
**Goal:** The capstone phase. Build and deploy a production LLM-powered application.

> Build and deploy a production LLM-powered application from first principles.

---

## Repo Usage

| Repo | How to use |
|------|-----------|
| `LLMs-from-scratch` | Core curriculum: chapters 1–7 in order, every notebook |
| `llm-course` | Supplement: RAG, fine-tuning, RLHF, deployment modules |
| `500-AI-Agents-Projects` | Pick 3 project ideas and build them |
| `ai-engineering-hub` | Production project examples: RAG, agents, MCP, fine-tuning |
| `nn-zero-to-hero` | Reference back to nanoGPT for architectural questions |

---

## Week 47 — Transformer Architecture Deep Dive

| Day | Focus | Task |
|-----|-------|------|
| Mon | LLMs-from-scratch Ch 1 | Data preparation. Tokenization. Build BPE tokenizer. |
| Tue | LLMs-from-scratch Ch 2 | Token embeddings. Positional embeddings. Attention masking. |
| Wed | LLMs-from-scratch Ch 3 | Self-attention from scratch. Multi-head attention. |
| Thu | LLMs-from-scratch Ch 3 | Implement causal self-attention. Compare to Karpathy's version. |
| Fri | LLMs-from-scratch Ch 4 | GPT model architecture. LayerNorm, GELU, residual connections. |
| Sat | Build | Train a tiny GPT (10M params) on a text corpus. Generate samples. |

---

## Week 48 — Pretraining + Training Dynamics

| Day | Focus | Task |
|-----|-------|------|
| Mon | LLMs-from-scratch Ch 5 | Pretraining loop. Cross-entropy loss. Gradient clipping. |
| Tue | Training Dynamics | Learning rate warmup, cosine annealing. Study loss curves. |
| Wed | Scaling Laws | Read "Scaling Laws for Neural Language Models" (Kaplan et al.) summary. |
| Thu | Tokenizer Deep Dive | Implement BPE from scratch. Compare to tiktoken. Understand vocabulary size trade-offs. |
| Fri | Build | Extend nanoGPT training: add gradient accumulation + mixed precision (bf16). |
| Sat | Study | Read "Language Models are Few-Shot Learners" (GPT-3 paper) — abstract + architecture sections. |

---

## Week 49 — Fine-Tuning

| Day | Focus | Task |
|-----|-------|------|
| Mon | LLMs-from-scratch Ch 6 | Instruction fine-tuning. Data formatting (Alpaca format). |
| Tue | LLMs-from-scratch Ch 7 | Preference fine-tuning (DPO basics). |
| Wed | LoRA | Low-rank adaptation. Why it works. Implement LoRA layers. |
| Thu | QLoRA | 4-bit quantization + LoRA. Run QLoRA fine-tuning on a 7B model locally. |
| Fri | Datasets | Study dataset curation. Deduplication, quality filtering, format conversion. |
| Sat | Build | Fine-tune a 7B model on a domain-specific task using QLoRA. |

---

## Week 50 — RAG Systems

| Day | Focus | Task |
|-----|-------|------|
| Mon | Embeddings | Sentence transformers. Embedding models (`all-MiniLM-L6-v2`, `text-embedding-3-small`). |
| Tue | Vector Databases | ChromaDB (local) → Pinecone (cloud). HNSW index. Similarity search. |
| Wed | RAG Pipeline | Chunk → embed → store → retrieve → augment → generate. Build end-to-end. |
| Thu | Chunking Strategies | Fixed-size, recursive, semantic chunking. Study trade-offs. |
| Fri | Retrieval Quality | MMR, hybrid search (BM25 + dense), reranking (cross-encoders). |
| Sat | Build | RAG over a domain-specific document corpus. |

---

## Week 51 — Advanced RAG + Evaluation

| Day | Focus | Task |
|-----|-------|------|
| Mon | Advanced RAG | Parent-child chunking, HyDE (hypothetical document embeddings), multi-query retrieval. |
| Tue | RAGAS | Faithfulness, answer relevancy, context precision/recall. Evaluate your RAG pipeline. |
| Wed | Hallucination | Why LLMs hallucinate. Mitigation: grounding, citations, retrieval verification. |
| Thu | LLM Evals | G-Eval, LLM-as-judge. Build an eval harness. |
| Fri | Build | Add RAGAS evaluation to CI/CD — fail deploy if faithfulness score drops below threshold. |
| Sat | Study | Read "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" paper (Lewis et al. 2020). |

---

## Week 52 — AI Agents

| Day | Focus | Task |
|-----|-------|------|
| Mon | Agent Concepts | ReAct, Chain of Thought, tool calling. Study `500-AI-Agents-Projects/` and `ai-engineering-hub/` for ideas. |
| Tue | Tool Calling | Anthropic tool use or OpenAI function calling. Build agent with: web search, PDF reader, custom tools. |
| Wed | LangGraph | Stateful agent graphs. Checkpointing. Build a multi-step research agent. |
| Thu | Memory | Short-term (conversation), long-term (vector store), episodic. Add memory to your agent. |
| Fri | Multi-Agent | Orchestrator + worker pattern. Build: researcher agent + writer agent working together. |
| Sat | Build | End-to-end agentic workflow: agent reads input → researches → synthesizes → produces output. |

---

## Week 53 — LLM Deployment

| Day | Focus | Task |
|-----|-------|------|
| Mon | Quantization | GGUF (llama.cpp), GPTQ, AWQ. Run a quantized 7B model on CPU. Compare quality vs speed. |
| Tue | Inference Servers | vLLM, Ollama, TGI (Text Generation Inference). Deploy local inference endpoint. |
| Wed | Streaming | Token streaming with SSE. Add streaming to your web app AI chat. |
| Thu | Caching | Semantic caching (GPTCache). Prompt caching (Anthropic API). |
| Fri | Cloud Inference | AWS Bedrock, Google Vertex AI, Azure OpenAI. Cost comparison. |
| Sat | Build | Deploy LLM inference on K8s (from Phase 4). vLLM + GPU node. Auto-scale on request queue depth. |

---

## Week 54 — Production LLMs

| Day | Focus | Task |
|-----|-------|------|
| Mon | Prompt Engineering | System prompts, few-shot, chain-of-thought, structured output (JSON mode). |
| Tue | Structured Output | Instructor library, Pydantic models, function calling for reliable JSON. |
| Wed | Cost Optimization | Token counting, prompt compression, caching, model routing. |
| Thu | Observability | LangSmith or Langfuse. Trace every LLM call. Monitor latency, cost, quality. |
| Fri | Guardrails | Content moderation, PII detection, prompt injection defense. |
| Sat | Build | Add full LLM observability: every call traced, cost tracked, quality scored. |

---

## Week 55 — Advanced Topics

| Day | Focus | Task |
|-----|-------|------|
| Mon | RLHF | PPO, reward modeling, preference data. Read "InstructGPT" paper summary. |
| Wed | DPO | Direct Preference Optimization. Simpler alternative to RLHF. |
| Thu | Multimodal | Vision-language models (LLaVA, GPT-4V). Add image/screenshot analysis. |
| Fri | Coding LLMs | Code-specific models (DeepSeek Coder, CodeLlama). Use for code analysis features. |
| Sat | Build | Add multimodal: user uploads image → LLM extracts text + structure. |

---

## Week 56 — AI Safety + Ethics

| Day | Focus | Task |
|-----|-------|------|
| Mon | AI Safety Basics | Alignment problem. Constitutional AI. Read Anthropic's alignment research overview. |
| Tue | Bias in LLMs | Sources of bias. Evaluation. Debiasing strategies. Audit your app for bias. |
| Wed | Privacy | PII in training data. GDPR compliance for LLM applications. Add PII scrubbing to pipeline. |
| Thu | Responsible AI | EU AI Act overview. Risk classification. |
| Fri | Red Teaming | Prompt injection attacks. Jailbreaking. How to defend. |
| Sat | Build | Security audit of LLM features. Fix all prompt injection vulnerabilities. |

---

## Weeks 57–60 — Capstone: Ship It

| Week | Dates | Goal |
|------|-------|------|
| Week 57 | Mar 22 – Mar 28 | Feature freeze. Write comprehensive README. Set up landing page. |
| Week 58 | Mar 29 – Apr 4 | Add demo mode with sample data. Record a 5-min demo video. |
| Week 59 | Apr 5 – Apr 11 | Write a detailed technical blog post on what you built. |
| Week 60 | Apr 12 – Apr 18 | Deploy to production. Open source it. Post on LinkedIn/HN. |

> **Roadmap Complete — You are now an AI/LLM Engineer.**

---

## Resources

### Books
- **Build a Large Language Model (From Scratch)** — Sebastian Raschka. Companion to `LLMs-from-scratch/`.
- **Hands-On Large Language Models** — Jay Alammar & Maarten Grootendorst.
- **Natural Language Processing with Transformers** — Tunstall, von Werra, Wolf.
- **AI Engineering** — Chip Huyen. Production AI systems. Essential.
- **Designing Machine Learning Systems** — Chip Huyen.
- **[How To Scale Your Model](https://jax-ml.github.io/scaling-book/)** — Austin et al., Google DeepMind. Free. Scaling LLMs on TPUs.

### Videos
- **Andrej Karpathy (YouTube)** — "Let's build GPT", "Let's reproduce GPT-2". Watch repeatedly.
- **Umar Jamil (YouTube)** — Implements transformers, BERT, LLaMA from scratch.
- **Aleksa Gordic — The AI Epiphany (YouTube)** — Paper implementations + walkthroughs.
- **Yannic Kilcher (YouTube)** — Paper reviews: GPT-3, RLHF, DPO, LoRA.

### Newsletters
- **Ahead of AI — Sebastian Raschka** — Every issue is essential.
- **Lilian Weng's Blog** — Deep posts on RL, diffusion, attention.
- **Nathan Lambert — Interconnects** — RLHF, alignment, LLM training.
- **Chip Huyen's Blog** — AI engineering, production ML.
- **Simon Willison's Blog** — Practical LLM experiments.

### Podcasts
- **Latent Space** — Best AI engineering podcast.
- **Lex Fridman Podcast** — Karpathy, Ilya Sutskever, Sam Altman episodes.
- **Machine Learning Street Talk** — Research-focused, dense and technical.
- **The Cognitive Revolution** — AI applications and business impact.
