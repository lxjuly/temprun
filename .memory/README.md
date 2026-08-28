# temprun Memory

`.memory` is the persistent project memory for humans and coding agents. It follows a lightweight Chronelle-style ontology: store durable context as typed knowledge rather than accumulating conversation transcripts.

## Ontology

### `CONTEXT.md`
Stable project identity, goals, architecture, constraints, and current milestone. Update when the project's direction or milestone materially changes.

### `DECISIONS.md`
Append-only architectural decision log. Record decisions that future work should not have to rediscover.

Format:

```markdown
## YYYY-MM-DD — Decision title

**Context:** Why the decision was needed.

**Decision:** What was chosen.

**Rationale:** Why.

**Consequences:** What this enables or constrains.
```

### `LEARNINGS.md`
Durable technical knowledge learned through implementation. Focus especially on Temporal and distributed-systems semantics: replay, delivery guarantees, retries, idempotency, scheduling, failure modes, and worker behavior.

Do not simply copy documentation. Record what became clear through this project and why it matters.

### `QUESTIONS.md`
Investigation backlog. Questions are never deleted; change `OPEN` to `ANSWERED` and record the answer or link to the relevant learning/decision.

### `EXPERIMENTS.md`
Empirical notebook for distributed-systems behavior. Prefer experiments over assumptions.

Each experiment should capture:

```markdown
## Experiment: title
Status: PLANNED | RUNNING | COMPLETE

Hypothesis:
Setup:
Expected:
Observed:
Conclusion:
```

### `HANDOFF.md`
Short-lived continuation state for the next coding session or agent. Keep it concise and current: what exists, what was just done, next action, and blockers.

## Memory rules

1. Memory is not a transcript.
2. Prefer concise facts with enough context to remain understandable months later.
3. Record *why* for decisions, not just what changed.
4. Separate observation from inference in experiments.
5. Preserve answered questions and superseded decisions as history.
6. Update `HANDOFF.md` before ending substantial work.
7. If a new insight changes an architectural assumption, update both the relevant learning and decision/context entry.

The purpose is continuation: a new agent should be able to inspect `AGENTS.md` and `.memory` and continue the project without reconstructing its intent from chat history.
