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

# tests for the cost field
@pytest.mark.asyncio
@pytest.mark.xfail(reason = "Trying to create a product with cost not a multiple of 5 should fail ")
async def test_product_cost_must_be_a_multiple_of_5():    
    test_coke = im.Product(id = 1, productName="Coke", amountAvailable=10, cost=3)
      

@pytest.mark.asyncio
@pytest.mark.xfail(reason = "Trying to create a product with cost less than 0 should fail.")
async def test_product_cost_must_be_greater_than_0():    
    test_coke = im.Product(id = 1, productName="Coke", amountAvailable=10, cost=-1)

@pytest.mark.asyncio
@pytest.mark.xfail(reason = "Trying to create a product with cost more than 100000 should fail.")
async def test_product_cost_must_be_less_than_10000():    
    test_coke = im.Product(id = 1, productName="Coke", amountAvailable=10, cost=1000000)

# tests for the productName field
@pytest.mark.asyncio
@pytest.mark.xfail(reason = "Trying to create a product with empty string should fail.")
async def test_product_name_cannot_be_an_empty_string():
    test_coke = im.Product(id = 1, productName="", amountAvailable=10, cost=1000000)


@pytest.mark.asyncio
@pytest.mark.xfail(reason = "Trying to create a product with a name longer than 128 chars should fail.")
async def test_product_name_with_string_longer_than_128_chars():

    long_pepsi_name = "pepsi" * 32  # 4 characters in "pepsi", so 32 * 4 = 128
    test_name = long_pepsi_name + "i"
    test_coke = im.Product(id = 1, productName=test_name, amountAvailable=10, cost=10)

# tests for the amountAvailable field
@pytest.mark.asyncio
@pytest.mark.xfail(reason = "Trying to create a product with amountAvailable less than 0 should fail.")
async def test_product_amount_cannot_be_negative():
    test_coke = im.Product(id = 1, productName="", amountAvailable=-1, cost=100)

@pytest.mark.asyncio
@pytest.mark.xfail(reason = "Trying to create a product with amountAvailable more than the machine capacity.")
async def test_product_amount_cannot_be_more_than_machine_capacity():
    machine_capacity_for_product_amount = 100 # TODO: move to config
    test_coke = im.Product(id = 1, productName="", amountAvailable=machine_capacity_for_product_amount+1, cost=100)


    

