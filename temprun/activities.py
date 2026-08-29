from __future__ import annotations

from temporalio import activity

from .models import AgentResult, AgentTask, ResearchBrief, ResearchPlan, ResearchRequest, SynthesisInput


@activity.defn
async def plan_research(request: ResearchRequest) -> ResearchPlan:
    """Activity boundary: planning may later call models or tools outside workflow replay."""
    return ResearchPlan(
        topic=request.topic,
        depth=request.depth,
        agents=["web", "papers", "systems", "implementation", "security", "critic"],
    )


@activity.defn
async def run_fake_agent(task: AgentTask) -> AgentResult:
    """Fake agent Activity used to study retries before adding real LLM/network I/O."""
    info = activity.info()
    planned_failures = task.fail_agent_attempts.get(task.agent, 0)
    if task.fail_agent_once == task.agent:
        planned_failures = max(planned_failures, 1)
    if info.attempt <= planned_failures:
        raise RuntimeError(
            f"controlled failure {info.attempt} of {planned_failures} for {task.agent} agent"
        )

    findings = {
        "web": (
            "Temporal positions Workflow history as the durable source of progress.",
            ["workflow event history", "activity completion events"],
        ),
        "papers": (
            "Research quality improves when claims trace back to primary sources.",
            ["source selection criteria", "citation-backed synthesis"],
        ),
        "systems": (
            "Activities are at-least-once, so external effects need idempotency keys.",
            ["retry attempt metadata", "idempotent side-effect boundary"],
        ),
        "implementation": (
            "The workflow stays small when orchestration logic avoids provider-specific code.",
            ["thin workflow coordinator", "activity-owned integration code"],
        ),
        "security": (
            "Local services exposed through a private tailnet should still keep explicit trust boundaries.",
            ["tailnet-only access", "localhost Temporal service"],
        ),
        "critic": (
            "Workflow code should coordinate state and avoid nondeterministic side effects.",
            ["deterministic replay", "activity isolation"],
        ),
    }
    finding, evidence = findings[task.agent]
    return AgentResult(agent=task.agent, finding=finding, evidence=evidence)


@activity.defn
async def synthesize_research(payload: SynthesisInput) -> ResearchBrief:
    """Synthesis is an Activity because real summarization may later call an LLM."""
    findings = [f"{result.agent}: {result.finding}" for result in payload.results]
    summary = (
        f"{payload.topic} researched at {payload.depth} depth by "
        f"{len(payload.results)} fake agents."
    )
    return ResearchBrief(
        topic=payload.topic,
        depth=payload.depth,
        summary=summary,
        findings=findings,
        retry_lesson=(
            "Temporal retries failed Activities from history according to RetryPolicy; "
            "Workflow code does not implement a manual retry loop."
        ),
    )
