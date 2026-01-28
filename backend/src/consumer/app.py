from faststream import FastStream

from src.broker import broker
from src.consumer.task import router as task_router

app = FastStream(
    broker,
)

broker.include_router(task_router)
