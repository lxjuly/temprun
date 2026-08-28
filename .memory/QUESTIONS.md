# Questions

## OPEN — What exactly is persisted for a Workflow?

Trace a Workflow through execution and replay. Distinguish persisted event history from in-memory worker state and derived Workflow state.

## OPEN — What are Temporal's effective delivery guarantees for Activities?

Understand why Activity execution is commonly reasoned about as at-least-once under retry/failure and what this means for idempotency.

## OPEN — What happens at each worker crash point?

Compare crashes:

- before an Activity starts;
- while an Activity is running;
- after an external side effect but before Activity completion is recorded;
- after Activity completion;
- while a Workflow is durably waiting.

## OPEN — How does Temporal detect and recover long-running Activity failure?

Investigate Activity timeouts and heartbeats and understand the distinction between them.

## OPEN — How should agent fan-out map to Activities vs Child Workflows?

Start with Activities, then convert one agent to a Child Workflow and compare lifecycle, isolation, history, retry, cancellation, and operational semantics.

## OPEN — How should concurrency limits be enforced?

Explore worker concurrency, task queues, and application-level constraints. Later consider per-tenant limits and fairness.

## OPEN — What makes Workflow code replay-safe across deployments?

Investigate deterministic changes, Worker Versioning/versioning APIs, and behavior of long-running Workflows when code changes.

## OPEN — When is Continue-As-New required?

Create enough workflow activity to understand history growth and why long-lived workflows may need Continue-As-New.
