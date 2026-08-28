# Handoff

## Current state

The repository has been initialized as a Temporal/distributed-systems interview learning project.

`AGENTS.md` defines the learning-first development rules. `.memory/` contains the persistent project ontology, initial context, decisions, questions, learnings, and planned failure experiments.

No Temporal application code has been implemented yet.

## Just completed

- Established project purpose and learning sequence.
- Established Chronelle-style project memory.
- Recorded the initial durable research-workflow scenario.
- Seeded the important Temporal questions and failure experiments.

## Next action

Bootstrap the minimal Python project and implement milestone 1:

```text
ResearchWorkflow
      |
      +--> fake research Activity
      +--> fake technical Activity
      +--> fake critic Activity
      |
      v
parallel fan-in
      |
      v
synthesis Activity
      |
      v
result
```

Use the official Temporal Python SDK. Keep the implementation intentionally small and expose Temporal primitives directly.

Add controlled Activity failure injection and a RetryPolicy so the first hands-on experiment is Activity retry behavior.

## After milestone 1

1. Add Signal + durable human approval.
2. Add Query for workflow progress/state.
3. Perform worker kill/restart experiments.
4. Convert one agent into a Child Workflow.
5. Explore cancellation and heartbeats.

## Blockers

None known.
