from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.core import TaskRepository
from src.database.deps import get_session
from src.schemas.task import TaskCreateRequest, TaskResponse

router = APIRouter(prefix="/task", tags=["Task"])


@router.get("/get_all", response_model=list[TaskResponse])
async def get_tasks(
    user_id: int,
    session: AsyncSession = Depends(get_session),
):
    return await TaskRepository.get_all_by_user_id(
        session=session,
        user_id=user_id,
    )


@router.post("/add", response_model=TaskResponse)
async def add_task(
    task: TaskCreateRequest,
    session: AsyncSession = Depends(get_session),
):
    return await TaskRepository.add_one(
        session=session,
        task_data=task,
    )


@router.delete("/delete")
async def delete_task(
    task_id: int,
    session: AsyncSession = Depends(get_session),
):
    res = await TaskRepository.delete_one(session, task_id)

    if res == 0:
        return {"detail": "Task not found"}
    return {"detail": "Task deleted successfully"}
