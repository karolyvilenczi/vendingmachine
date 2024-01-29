import pytest

from busapp.services import inventory_manager as im

# ------------------------------------------------------
from busapp.apputils.app_logger import applog


# ------------------------------------------------------
@pytest.mark.asyncio
async def test_create_a_product():
    test_coke = im.Product(id = 1, productName="Coke", amountAvailable=10, cost=10)
    applog.debug(test_coke)
    return True