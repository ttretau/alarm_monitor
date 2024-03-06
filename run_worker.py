import asyncio
import os

from temporalio.client import Client
from temporalio.worker import Worker

from activities import handle_page
from converter import pydantic_data_converter
from workflows import APageWorkflow


async def main():
    client = await Client.connect(
        f"{os.getenv('TEMPORAL_HOST', 'localhost')}:7233",
        namespace="alarm", data_converter=pydantic_data_converter)

    worker = Worker(
        client,
        task_queue="alarm-task-queue",
        workflows=[APageWorkflow],
        activities=[
            handle_page
        ],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
