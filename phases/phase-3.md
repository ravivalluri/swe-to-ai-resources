# Phase 3 — Frontend + Full-Stack

**Dates:** Jul 13 – Sep 6, 2026 (Weeks 21–28)
**Goal:** Build production-grade full-stack apps: Next.js, FastAPI, React Native, and monorepo architecture.

---

## Repo Usage

| Repo | How to use |
|------|-----------|
| your portfolio project | Study TailwindCSS + Radix UI / component library patterns |
| your React Native project | Study Reanimated + animated UI patterns |
| `javascript-algorithms` | Reference for TypeScript patterns |

---

## Week 21 — TypeScript Mastery

| Day | Focus | Task |
|-----|-------|------|
| Mon | TypeScript Basics | Types, interfaces vs types, unions, intersections. Read all existing `.ts` files in a project. |
| Tue | Generics | Write generic utilities. Study TypeScript patterns in existing codebases. |
| Wed | Utility Types | `Partial`, `Required`, `Pick`, `Omit`, `Record`, `ReturnType`. Refactor one file with these. |
| Thu | Type Narrowing | Type guards, discriminated unions, `never`. Find 3 places to improve types. |
| Fri | Advanced Patterns | Mapped types, conditional types, template literals. |
| Sat | Build | Fully type an existing project — no `any` allowed. Add `strict: true` to tsconfig. |

---

## Week 22 — React Patterns

| Day | Focus | Task |
|-----|-------|------|
| Mon | Hooks Deep Dive | `useState`, `useEffect`, `useCallback`, `useMemo` — when each is needed. |
| Tue | Custom Hooks | Extract 3 custom hooks from an existing project. |
| Wed | State Management | Context API vs Zustand vs Redux. Add Zustand to a React Native app. |
| Thu | Performance | `React.memo`, lazy loading, code splitting, virtualized lists. Profile one of your apps. |
| Fri | Compound Components | Build a compound component (e.g., `<Tabs>`) from scratch. |
| Sat | Build | Refactor a project — extract all business logic into custom hooks. |

---

## Week 23 — Next.js App Router

| Day | Focus | Task |
|-----|-------|------|
| Mon | App Router Basics | File-based routing, layouts, loading/error UI. |
| Tue | Server Components | RSC vs Client Components. When to use each. Refactor to maximize server components. |
| Wed | Data Fetching | `fetch` with caching, `revalidatePath`, Server Actions. |
| Thu | Auth | NextAuth.js or Clerk integration. |
| Fri | Build | Scaffold a Next.js 15 App Router project + TypeScript + Tailwind + shadcn/ui. |
| Sat | Build | Add dashboard page: list items, status filters, data tables. |

---

## Week 24 — Next.js Advanced + API

| Day | Focus | Task |
|-----|-------|------|
| Mon | API Routes | Route handlers, middleware, edge runtime. |
| Tue | Streaming + Suspense | Streaming SSR, Suspense boundaries, skeleton loading. |
| Wed | Optimistic Updates | `useOptimistic` hook. Add optimistic UI to a data-mutation flow. |
| Thu | Testing | Vitest + React Testing Library. Write tests for 3 components. |
| Fri | Deployment Prep | Docker multi-stage build for a Next.js app. |
| Sat | Build | Complete an MVP: all core pages working. |

---

## Week 25 — Backend API (FastAPI)

| Day | Focus | Task |
|-----|-------|------|
| Mon | FastAPI Fundamentals | Pydantic models, path params, query params, dependency injection. |
| Tue | Database Integration | SQLAlchemy ORM + Alembic migrations. Design and implement a schema. |
| Wed | Auth in FastAPI | JWT tokens, OAuth2 with Password flow, role-based access control. |
| Thu | Background Tasks | Celery + Redis for async job processing. |
| Fri | API Documentation | OpenAPI/Swagger auto-generation. API versioning strategy. |
| Sat | Build | Complete API v2: full auth, database, async tasks, documented API. |

---

## Week 26 — React Native Polish

| Day | Focus | Task |
|-----|-------|------|
| Mon | Expo SDK Patterns | New architecture, Fabric renderer. Study an existing Expo project's architecture. |
| Tue | Animations | Reanimated 3 worklets, shared values, gesture handling. |
| Wed | Navigation | Expo Router file-based routing, deep linking, tab + stack + modal navigation. |
| Thu | Native Features | Haptics, camera, notifications, secure storage. |
| Fri | Performance | Hermes engine, FlashList, image optimization. Profile your app. |
| Sat | Build | Mirror a web dashboard feature as a native screen. |

---

## Week 27 — Full-Stack Integration

| Day | Focus | Task |
|-----|-------|------|
| Mon | Monorepo Setup | Turborepo or Nx. Structure multiple packages in a monorepo. |
| Tue | Shared Types | Create a `packages/types` package — share TypeScript types across web, mobile, API. |
| Wed | Real-time | Add WebSocket connection: API → web live updates. |
| Thu | File Uploads | S3 presigned URLs. Parse PDF with PyMuPDF. |
| Fri | Email | SendGrid or Resend integration for transactional email. |
| Sat | Build | Full end-to-end test: upload file → extract text → display in web + mobile. |

---

## Week 28 — Testing + Consolidation

| Day | Focus | Task |
|-----|-------|------|
| Mon | Unit Tests | Pytest for API, Vitest for web. Aim for 70% coverage. |
| Tue | Integration Tests | Test API → DB flows end to end. |
| Wed | E2E Tests | Playwright for web. Test the critical user flow. |
| Thu | Accessibility | Add ARIA labels. Run axe-core audit. Fix all critical issues. |
| Fri | Performance Audit | Lighthouse audit. Fix LCP, CLS, FID issues. |
| Sat | Retrospective | Write Phase 3 retrospective. Document all architectural decisions. |

---

## Resources

### Books
- **You Don't Know JS** — Kyle Simpson. Free on GitHub. Read *Scope & Closures* and *this & Object Prototypes*.
- **Learning TypeScript** — Josh Goldberg. Best TypeScript book for intermediate learners.
- **Fluent React** — Tejas Kumar. Advanced React internals.

### Videos
- **Fireship (YouTube)** — Best quick-concept videos.
- **Theo — t3.gg (YouTube)** — Full-stack TypeScript opinions.
- **Jack Herrington (YouTube)** — Advanced React and TypeScript patterns.
- **Vercel YouTube Channel** — Next.js conf talks.

### Blogs & Newsletters
- **Josh W. Comeau's Blog** — Best CSS + React content.
- **[overreacted.io](https://overreacted.io)** — Dan Abramov (React creator).
- **Total TypeScript (Matt Pocock)** — Best TypeScript content.
- **Lee Robinson's Blog** — Next.js best practices.
- **[Bytes.dev](https://bytes.dev) Newsletter** — Weekly JS/TS news.

### Podcasts
- **[Syntax.fm](https://syntax.fm)** — Wes Bos & Scott Tolinski. The frontend podcast.
- **JS Party** — JavaScript ecosystem news.
