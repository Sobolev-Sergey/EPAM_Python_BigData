import logging.config

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_CONFIG = {
    "version": 1,
    "handlers": {
        "fileHandler": {
            "class": "logging.FileHandler", "formatter": "myFormatter",
            "filename": "some_logger2.log"
        }
    },
    "loggers": {"someLogger": {"handlers": ["fileHandler"], "level": "INFO"}},
    "formatters": {"myFormatter": {"format": LOG_FORMAT, "datefmt": "%Y.%m.%d %H:%M:%S"}}
}

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger("someLogger")
logger.info("Program started")
logger.info("Done!")
