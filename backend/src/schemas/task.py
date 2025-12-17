import datetime

from .base import BaseSchema


class TaskCreateRequest(BaseSchema):
    user_id: int
    name: str
    description: str


class TaskResponse(BaseSchema):
    id: int
    user_id: int
    name: str
    description: str
    created_at: datetime.datetime
