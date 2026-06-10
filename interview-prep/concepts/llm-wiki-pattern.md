# LLM Wiki Pattern

A method for building personal knowledge bases where an LLM incrementally builds and maintains a persistent wiki alongside your raw sources. Knowledge is compiled once and kept current — not re-derived on every question.

---

## The Core Distinction

Most LLM-document systems work via **RAG**: retrieve relevant chunks at query time, generate an answer, discard the work. Nothing accumulates. The LLM Wiki flips this: the LLM writes a persistent, interlinked wiki that grows richer with every source added and every question asked.

The wiki is a **compounding artifact** — cross-references are already there, contradictions are already flagged, synthesis already reflects everything ingested so far.

See [rag.md](rag.md) for the contrast case.

---

## Three Layers

| Layer | Owner | Rule |
|-------|-------|------|
| Raw sources | Human | Immutable — LLM reads, never writes |
| Wiki | LLM | Created and maintained entirely by the LLM |
| Schema | Human + LLM | Co-evolved over time; tells LLM the conventions and workflows |

---

## Three Operations

**Ingest** — drop a source, LLM reads it, updates 5–15 wiki pages, logs the run. The LLM doesn't just summarize; it integrates: updating entity pages, flagging where new data contradicts old claims, adding cross-references.

**Query** — ask a question; LLM reads the index, reads relevant pages, answers with citations. Crucially: valuable answers (comparisons, analyses, non-obvious connections) get filed back into the wiki rather than disappearing into chat history.

**Lint** — periodic health check: contradictions, orphan pages, stale claims, missing pages, data gaps. The LLM proposes fixes; the human approves.

---

## Indexing

Two special files anchor navigation:

- **`index.md`** — content-oriented catalog; every page listed with a one-line summary organized by category. Read first on every query.
- **`log.md`** — append-only chronological record; each entry prefixed `## [YYYY-MM-DD] operation | title` so it's parseable with `grep "^## \["`.

---

## Why It Works

The tedious part of maintaining a knowledge base is the bookkeeping — updating cross-references, keeping summaries current, noting contradictions. Humans abandon wikis because maintenance burden grows faster than value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass.

**Human's job**: curate sources, direct analysis, ask good questions.
**LLM's job**: everything else.

---

## Tooling

| Tool | Purpose |
|------|---------|
| [Obsidian](https://obsidian.md) | Recommended viewer — graph view, Dataview queries, Marp slide decks |
| [qmd](https://github.com/simonw/llm-cmd) | Local hybrid BM25/vector search for markdown; useful once the wiki outgrows the index file |
| [Obsidian Web Clipper](https://obsidian.md/clipper) | Converts web articles to Markdown for quick raw-source capture |
| [MarkDownload](https://github.com/deathau/markdownload) | Browser extension — save any page as clean Markdown |

---

## Analogies and Antecedents

- **Vannevar Bush's Memex (1945)** — private, curated knowledge store with associative trails. Bush's vision was closer to this than to what the web became. The unsolved part was who does the maintenance — answered here by the LLM.
- **Fan wikis** (e.g. Tolkien Gateway) — thousands of interlinked pages built by volunteers over years. This pattern lets one person build something comparable, personally, as they read.
- **RAG** — the contrast case. Retrieves but does not accumulate. No compounding. See [rag.md](rag.md).

---

## RAG vs LLM Wiki

| Dimension | RAG | LLM Wiki |
|-----------|-----|----------|
| Knowledge persistence | None — ephemeral per query | Yes — compounding wiki |
| Cross-referencing | Done at query time | Pre-built, always available |
| Contradiction detection | None | Explicit, filed as notes |
| Infrastructure needed | Vector DB, embedding model | Markdown files |
| Best for | Large static corpora, Q&A over docs | Personal KB, evolving research |

The two are not mutually exclusive — the wiki's index file is a lightweight RAG-alternative at small scale; add vector search when the wiki grows large.
