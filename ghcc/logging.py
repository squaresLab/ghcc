import logging
import coloredlogs

from argtyped import Arguments

LOG_FORMAT = "[%(levelname)-7.7s] %(asctime)s %(message)s"


def init_logger(args: Arguments) -> None:
    coloredlogs.DEFAULT_FIELD_STYLES["levelname"]["color"] = "cyan"
    coloredlogs.install(
        level=args.logging_level, fmt=LOG_FORMAT,
    )
