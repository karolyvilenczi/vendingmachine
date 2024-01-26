"""
Module to implement the money management functions.
"""

from pydantic import BaseModel
from typing import List

from busapp.apputils import app_logger

# ------------------------------------------------------
applog = app_logger.make_logger("SRV:MONEY MANAGER")


# TODO: Add some stacks based model to have coins  (in an array of 5, 10, 20, 50 and 100 cent coins)
# TODO: add tests