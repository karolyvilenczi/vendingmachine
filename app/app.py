# from busapp.apputils import app_logger
from busapp.epserver import ep_server
from busapp.apputils.app_logger import applog

# ---------------------------------------------------------------
applog.debug(f"Attempting to create a FastAPI instance obj.")
try:
    ep_app = ep_server.init_app()
    
except Exception as e:
    applog.error(f"Could not create FastAPI instance.")
    ep_app = None


# ===============================================================
if __name__ == "__main__":
    applog.info("App started directly")
else:
    applog.info("App started as a module.")
