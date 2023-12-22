import asyncio

from temporalio import activity

from models import PageEvent


@activity.defn
async def handle_page(event: PageEvent) -> str:
    await asyncio.sleep(3)
    print(activity.info())
    print(f"Event handling: {event}")
    return "handled event"
