from datetime import datetime

from pydantic import BaseModel, Field


class PageEvent(BaseModel):
    keyword: str
    unit: str


class AlarmEvent(BaseModel):
    title: str | None
    text: str
    created: datetime = Field(default_factory=datetime.now)
    closed: bool = False
