from __future__ import annotations

import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from .activities import plan_research, run_fake_agent, synthesize_research
from .workflows import ResearchWorkflow

TASK_QUEUE = "temprun-research"


async def main() -> None:
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue=TASK_QUEUE,
        workflows=[ResearchWorkflow],
        activities=[plan_research, run_fake_agent, synthesize_research],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
