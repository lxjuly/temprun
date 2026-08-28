# Experiments

## Experiment: Activity retry
Status: PLANNED

**Hypothesis:** A failing Activity can be retried according to Temporal's RetryPolicy while the Workflow continues to represent one logical execution.

**Setup:** Add controlled failure injection to one fake research Activity. Configure a short RetryPolicy and record attempt information.

**Expected:** Temporal schedules another Activity attempt according to policy rather than requiring a manual retry loop in Workflow code.

**Observed:** Not run yet.

**Conclusion:** Pending.

## Experiment: kill worker during Activity
Status: PLANNED

**Hypothesis:** Killing the worker does not destroy the logical Workflow. After workers return, Temporal can continue execution according to Activity timeout/retry semantics.

**Setup:** Start a Workflow with a deliberately slow Activity. Kill the worker process while the Activity is executing, then restart it.

**Expected:** Workflow state remains durable and work eventually resumes/retries rather than restarting the entire logical workflow from scratch.

**Observed:** Not run yet.

**Conclusion:** Pending.

## Experiment: kill worker while Workflow waits for approval
Status: PLANNED

**Hypothesis:** A Workflow waiting on a durable condition/Signal does not require a continuously running worker process.

**Setup:** Add an approval Signal and durable wait. Reach the waiting state, terminate the worker, restart it, then send approval.

**Expected:** The Workflow remains logically waiting and resumes after approval when a compatible worker is available.

**Observed:** Not run yet.

**Conclusion:** Pending.

## Experiment: ambiguous external side effect
Status: PLANNED

**Hypothesis:** If an Activity performs an external side effect and fails before Temporal records successful completion, the Activity may execute again, demonstrating why side effects should be idempotent.

**Setup:** Use a simple external-looking side effect with an observable idempotency key, then intentionally fail after the side effect but before successful Activity return.

**Expected:** Retry can repeat the Activity invocation; an idempotency mechanism prevents duplicate logical effects.

**Observed:** Not run yet.

**Conclusion:** Pending.
