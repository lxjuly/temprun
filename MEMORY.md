# temprun Memory

Updated: 2026-08-29

This file is the current-state projection for agents resuming temprun work. Detailed paper trail belongs in `journal/`.

## Current Focus

Add a local API bridge behind the Tailscale-served demo so the UI can start and query real Temporal workflows.

## Claims

- [settled] temprun-is-learning-lab: temprun exists primarily to learn Temporal and durable distributed execution, not to become a polished agent framework.
- [settled] temporal-primitives-should-stay-visible: Early code should expose Workflows, Activities, Signals, Queries, retries, task queues, and Child Workflows directly rather than hide them behind custom abstractions.
- [settled] fake-agents-first: Initial agents should be fake Activities so Temporal behavior can be studied without LLM/provider complexity.
- [settled] failure-experiments-are-core: Retry, replay, worker crash, cancellation, idempotency, and durable waiting should be learned through explicit experiments.
- [settled] workflow-activity-boundary-is-central: Workflow code coordinates durable state and must remain replay-safe; external or nondeterministic work belongs in Activities.
- [settled] retry-policy-works-with-fake-agent-failure: Controlled fake agent Activity failures are retried by Temporal according to RetryPolicy without a manual workflow retry loop.
- [settled] demo-ui-should-teach-workflow-shape: The first demo UI should visualize the Temporal research workflow, parallel fan-out, and retry paths without adding backend framework dependencies.
- [settled] research-workflow-has-six-fake-agents: The current fake plan fans out to `web`, `papers`, `systems`, `implementation`, `security`, and `critic` agents.
- [settled] failure-injection-is-per-agent-attempt-count: `ResearchRequest.fail_agent_attempts` can make multiple agents fail for configurable attempt counts before succeeding.
- [settled] demo-fanout-must-be-visually-obvious: During the simulated fan-out phase, the UI highlights the split/merge lanes, labels the run status as `6 parallel`, and animates each active agent card.
- [settled] github-pages-docs-source-is-demo-target: The static demo should live in `docs/` so GitHub Pages can publish it from `main` without a build step.
- [settled] tailscale-serve-is-demo-access-layer: The working demo should be reachable through Tailscale Serve while Temporal server and worker remain local to the machine.
- [settled] local-api-bridge-is-next-runtime-boundary: The browser UI should talk to a local HTTP API bridge, and that bridge should use the Temporal Python client.

## Commitments

- [done] bootstrap-temporal-project: Created the minimal Python Temporal project and first ResearchWorkflow.
- [done] implement-parallel-agent-fanout: Runs six fake agent Activities in parallel and synthesizes their results.
- [done] add-controlled-retry-experiment: Added controlled Activity failures plus Temporal RetryPolicy and verified retry behavior with tests.
- [done] add-static-demo-ui: Added a dependency-free static demo that simulates request, planning, parallel agents, retries, synthesis, and final brief states.
- [done] make-parallel-work-visible: Added highlighted fan-out lanes and per-agent progress animation so simultaneous Activity execution is visible in the demo.
- [done] prepare-github-pages-demo: Moved the static demo to `docs/` and documented the `main` / `docs` Pages source.
- [done] expose-static-demo-with-tailscale-serve: Exposed the static demo on the tailnet at `https://xiangs-mac-studio.tail1aa4f.ts.net/`.
- [active] add-signal-approval: Add durable human approval via Signal and Query after synthesis.
- [active] add-local-api-bridge: Serve API routes beside the UI so remote tailnet clients can start and inspect local Temporal workflows.
- [proposed] run-worker-crash-experiments: Kill and restart workers at adversarial points and document observed behavior.

## Next Actions

- Replace the static Python file server with a small `temprun.local_api` HTTP server.
- Serve `docs/` at `/` and expose health at `/api/health`.
- Add `/api/research` to start `ResearchWorkflow` through the local Temporal Python client.
- Keep Tailscale Serve pointing at the localhost API/UI server.
- Add approval state to `ResearchWorkflow`.
- Add a Signal that approves or rejects the synthesized brief.
- Add a Query that exposes workflow status while waiting for approval.
- Test durable waiting with Temporal's testing environment.
- Then run worker-crash experiments against the approval wait state.
