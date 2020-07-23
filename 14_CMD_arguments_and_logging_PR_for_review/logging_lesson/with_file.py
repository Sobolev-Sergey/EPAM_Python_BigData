import logging

# add filemode="w" to overwrite
logging.basicConfig(level=logging.INFO, filename='sample.log')
logger = logging.getLogger("Main module")

logger.info("Informational message")
