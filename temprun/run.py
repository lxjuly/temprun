from __future__ import annotations

import asyncio
from uuid import uuid4

from temporalio.client import Client

from .models import ResearchRequest
from .worker import TASK_QUEUE
from .workflows import ResearchWorkflow


async def main() -> None:
    client = await Client.connect("localhost:7233")
    result = await client.execute_workflow(
        ResearchWorkflow.run,
        ResearchRequest(
            topic="Temporal workflow determinism",
            fail_agent_once="systems",
        ),
        id=f"research-{uuid4().hex}",
        task_queue=TASK_QUEUE,
    )
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
