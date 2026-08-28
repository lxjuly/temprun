# AGENTS.md

## Purpose

`temprun` is a learning project for mastering Temporal and distributed-systems concepts through a small durable multi-agent runtime.

The primary goal is interview preparation. Optimize the codebase for understanding, experimentation, and clear failure semantics—not product polish or framework abstraction.

## Working principles

- Prefer simple, explicit implementations over clever abstractions.
- Keep Temporal primitives visible. Do not hide Workflows, Activities, Signals, Queries, retries, timers, or Child Workflows behind custom framework layers until their behavior is well understood.
- Prefer Python and the official Temporal Python SDK.
- Every nontrivial Temporal feature should include a short comment explaining *why* it exists and what failure mode it handles.
- Workflow code must remain deterministic and replay-safe.
- External I/O, wall-clock access, randomness, network calls, database calls, LLM calls, and other nondeterministic side effects belong in Activities unless a Temporal-safe API is explicitly used.
- Activities may execute more than once. Treat idempotency as a first-class design concern.
- For each important feature, add a failure/recovery experiment or test where practical.
- Favor reasoning about state machines, retries, replay, scheduling, queues, worker failure, and consistency over UI or product features.
- Keep dependencies minimal.
- Do not add FastAPI, persistence layers, or real LLM integrations until they are needed to teach a Temporal concept.

## Initial learning sequence

1. Workflow vs Activity.
2. Parallel Activity fan-out/fan-in.
3. Retry policies and timeouts.
4. Deterministic replay and worker restart.
5. Signals and durable waiting.
6. Queries for workflow state.
7. Child Workflows.
8. Cancellation and Activity heartbeats.
9. Idempotent external side effects.
10. Task queues, worker concurrency, and scheduling limits.
11. Continue-As-New and long workflow histories.
12. Deployment/versioning behavior for long-running Workflows.

## Project shape

The first scenario is a durable research workflow:

```text
request
  -> parallel research agents
  -> collect results
  -> synthesis
  -> optional human approval
  -> finalize
```

Agents may initially be fake Activities. Their purpose is to create realistic orchestration and failure behavior without distracting from Temporal.

## Memory discipline

Read `.memory/README.md` before substantial work.

Update the relevant memory files as work progresses:

- `CONTEXT.md` for stable project context or milestone changes.
- `DECISIONS.md` for architecture decisions and their consequences.
- `LEARNINGS.md` for durable Temporal/distributed-systems lessons.
- `QUESTIONS.md` for unresolved or answered investigation questions.
- `EXPERIMENTS.md` for crash/retry/replay experiments and observed behavior.
- `HANDOFF.md` before ending substantial work so another agent can continue without reconstructing context.

Do not use `.memory` as a raw transcript. Store concise facts, decisions, experiments, and unresolved questions that will remain useful later.

## Definition of done for a learning increment

A learning increment is complete when:

1. the behavior works;
2. the failure semantics are understood;
3. at least one relevant failure/recovery case has been tested or explicitly documented;
4. the corresponding lesson or experiment is captured in `.memory`;
5. `HANDOFF.md` accurately describes the next step.
