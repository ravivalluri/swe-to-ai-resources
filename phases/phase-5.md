# Phase 5 — ML Foundations

**Dates:** Nov 16, 2026 – Jan 10, 2027 (Weeks 39–46)
**Cert:** Google Professional ML Engineer (Jan 10, 2027)
**Goal:** Build the mathematical and practical ML foundations needed before diving into LLMs.

---

## Repo Usage

| Repo | How to use |
|------|-----------|
| `TheAlgorithms/Python` | `machine_learning/` and `neural_network/` — study then rewrite from scratch |
| `nn-zero-to-hero` | Core curriculum: follow every notebook in order |
| `micrograd` | Companion to Lecture 1 — read source alongside the notebook, then rewrite from memory |
| `makemore` | Companion to Lectures 2–5 — bigram → MLP → backprop → WaveNet |

---

## Week 39 — Math Foundations

| Day | Focus | Task |
|-----|-------|------|
| Mon | Linear Algebra | Vectors, matrices, matrix multiplication, eigenvalues. Watch 3Blue1Brown "Essence of Linear Algebra" (all 15 videos). |
| Tue | Calculus | Derivatives, chain rule, partial derivatives, gradients. Watch 3Blue1Brown "Essence of Calculus". |
| Wed | Statistics | Mean, variance, distributions (normal, binomial). Bayes' theorem. Maximum likelihood. |
| Thu | Probability | Conditional probability, expectation, entropy, KL divergence. |
| Fri | NumPy | Implement matrix operations from scratch. Then use NumPy. Understand broadcasting. |
| Sat | Build | Implement gradient descent from scratch on a quadratic function. Visualize convergence. |

---

## Week 40 — Classic ML Algorithms

| Day | Focus | Task |
|-----|-------|------|
| Mon | Linear Regression | Derive the cost function. Implement gradient descent. Study `TheAlgorithms/Python/machine_learning/linear_regression.py`. |
| Tue | Logistic Regression | Sigmoid, binary cross-entropy. Implement from scratch. |
| Wed | Decision Trees | Information gain, Gini impurity. Read the decision tree implementation. |
| Thu | k-NN + k-Means | Implement both from scratch. |
| Fri | SVM | Hinge loss, margin maximization. Conceptual understanding. |
| Sat | Build | Train a logistic regression classifier on a text dataset from scratch (no sklearn). |

---

## Week 41 — Neural Networks from Scratch

| Day | Focus | Task |
|-----|-------|------|
| Mon | Perceptron | Implement a single neuron with sigmoid activation. Understand weight update. |
| Tue | MLP Forward Pass | Implement a 2-layer MLP. Matrix math only. Study `TheAlgorithms/Python/neural_network/`. |
| Wed | Backpropagation | Derive backprop by hand. Implement it. Compare output with numerical gradient check. |
| Thu | Karpathy micrograd | Complete `nn-zero-to-hero/` Lecture 1 (micrograd). Understand autograd. |
| Fri | Activation Functions | ReLU, sigmoid, tanh, GELU. When to use each. |
| Sat | Build | Train your MLP from scratch on MNIST. Get >90% accuracy without any ML libraries. |

---

## Week 42 — PyTorch Fundamentals

| Day | Focus | Task |
|-----|-------|------|
| Mon | Tensors | PyTorch tensors vs NumPy. Gradients, autograd, `requires_grad`. |
| Tue | nn.Module | Build your MLP in PyTorch. Understand `forward()`, `parameters()`, `zero_grad()`. |
| Wed | Training Loop | Dataloaders, loss functions, optimizers (SGD, Adam). Write the canonical training loop. |
| Thu | Karpathy makemore | Complete `nn-zero-to-hero/` Lecture 2 (bigram language model). |
| Fri | CNNs | Convolutions, pooling, stride. Implement CNN for image classification. |
| Sat | Build | Train PyTorch CNN on CIFAR-10. Log training curves. |

---

## Week 43 — Karpathy Zero to Hero

