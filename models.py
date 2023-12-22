from pydantic import BaseModel


class PageEvent(BaseModel):
    keyword: str
    unit: str
