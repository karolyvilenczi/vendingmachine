from typing import List, Dict, Annotated
from pprint import pprint as pp

from fastapi import APIRouter, Depends

from busapp.apputils.app_logger import applog
from busapp.services.crud_service import MoneyCRUDService
from busapp.services.models.money import Coin

from busapp.services.vending_machine import (
    VendingMachine, States
)

global vm
vm = VendingMachine()

# ------------------------------------------------------

crud_service_money = MoneyCRUDService(Coin)
router_money = APIRouter(prefix="/money")

async def is_machine_ready():
    if vm.state is States.READY:
        applog.debug("Machine is ready")
        return True
    else:
        applog.warning("Machine is not ready, cannot perform operation.")
        return False

# CommonsDep = Annotated[dict, Depends(is_machine_ready)]
    
# ------------------------------------------------------

@router_money.post("/deposit", response_model=Dict)
async def add_coin(coin: Coin, is_vm_ready: bool = Depends(is_machine_ready)):
    if is_vm_ready:
        return crud_service_money.create(coin).model_dump()
    else:
        return{"error":"Machine not ready."}


@router_money.post("/tresor", response_model=Dict)
async def add_sum_to_tresor(sum:int, is_vm_ready: bool = Depends(is_machine_ready)):
    # TODO: # some method to save to the VM tresor
    # return crud_service_money.create(coin)
    pass


@router_money.get("/sum",response_model=Dict)
async def get_sum(is_vm_ready: bool = Depends(is_machine_ready)):
    """
    Gets the sum of money inserted
    """
    if is_vm_ready:
        return crud_service_money.get_sum()
    else:
        return{"error":"Machine not ready."}
    


@router_money.get("/all",  response_model=List)
async def get_all_coins_inserted( is_vm_ready: bool = Depends(is_machine_ready)):
    """
    Gets the list of all the coins    
    """
    if is_vm_ready:
        return crud_service_money.get_all()
    else:
        return[{"error":"Machine not ready."}]


@router_money.delete("/reset")
async def delete_all(is_vm_ready:bool = Depends(is_machine_ready)):
    """
    This is the reset button, gives back all coins    
    """
    
    if is_vm_ready:
        return crud_service_money.delete_all()                
    else:
        return{"error":"Machine not ready."}
        
