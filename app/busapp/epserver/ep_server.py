from typing import Optional
from fastapi import FastAPI
# fastapi cors support
from fastapi.middleware.cors import CORSMiddleware
# to integrate with prometheus monitoring
from starlette_prometheus import metrics, PrometheusMiddleware

from busapp.epserver.ep_routes import (
    r_users,
    r_products, 
    r_vending_machine
)

from busapp.apputils.app_logger import applog

# --------------------------------------------------------------
def init_app():
    """Initialize the core application."""
    # TODO: add try-c parts to handle exceptions
    app = FastAPI(
        # TODO: move to ext. config
        title="Wending machine app",  # FIX
        description="Part of the interview process for Oliver Wynman",  # FIX
        version="0.0.1",
        terms_of_service="http://example.com/terms/",  # FIX
        contact={
            "name": "Charles Vilenczi",
            "url": "my url",  # FIX
            "email": "mail@mail.com",  # FIX
        },
        license_info={
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
    )
    # TODO: make conditional from env
    applog.debug(f"FastAPI main instance created: {app}")

    # adding prometheus
    app.add_middleware(PrometheusMiddleware)
    app.add_route("/metrics", metrics)

    # adding cors
    # TODO: turn on / off by config
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # TODO: add all the other routes

    app.include_router(r_users.router_users)
    app.include_router(r_products.router_products)
    app.include_router(r_vending_machine.router_vm)

    return app
    # TODO: test in app created from multiple settings


# ===============================================================
if __name__ == "__main__":
    applog.info(f"ep_server started directly")
else:
    applog.info(f"ep_server started as a module")
