"""
Module to implement routes using the services/wending_machine.py
"""

from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel

from busapp.apputils.app_logger import applog
from busapp.services.vending_machine import VendingMachine, States

from pprint import pprint as pp

# ------------------------------------------------------
vm = VendingMachine()
 
class MachineState(BaseModel):
    desired_state: str
    
router_vm = APIRouter()


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
        
    return {"state":vm.state.value}

