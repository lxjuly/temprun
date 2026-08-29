from __future__ import annotations

import asyncio
from datetime import timedelta

from temporalio import workflow
from temporalio.common import RetryPolicy

from .models import AgentTask, ResearchBrief, ResearchRequest, SynthesisInput

with workflow.unsafe.imports_passed_through():
    from .activities import plan_research, run_fake_agent, synthesize_research


@workflow.defn
class ResearchWorkflow:
    @workflow.run
    async def run(self, request: ResearchRequest) -> ResearchBrief:
        plan = await workflow.execute_activity(
            plan_research,
            request,
            start_to_close_timeout=timedelta(seconds=10),
        )

        retry_policy = RetryPolicy(
            initial_interval=timedelta(seconds=1),
            maximum_interval=timedelta(seconds=5),
            maximum_attempts=4,
        )

        # Parallel Activity fan-out/fan-in is the first core Temporal concept in this repo.
        agent_results = await asyncio.gather(
            *[
                workflow.execute_activity(
                    run_fake_agent,
                    AgentTask(
                        topic=plan.topic,
                        depth=plan.depth,
                        agent=agent,
                        fail_agent_once=request.fail_agent_once,
                        fail_agent_attempts=dict(request.fail_agent_attempts),
                    ),
                    start_to_close_timeout=timedelta(seconds=10),
                    retry_policy=retry_policy,
                )
                for agent in plan.agents
            ]
        )

        return await workflow.execute_activity(
            synthesize_research,
            SynthesisInput(topic=plan.topic, depth=plan.depth, results=list(agent_results)),
            start_to_close_timeout=timedelta(seconds=10),
        )
