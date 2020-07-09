import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Main module")

logger.debug("This is a debug message")
logger.info("Informational message")
logger.warning("Warning appeared")
logger.error("An error has happened!")
logger.critical("Critical error. Time to self-termination")
