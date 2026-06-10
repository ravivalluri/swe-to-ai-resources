#!/usr/bin/env python3
"""
Watch a transcript file and display new lines as they arrive.
Press Ctrl+C to stop and print the full transcript (ready to paste into Claude).

Usage:
    python watch_transcript.py
    TRANSCRIPT_FILE=my_session.txt python watch_transcript.py
"""

import os
import sys
import time

TRANSCRIPT_FILE = os.environ.get("TRANSCRIPT_FILE", "transcript.txt")
CHECK_INTERVAL = 5  # seconds


def watch():
    print(f"Watching: {TRANSCRIPT_FILE}\nPress Ctrl+C to print full transcript.\n" + "=" * 80 + "\n")

    last_position = 0
    if os.path.exists(TRANSCRIPT_FILE):
        with open(TRANSCRIPT_FILE) as f:
            last_position = f.seek(0, 2)

    full_lines = []

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
                for line in lines:
                    print(line)
                    full_lines.append(line)

            time.sleep(CHECK_INTERVAL)

        except KeyboardInterrupt:
            print("\n\n" + "=" * 80)
            print("FULL TRANSCRIPT — paste into Claude for analysis")
            print("=" * 80 + "\n")
            print("\n".join(full_lines))
            print("\n" + "=" * 80)
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    watch()
