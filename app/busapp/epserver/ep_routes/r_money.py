from typing import List, Optional, Dict

from fastapi import APIRouter

from busapp.apputils.app_logger import applog
from busapp.services.crud_service import CRUDService, MoneyCRUDService
from busapp.services.models.money import Coin

# ------------------------------------------------------

# crud_service_user = CRUDService[User](User)
crud_service_money = MoneyCRUDService(Coin)
router_money = APIRouter(prefix="/money")

# ------------------------------------------------------

@router_money.post("/", response_model=Coin)
async def add_coin(coin: Coin):
    return crud_service_money.create(coin)

# Gets the sum of money inserted
@router_money.get("/", response_model=Dict)
async def get_sum():
    return crud_service_money.get_sum()

# Gets the list of all the coins
@router_money.get("/all", response_model=Dict)
async def get_all_coins_inserted():
    return crud_service_money.get_all()

# this is the reset button, gives back all coins
@router_money.delete("/reset")
async def delete_user(user_id: int):
    return crud_service_money.delete()
