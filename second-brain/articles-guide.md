# Capturing Articles into Your Second Brain

A lightweight guide for saving web content, papers, and long-form articles into a markdown-based second brain (Obsidian or similar).

---

## What to Capture

- PDFs of research papers or long-form articles
- Markdown/HTML exports from read-later apps (Readwise, Instapaper, Pocket)
- Web clips saved via browser extensions
- Papers from arXiv, ACM, semantic scholar

---

## Recommended Capture Tools

| Tool | Best for | Output |
|------|----------|--------|
| [MarkDownload](https://github.com/deathau/markdownload) | Any webpage | Clean Markdown |
| [Obsidian Web Clipper](https://obsidian.md/clipper) | Pages you want in Obsidian directly | Markdown with metadata |
| [Readwise Export](https://readwise.io/export) | Highlights from books, articles, PDFs | Markdown with highlights |
| Browser Print → Save as PDF | Anything that doesn't export well | PDF |

---

## Naming Convention

```
YYYY-MM-DD-author-or-site-short-title.md
```

**Examples:**
```
2026-05-14-andrej-karpathy-software-2.md
2026-06-01-lilian-weng-rlhf-overview.md
2026-07-20-neo-kim-kafka-deep-dive.md
```

---

## What to Do After Capturing

1. Add the source URL at the top of the file if not already present
2. Skim and highlight key passages
3. Ask your LLM to extract key ideas and create or update a concept page in `wiki/concepts/`
4. Log the ingest in `wiki/log.md`

---

## LLM Wiki Integration

If you're using the [LLM Wiki Pattern](../interview-prep/concepts/llm-wiki-pattern.md), raw articles live in `raw/articles/` and the LLM:
- Reads the article
- Creates or updates concept pages in `wiki/concepts/`
- Flags contradictions with existing wiki pages
- Updates `wiki/index.md` and appends to `wiki/log.md`

The raw article is never modified — it stays as the immutable source of record.

---

## High-Value Sources to Clip Regularly

| Source | Why |
|--------|-----|
| [Lilian Weng's Blog](https://lilianweng.github.io) | Deep posts on attention, RL, diffusion — dense, worth re-reading |
| [Sebastian Raschka — Ahead of AI](https://magazine.sebastianraschka.com) | LLM research breakdowns with code |
| [Simon Willison's Blog](https://simonwillison.net) | Practical LLM experiments and findings |
| [Neo Kim — System Design Newsletter](https://newsletter.systemdesign.one) | Architecture deep dives |
| arXiv CS papers | Primary source for any paper referenced in the roadmap |
