from typing import List

from fastapi import APIRouter

from busapp.apputils.app_logger import applog
from busapp.services.crud_service import CRUDService
from busapp.services.models.user import User, UserWoId

# ------------------------------------------------------

crud_service_user = CRUDService[User](User)
router_users = APIRouter()

# ------------------------------------------------------

@router_users.post("/users/", response_model=User)
async def create_user(userwoid: UserWoId):
    return crud_service_user.create(userwoid)

@router_users.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    return crud_service_user.get(user_id)

@router_users.get("/users/", response_model=List[User])
async def get_users():
    return crud_service_user.get_all()

@router_users.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, updated_user: UserWoId):
    return crud_service_user.update(user_id, updated_user)

@router_users.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    return crud_service_user.delete(user_id)
