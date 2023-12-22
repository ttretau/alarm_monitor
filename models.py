from datetime import datetime

from pydantic import BaseModel


class PageEvent(BaseModel):
    keyword: str
    unit: str


class AlarmEvent(BaseModel):
    title: str | None
    text: str
    created: datetime | None
    closed: bool = False
