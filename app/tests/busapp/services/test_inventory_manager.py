import pytest

from busapp.services import inventory_manager as im

# ------------------------------------------------------
from busapp.apputils.app_logger import applog


# ------------------------------------------------------
@pytest.mark.asyncio
async def test_product_object_gets_created():
    try:
        test_coke = im.Product(id = 1, productName="Coke", amountAvailable=10, cost=10)
    except ValueError as ve:
        applog.error(f"Could not create product: {ve=}")
    except Exception as e:
        applog.error(f"Could not create product (other exc): {e=}")

    test_code_dict = {'id': 1, 'productName': 'Coke', 'amountAvailable': 10, 'cost': 10.0}

    assert test_coke.__dict__ == test_code_dict, "OK"

@pytest.mark.asyncio
@pytest.mark.xfail(reason = "Trying to create a product with cost not a multiple of 5 should fail ")
async def test_create_product_cost_is_not_a_multiple_of_five():    
    try:
        test_coke = im.Product(id = 1, productName="Coke", amountAvailable=10, cost=3)
    except ValueError as ve:
        # applog.error(f"Could not create product: {ve=}")
        pass
    except Exception as e:
        # applog.error(f"Could not create product (other exc): {e=}")
        pass
      