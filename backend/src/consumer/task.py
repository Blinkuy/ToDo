from fastapi import Depends
from faststream.kafka import KafkaRouter

from src.config import settings
from src.database.core import NotificationRepository
from src.database.deps import get_session
from src.schemas.message import TaskMessage

router = KafkaRouter()


@router.subscriber(settings.KAFKA_TOPIC_TASK_CREATED)
async def handle_task_created(message: TaskMessage, session = Depends(get_session)):

    NotificationRepository.create_for_all_users(
        session=session,
        task_id=message.task_id
)
