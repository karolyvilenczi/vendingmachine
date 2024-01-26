# system imports

# third party imports
from fastapi import APIRouter

# local imports (using absolute path notation)
# logger obj
from busapp.apputils import app_logger
applog = app_logger.make_logger("ROUTE USERS")

# from app.busapp.services import user_manager
from busapp.services import user_manager as um


# ------------------------------------------------------
router_users = APIRouter()


# ------------------------------------------------------
@router_users.get("/users")
async def fetch_users():
    applog.debug("Fetching users")
    result = await um.get_user_list()
    return result
