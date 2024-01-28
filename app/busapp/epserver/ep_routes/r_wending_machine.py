"""
Module to implement routes using the services/wending_machine.py
"""

from fastapi import APIRouter
from busapp.apputils.app_logger import applog

from busapp.services import wending_machine as wm

# ------------------------------------------------------
router_wm = APIRouter()

# ------------------------------------------------------
@router_wm.get("/items")
async def fetch_items():
    applog.debug("Fetching items")
    result = await wm.get_items()
    return result
