# SWE → AI/ML Engineer Resources

A curated second-brain for my 15-month transition from Software Engineer to AI/ML Engineer (Feb 2026 → Apr 2027). Built with Obsidian, published here for anyone following a similar path.

## Contents

| File / Folder | Description |
|---|---|
| [roadmap.md](roadmap.md) | High-level timeline, living project arc, essential papers, top newsletters |
| [links.md](links.md) | Curated resources per phase — courses, books, videos, blogs, podcasts, practice tools |
| [books.md](books.md) | Consolidated reading list with free/official links where available |
| [certifications.md](certifications.md) | Certification plan with target dates, study hours, and fees |
| [links-2026-finds.md](links-2026-finds.md) | Time-stamped finds: AI engineer interview prep, production RAG/agents, 2026 career roadmaps |
| [phases/](phases/) | Week-by-week study schedules for all 7 phases (daily tasks, repos, build milestones) |
| [interview-prep/](interview-prep/) | Real-time transcription, live Claude coaching, mock interview agent, transcript evals, concept notes |

## Roadmap at a Glance

| Phase | Focus | Dates |
|-------|-------|-------|
| 0 | CS Foundations (CS50) | Feb – Mar 2026 |
| 1 | DSA Deep Dive | Mar – May 2026 |
| 2 | System Design + Networking | May – Jul 2026 |
| 3 | Frontend + Full-Stack | Jul – Sep 2026 |
| 4 | Cloud Infrastructure | Sep – Nov 2026 |
| 5 | ML Foundations | Nov 2026 – Jan 2027 |
| 6 | LLMs + AI Engineering | Jan – Apr 2027 |

## Interview Prep Toolkit

The [`interview-prep/`](interview-prep/) folder contains a full practice pipeline:

```
Live session audio
      ↓
realtime_transcription.py  →  transcript.txt
      ↓
transcript_to_claude.py    →  real-time Claude coaching
      ↓
evals/eval_transcript.py   →  scored report (5 dimensions)
agents/mock_interview.py   →  structured mock sessions with instant feedback
```

See [interview-prep/README.md](interview-prep/README.md) for quick start and [interview-prep/SETUP.md](interview-prep/SETUP.md) for macOS audio setup.

## Related Projects

This repo is the learning layer. The active build layer lives in the `job-assistant-*` ecosystem:

| Repo | Description |
|------|-------------|
| [job-assistant-api](https://github.com/ravivalluri/job-assistant-api) | Central backend: interview prep chat, offer evaluation (A–F), company research |
| [job-assistant-cli](https://github.com/ravivalluri/job-assistant-cli) | Go CLI: manage applications, generate tailored resumes |
| [job-assistant-resume](https://github.com/ravivalluri/job-assistant-resume) | AI resume tailoring with ATS scoring and DOCX export |
| [career-ops](https://github.com/ravivalluri/career-ops) | Full agentic pipeline: job portal scanning, batch evaluation, STAR story bank, negotiation scripts |

## License

[CC BY 4.0](LICENSE) — share and adapt freely with attribution.
