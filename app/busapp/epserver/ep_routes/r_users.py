from typing import List, Optional

from fastapi import APIRouter, Depends

from busapp.apputils.app_logger import applog
from busapp.services.crud_service import UserCRUDService
from busapp.services.models.user import User


from busapp.services.vending_machine import (
    VendingMachine, States
)
# ------------------------------------------------------

global vm
vm = VendingMachine()

async def is_machine_in_maintenance():
    if vm.state is States.MAINTENANCE:
        applog.debug("Machine is in maintennance")
        return True
    else:
        # applog.warning("Machine is not ready, cannot perform requested operation.")
        return False


# ------------------------------------------------------

# crud_service_user = CRUDService[User](User)
crud_service_user = UserCRUDService(User)
router_users = APIRouter(prefix="/users")

# ------------------------------------------------------


@router_users.post("/", response_model=Optional[User])
async def create_user(user: User, in_maintenance: bool = Depends(is_machine_in_maintenance)):
    if in_maintenance:        
        return crud_service_user.create(user)
    else:
        return{"error":"User operations can only be performed in maintenance mode."}


@router_users.get("/", response_model=Optional[List[User]])
async def get_users( in_maintenance: bool = Depends(is_machine_in_maintenance)):
    if in_maintenance:
        return crud_service_user.get_all()
    else:
        return{"error":"User operations can only be performed in maintenance mode."}


@router_users.get("/detail/{user_id}", response_model=Optional[User])
async def get_user(user_id: int,  in_maintenance: bool = Depends(is_machine_in_maintenance)):
    if in_maintenance:
        return crud_service_user.get(user_id)
    else:
        return{"error":"User operations can only be performed in maintenance mode."}



@router_users.put("/{user_id}", response_model=Optional[User])
async def update_user(user_id: int, updated_user: User,  in_maintenance: bool = Depends(is_machine_in_maintenance)):
    if in_maintenance:
        return{"error":"User operations can only be performed in maintenance mode."}
    else:
        return crud_service_user.update(user_id, updated_user)



@router_users.delete("/{user_id}", response_model=Optional[User])
async def delete_user(user_id: int,  in_maintenance: bool = Depends(is_machine_in_maintenance)):
    if in_maintenance:
        return crud_service_user.delete(user_id)
    else:
        return{"error":"User operations can only be performed in maintenance mode."}
    

@router_users.post("/save")
async def save_users_to_machine(in_maintenance: bool = Depends(is_machine_in_maintenance)):
    if in_maintenance:        
        current_users =  crud_service_user.get_all()
        vm.users = current_users
    else:
        return{"error":"User operations can only be performed in maintenance mode."}

