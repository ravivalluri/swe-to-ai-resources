#!/usr/bin/env python3
"""
Integrated real-time AI assistant: captures audio, transcribes with Whisper,
and sends accumulated context to Claude every 15 seconds.

Usage:
    python realtime_ai_assistant.py
    TRANSCRIPT_FILE=session.txt RESPONSE_INTERVAL=10 python realtime_ai_assistant.py
"""

import os
import queue
import sys
import threading
from collections import deque
from datetime import datetime

import anthropic
import numpy as np
import sounddevice as sd
import whisper

SAMPLE_RATE = 16000
CHUNK_DURATION = 5
CHUNK_SIZE = int(SAMPLE_RATE * CHUNK_DURATION)
CONTEXT_WINDOW = 10  # last N transcript chunks sent as context
RESPONSE_INTERVAL = int(os.environ.get("RESPONSE_INTERVAL", 15))
TRANSCRIPT_FILE = os.environ.get("TRANSCRIPT_FILE", "transcript.txt")

audio_queue: queue.Queue = queue.Queue()
transcript_queue: queue.Queue = queue.Queue()
recent_transcripts: deque = deque(maxlen=CONTEXT_WINDOW)
system_instruction = ""


def list_audio_devices():
    print("\n=== Available Audio Devices ===")
    devices = sd.query_devices()
    for idx, d in enumerate(devices):
        print(f"{idx}: {d['name']} (in: {d['max_input_channels']}, out: {d['max_output_channels']})")
    print("=" * 50 + "\n")
    return devices


def audio_callback(indata, frames, time, status):
    if status:
        print(f"Audio status: {status}", file=sys.stderr)
    mono = indata.mean(axis=1) if len(indata.shape) > 1 else indata
    audio_queue.put(mono.copy())


def transcribe_worker(model, stop_event):
    buffer = np.array([], dtype=np.float32)

    with open(TRANSCRIPT_FILE, "w") as f:
        f.write(f"=== Session started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n\n")

    print("\nListening...\n" + "=" * 80)

    while not stop_event.is_set():
        try:
            chunk = audio_queue.get(timeout=0.5)
            buffer = np.concatenate([buffer, chunk.flatten()])

            if len(buffer) >= CHUNK_SIZE:
                audio_chunk = buffer[:CHUNK_SIZE]
                buffer = buffer[CHUNK_SIZE:]

                if np.abs(audio_chunk).mean() < 0.001:
                    continue

                result = model.transcribe(audio_chunk, language="en", fp16=False, verbose=False)
                text = result["text"].strip()

                if text:
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    print(f"[{timestamp}] {text}")
                    with open(TRANSCRIPT_FILE, "a") as f:
                        f.write(f"[{timestamp}] {text}\n")
                    transcript_queue.put(text)
                    recent_transcripts.append(text)
                    sys.stdout.flush()

        except queue.Empty:
            continue
        except Exception as e:
            print(f"Transcription error: {e}", file=sys.stderr)


def claude_worker(stop_event):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("No ANTHROPIC_API_KEY — Claude responses disabled.")
        return

    client = anthropic.Anthropic(api_key=api_key)
    print("Claude assistant ready\n")

    buffer = []
    conversation_history = []
    last_response = datetime.now()

    while not stop_event.is_set():
        try:
            try:
                text = transcript_queue.get(timeout=1)
                buffer.append(text)
            except queue.Empty:
                pass

            elapsed = (datetime.now() - last_response).total_seconds()
            if buffer and elapsed >= RESPONSE_INTERVAL:
                context = " ".join(list(recent_transcripts))
                prompt = (
                    f"{system_instruction}\n\nRecent transcript:\n{context}"
                    if system_instruction
                    else f"Recent transcript:\n{context}\n\nProvide a brief, actionable insight."
                )

                if len(conversation_history) > 10:
                    conversation_history = conversation_history[-6:]
                conversation_history.append({"role": "user", "content": prompt})

                try:
                    message = client.messages.create(
                        model="claude-sonnet-4-6",
                        max_tokens=2048,
                        messages=conversation_history,
                    )
                    response = message.content[0].text
                    conversation_history.append({"role": "assistant", "content": response})

                    timestamp = datetime.now().strftime("%H:%M:%S")
                    print(f"\n{'='*80}\n[{timestamp}] Claude:\n{response}\n{'='*80}\n")

                    with open(TRANSCRIPT_FILE, "a") as f:
                        f.write(f"\n[{timestamp}] CLAUDE: {response}\n\n")

                except Exception as e:
                    print(f"Claude API error: {e}")

                buffer = []
                last_response = datetime.now()

        except Exception as e:
            print(f"Claude worker error: {e}", file=sys.stderr)


def main():
    global system_instruction

    print("=" * 80 + "\nREAL-TIME AI INTERVIEW ASSISTANT\n" + "=" * 80)
    print("\nSet Claude's behavior (Enter for default):")
    print("  Examples: 'Flag weak answers and suggest improvements'")
    print("            'Note missed STAR format moments'")
    print("            'Summarize key points every 15 seconds'\n")
    system_instruction = input("Instruction: ").strip()

    devices = list_audio_devices()
    print("Enter device number for your BlackHole/Aggregate device")
    try:
        device_id = int(input("Device ID: "))
        selected = devices[device_id]
        max_ch = selected["max_input_channels"]
        if max_ch == 0:
            print(f"Error: '{selected['name']}' has no input channels")
            return
        channels = min(max_ch, 2)
        print(f"\nSelected: {selected['name']}\n")
    except (ValueError, IndexError):
        print("Invalid device ID.")
        return

    print("Loading Whisper model...")
    model = whisper.load_model("base")
    print("Model loaded\n")

    stop_event = threading.Event()
    threads = [
        threading.Thread(target=transcribe_worker, args=(model, stop_event), daemon=True),
        threading.Thread(target=claude_worker, args=(stop_event,), daemon=True),
    ]
    for t in threads:
        t.start()

    try:
        with sd.InputStream(
            device=device_id,
            channels=channels,
            samplerate=SAMPLE_RATE,
            callback=audio_callback,
            blocksize=int(SAMPLE_RATE * 0.5),
        ):
            print("LIVE — Press Ctrl+C to stop\n" + "=" * 80 + "\n")
            while True:
                sd.sleep(1000)
    except KeyboardInterrupt:
        print("\nStopping...")
        stop_event.set()
        for t in threads:
            t.join(timeout=2)
        print("Done")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        stop_event.set()


if __name__ == "__main__":
    main()
