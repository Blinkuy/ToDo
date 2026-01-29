from faststream.kafka import KafkaBroker
import logging

from src.config import settings

logger = logging.getLogger("kafka")

broker = KafkaBroker(settings.KAFKA_URL, logger=logger)
