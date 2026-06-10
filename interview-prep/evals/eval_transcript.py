#!/usr/bin/env python3
"""
Evaluate an interview transcript using Claude.
Scores five dimensions and outputs an actionable report.

Usage:
    python evals/eval_transcript.py transcript.txt
    python evals/eval_transcript.py transcript.txt --role "Senior AI Engineer"
    python evals/eval_transcript.py transcript.txt --json
"""

import argparse
import json
import os
import sys

import anthropic

EVAL_SYSTEM = """You are an expert technical interviewer and communication coach.
Evaluate the interview transcript and return a JSON object with this exact structure:
{
  "overall_score": <0-100>,
  "dimensions": {
    "technical_accuracy": {"score": <0-100>, "feedback": "<string>", "examples": ["<string>"]},
    "communication_clarity": {"score": <0-100>, "feedback": "<string>", "examples": ["<string>"]},
    "star_format": {"score": <0-100>, "feedback": "<string>", "examples": ["<string>"]},
    "confidence": {"score": <0-100>, "feedback": "<string>"},
    "pacing": {"score": <0-100>, "feedback": "<string>"}
  },
  "strengths": ["<string>"],
  "improvements": ["<string>"],
  "recommended_practice": ["<string>"]
}

Be specific — reference actual moments from the transcript. Return only valid JSON, no prose outside it."""


def evaluate(transcript_path: str, role: str = "") -> dict:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not set")
        sys.exit(1)

    with open(transcript_path) as f:
        transcript = f.read()

    client = anthropic.Anthropic(api_key=api_key)
    role_line = f"Role: {role}\n\n" if role else ""
    prompt = f"{role_line}Transcript:\n\n{transcript}"

    print("Evaluating with Claude...")
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=EVAL_SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = message.content[0].text.strip()
    if raw.startswith("```"):
        parts = raw.split("```")
        raw = parts[1].lstrip("json").strip() if len(parts) > 1 else raw

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"raw_feedback": raw}


def print_report(result: dict):
    if "raw_feedback" in result:
        print(result["raw_feedback"])
        return

    print("\n" + "=" * 60)
    print("INTERVIEW EVALUATION REPORT")
    print("=" * 60)
    print(f"\nOverall Score: {result.get('overall_score', 'N/A')}/100\n")

    for key, dim in result.get("dimensions", {}).items():
        label = key.replace("_", " ").title()
        print(f"{label}: {dim.get('score', 'N/A')}/100")
        print(f"  {dim.get('feedback', '')}")
        for ex in dim.get("examples", []):
            print(f"  • {ex}")
        print()

    for heading, field in [("Strengths", "strengths"), ("Areas to Improve", "improvements"), ("Recommended Practice", "recommended_practice")]:
        items = result.get(field, [])
        if items:
            symbols = {" Strengths": "+", "Areas to Improve": "-", "Recommended Practice": "→"}
            sym = symbols.get(heading, "•")
            print(f"{heading}:")
            for item in items:
                print(f"  {sym} {item}")
            print()

    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Evaluate an interview transcript")
    parser.add_argument("transcript", help="Path to transcript file")
    parser.add_argument("--role", default="", help="Role being interviewed for")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output raw JSON")
    args = parser.parse_args()

    if not os.path.exists(args.transcript):
        print(f"Error: '{args.transcript}' not found")
        sys.exit(1)

    result = evaluate(args.transcript, role=args.role)
    if args.as_json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)


if __name__ == "__main__":
    main()
