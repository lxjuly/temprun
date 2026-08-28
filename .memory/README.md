# Chronelle Memory

`.memory/` contains temprun's historical durable source memory.

The source primitive model is intentionally only:

- Claim: truth-apt memory
- Commitment: will-apt memory

The current working memory interface is:

```text
MEMORY.md
journal/
```

`MEMORY.md` tracks current status for fast agent resume. `journal/` stores the detailed dated paper trail.

Compact `.chron` records live under:

```text
.memory/records/
```

Each record is a Git-committed memory payload containing Claims and Commitments. Git is the ledger for this local-file implementation.

Human-facing artifacts, task plans, checkpoints, `MEMORY.md`, and `journal/` live outside `.memory/`.

For temprun, use `.memory/records/YYYY/MM/DD/*.chron` only for durable compact records. Keep working status in `MEMORY.md` and narrative/experimental detail in `journal/YYYY-MM-DD.md`.
