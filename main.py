import os
import uuid

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Security
from fastapi.security import APIKeyHeader
import logging

from starlette import status
from temporalio.client import Client

from converter import pydantic_data_converter
from models import PageEvent, AlarmEvent
from workflows import APageWorkflow

logger = logging.getLogger(__name__)
load_dotenv()

API_KEYS = os.getenv("API_KEYS").split(',')
api_key_header = APIKeyHeader(name="x-api-key")

app = FastAPI()


async def get_temporal_client():
    return await Client.connect(
        f"{os.getenv('TEMPORAL_HOST', 'localhost')}:7233",
        namespace="alarm", data_converter=pydantic_data_converter)


def get_api_key(api_key_header: str = Security(api_key_header)) -> str:
    if api_key_header in API_KEYS:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.post("/api/apages/")
async def handle_apage_event(event: PageEvent,
                             api_key: str = Security(get_api_key)):
    logger.info(f"Apage event: {event}")
    client = await get_temporal_client()
    handle = await client.start_workflow(APageWorkflow.run, event,
                                         id=str(uuid.uuid4()),
                                         task_queue="alarm-task-queue")
    return {"run_id": handle.first_execution_run_id}


@app.post("/api/alarms/")
async def handle_mobile_alarm_event(event: AlarmEvent,
                                    api_key: str = Security(get_api_key)):
    logger.info(f"Alarm event: {event}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
