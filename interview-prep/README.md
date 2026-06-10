# Interview Prep Toolkit

A set of tools for practicing, recording, and evaluating technical interviews using real-time audio transcription and Claude AI.

## How it fits together

```
Live interview / mock session
        ↓
realtime_transcription.py   — captures audio → transcript.txt
        ↓                           ↓
realtime_ai_assistant.py    watch_transcript.py
(live Claude feedback)       (manual copy-paste flow)
        ↓
transcript_to_claude.py     — streams new lines to Claude in real-time
        ↓
evals/eval_transcript.py    — post-session scored report
agents/mock_interview.py    — structured mock interview with instant feedback
```

## Quick Start

**First time:** follow [SETUP.md](SETUP.md) to install BlackHole, Whisper, and deps.

### Option A — Live interview with real-time AI coaching

Terminal 1: capture audio
```bash
python realtime_transcription.py
```

Terminal 2: stream to Claude
```bash
python transcript_to_claude.py
```

### Option B — Integrated (audio + Claude in one process)

```bash
python realtime_ai_assistant.py
# Enter an instruction, e.g. "Flag weak answers and suggest improvements"
```

### Option C — Watch only, analyze after

```bash
python watch_transcript.py
# Press Ctrl+C to print the full transcript for manual paste into Claude
```

### Mock interview practice

```bash
# Default: 4 questions, behavioral + ML/AI
python agents/mock_interview.py

# Custom role and categories
python agents/mock_interview.py --role "Staff ML Engineer" --categories behavioral ml_ai system_design --questions 6
```

### Post-session evaluation

```bash
python evals/eval_transcript.py transcript.txt --role "Senior AI Engineer"
python evals/eval_transcript.py mock_interview_20260609_143000.txt --json
```

## Tools

| File | Purpose |
|------|---------|
| `realtime_transcription.py` | Whisper-based audio capture → `transcript.txt` |
| `transcript_to_claude.py` | Streams new transcript lines to Claude every 2s |
| `realtime_ai_assistant.py` | Integrated: audio capture + Claude responses every 15s |
| `watch_transcript.py` | Display-only watcher; Ctrl+C prints full transcript |
| `evals/eval_transcript.py` | Scores a transcript on 5 dimensions, outputs report or JSON |
| `agents/mock_interview.py` | Interactive mock interview with per-answer feedback + final score |

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ANTHROPIC_API_KEY` | — | Required |
| `TRANSCRIPT_FILE` | `transcript.txt` | Path to transcript file |
| `RESPONSE_INTERVAL` | `15` | Seconds between Claude responses (ai_assistant only) |

## Related Projects

This toolkit integrates with the broader job-assistant ecosystem:

- **[job-assistant-api](https://github.com/ravivalluri/job-assistant-api)** — interview prep chat, offer evaluation, company research
- **[job-assistant-cli](https://github.com/ravivalluri/job-assistant-cli)** — Go CLI: manage applications, build tailored resumes
- **[job-assistant-resume](https://github.com/ravivalluri/job-assistant-resume)** — AI-powered resume tailoring with ATS scoring
- **[career-ops](https://github.com/ravivalluri/career-ops)** — full agentic pipeline: job scanning, evaluation, STAR story bank, negotiation scripts
