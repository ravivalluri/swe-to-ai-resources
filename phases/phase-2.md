# Phase 2 — System Design + Networking

**Dates:** May 18 – Jul 12, 2026 (Weeks 13–20)
**Goal:** Build the architectural thinking and networking depth that separates senior engineers from juniors.

> Build the architectural thinking and networking depth that separates senior engineers from juniors.

---

## Repo Usage

| Repo | How to use |
|------|-----------|
| `system-design-primer` | Core reading — work through every section |
| `low-level-design-primer` | OOP design problems, one per week |
| `awesome-system-design-resources` | Supplementary reference |
| a microservices repo | Study existing architecture, document bottlenecks |

---

## Week 13 — Networking Fundamentals

| Day | Focus | Task |
|-----|-------|------|
| Mon | OSI Model | Study all 7 layers. Draw the model from memory. Understand what happens when you type a URL. |
| Tue | TCP/IP | Study TCP 3-way handshake, congestion control, flow control. Read `system-design-primer` networking section. |
| Wed | DNS + HTTP | Study DNS resolution chain. HTTP/1.1 vs HTTP/2 vs HTTP/3. HTTPS and TLS handshake. |
| Thu | WebSockets + gRPC | Study when to use WebSockets vs REST vs gRPC. |
| Fri | Build | Write a raw TCP echo server in Python (no frameworks). Then an HTTP server that parses GET requests. |
| Sat | Build | Add WebSocket support to an API project. Push updates to client in real-time. |

---

## Week 14 — Databases Deep Dive

| Day | Focus | Task |
|-----|-------|------|
| Mon | SQL Deep Dive | Indexes, query plans, EXPLAIN ANALYZE. Study `system-design-primer` — Database section. |
| Tue | SQL vs NoSQL | When to use each. Study CAP theorem. Study `system-design-primer` — NoSQL section. |
| Wed | Replication | Master-slave, master-master, read replicas. Study consistency models. |
| Thu | Sharding | Horizontal vs vertical, consistent hashing, hot spots. |
| Fri | Transactions | ACID, isolation levels (dirty read, phantom read). Optimistic vs pessimistic locking. |
| Sat | Build | Design a database schema for your project. Justify every table, index, and relationship choice. |

---

## Week 15 — Caching + Message Queues

| Day | Focus | Task |
|-----|-------|------|
| Mon | Caching | Cache-aside, read-through, write-through, write-back. Eviction policies (LRU, LFU). Study Redis. |
| Tue | CDN | How CDNs work. Push vs pull. When to use. |
| Wed | Message Queues | Kafka vs RabbitMQ. Pub/Sub pattern. At-least-once vs exactly-once delivery. |
| Thu | Rate Limiting | Token bucket, leaky bucket, fixed window, sliding window algorithms. Implement one. |
| Fri | Build | Add Redis caching to an API. Cache frequently-read data. Implement rate limiter middleware. |
| Sat | Build | Add async job processing using a queue (Redis + Bull or Celery). |

---

## Week 16 — Distributed Systems

| Day | Focus | Task |
|-----|-------|------|
| Mon | Load Balancing | L4 vs L7. Round robin, least connections, consistent hashing. Health checks. |
| Tue | Microservices vs Monolith | Trade-offs. Service discovery. Study a microservices architecture. |
| Wed | Consistency Patterns | Strong, eventual, weak. Read `system-design-primer` — Consistency patterns. |
| Thu | Availability Patterns | Failover, replication, active-active vs active-passive. |
| Fri | Classic Design Problems | Design URL Shortener. Design Key-Value Store. Use `system-design-primer` solutions. |
| Sat | Build | Write a system design doc for a microservices project. Identify 3 bottlenecks and propose fixes. |

---

## Week 17 — Low-Level Design + OOP

| Day | Focus | Task |
|-----|-------|------|
| Mon | SOLID Principles | Study each principle. Find violations in your own code. Fix them. |
| Tue | Creational Patterns | Factory, Abstract Factory, Builder, Singleton. Study `low-level-design-primer`. |
| Wed | Structural Patterns | Adapter, Decorator, Facade, Proxy. Implement one in Python. |
| Thu | Behavioral Patterns | Observer, Strategy, Command, Iterator. Implement Observer for an event system. |
| Fri | LLD Problem | Design a Parking Lot system (full OOP). Use `low-level-design-primer` as reference. |
| Sat | LLD Problem | Design a URL Shortener (full OOP + API layer). |

