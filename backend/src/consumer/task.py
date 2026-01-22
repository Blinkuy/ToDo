from faststream.kafka import KafkaRouter
from sqlalchemy import select

from src.database.database import AsyncSessionLocal
from src.database.models import Notification, User

router = KafkaRouter()


@router.subscriber("task_created")
async def handle_task_created(message: dict):
    print("On handle")
    task_id = message["task_id"]

    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()

        notifications = [Notification(user_id=user.id, task_id=task_id) for user in users]

        session.add_all(notifications)
        await session.commit()
