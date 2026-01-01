from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Task
from src.schemas.task import TaskCreateRequest


class TaskRepository:
    @staticmethod
    async def get_one_or_none(
        session: AsyncSession,
        task_id: int,
    ) -> Task | None:
        stmt = select(Task).where(Task.id == task_id)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    @staticmethod
    async def add_one(
        session: AsyncSession,
        task_data: TaskCreateRequest,
    ) -> Task:
        task = Task(
            user_id=task_data.user_id,
            name=task_data.name,
            description=task_data.description,
        )
        session.add(task)
        await session.commit()
        await session.refresh(task)
        return task

    @staticmethod
    async def get_all_by_user_id(
        session: AsyncSession,
        user_id: int,
    ) -> list[Task]:
        stmt = select(Task).where(Task.user_id == user_id)
        result = await session.execute(stmt)
        return result.scalars().all()

    @staticmethod
    async def delete_one(
        session: AsyncSession,
        task_id: int,
    ) -> int:
        stmt = delete(Task).where(Task.id == task_id)
        result = await session.execute(stmt)
        await session.commit()
        return result.rowcount
