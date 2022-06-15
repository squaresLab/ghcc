import logging
import coloredlogs

LOG_FORMAT = "[%(levelname)-7.7s] %(asctime)s %(message)s"


def init_logger(logging_level: int=logging.INFO) -> None:
    coloredlogs.DEFAULT_FIELD_STYLES["levelname"]["color"] = "cyan"
    coloredlogs.install(
        level=logging_level, fmt=LOG_FORMAT,
    )
