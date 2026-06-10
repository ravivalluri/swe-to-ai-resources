# Roadmap Overview

> **Philosophy:** Learn through repos you already own. Build one real project that grows each phase.
> **Commitment:** 2–3 hrs/day, 6 days/week (Sunday = rest/review). **Duration:** ~15 months (Feb 2026 → Apr 2027)

## Timeline

| Phase | Weeks | Dates | Focus |
|---|---|---|---|
| 0 | 1–4 | Feb 24 – Mar 22, 2026 | CS50 Foundations |
| 1 | 5–12 | Mar 23 – May 17, 2026 | DSA Deep Dive |
| 2 | 13–20 | May 18 – Jul 12, 2026 | System Design + Networking |
| 3 | 21–28 | Jul 13 – Sep 6, 2026 | Frontend + Full-Stack |
| 4 | 29–38 | Sep 7 – Nov 15, 2026 | Cloud Infrastructure |
| 5 | 39–46 | Nov 16, 2026 – Jan 10, 2027 | ML Foundations |
| 6 | 47–60 | Jan 11 – Apr 18, 2027 | LLMs + AI Engineering |

## The Living Project (`job-assistant-*`)

| Repo | Phase | Role |
|---|---|---|
| `job-assistant-cli` | 0 | Rewrite core logic while learning memory |
| `job-assistant-api` | 2/3 | System design + REST API layer |
| `job-assistant-extension` | 3 | TypeScript/React patterns |
| `job-assistant-mobile` | 3 | Expo + React Native polish |
| `job-assistant-web` | 3 → 4 → 6 | Build Next.js dashboard → containerize on K8s → add RAG + agent brain |
| `job-assistant-resume` | 5/6 | ML + LLM-powered resume tailoring |

**End goal:** a deployed, cloud-native, LLM-powered job intelligence platform built from first principles.

## Essential Papers (read in order)

| Paper | Phase | Why |
|---|---|---|
| [Attention Is All You Need (2017)](https://arxiv.org/abs/1706.03762) | 5 | Foundation of all modern LLMs |
| [BERT (2018)](https://arxiv.org/abs/1810.04805) | 5 | Bidirectional transformers |
| [GPT-3 (2020)](https://arxiv.org/abs/2005.14165) | 6 | Few-shot learning, scaling |
| [RAG — Lewis et al. (2020)](https://arxiv.org/abs/2005.11401) | 6 | Retrieval-augmented generation |
| [Scaling Laws (Kaplan et al., 2020)](https://arxiv.org/abs/2001.08361) | 6 | Why scale works |
| [LoRA (2021)](https://arxiv.org/abs/2106.09685) | 6 | Parameter-efficient fine-tuning |
| [InstructGPT (2022)](https://arxiv.org/abs/2203.02155) | 6 | RLHF and alignment |
| [Chain-of-Thought Prompting (2022)](https://arxiv.org/abs/2201.11903) | 6 | Reasoning in LLMs |
| [LLaMA (2023)](https://arxiv.org/abs/2302.13971) | 6 | Open-weight models |
| [DPO (2023)](https://arxiv.org/abs/2305.18290) | 6 | Simpler alternative to RLHF |
| [Mixtral (2023)](https://arxiv.org/abs/2401.04088) | 6 | Mixture of Experts |

## Top 10 Must-Subscribe Newsletters

1. [ByteByteGo](https://blog.bytebytego.com) — system design, 2×/week
2. [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com) — big tech engineering
3. [Ahead of AI](https://magazine.sebastianraschka.com) — LLM/ML research
4. [Latent Space](https://www.latent.space) — AI engineering
5. [Quastor](https://www.quastor.org) — DSA + system design, free
6. [The Batch](https://www.deeplearning.ai/the-batch/) — AI news
7. [Last Week in AWS](https://www.lastweekinaws.com) — cloud/AWS
8. [Lilian Weng](https://lilianweng.github.io) — research blog
9. [Bytes.dev](https://bytes.dev) — JS/TS news
10. [Interconnects](https://www.interconnects.ai) — LLM training + RLHF
