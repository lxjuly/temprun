# Decisions

## 2026-08-28 — Use Temporal as the visible execution model

**Context:** The project's purpose is to learn Temporal deeply rather than create a generic agent framework.

**Decision:** Use Temporal Workflows, Activities, Signals, Queries, Child Workflows, task queues, and retry policies directly in application code during early milestones.

**Rationale:** Hiding Temporal behind custom abstractions would make the project less useful for learning its execution and failure semantics.

**Consequences:** Some early code may look more explicit or repetitive than production framework code. Abstraction is deferred until the underlying semantics are understood.

## 2026-08-28 — Use fake agents before real LLM integrations

**Context:** Real LLM calls add cost, latency, provider behavior, prompts, and application concerns that are orthogonal to the initial learning objective.

**Decision:** Represent agents as deterministic-looking fake Activities with controllable delay/failure behavior.

**Rationale:** This isolates Temporal orchestration, retry, scheduling, and recovery behavior.

**Consequences:** Early demos will not perform useful research. A real model can be introduced later as an external side effect implemented as an Activity.

## 2026-08-28 — Treat failure experiments as part of implementation

**Context:** Distributed execution semantics are difficult to learn from happy-path code alone.

**Decision:** Important Temporal features should be paired with tests or explicit experiments involving failure, retry, restart, cancellation, or replay.

**Rationale:** Observing failure behavior builds the intuition needed for distributed-systems interviews.

**Consequences:** A feature is not considered fully learned merely because its happy path works.
