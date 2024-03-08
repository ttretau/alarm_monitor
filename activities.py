import asyncio

from temporalio import activity

from models import PageEvent, AlarmEvent


@activity.defn
async def handle_page(event: PageEvent) -> str:
    await asyncio.sleep(3)
    print(activity.info())
    print(f"Event handling: {event}")
    return "handled event"


@activity.defn
async def handle_alarm(event: AlarmEvent) -> str:
    await asyncio.sleep(3)
    print(activity.info())
    print(f"Event handling: {event}")
    return "handled alarm event"
