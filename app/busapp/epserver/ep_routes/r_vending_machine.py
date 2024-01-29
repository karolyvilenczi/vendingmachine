"""
Module to implement routes using the services/wending_machine.py
"""

from fastapi import APIRouter
from busapp.apputils.app_logger import applog

from busapp.services.vending_machine import VendingMachine

# ------------------------------------------------------
vm = VendingMachine()
vm.turn_key_to_ready()

router_vm = APIRouter()



# ------------------------------------------------------
@router_vm.get("/funds")
def fetch_items():
    applog.debug("Fetching funds")
    result = vm.get_current_funds()
    return result
