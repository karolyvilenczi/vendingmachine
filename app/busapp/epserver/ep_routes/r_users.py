from typing import List, Optional

from fastapi import APIRouter

from busapp.apputils.app_logger import applog
from busapp.services.crud_service import CRUDService
from busapp.services.models.user import User, UserResponse

# ------------------------------------------------------

crud_service_user = CRUDService[User](User)
router_users = APIRouter(prefix="/users")

# ------------------------------------------------------


@router_users.post("/", response_model=User)
async def create_user(user: UserResponse):
    return crud_service_user.create(user)

@router_users.get("/", response_model=List[User])
async def get_users():
    return crud_service_user.get_all()

@router_users.get("/detail/{user_id}", response_model=User)
async def get_user(user_id: int):
    return crud_service_user.get(user_id)


@router_users.put("/{user_id}", response_model=User)
async def update_user(user_id: int, updated_user: UserResponse):
    return crud_service_user.update(user_id, updated_user)

@router_users.delete("/{user_id}", response_model=User)
async def delete_user(user_id: int):
    return crud_service_user.delete(user_id)
