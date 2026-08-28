# temprun Memory

Updated: 2026-08-28

This file is the current-state projection for agents resuming temprun work. Detailed paper trail belongs in `journal/`.

## Current Focus

Bootstrap a minimal Temporal learning project for distributed-systems interview preparation.

## Claims

- [settled] temprun-is-learning-lab: temprun exists primarily to learn Temporal and durable distributed execution, not to become a polished agent framework.
- [settled] temporal-primitives-should-stay-visible: Early code should expose Workflows, Activities, Signals, Queries, retries, task queues, and Child Workflows directly rather than hide them behind custom abstractions.
- [settled] fake-agents-first: Initial agents should be fake Activities so Temporal behavior can be studied without LLM/provider complexity.
- [settled] failure-experiments-are-core: Retry, replay, worker crash, cancellation, idempotency, and durable waiting should be learned through explicit experiments.
- [settled] workflow-activity-boundary-is-central: Workflow code coordinates durable state and must remain replay-safe; external or nondeterministic work belongs in Activities.

## Commitments

- [active] bootstrap-temporal-project: Create the minimal Python Temporal project and first ResearchWorkflow.
- [active] implement-parallel-agent-fanout: Run three fake agent Activities in parallel and synthesize their results.
- [active] add-controlled-retry-experiment: Add controlled Activity failure plus Temporal RetryPolicy and observe retry behavior.
- [proposed] add-signal-approval: Add durable human approval via Signal after milestone 1.
- [proposed] run-worker-crash-experiments: Kill and restart workers at adversarial points and document observed behavior.

## Next Actions

- Bootstrap Python 3.11+ project with official Temporal Python SDK.
- Implement one ResearchWorkflow, three parallel fake research Activities, and one synthesis Activity.
- Keep the implementation intentionally small and explicit.
- Add controlled failure injection and a short RetryPolicy.
- Add tests using Temporal's testing support.
- Record implementation details and experiments in `journal/2026-08-28.md` and durable source records when appropriate.
