import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ex")

try:
    raise RuntimeError
except RuntimeError:
    logger.exception("Error!")
