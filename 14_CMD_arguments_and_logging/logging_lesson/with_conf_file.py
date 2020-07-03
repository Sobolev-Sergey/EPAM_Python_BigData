import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger("someLogger")
logger.info("Informational message")

root_logger = logging.getLogger()
root_logger.critical("Critical")
