# Learnings

This file records durable lessons confirmed while building and experimenting with `temprun`.

## Seed mental model

### Workflow vs Activity

A Temporal Workflow expresses durable orchestration and logical state. An Activity performs work with external side effects or nondeterministic behavior.

A useful working model is:

```text
Workflow = durable state machine / coordination
Activity = failure-prone interaction with the outside world
```

This model should be refined based on actual experiments rather than treated as complete.

### Replay is central

Temporal can reconstruct Workflow execution from persisted event history. Workflow code therefore has determinism constraints: replaying the same history must reproduce compatible workflow decisions.

This is why arbitrary network calls, wall-clock reads, and randomness should not simply be placed inside Workflow code.

### Activity retry implies idempotency concerns

An Activity can be retried when completion is uncertain. External side effects therefore cannot be assumed to execute exactly once merely because they are represented by one logical Activity invocation.

Future experiments should deliberately create ambiguous failure points around external side effects and verify the resulting behavior.

---

Add confirmed implementation-specific learnings below this line as the project progresses.
