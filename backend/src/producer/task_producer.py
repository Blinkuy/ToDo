from src.fs_broker import broker


async def publish_task_create(task_id: int) -> None:
    await broker.publish(
        {"task_id": task_id},
        topic="task_created",
    )