"""
An app wide logger module
TODO: replace with loguru
"""

import logging


def make_logger(logger_name="APP LOGGER"):
    # create logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter(
        ">>> %(asctime)s - %(name)s - %(levelname)s - %(message)s <<<"
    )

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    return logger
