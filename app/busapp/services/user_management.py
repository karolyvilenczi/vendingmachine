"""
Module to ...
"""

from busapp.apputils import app_logger

# ------------------------------------------------------
applog = app_logger.make_logger("USER MANAGEMENT")


# ------------------------------------------------------
async def get_user_list():
    applog.debug(f"Getting user list.")
    return {"users": ["a", "b", "c"]}


# ===============================================================
if __name__ == "__main__":
    applog.info("Started directly")
else:
    applog.info("Started as module")