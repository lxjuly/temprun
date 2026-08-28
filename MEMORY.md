# temprun Memory

Updated: 2026-08-28

This file is the current-state projection for agents resuming temprun work. Detailed paper trail belongs in `journal/`.

## Current Focus

Extend the first Temporal research workflow with durable human approval via Signal and Query.

## Claims

- [settled] temprun-is-learning-lab: temprun exists primarily to learn Temporal and durable distributed execution, not to become a polished agent framework.
- [settled] temporal-primitives-should-stay-visible: Early code should expose Workflows, Activities, Signals, Queries, retries, task queues, and Child Workflows directly rather than hide them behind custom abstractions.
- [settled] fake-agents-first: Initial agents should be fake Activities so Temporal behavior can be studied without LLM/provider complexity.
- [settled] failure-experiments-are-core: Retry, replay, worker crash, cancellation, idempotency, and durable waiting should be learned through explicit experiments.
- [settled] workflow-activity-boundary-is-central: Workflow code coordinates durable state and must remain replay-safe; external or nondeterministic work belongs in Activities.
- [settled] retry-policy-works-with-fake-agent-failure: A controlled one-time fake agent Activity failure is retried by Temporal according to RetryPolicy without a manual workflow retry loop.

## Commitments

- [done] bootstrap-temporal-project: Created the minimal Python Temporal project and first ResearchWorkflow.
- [done] implement-parallel-agent-fanout: Runs three fake agent Activities in parallel and synthesizes their results.
- [done] add-controlled-retry-experiment: Added controlled Activity failure plus Temporal RetryPolicy and verified retry behavior with tests.
- [active] add-signal-approval: Add durable human approval via Signal and Query after synthesis.
- [proposed] run-worker-crash-experiments: Kill and restart workers at adversarial points and document observed behavior.

## Next Actions

- Add approval state to `ResearchWorkflow`.
- Add a Signal that approves or rejects the synthesized brief.
- Add a Query that exposes workflow status while waiting for approval.
- Test durable waiting with Temporal's testing environment.
- Then run worker-crash experiments against the approval wait state.
