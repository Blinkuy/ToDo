from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.core import TaskRepository
from src.database.deps import get_session
from src.producer.task_producer import publish_task_create
from src.schemas.task import TaskCreateRequest, TaskResponse
from src.utils.errors import ErrorDetail
import logging

router = APIRouter(prefix="/task", tags=["Task"])

logger = logging.getLogger(__name__)

@router.get("/get_all", response_model=list[TaskResponse])
async def get_tasks(
    user_id: int,
    session: AsyncSession = Depends(get_session),
):
    logger.info("Getting tasks. User id: %s", user_id)
    tasks = await TaskRepository.get_all_by_user_id(
        session=session,
        user_id=user_id,
    )

    return [TaskResponse.from_orm_to_schema(t) for t in tasks]


@router.post("/add", response_model=TaskResponse)
async def add_task(
    task: TaskCreateRequest,
    session: AsyncSession = Depends(get_session),
):
    task = await TaskRepository.add_one(session=session, task_data=task, with_commit=True)

    await publish_task_create(task.id)
    logger.info("Published task added event")
    return TaskResponse.from_orm_to_schema(task)


@router.delete("/delete")
async def delete_task(
    task_id: int,
    session: AsyncSession = Depends(get_session),
):
    res = await TaskRepository.delete_one(session, task_id, with_commit=True)

    if res == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=ErrorDetail.TASK_NOT_FOUND
        )
    else:
        logger.info("Task with id: %s deleted", task_id)
