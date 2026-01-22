import datetime

from src.database.models import Task
from src.schemas.base import BaseSchema


class TaskCreateRequest(BaseSchema):
    user_id: int
    name: str
    description: str


class TaskResponse(BaseSchema[Task]):
    id: int
    user_id: int
    name: str
    description: str
    created_at: datetime.datetime
