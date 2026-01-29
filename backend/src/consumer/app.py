from faststream import FastStream

from src.broker import broker
from src.consumer.task import router as task_router
import logging

logger = logging.getLogger("kafka")

app = FastStream(
    broker,
    logger=logger
)

broker.include_router(task_router)
