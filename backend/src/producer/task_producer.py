from src.broker import broker
from src.config import settings
from src.schemas.message import TaskMessage


@broker.publisher(topic=settings.KAFKA_TOPIC_TASK_CREATED)
async def publish_task_create(task_id: int) -> TaskMessage:
    return {"task_id": task_id}
