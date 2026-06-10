# Setup Guide

## Prerequisites

- macOS (for audio routing via BlackHole — Linux users can use PulseAudio loopback instead)
- Python 3.10+
- An Anthropic API key

## 1. Install BlackHole (macOS audio loopback)

BlackHole routes system audio (Zoom, Google Meet, etc.) into a virtual input device so Whisper can transcribe it.

```bash
brew install blackhole-2ch
```

Then open **Audio MIDI Setup** (search in Spotlight), click `+` → **Create Aggregate Device**, and check both your microphone and BlackHole 2ch. Name it "Interview Aggregate".

## 2. Install Python dependencies

```bash
pip install openai-whisper sounddevice numpy anthropic
```

> Whisper downloads model weights on first run (~140MB for `base`).

## 3. Set your API key

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

Add this to your `~/.zshrc` or `~/.bashrc` to persist it.

## 4. Verify audio setup

```bash
python realtime_transcription.py
```

Select your "Interview Aggregate" device. Speak — you should see transcribed lines appear within 5 seconds.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `No module named 'whisper'` | `pip install openai-whisper` (not `whisper`) |
| No audio captured | Select the correct aggregate device; check macOS mic permissions for Terminal |
| `ANTHROPIC_API_KEY not set` | Run `export ANTHROPIC_API_KEY="..."` in the same shell |
| Bus error on audio | Aggregate device channel count mismatch — re-create the aggregate device |
