from pydantic import BaseModel


class TaskMessage(BaseModel):
    task_id: int
