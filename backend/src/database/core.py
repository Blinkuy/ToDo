from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Notification, Task, User
from src.schemas.task import TaskCreateRequest
from src.schemas.user import UserCreateRequest


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
        with_commit: bool = False,
    ) -> Task:
        task = Task(
            user_id=task_data.user_id,
            name=task_data.name,
            description=task_data.description,
        )
        session.add(task)
        await session.flush()
        if with_commit:
            await session.commit()
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
        with_commit: bool = False,
    ) -> None:
        stmt = delete(Task).where(Task.id == task_id)
        await session.execute(stmt)

        if with_commit:
            await session.commit()


class UserRepository:
    @staticmethod
    async def get_one_or_none(
        user_id: int,
        session: AsyncSession,
    ) -> User | None:
        stmt = select(User).where(User.id == user_id)
        result = await session.execute(stmt)

        return result.scalar_one_or_none()

    @staticmethod
    async def add_one(
        session: AsyncSession,
        user_data: UserCreateRequest,
    ) -> User:
        user = User(
            username=user_data.username,
            password=user_data.password,
        )

        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

    @staticmethod
    async def get_all(
        session: AsyncSession,
    ) -> list[User]:
        stmt = select(User)
        result = await session.execute(stmt)

        return result.scalars().all()


class NotificationRepository:
    @staticmethod
    async def get_all(
        session: AsyncSession,
    ) -> list[User]:
        stmt = select(Notification)
        result = await session.execute(stmt)

        return result.scalars().all()
