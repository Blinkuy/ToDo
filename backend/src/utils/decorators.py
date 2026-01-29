import functools
import time
import logging

logger = logging.getLogger(__name__)


def log_execution_time(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return await func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            logger.info(f"Время выполнения {func.__qualname__} — {elapsed:.4f} сек")
    return wrapper