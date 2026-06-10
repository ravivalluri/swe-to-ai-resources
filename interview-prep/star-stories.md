# STAR Story Bank

A template for building and organizing your own interview-ready stories in STAR format (Situation, Task, Action, Result).

---

## STAR Format

```
Situation: Set the scene — context, team size, stakes, constraints
Task:      What was your specific responsibility or goal
Action:    What YOU did (not "we") — specific steps, decisions, tradeoffs
Result:    Quantified outcome — %, time saved, errors reduced, users affected
```

**Rule**: One story per theme. Don't reuse stories for different question types — interviewers compare notes.

---

## Story Categories

### Technical Stories (build these first)

| Theme | Question it answers |
|-------|-------------------|
| Performance optimization | "Tell me about a performance problem you solved." |
| Security / reliability | "Describe a security challenge you tackled." |
| System design decision | "Tell me about an architectural decision you made." |
| Debugging hard problem | "Walk me through the hardest bug you've fixed." |
| Feature shipped end-to-end | "Describe a feature you owned from idea to production." |
| Technical debt / refactor | "Tell me about a time you improved an existing system." |

### Behavioral Stories (have at least one each)

| Theme | Question it answers |
|-------|-------------------|
| Conflict resolution | "Tell me about a time you disagreed with a teammate / manager." |
| Influence without authority | "Tell me about a time you drove change you didn't control." |
| Failure + recovery | "Tell me about a time you failed." |
| Mentoring / peer coaching | "Tell me about a time you helped a struggling teammate." |
| Ambiguity / unclear requirements | "Tell me about a time you had to work with unclear direction." |
| Cross-functional collaboration | "Tell me about a time you worked across teams." |

---

## Story Template

Copy this block for each story:

```markdown
### [Short Title]

**Q: [Interview question this answers]**

- **S**: [1-2 sentences of context]
- **T**: [Your specific responsibility]
- **A**: [3-5 specific actions you took — use "I", not "we"]
- **R**: [Quantified result — numbers preferred]

**Also answers**: [other questions this story works for]
**Keywords**: [performance | security | ownership | mentoring | ...]
```

---

## Tips

- **Quantify everything**: "50% faster", "reduced errors from 12/week to 0", "shipped to 10M users"
- **Say "I", not "we"**: Interviewers are evaluating your individual contribution
- **Keep actions specific**: Not "I improved the code" — "I replaced N+1 queries with a batch query and added a covering index"
- **Prepare 6–8 stories total**: Most questions can be answered by rotating through them
- **Practice with the mock agent**: Run `python agents/mock_interview.py` and use your stories live

---

## Running a Post-Session Eval

After each practice session:

```bash
python evals/eval_transcript.py <session_file>.txt --role "AI Engineer"
```

The eval scores STAR format adherence as one of the five dimensions.
