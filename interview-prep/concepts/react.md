# React Fundamentals

Core React knowledge for frontend development and interviews. Covers the component model, state and lifecycle, hooks, performance, ecosystem libraries, and testing.

---

## Core Concepts

| Concept | Summary |
|---------|---------|
| **Components** | Reusable UI units. Functional (JS functions returning JSX) preferred over class components. |
| **Virtual DOM** | Lightweight DOM copy. React diffs old vs new, updates only changed parts — efficient re-renders. |
| **Props** | Read-only data passed parent → child. |
| **Keys** | Stable identity for list items; helps React track additions, removals, and reorders. |
| **State** | `useState` (functional) or `setState` (class) — triggers re-render on change. |

## Hooks

| Hook | Purpose |
|------|---------|
| `useState` | Local component state |
| `useEffect` | Side effects (data fetch, subscriptions, DOM mutations) |
| `useContext` | Consume context without prop drilling |
| `useMemo` / `useCallback` | Memoize values / functions to skip unnecessary work |
| `useRef` | Mutable ref that doesn't trigger re-renders; also DOM access |
| `useReducer` | Complex state logic; alternative to `useState` |

## Advanced Patterns

- **Context API**: global-ish data (theme, auth, locale) without Redux overhead; avoids prop drilling
- **Controlled components**: form state lives in React (`value` + `onChange`); uncontrolled = DOM manages state via `ref`
- **Error boundaries**: class components wrapping subtrees; catch JS errors and render fallback UI
- **Code splitting**: `React.lazy` + `Suspense` defers loading non-critical bundles; reduces initial payload
- **Compound components**: components that share implicit state (e.g., `<Tabs>` + `<Tab>` + `<Panel>`)
- **Render props / HOC**: patterns for logic reuse (largely superseded by hooks)

## Ecosystem

| Library | Role |
|---------|------|
| **Redux / Zustand** | Global state — Redux for complex interactions, Zustand for simpler cases |
| **React Router** | Client-side navigation without full-page refresh |
| **Next.js** | SSR + SSG + App Router; vs Vite/CRA which are pure CSR |
| **TanStack Query** | Server state, caching, background refresh |
| **React Hook Form** | Performant forms with minimal re-renders |

## Performance Optimizations

- `React.memo` — skip re-renders when props haven't changed
- `useMemo` / `useCallback` — avoid recreating expensive values/functions on every render
- Code splitting + lazy loading — reduce initial JS bundle
- Virtualization (react-window, FlashList) — render only visible list items
- React DevTools Profiler — identify slow components

## Testing

- **Vitest / Jest**: unit tests, mocking, assertions
- **React Testing Library**: test from the user's perspective — query by role, label, text (not implementation details)
- **Playwright / Cypress**: E2E tests for critical user flows

## Interview Questions

| Question | Key points |
|----------|-----------|
| What is the virtual DOM? | Lightweight copy; diffing algorithm; batched updates |
| `useState` vs `useReducer`? | `useReducer` for complex state transitions; `useState` for simple values |
| When would you use `useCallback`? | Prevent child re-renders when passing functions as props; dependency arrays |
| Context vs Redux? | Context for low-frequency updates (theme, auth); Redux/Zustand for high-frequency app state |
| How does React reconciliation work? | Fiber architecture; tree diffing; keys help identify moved elements |
| Controlled vs uncontrolled? | Controlled = React owns state; uncontrolled = DOM owns state via ref |

## Related

- See `phases/phase-3.md` for the full React + Next.js study schedule
- See `interview-prep/agents/mock_interview.py` to practice these questions live
