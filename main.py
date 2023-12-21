import os
from datetime import datetime

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Security
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
import logging

from starlette import status

logger = logging.getLogger(__name__)
load_dotenv()

API_KEYS = [os.getenv("API_KEY").split(',')]
api_key_header = APIKeyHeader(name="x-api-key")

app = FastAPI()


class PageEvent(BaseModel):
    keyword: str
    unit: str


class AlarmEvent(BaseModel):
    title: str | None
    text: str
    created: datetime | None
    closed: bool = False


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.post("/api/apages/")
async def handle_apage_event(event: PageEvent,
                             api_key: str = Security(api_key_header)):
    logger.info(f"Apage event: {event}")


@app.post("/api/alarms/")
async def handle_apage_event(event: PageEvent,
                             api_key: str = Security(api_key_header)):
    logger.info(f"Alarm event: {event}")


def get_api_key(api_key_header: str = Security(api_key_header)) -> str:
    if api_key_header in API_KEYS:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
