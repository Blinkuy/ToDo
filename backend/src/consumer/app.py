import logging

from faststream import FastStream

from src.broker import broker
from src.consumer.task import router as task_router
from src.logger import setup_root_logger

setup_root_logger()


logger = logging.getLogger("kafka")

app = FastStream(
    broker,
    logger=logger,
)

broker.include_router(task_router)
