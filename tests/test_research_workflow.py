from __future__ import annotations

from collections import Counter
from uuid import uuid4

from temporalio.testing import WorkflowEnvironment
from temporalio.worker import Worker

from temprun.activities import plan_research, run_fake_agent, synthesize_research
from temprun.models import ResearchRequest
from temprun.workflows import ResearchWorkflow


async def test_research_workflow_fans_out_and_synthesizes() -> None:
    async with await WorkflowEnvironment.start_time_skipping() as env:
        async with Worker(
            env.client,
            task_queue="test-research",
            workflows=[ResearchWorkflow],
            activities=[plan_research, run_fake_agent, synthesize_research],
        ):
            result = await env.client.execute_workflow(
                ResearchWorkflow.run,
                ResearchRequest(topic="Temporal replay"),
                id=f"test-research-{uuid4().hex}",
                task_queue="test-research",
            )

    assert result.topic == "Temporal replay"
    assert result.depth == "interview-prep"
    assert result.summary == "Temporal replay researched at interview-prep depth by 3 fake agents."
    assert {finding.split(":", 1)[0] for finding in result.findings} == {"web", "systems", "critic"}


async def test_research_workflow_retries_one_failed_agent_activity() -> None:
    attempts: Counter[str] = Counter()

    async def tracked_fake_agent(task):
        attempts[task.agent] += 1
        return await run_fake_agent(task)

    tracked_fake_agent.__temporal_activity_definition = (
        run_fake_agent.__temporal_activity_definition
    )

    async with await WorkflowEnvironment.start_time_skipping() as env:
        async with Worker(
            env.client,
            task_queue="test-retry",
            workflows=[ResearchWorkflow],
            activities=[plan_research, tracked_fake_agent, synthesize_research],
        ):
            result = await env.client.execute_workflow(
                ResearchWorkflow.run,
                ResearchRequest(
                    topic="Temporal Activity retries",
                    fail_agent_once="systems",
                ),
                id=f"test-retry-{uuid4().hex}",
                task_queue="test-retry",
            )

    assert result.topic == "Temporal Activity retries"
    assert attempts["systems"] == 2
    assert attempts["web"] == 1
    assert attempts["critic"] == 1
    assert "manual retry loop" in result.retry_lesson
