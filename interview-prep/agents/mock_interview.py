#!/usr/bin/env python3
"""
Mock interview agent. Conducts a structured practice interview with real-time feedback.
Saves the full transcript + final assessment for use with eval_transcript.py.

Usage:
    python agents/mock_interview.py
    python agents/mock_interview.py --role "Staff ML Engineer" --categories behavioral ml_ai --questions 5
"""

import argparse
import os
import sys
from datetime import datetime

import anthropic

QUESTION_BANKS: dict[str, list[str]] = {
    "behavioral": [
        "Tell me about a time you had to deal with a difficult stakeholder.",
        "Describe a project where you had to learn a new technology quickly.",
        "Tell me about a time you failed and what you learned from it.",
        "Describe a situation where you had to influence without authority.",
        "Tell me about the most impactful project you've shipped.",
    ],
    "system_design": [
        "Design a real-time chat system that scales to 10M concurrent users.",
        "How would you design a URL shortener?",
        "Design a distributed job queue with at-least-once delivery guarantees.",
        "How would you build a recommendation engine for a streaming platform?",
        "Design an API rate limiter that works across a distributed fleet.",
    ],
    "ml_ai": [
        "How would you design a RAG pipeline for a customer support system?",
        "Walk me through how you'd evaluate an LLM-based feature in production.",
        "How would you handle hallucinations in a production LLM application?",
        "Design an agentic system for automating code review.",
        "When would you choose fine-tuning over prompt engineering, and vice versa?",
    ],
    "technical": [
        "Explain the difference between concurrency and parallelism.",
        "How does a hash table work, and what are common collision resolution strategies?",
        "What is the CAP theorem and how does it shape distributed system design?",
        "Explain how the transformer architecture works at a high level.",
        "What's the difference between supervised, unsupervised, and reinforcement learning?",
    ],
}

INTERVIEWER_SYSTEM = """You are a senior technical interviewer at a top AI company.

Your role during each question:
1. After the candidate answers, give specific feedback in 2-3 sentences — what landed, what was missing.
2. If the answer is incomplete, ask one natural follow-up question.
3. Otherwise end with "Good, let's move on."

At the final summary:
- Score each dimension 0-100: Technical Depth, Communication, Problem Solving, STAR Format (behavioral), Overall.
- List the top 3 concrete improvements with example phrasing.

Be direct but encouraging. Reference specific parts of their answers."""


def collect_answer() -> str:
    print("(Press Enter twice when done, or type 'skip' / 'quit')\n")
    lines = []
    while True:
        line = input()
        if line.lower() in ("skip", "quit"):
            return line.lower()
        if line == "" and lines and lines[-1] == "":
            break
        lines.append(line)
    return "\n".join(lines).strip()


def run_interview(role: str, categories: list[str], num_questions: int):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not set")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # Build question list
    questions: list[tuple[str, str]] = []
    per_cat = max(1, num_questions // len(categories))
    for cat in categories:
        for q in QUESTION_BANKS.get(cat, [])[:per_cat]:
            questions.append((cat, q))
    questions = questions[:num_questions]

    print("\n" + "=" * 60)
    print(f"MOCK INTERVIEW — {role.upper()}")
    print(f"Questions: {len(questions)} | Categories: {', '.join(categories)}")
    print("=" * 60 + "\n")

    transcript_lines = [
        f"Mock Interview — {role}",
        f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"Categories: {', '.join(categories)}",
        "",
    ]
    conversation_history: list[dict] = []

    for i, (cat, question) in enumerate(questions, 1):
        print(f"\n[Q{i}/{len(questions)}] [{cat.upper()}]\n{question}\n")
        transcript_lines.append(f"\nQ{i} [{cat}]: {question}")

        answer = collect_answer()

        if answer == "quit":
            print("\nEnding interview early.")
            break
        if answer == "skip":
            transcript_lines.append("A: [skipped]")
            continue

        transcript_lines.append(f"A: {answer}")

        prompt = (
            f"Role: {role}\n"
            f"Question {i} [{cat}]: {question}\n"
            f"Candidate's answer: {answer}\n\n"
            "Give feedback and a follow-up if needed."
        )
        conversation_history.append({"role": "user", "content": prompt})

        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=512,
            system=INTERVIEWER_SYSTEM,
            messages=conversation_history,
        )

        feedback = message.content[0].text
        conversation_history.append({"role": "assistant", "content": feedback})

        print(f"\nInterviewer: {feedback}\n" + "-" * 60)
        transcript_lines.append(f"Feedback: {feedback}")

    # Final assessment
    print("\n" + "=" * 60 + "\nGenerating final assessment...\n" + "=" * 60)

    full_transcript = "\n".join(transcript_lines)
    conversation_history.append({
        "role": "user",
        "content": f"Full transcript:\n\n{full_transcript}\n\nProvide the final assessment with scores and top 3 improvements.",
    })

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=INTERVIEWER_SYSTEM,
        messages=conversation_history,
    )

    summary = message.content[0].text
    print(f"\n{summary}\n")

    # Save
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = f"mock_interview_{ts}.txt"
    with open(out_path, "w") as f:
        f.write(full_transcript)
        f.write(f"\n\n=== FINAL ASSESSMENT ===\n{summary}")

    print(f"Transcript saved to: {out_path}")
    print(f"Run a detailed eval with: python evals/eval_transcript.py {out_path} --role \"{role}\"\n")


def main():
    parser = argparse.ArgumentParser(description="Mock interview agent")
    parser.add_argument("--role", default="AI/ML Engineer", help="Role you are interviewing for")
    parser.add_argument(
        "--categories",
        nargs="+",
        choices=list(QUESTION_BANKS.keys()),
        default=["behavioral", "ml_ai"],
        help="Question categories",
    )
    parser.add_argument("--questions", type=int, default=4, help="Number of questions")
    args = parser.parse_args()

    run_interview(args.role, args.categories, args.questions)


if __name__ == "__main__":
    main()
