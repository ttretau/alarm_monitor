from datetime import timedelta

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from models import PageEvent, AlarmEvent
    from activities import handle_page, handle_alarm
    from converter import pydantic_data_converter


@workflow.defn
class APageWorkflow:

    def __init__(self) -> None:
        self._pending_alarm: AlarmEvent | None = None
        self._exit = False

    @workflow.run
    async def run(self, input: PageEvent):
        output = await workflow.execute_activity(
            handle_page,
            input,
            start_to_close_timeout=timedelta(seconds=30),
        )
        while True:
            await workflow.wait_condition(
                lambda: self._pending_alarm or self._exit
            )

            if self._pending_alarm:
                output = await workflow.execute_activity(
                    handle_alarm,
                    self._pending_alarm,
                    start_to_close_timeout=timedelta(seconds=30),
                )

            if self._exit:
                return self._pending_alarm

    @workflow.signal
    async def submit_alarm(self, event: AlarmEvent):
        self._pending_alarm = event

    @workflow.signal
    def exit(self) -> None:
        self._exit = True
