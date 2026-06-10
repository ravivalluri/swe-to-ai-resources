#!/usr/bin/env python3
"""
Real-time audio transcription using Whisper.
Captures audio from a BlackHole/aggregate device and writes timestamped lines to a transcript file.

Usage:
    python realtime_transcription.py
    TRANSCRIPT_FILE=my_session.txt python realtime_transcription.py
"""

import os
import queue
import sys
import threading
from datetime import datetime

import numpy as np
import sounddevice as sd
import whisper

SAMPLE_RATE = 16000
CHUNK_DURATION = 5  # seconds per transcription chunk
CHUNK_SIZE = int(SAMPLE_RATE * CHUNK_DURATION)
TRANSCRIPT_FILE = os.environ.get("TRANSCRIPT_FILE", "transcript.txt")

audio_queue: queue.Queue = queue.Queue()


def list_audio_devices():
    print("\n=== Available Audio Devices ===")
    devices = sd.query_devices()
    for idx, device in enumerate(devices):
        print(f"{idx}: {device['name']} (in: {device['max_input_channels']}, out: {device['max_output_channels']})")
    print("=" * 50 + "\n")
    return devices


def audio_callback(indata, frames, time, status):
    if status:
        print(f"Audio status: {status}", file=sys.stderr)
    mono = indata.mean(axis=1) if len(indata.shape) > 1 else indata
    audio_queue.put(mono.copy())


def transcribe_worker(model, stop_event):
    buffer = np.array([], dtype=np.float32)
    chunk_count = 0

    with open(TRANSCRIPT_FILE, "w") as f:
        f.write(f"=== Transcription started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n\n")

    print(f"\nListening and transcribing...\nSaving to: {TRANSCRIPT_FILE}\n" + "=" * 80)

    while not stop_event.is_set():
        try:
            chunk = audio_queue.get(timeout=0.5)
            buffer = np.concatenate([buffer, chunk.flatten()])

            if len(buffer) >= CHUNK_SIZE:
                chunk_count += 1
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
                    sys.stdout.flush()

        except queue.Empty:
            continue
        except Exception as e:
            print(f"Transcription error: {e}", file=sys.stderr)


def main():
    print("Real-time Audio Transcription with Whisper\n" + "=" * 80)

    devices = list_audio_devices()
    print("Enter the device number for your BlackHole/Aggregate device")
    try:
        device_id = int(input("Device ID: "))
        selected = devices[device_id]
        max_ch = selected["max_input_channels"]
        if max_ch == 0:
            print(f"Error: '{selected['name']}' has no input channels")
            return
        channels = min(max_ch, 2)
        print(f"\nSelected: {selected['name']} ({channels} channels)\n")
    except (ValueError, IndexError):
        print("Invalid device ID.")
        return

    print("Loading Whisper 'base' model...")
    model = whisper.load_model("base")
    print("Model loaded\n")

    stop_event = threading.Event()
    t = threading.Thread(target=transcribe_worker, args=(model, stop_event), daemon=True)
    t.start()

    try:
        with sd.InputStream(
            device=device_id,
            channels=channels,
            samplerate=SAMPLE_RATE,
            callback=audio_callback,
            blocksize=int(SAMPLE_RATE * 0.5),
        ):
            print("LIVE — Press Ctrl+C to stop\n")
            while True:
                sd.sleep(1000)
    except KeyboardInterrupt:
        print("\nStopping...")
        stop_event.set()
        t.join(timeout=2)
        print("Done")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        stop_event.set()


if __name__ == "__main__":
    main()
