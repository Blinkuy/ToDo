import datetime

from src.database.models import Task
from src.schemas.base import BaseSchema


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

    @classmethod
    def from_orm_model(cls, task: Task) -> "TaskResponse":
        return cls(
            id=task.id,
            user_id=task.user_id,
            name=task.name,
            description=task.description,
            created_at=task.created_at,
        )
