# Project Context

## Purpose

`temprun` is a hands-on Temporal learning lab built around a small durable multi-agent execution runtime.

The immediate objective is to develop strong intuition for Temporal and the distributed-systems concepts relevant to an agent-runtime engineering interview. Building a production-ready agent framework is explicitly not the goal.

## Core problem

Run agent work as durable workflows that can fan out, fail, retry, wait, resume, and survive worker/process failure without losing logical execution state.

Initial scenario:

```text
Research request
      |
      +--> research agent
      +--> technical agent
      +--> critic agent
      |
      v
   synthesis
      |
      v
human approval
      |
      v
   finalize
```

The agents should initially be fake. Temporal behavior is the subject being studied; LLM quality is not.

## Architecture direction

- Language: Python 3.11+
- Orchestrator: Temporal using the official Python SDK
- Workflows: durable orchestration/state-machine logic
- Activities: external or nondeterministic work
- Workers: disposable execution processes consuming Temporal task queues
- Tests/experiments: first-class part of the project

Avoid unnecessary API, database, UI, and agent-framework layers during early milestones.

## Current milestone

Bootstrap the project and implement the smallest useful workflow:

1. one `ResearchWorkflow`;
2. three parallel fake research Activities;
3. fan-in of their results;
4. one synthesis Activity;
5. Temporal RetryPolicy and controlled failure injection;
6. tests using Temporal's testing support.

The milestone after that is Signals + durable human approval, followed by explicit worker kill/restart experiments.

## Learning objective

For every feature, be able to answer both:

1. How do I implement this with Temporal?
2. What distributed-systems problem is Temporal solving for me?

Important subjects include deterministic replay, event history, retries, at-least-once Activity execution, idempotency, timeouts, durable timers, Signals, Queries, Child Workflows, cancellation, heartbeats, task queues, worker concurrency, long histories, and safe deployment/versioning.