| Day | Focus | Task |
|-----|-------|------|
| Mon | makemore MLP | Complete `nn-zero-to-hero/` Lecture 3 (MLP language model, batch norm). |
| Tue | makemore Backprop | Complete `nn-zero-to-hero/` Lecture 4 (manual backprop). |
| Wed | WaveNet | Complete `nn-zero-to-hero/` Lecture 5 (WaveNet-style model). |
| Thu | GPT Attention | Complete `nn-zero-to-hero/` Lecture 6 (building GPT) — first half. |
| Fri | nanoGPT | Complete `nn-zero-to-hero/` Lecture 6 second half. Train a small GPT. |
| Sat | Build | Train nanoGPT on a custom text dataset of your choosing. |

---

## Week 44 — Modern ML in Practice

| Day | Focus | Task |
|-----|-------|------|
| Mon | Transfer Learning | Fine-tuning pretrained models. HuggingFace `transformers` basics. |
| Tue | Embeddings | Word2Vec, GloVe, sentence-transformers. Generate embeddings for a text corpus. |
| Wed | Vector Similarity | Cosine similarity, approximate nearest neighbor search. |
| Thu | Model Evaluation | Precision, recall, F1, AUC-ROC, confusion matrix. Evaluate your classifier. |
| Fri | MLOps Basics | Experiment tracking (MLflow or W&B). Model versioning. Save/load models. |
| Sat | Build | Add ML-powered matching to a project: embed two documents → cosine similarity score. |

---

## Week 45 — Regularization + Optimization

| Day | Focus | Task |
|-----|-------|------|
| Mon | Overfitting | Bias-variance tradeoff. L1/L2 regularization, dropout. |
| Tue | Optimizers | SGD, Momentum, RMSprop, Adam, AdamW. Learning rate schedules. |
| Wed | Batch Normalization | Why it works. Implement from scratch. Read the original paper. |
| Thu | Attention Mechanism | Study attention from scratch before Phase 6. Read "Attention is All You Need" abstract + architecture. |
| Fri | Build | Hyperparameter tune your model. Grid search over learning rate + dropout. |
| Sat | Retrospective | Write Phase 5 retrospective. Document what surprised you most. |

---

## Week 46 — Transition to LLMs

| Day | Focus | Task |
|-----|-------|------|
| Mon | Transformer Architecture | Study "Attention is All You Need" architecture carefully. Draw every component. |
| Tue | Tokenization | BPE, WordPiece, SentencePiece. Implement a basic BPE tokenizer. Study `LLMs-from-scratch/` Ch 1–2. |
| Wed | Positional Encoding | Sinusoidal vs RoPE vs ALiBi. Implement sinusoidal PE. |
| Thu | Self-Attention | Multi-head attention from scratch. Study `LLMs-from-scratch/` Ch 3. |
| Fri | Phase 6 Prep | Set up GPU environment (CUDA or Apple Silicon MPS). Test PyTorch GPU training. |
| Sat | Review | Complete all `nn-zero-to-hero/` notebooks if any unfinished. |

> **Jan 10: Take Google Professional ML Engineer exam**

---

## Resources

### Books
- **Hands-On Machine Learning** — Aurélien Géron. Best practical ML book.
- **[Deep Learning](https://www.deeplearningbook.org)** — Goodfellow, Bengio, Courville. Free online. The theoretical bible.
- **[Mathematics for Machine Learning](https://mml-book.github.io)** — Deisenroth et al. Free online.
- **[Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com)** — Nielsen. Free online. Best conceptual introduction.

### Videos
- **3Blue1Brown (YouTube)** — Watch "Neural Networks" playlist first. Then Linear Algebra + Calculus.
- **Andrej Karpathy (YouTube)** — `nn-zero-to-hero` lectures. Watch all 7 in order.
- **StatQuest (YouTube)** — Statistics + ML intuitions. Essential.
- **Yannic Kilcher (YouTube)** — ML paper reviews.

### Newsletters
- **Ahead of AI — Sebastian Raschka** — Subscribe immediately. Best ML + LLM research newsletter.
- **Lilian Weng's Blog** — Deep posts on attention, RL, diffusion. Bookmark every post.
- **The Batch (Andrew Ng)** — Weekly AI news.
- **Chip Huyen's Blog** — ML systems, production ML.

### Podcasts
- **Lex Fridman Podcast** — Karpathy, Hinton, LeCun episodes.
- **Machine Learning Street Talk** — Technical ML discussions.
- **TWIML AI Podcast** — Weekly practitioner interviews.
