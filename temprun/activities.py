from __future__ import annotations

from temporalio import activity

from .models import AgentResult, AgentTask, ResearchBrief, ResearchPlan, ResearchRequest, SynthesisInput


@activity.defn
async def plan_research(request: ResearchRequest) -> ResearchPlan:
    """Activity boundary: planning may later call models or tools outside workflow replay."""
    return ResearchPlan(
        topic=request.topic,
        depth=request.depth,
        agents=["web", "systems", "critic"],
    )


@activity.defn
async def run_fake_agent(task: AgentTask) -> AgentResult:
    """Fake agent Activity used to study retries before adding real LLM/network I/O."""
    info = activity.info()
    if task.fail_agent_once == task.agent and info.attempt == 1:
        raise RuntimeError(f"controlled one-time failure for {task.agent} agent")

    findings = {
        "web": (
            "Temporal positions Workflow history as the durable source of progress.",
            ["workflow event history", "activity completion events"],
        ),
        "systems": (
            "Activities are at-least-once, so external effects need idempotency keys.",
            ["retry attempt metadata", "idempotent side-effect boundary"],
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
