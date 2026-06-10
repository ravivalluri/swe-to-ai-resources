# Evals

Post-session transcript evaluation using Claude.

## eval_transcript.py

Scores a transcript on five dimensions and outputs a structured report.

**Dimensions scored (0-100):**
- Technical Accuracy — correctness and depth of technical answers
- Communication Clarity — structure, conciseness, jargon control
- STAR Format — situation/task/action/result for behavioral questions
- Confidence — assertive framing vs. hedging/filler phrases
- Pacing — whether answers were too brief, too rambling, or well-calibrated

**Usage:**
```bash
# Human-readable report
python evals/eval_transcript.py transcript.txt --role "Senior AI Engineer"

# Raw JSON (pipe into jq, store for tracking over time)
python evals/eval_transcript.py transcript.txt --json | jq .
```

**Track progress over time:**
```bash
python evals/eval_transcript.py session_1.txt --json > scores/session_1.json
python evals/eval_transcript.py session_2.txt --json > scores/session_2.json
# Compare overall_score across sessions to measure improvement
```
