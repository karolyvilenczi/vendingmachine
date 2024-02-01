"""
Module to implement routes using the services/wending_machine.py
"""

from fastapi import APIRouter
from fastapi import HTTPException

from busapp.apputils.app_logger import applog
from busapp.services.vending_machine import (
    VendingMachine, 
    States
)
from busapp.services.models.vending_machine import MachineState

from pprint import pprint as pp

# ------------------------------------------------------
global vm
vm = VendingMachine()
  
router_vm = APIRouter(prefix="/machine")

# ------------------------------------------------------
@router_vm.post("/state")
async def set_state(state:MachineState):
    
    if (state.desired_state == States.READY.value):
        try:
            vm.turn_key_to_ready()
        except Exception as e:
            err_msg = f"Could not turn on machine on: {e}"
            applog.error(err_msg)
            raise HTTPException(status_code=500, detail=err_msg)

    if (state.desired_state == States.MAINTENANCE.value):    
        try:
           vm.turn_key_to_maintenance()
        except Exception as e:
            err_msg = f"Could not go to maintenance mode: {e}"
            applog.error(err_msg)
            raise HTTPException(status_code=500, detail=err_msg)
        
    return {"current_state":vm.state.value}


@router_vm.get("/state")
async def get_current_state():
    return {"current_state":vm.state.value}


@router_vm.get("/users")
async def get_current_state():
            
    return {"current_users":vm.users}