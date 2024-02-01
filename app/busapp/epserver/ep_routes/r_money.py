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
        # applog.warning("Machine is not ready, cannot perform requested operation.")
        return False

async def is_machine_selling():
    if vm.state is States.SELLING:
        applog.debug("Machine is selling")
        return True
    else:
        # applog.warning("Machine is not in state selling, cannot perform operation.")
        return False

async def is_machine_ready_or_selling():
    return True if await is_machine_ready() or await is_machine_selling() else False
       
    

# DepMachineIsReadyOrSelling = Annotated[dict, Depends(is_machine_ready)]
    
# ------------------------------------------------------

@router_money.post("/deposit", response_model=Dict)
async def add_coin(coin: Coin, ready_or_selling: bool = Depends(is_machine_ready_or_selling)):
    if ready_or_selling:
        vm.coin_inserted() #triggers transition READY -> SELLING
        return crud_service_money.create(coin).model_dump()
    else:
        return{"error":"Machine not ready."}


@router_money.post("/tresor", response_model=Dict)
async def add_sum_to_tresor(sum:int, is_desired_state: bool = Depends(is_machine_selling)):
    # TODO: # some method to save to the VM tresor
    # return crud_service_money.create(coin)
    pass


@router_money.get("/sum",response_model=Dict)
async def get_sum(selling: bool = Depends(is_machine_selling)):
    """
    Gets the sum of money inserted
    """
    if selling:
        return crud_service_money.get_sum()
    else:
        return({"error":"Machine is not in state selling, cannot perform operation."})
    


@router_money.get("/all",  response_model=List)
async def get_all_coins_inserted( selling: bool = Depends(is_machine_selling)):
    """
    Gets the list of all the coins    
    """
    if selling:
        return crud_service_money.get_all()
    else:
        return([{"error":"Machine is not in state selling, cannot perform operation."}])


@router_money.delete("/reset")
async def delete_all(selling:bool = Depends(is_machine_selling)):
    """
    This is the reset button, gives back all coins    
    """
    
    if selling:
        vm.press_reset()
        return crud_service_money.delete_all()                
    else:
        return({"error":"Machine is not in state selling, cannot perform operation."})
        
