from pydantic import BaseModel
from datetime import datetime


class TodoBase(BaseModel):
    title: str
    content: str


class TodoIn(TodoBase):
    pass


class TodoOut(TodoBase):
    author: str
    date_created: datetime


class TodoUpdate(TodoBase):
    pass
