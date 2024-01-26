import os
import sys
import inspect

import pytest

from busapp.apputils import app_logger
from busapp.services import user_management

# ------------------------------------------------------
applog = app_logger.make_logger("TEST USER MANAGEMENT")


# ------------------------------------------------------
@pytest.mark.asyncio
async def test_get_user_list():
    applog.info("Running test_user_list")  # not needed
    result = await user_management.get_user_list()
    assert result == {
        "users": ["a", "b", "c"]
    }, "Expected resp: {'users': ['a', 'b', 'c']}"
