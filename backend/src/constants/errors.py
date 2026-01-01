from enum import Enum


class ErrorDetail(str, Enum):
    TASK_NOT_FOUND = "Task not found"
