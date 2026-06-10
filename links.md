# Learning Resources

Consolidated from my SWE → AI/LLM Engineer roadmap. Organized by phase.

## Core GitHub Repos (used throughout)

- [coding-interview-university](https://github.com/jwasham/coding-interview-university) — master checklist for CS fundamentals
- [javascript-algorithms](https://github.com/trekhleb/javascript-algorithms) — read explanations before implementing
- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) — implement every algorithm yourself
- [system-design-primer](https://github.com/donnemartin/system-design-primer) — core system design reading
- [interactive-coding-challenges](https://github.com/donnemartin/interactive-coding-challenges) — Jupyter practice after each topic
- [low-level-design-primer](https://github.com/prasadgujar/low-level-design-primer) — OOP design problems
- [awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) — supplementary reference
- [90DaysOfDevOps](https://github.com/MichaelCade/90DaysOfDevOps) — DevOps curriculum
- [kubernetes-the-hard-way](https://github.com/kelseyhightower/kubernetes-the-hard-way) — K8s from first principles
- [devops-exercises](https://github.com/bregman-arie/devops-exercises) — interview-style infra exercises
- [nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) — Karpathy's core ML curriculum, every notebook in order
- [micrograd](https://github.com/karpathy/micrograd) — tiny scalar autograd engine (~100 lines); read alongside Lecture 1
- [makemore](https://github.com/karpathy/makemore) — autoregressive character-level LM; companion to Lectures 2–5
- [nanoGPT](https://github.com/karpathy/nanoGPT) — fastest repo for training/fine-tuning medium-sized GPTs (59k⭐)
- [build-nanogpt](https://github.com/karpathy/build-nanogpt) — video + code: build nanoGPT step by step; watch "Let's reproduce GPT-2"
- [minbpe](https://github.com/karpathy/minbpe) — minimal BPE tokenizer from scratch; essential companion to Phase 6 tokenization
- [llama2.c](https://github.com/karpathy/llama2.c) — Llama 2 inference in a single C file; understand inference mechanics at the metal
- [llm.c](https://github.com/karpathy/llm.c) — LLM training in raw C/CUDA; advanced; tackle in Phase 6 capstone (30k⭐)
- [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) — Raschka, chapters 1–7
- [llm-course](https://github.com/mlabonne/llm-course) — RAG, fine-tuning, RLHF, deployment modules
- [500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) — agent project ideas
- [ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) — 93+ production-ready LLM/RAG/agent projects, beginner → advanced (35k⭐)

## Phase 0 — CS Foundations

**Course:** [Harvard CS50x](https://cs50.harvard.edu/x) (free; also on [edX](https://www.edx.org/cs50) with graded problem sets and [YouTube](https://www.youtube.com/@cs50))

**Books:** *The C Programming Language* (K&R) · *Python Crash Course* (Matthes) · *Grokking Algorithms* (Bhargava)

**Essays:** [Paul Graham — Hackers and Painters](https://www.paulgraham.com/articles.html) · [Joel on Software](https://www.joelonsoftware.com)

**Podcasts:** [Software Engineering Daily](https://softwareengineeringdaily.com) · [CoRecursive](https://corecursive.com)

## Phase 1 — DSA

**Books:** *Cracking the Coding Interview* (McDowell) · *Grokking Algorithms* · *CLRS* (reference) · *The Algorithm Design Manual* (Skiena, Part I) · *Elements of Programming Interviews*

**Videos:** [NeetCode](https://www.youtube.com/@NeetCode) (best problem explanations) · Abdul Bari (deepest algorithm explanations) · Back to Back SWE · [3Blue1Brown](https://www.youtube.com/@3blue1brown) (math intuition)

**Practice/Newsletters:** [NeetCode.io](https://neetcode.io) (daily problem queue) · [AlgoMaster — Ashish Pratap Singh](https://blog.algomaster.io) · [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com) · [Quastor](https://www.quastor.org) (free)

## Phase 2 — System Design + Networking

**Books:** *Designing Data-Intensive Applications* (Kleppmann — most important book in the roadmap) · *System Design Interview Vol. 1 & 2* (Alex Xu) · *Computer Networks: A Top-Down Approach* (Kurose & Ross, Ch 1–4) · *Clean Architecture* (Martin)

**Videos:** [ByteByteGo](https://www.youtube.com/@ByteByteGo) (best system design animations) · Gaurav Sen · [Hussein Nasser](https://www.youtube.com/@hnasr) (networking + backend) · [NetworkChuck](https://www.youtube.com/@NetworkChuck)

**Blogs/Newsletters:** [ByteByteGo Newsletter](https://blog.bytebytego.com) · [High Scalability](http://highscalability.com) · [Martin Fowler](https://martinfowler.com) · [Netflix Tech Blog](https://netflixtechblog.com) (1 post/week) · [Haki Benita](https://hakibenita.com) (PostgreSQL internals) · [Neo Kim — System Design Newsletter](https://newsletter.systemdesign.one) (deep dives on real architectures — Kafka, S3, Tinder, WhatsApp, Uber, Vitess, Stock Exchange, OpenAI's Postgres scale)

**Must-read architecture deep dives (Neo Kim + others):** Airbnb monolith → microservices · WhatsApp system design · Spotify architecture · How Reddit works · How Bluesky works · How Google Docs works · Kafka mechanics · Tinder architecture · Slack architecture · S3 architecture · URL shortener · Serverless architecture · Vitess MySQL · AWS at scale · Stock exchange system design · How Uber finds nearby drivers · How OpenAI scaled to 800M users with Postgres

**Practice:** [Codemia](https://codemia.io) — system design problem practice

**Tools:** [draw.io](https://draw.io) · [Excalidraw](https://excalidraw.com) for architecture diagrams

## Phase 3 — Frontend + Full-Stack

**Books:** [*You Don't Know JS*](https://github.com/getify/You-Dont-Know-JS) (free — Scope & Closures, this & Object Prototypes) · *Learning TypeScript* (Goldberg) · *Fluent React* (Kumar)

**Videos:** [Fireship](https://www.youtube.com/@Fireship) · [Theo — t3.gg](https://www.youtube.com/@t3dotgg) · Jack Herrington · Vercel channel (Next.js Conf talks)

**Blogs/Newsletters:** [Josh W. Comeau](https://www.joshwcomeau.com) (CSS + React) · [overreacted.io](https://overreacted.io) (Dan Abramov) · [Total TypeScript](https://www.totaltypescript.com) (Matt Pocock) · [Lee Robinson](https://leerob.com) (Next.js) · [Bytes.dev](https://bytes.dev) (weekly JS/TS)

**Podcasts:** [Syntax.fm](https://syntax.fm) · JS Party

## Phase 4 — Cloud Infrastructure

**Certs targeted:** AWS Cloud Practitioner → Terraform Associate → AWS Solutions Architect Associate → CKA

**Books:** *The DevOps Handbook* · [*Site Reliability Engineering*](https://sre.google/books/) (Google, free — the production-systems bible) · *Terraform: Up & Running* (Brikman) · *Kubernetes in Action* (Luksa) · *Cloud Native Patterns* (Davis)

**Videos:** [TechWorld with Nana](https://www.youtube.com/@TechWorldwithNana) (best Docker/K8s/CI-CD — watch everything) · Fireship · NetworkChuck · AWS re:Invent talks

**Newsletters/Blogs:** [Last Week in AWS](https://www.lastweekinaws.com) (Corey Quinn) · [Kubernetes Blog](https://kubernetes.io/blog/) · [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/) · The Pragmatic Engineer

## Phase 5 — ML Foundations

**Cert targeted:** Google Professional ML Engineer

**Books:** *Hands-On Machine Learning* (Géron) · [*Deep Learning*](https://www.deeplearningbook.org) (Goodfellow et al., free) · [*Mathematics for Machine Learning*](https://mml-book.github.io) (free) · [*Neural Networks and Deep Learning*](http://neuralnetworksanddeeplearning.com) (Nielsen, free)

**Videos:** [3Blue1Brown](https://www.youtube.com/@3blue1brown) — Neural Networks playlist first, then Essence of Linear Algebra (15 videos) and Essence of Calculus · [Andrej Karpathy](https://www.youtube.com/@AndrejKarpathy) — all 7 zero-to-hero lectures in order · [StatQuest](https://www.youtube.com/@statquest) · [Yannic Kilcher](https://www.youtube.com/@YannicKilcher) (paper reviews)

**Blogs/Newsletters:** [Ahead of AI — Sebastian Raschka](https://magazine.sebastianraschka.com) (subscribe immediately) · [Lilian Weng](https://lilianweng.github.io) (bookmark every post) · [The Batch](https://www.deeplearning.ai/the-batch/) (Andrew Ng) · [Chip Huyen](https://huyenchip.com/blog/)

**Papers:** Attention Is All You Need (architecture, before Phase 6) · the original Batch Normalization paper

**Podcasts:** Lex Fridman (Karpathy, Hinton, LeCun episodes) · Machine Learning Street Talk · TWIML AI

## Phase 6 — LLMs + AI Engineering

**Books:** *Build a Large Language Model (From Scratch)* (Raschka) · *Hands-On Large Language Models* (Alammar & Grootendorst) · *NLP with Transformers* (Tunstall, von Werra, Wolf) · *AI Engineering* (Chip Huyen — essential) · *Designing Machine Learning Systems* (Chip Huyen)

**Videos:** Karpathy — "Let's build GPT" and "Let's reproduce GPT-2" (watch repeatedly) · Umar Jamil (transformers/BERT/LLaMA from scratch) · Aleksa Gordić — The AI Epiphany · Yannic Kilcher (GPT-3, RLHF, DPO, LoRA reviews)

**Blogs/Newsletters:** Ahead of AI · Lilian Weng · [Interconnects — Nathan Lambert](https://www.interconnects.ai) (RLHF/alignment) · Chip Huyen · [Simon Willison](https://simonwillison.net) (practical LLM experiments)

**Papers:** Scaling Laws for Neural Language Models (Kaplan et al.) · GPT-3 ("Language Models are Few-Shot Learners") · InstructGPT · the original RAG paper

**Podcasts:** [Latent Space](https://www.latent.space) (best AI engineering podcast) · Lex Fridman (Sutskever, Altman, Karpathy) · Machine Learning Street Talk · The Cognitive Revolution

**Repos:** [ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) — 93+ production projects (RAG pipelines, agentic systems, MCP, fine-tuning) with notebooks; work through these alongside Phase 6 reading · [How To Scale Your Model](https://jax-ml.github.io/scaling-book/) ([source](https://github.com/jax-ml/scaling-book)) — Google DeepMind textbook on LLM scaling: TPU architecture, parallelism strategies, roofline analysis, training vs inference tradeoffs; read after finishing the core LLM books · [nanoGPT](https://github.com/karpathy/nanoGPT) — Karpathy's fastest GPT training repo; use for Weeks 48–49 experiments · [build-nanogpt](https://github.com/karpathy/build-nanogpt) — lecture companion; watch before or alongside nanoGPT experiments · [minbpe](https://github.com/karpathy/minbpe) — BPE tokenizer from scratch; complete alongside Week 47 tokenization tasks · [llama2.c](https://github.com/karpathy/llama2.c) — Llama 2 inference in one C file; read Week 50 for inference internals · [llm.c](https://github.com/karpathy/llm.c) — LLM training in C/CUDA; capstone-level deep dive (Weeks 59–60)

## Misc Saved Links

- [How to Prepare for Coding Interviews in 2024](https://medium.com/javarevisited/how-to-prepare-for-coding-interviews-in-2024-with-resources-3135861186bf)
- [Create an Attractive GitHub Profile README](https://dev.to/parth_johri/create-an-attractive-github-profile-readme-noj)
- [Create a macOS App with React Native](https://www.freecodecamp.org/news/create-a-macos-app-with-react-native/)
- [Fly.io](https://fly.io) — app hosting for side projects
