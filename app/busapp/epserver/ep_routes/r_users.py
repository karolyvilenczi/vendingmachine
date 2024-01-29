from fastapi import APIRouter

from busapp.apputils.app_logger import applog

from busapp.services.crud_service import CRUDService
from busapp.services.models.user import User, UserWoId
from typing import List

# ------------------------------------------------------

cs_user = CRUDService[User](User)
router_users = APIRouter()

# ------------------------------------------------------

@router_users.post("/users/", response_model=User)
async def create_user(user: UserWoId):
    return cs_user.create(user)

@router_users.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    return cs_user.get(user_id)

@router_users.get("/users/", response_model=List[UserWoId])
async def read_users():
    return cs_user.get_all()

@router_users.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, updated_user: User):
    return cs_user.update(user_id, updated_user)

@router_users.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    return cs_user.delete(user_id)
