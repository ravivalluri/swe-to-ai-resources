# Agents

## mock_interview.py

An interactive mock interview agent that conducts a structured session and gives immediate per-answer feedback.

**Question banks available:**
- `behavioral` — STAR-format situational questions
- `system_design` — distributed systems design problems
- `ml_ai` — RAG, agents, evals, fine-tuning, production LLM questions
- `technical` — CS fundamentals, algorithms, ML theory

**Usage:**
```bash
# Default (4 questions, behavioral + ml_ai)
python agents/mock_interview.py

# Custom session
python agents/mock_interview.py \
  --role "Staff ML Engineer" \
  --categories behavioral ml_ai system_design \
  --questions 6
```

**Session output:**
- Saves full transcript + final assessment to `mock_interview_YYYYMMDD_HHMMSS.txt`
- Run `evals/eval_transcript.py` on the output for a detailed scored report

**During the session:**
- Type your answer, press Enter twice to submit
- Type `skip` to skip a question
- Type `quit` to end early and still get the final summary
