from fastapi import APIRouter

from busapp.apputils.app_logger import applog

from busapp.services import user_manager as um

# ------------------------------------------------------
router_users = APIRouter()

# ------------------------------------------------------
@router_users.get("/users")
async def fetch_users():
    applog.debug("Fetching users")
    result = await um.get_user_list()
    return result
