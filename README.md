# temprun

A durable multi-agent execution runtime built on Temporal.

The project exists primarily as a hands-on learning environment for Temporal and distributed-systems interview preparation. The goal is not to build a polished agent framework; it is to understand durable execution, retries, idempotency, replay, signals, cancellation, child workflows, worker failure, and scheduling by exercising them in a small agent-oriented system.

## First milestone

Build a research workflow that fans out to several agent activities, synthesizes their results, waits for approval, and can survive worker crashes without losing progress.

Current implementation:

```text
ResearchWorkflow
  -> plan_research Activity
  -> three parallel run_fake_agent Activities
  -> synthesize_research Activity
  -> ResearchBrief
```

The fake agent Activities are intentionally simple. They make Temporal's retry, timeout, deterministic replay, and Activity boundary behavior visible before any real LLM or network integration is added.

## Learning path

1. Run one Workflow and one Activity.
2. Fan out agent Activities in parallel.
3. Add retries, timeouts, and explicit failure injection.
4. Add a Signal for approval and a Query for status.
5. Convert one agent into a Child Workflow.
6. Add cancellation and heartbeat handling.
7. Kill workers at adversarial points and inspect replay/recovery.
8. Add idempotent external side effects and reason about at-least-once Activity execution.
9. Explore task queues, worker concurrency, and per-tenant execution limits.

## Local development

Requires Python 3.11+ and a local Temporal server.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
temporal server start-dev
```

In another terminal:

```bash
python -m temprun.worker
```

And in another:

```bash
python -m temprun.run
```

Run tests:

```bash
pytest
```

The tests use Temporal's Python testing environment. On first run, the Temporal SDK may download a local test server binary.

See `AGENTS.md`, `MEMORY.md`, and `.memory/README.md` for the learning constraints and project memory.
