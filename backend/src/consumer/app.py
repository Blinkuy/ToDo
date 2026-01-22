from faststream import FastStream

from src.consumer.task import router as task_router
from src.fs_broker import broker

app = FastStream(
    broker,
)

broker.include_router(task_router)
