from faststream.kafka import KafkaBroker

from src.config import settings

broker = KafkaBroker(settings.KAFKA_URL)