---

## Week 18 — Classic System Design Problems

| Day | Focus | Task |
|-----|-------|------|
| Mon | Design Twitter/X | Newsfeed generation. Fan-out on write vs read. Study `system-design-primer`. |
| Tue | Design WhatsApp | Real-time messaging. WebSockets, message queues, offline storage. |
| Wed | Design Netflix | CDN, video encoding, recommendation system high-level. |
| Thu | Design Uber | Geospatial indexing, matching algorithm, surge pricing architecture. |
| Fri | Mock System Design | Pick any problem. Whiteboard it for 45 minutes end-to-end. Record yourself. |
| Sat | Build | Apply one system design pattern to an existing project. |

---

## Week 19 — Security Fundamentals

| Day | Focus | Task |
|-----|-------|------|
| Mon | Auth Patterns | Session vs JWT vs OAuth2 vs OIDC. Refresh token rotation. |
| Tue | OWASP Top 10 | Study each vulnerability. Find examples in your existing code. |
| Wed | Encryption | TLS, AES, RSA, bcrypt/argon2. When to use each. |
| Thu | API Security | Rate limiting, input validation, CORS, CSRF protection. |
| Fri | Build | Audit a project for OWASP Top 10. Fix at least 3 issues. |
| Sat | Study | Read `system-design-primer` — Security section. |

---

## Week 20 — Consolidation

| Day | Focus | Task |
|-----|-------|------|
| Mon | Review | Re-read your Phase 2 notes. Fill gaps in `coding-interview-university` system design checklist. |
| Tue | Mock Interview | Full 45-min system design mock. Whiteboard a complete design. |
| Wed | Architecture Doc | Write a full architecture doc for a project. Include diagrams (draw.io or Excalidraw). |
| Thu | LLD Polish | Design a domain model with full UML. |
| Fri | Retrospective | Write Phase 2 retrospective. List top 5 things learned. |
| Sat | Next Phase Prep | Set up TypeScript environment. Read Next.js docs overview. |

---

## Architecture Deep Dives (Must-Read Articles)

From Neo Kim's [System Design Newsletter](https://newsletter.systemdesign.one) and others:

- Airbnb's move from monolith to microservices
- WhatsApp system design
- Spotify system design
- How Reddit works
- How Bluesky works
- How Google Docs works
- Kafka mechanics
- Tinder architecture
- Slack architecture
- S3 architecture
- URL shortening system design
- Serverless architecture
- Vitess MySQL
- AWS at scale
- Stock exchange system design
- How Uber finds nearby drivers
- How OpenAI scaled to 800M users with Postgres

---

## Resources

### Books
- **Designing Data-Intensive Applications** — Kleppmann. **The most important book in this roadmap.**
- **System Design Interview Vol. 1 & 2** — Alex Xu.
- **Computer Networks: A Top-Down Approach** — Kurose & Ross (Ch 1–4).
- **Clean Architecture** — Robert C. Martin.

### Videos
- **ByteByteGo (YouTube)** — Best system design animations.
- **Gaurav Sen (YouTube)** — Deep technical system design.
- **Hussein Nasser (YouTube)** — Best channel for networking + backend engineering.
- **NetworkChuck (YouTube)** — Fun networking fundamentals.

### Newsletters
- **[ByteByteGo Newsletter](https://blog.bytebytego.com)** — System design breakdowns with diagrams.
- **[Neo Kim — System Design Newsletter](https://newsletter.systemdesign.one)** — Real-world architecture deep dives.
- **The Pragmatic Engineer** — How big tech systems work.
- **[High Scalability](http://highscalability.com)** — Real architecture blog posts.
- **Martin Fowler's Blog** — Architecture patterns, microservices, refactoring.
- **[Netflix Tech Blog](https://netflixtechblog.com)** — How Netflix actually builds things.
- **Haki Benita** — Deep PostgreSQL internals.

### Practice
- **[Codemia](https://codemia.io)** — System design problem practice.
- **[draw.io](https://draw.io)** / **[Excalidraw](https://excalidraw.com)** — Architecture diagrams.
