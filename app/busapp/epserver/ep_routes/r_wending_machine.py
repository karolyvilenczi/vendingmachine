"""
Module to implement routes using the services/wending_machine.py
"""

from fastapi import APIRouter
from busapp.apputils import app_logger

from busapp.services import wending_machine as wm

applog = app_logger.make_logger("ROUTE: WENDING MACHINE")


# ------------------------------------------------------
router_wm = APIRouter()

# ------------------------------------------------------
@router_wm.get("/items")
async def fetch_items():
    applog.debug("Fetching items")
    result = await wm.get_items()
    return result
