# The Living Project

The roadmap is built around a single project that grows in complexity phase by phase — rather than building disconnected toy apps, every phase extends the same codebase with new capabilities.

This approach is described in the roadmap philosophy:
> "Learn through repos you already own. Build one real project that grows each phase."

---

## Phase-by-Phase Capability Map

| Repo | Phase | What gets built |
|------|-------|----------------|
| `job-assistant-cli` | 0 | Core logic rewrite — CS50 Flask + SQLite foundations |
| `job-assistant-api` | 2/3 | REST API layer, system design patterns, auth, async tasks |
| `job-assistant-extension` | 3 | Browser extension — TypeScript/React |
| `job-assistant-mobile` | 3 | Expo + React Native — shared API, native features |
| `job-assistant-web` | 3→4→6 | Next.js dashboard → containerized on K8s → RAG + agent brain |
| `job-assistant-resume` | 5/6 | ML + LLM-powered resume tailoring, ATS scoring, DOCX export |

---

## Target Architecture

AWS serverless stack (detailed in [interview-prep/concepts/aws-serverless.md](interview-prep/concepts/aws-serverless.md)):

```
Web (Vercel/Amplify) + Mobile (Expo EAS)
              ↓
        API Gateway → Lambda
              ↓
   DynamoDB (content) + S3 (media) + Cognito (auth)
              ↓
        CloudFront CDN
```

CI/CD: GitHub Actions → Lambda deploy (AWS SAM) + Vercel auto-deploy + Expo EAS CI

---

## End Goal

A fully deployed, cloud-native, LLM-powered job intelligence platform with:
- RAG over job descriptions and company research
- AI agent brain: reads JD → researches company → tailors resume → drafts cover letter
- ATS scoring, keyword gap analysis
- Native mobile + web dashboard

Built entirely from first principles across 15 months of learning.

---

## Why Build One Project Instead of Many

- **Retention**: concepts stick when applied to something you care about
- **Portfolio**: one polished, deployed platform > ten toy demos
- **Compounding**: Phase 4's K8s cluster runs Phase 6's LLM inference; the work stacks
- **Depth over breadth**: revisiting the same codebase forces you to refactor bad decisions

---

## Related

- [roadmap.md](roadmap.md) — full timeline and phase breakdown
- [phases/](phases/) — week-by-week study guides for each phase
- [interview-prep/concepts/aws-serverless.md](interview-prep/concepts/aws-serverless.md) — the target infra stack
