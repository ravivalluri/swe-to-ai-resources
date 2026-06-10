#!/usr/bin/env python3
"""
Monitor a transcript file and send new content to Claude in real-time.
Run alongside realtime_transcription.py in a separate terminal.

Usage:
    python transcript_to_claude.py
    TRANSCRIPT_FILE=my_session.txt python transcript_to_claude.py
"""

import os
import sys
import time

import anthropic

TRANSCRIPT_FILE = os.environ.get("TRANSCRIPT_FILE", "transcript.txt")
CHECK_INTERVAL = 2  # seconds


def monitor_transcript():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not set\nRun: export ANTHROPIC_API_KEY='your-key'")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    print(f"Monitoring: {TRANSCRIPT_FILE}\nChecking every {CHECK_INTERVAL}s\n" + "=" * 80)
    print("\nTip: start realtime_transcription.py in another terminal first.\n")

    last_position = 0
    if os.path.exists(TRANSCRIPT_FILE):
        with open(TRANSCRIPT_FILE) as f:
            last_position = f.seek(0, 2)

    conversation_history = []

    while True:
        try:
            if not os.path.exists(TRANSCRIPT_FILE):
                time.sleep(CHECK_INTERVAL)
                continue

            with open(TRANSCRIPT_FILE) as f:
                f.seek(last_position)
                new_content = f.read()
                last_position = f.tell()

            if new_content.strip():
                lines = [l for l in new_content.strip().splitlines() if l and not l.startswith("===")]
                if lines:
                    chunk = "\n".join(lines)
                    print(f"\nNew transcript:\n{chunk}\n")

                    prompt = (
                        f"New interview transcript chunk:\n\n{chunk}\n\n"
                        "Identify any weak answers, missed points, or follow-up opportunities. "
                        "Be brief and actionable."
                    )
                    conversation_history.append({"role": "user", "content": prompt})

                    message = client.messages.create(
                        model="claude-sonnet-4-6",
                        max_tokens=1024,
                        messages=conversation_history,
                    )

                    response = message.content[0].text
                    conversation_history.append({"role": "assistant", "content": response})

                    print(f"Claude: {response}\n" + "=" * 80)

            time.sleep(CHECK_INTERVAL)

        except KeyboardInterrupt:
            print("\nStopping monitor.")
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    monitor_transcript()
