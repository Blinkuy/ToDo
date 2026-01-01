from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.constants.errors import ErrorDetail
from src.database.core import TaskRepository
from src.database.deps import get_session
from src.schemas.task import TaskCreateRequest, TaskResponse

router = APIRouter(prefix="/task", tags=["Task"])


@router.get("/get_all", response_model=list[TaskResponse])
async def get_tasks(
    user_id: int,
    session: AsyncSession = Depends(get_session),
):
    tasks = await TaskRepository.get_all_by_user_id(
        session=session,
        user_id=user_id,
    )

    return [TaskResponse.from_orm_model(t) for t in tasks]


@router.post("/add", response_model=TaskResponse)
async def add_task(
    task: TaskCreateRequest,
    session: AsyncSession = Depends(get_session),
):
    task = await TaskRepository.add_one(
        session=session,
        task_data=task,
    )

    return TaskResponse.from_orm_model(task)


@router.delete("/delete")
async def delete_task(
    task_id: int,
    session: AsyncSession = Depends(get_session),
):
    res = await TaskRepository.delete_one(session, task_id)

    if res == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=ErrorDetail.TASK_NOT_FOUND
        )
