# Full-Stack Architecture Reference

A canonical layered architecture for production web applications. Use this as a mental model for system design interviews and as a checklist when designing new platforms.

---

## Layer Map

| # | Layer | Technologies |
|---|-------|-------------|
| 1 | **Frontend** | React (SPA), Next.js (SSR/SSG), state management |
| 2 | **BFF** | Node.js/Express; GraphQL aggregation layer |
| 3 | **Microservices** | REST or GraphQL APIs per domain |
| 4 | **Data** | PostgreSQL (relational), MongoDB/DynamoDB (document), Redis/Memcached (cache) |
| 5 | **Messaging** | Kafka / RabbitMQ (async, inter-service decoupling) |
| 6 | **Search** | Elasticsearch / OpenSearch |
| 7 | **CDN** | Static assets (JS, CSS, images) at edge |
| 8 | **Security** | OAuth + JWT + HTTPS; WAF; DDoS protection |
| 9 | **DevOps** | CI/CD; Docker + Kubernetes; Prometheus + ELK Stack |
| 10 | **Cloud** | AWS — EC2/Lambda, S3, RDS/DynamoDB |

---

## Key Design Decisions

### BFF Pattern
The Backend-for-Frontend aggregates calls from multiple microservices into the exact shape the UI needs. Prevents the frontend from orchestrating multiple API calls and avoids over-fetching. GraphQL is a natural fit here.

### Data Polyglot
No single database fits all domains:
- **PostgreSQL** — relational/transactional data, complex queries
- **DynamoDB/MongoDB** — document/schemaless, high write throughput
- **Redis** — caching, session storage, pub/sub, rate limiting

### Async via Messaging
Kafka/RabbitMQ decouple producers from consumers — producer doesn't wait for consumers. Improves resilience and throughput for non-critical-path operations (emails, notifications, analytics events, search indexing).

### Security Posture
- **Auth**: OAuth 2.0 for social login; JWT for stateless session management
- **Transport**: HTTPS everywhere
- **Input**: WAF blocks SQLi, XSS, and other OWASP Top 10
- **Sessions**: HttpOnly + Secure cookies prevent client-side access

---

## Serverless Variant

AWS serverless swaps the container/VM layer for managed services:

```
Web / Mobile clients
        ↓
   API Gateway       ← HTTP entry point; handles CORS
        ↓
   AWS Lambda        ← Business logic handlers (Node.js / Python)
   ┌────┼────┐
   ↓    ↓    ↓
DynamoDB  S3  Cognito
(data) (media) (auth)
        ↓
  CloudFront CDN
```

Good on-ramp — stays modular enough to migrate to ECS/EKS when needed. See `interview-prep/concepts/aws-serverless.md` for CDK boilerplate.

---

## Interview Checklist

When given a "design X" question, walk through these layers in order:

1. **Requirements clarification**: scale, consistency, latency, availability targets
2. **High-level design**: which layers exist, rough component diagram
3. **Data model**: schema, access patterns, database choice
4. **API design**: endpoints, request/response, versioning
5. **Scale**: horizontal scaling, caching, CDN, sharding
6. **Reliability**: failover, replication, retries, circuit breakers
7. **Security**: auth, encryption, rate limiting
8. **Observability**: logging, metrics, tracing

## Related

- `phases/phase-2.md` — System Design study schedule
- `phases/phase-4.md` — Cloud Infrastructure (Docker, K8s, Terraform)
- `interview-prep/concepts/aws-serverless.md` — serverless variant with CDK boilerplate
- `interview-prep/concepts/rag.md` — adds an LLM/AI layer on top of this architecture
