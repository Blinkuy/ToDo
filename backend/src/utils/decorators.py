import functools
import logging
import time

logger = logging.getLogger(__name__)


def log_execution_time(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return await func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            logger.debug("Execution time of %s: %.4f seconds", func.__qualname__, elapsed)

    return wrapper
