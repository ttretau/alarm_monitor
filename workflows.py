from datetime import timedelta

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from models import PageEvent
    from activities import handle_page
    from converter import pydantic_data_converter


@workflow.defn
class APageWorkflow:
    @workflow.run
    async def run(self, input: PageEvent):
        output = await workflow.execute_activity(
            handle_page,
            input,
            start_to_close_timeout=timedelta(seconds=30),
        )
        return output
