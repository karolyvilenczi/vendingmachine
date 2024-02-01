from typing import List, Optional, Dict

from fastapi import APIRouter

from busapp.apputils.app_logger import applog
from busapp.services.crud_service import CRUDService, MoneyCRUDService
from busapp.services.models.money import Coin

# ------------------------------------------------------

crud_service_money = MoneyCRUDService(Coin)
router_money = APIRouter(prefix="/money")

# ------------------------------------------------------

@router_money.post("/deposit", response_model=Coin)
async def add_coin(coin: Coin):
    return crud_service_money.create(coin)


@router_money.post("/tresor", response_model=Dict)
async def add_sum_to_tresor(sum:int):
    # TODO: # some method to save to the VM tresor
    # return crud_service_money.create(coin)
    pass


@router_money.get("/sum",response_model=Dict)
async def get_sum():
    """
    Gets the sum of money inserted
    """
    return crud_service_money.get_sum()


@router_money.get("/all",  response_model=List)
async def get_all_coins_inserted():
    """
    Gets the list of all the coins
    """
    return crud_service_money.get_all()


@router_money.delete("/reset")
async def delete_all():
    """
    This is the reset button, gives back all coins
    """
    return crud_service_money.delete_all()
