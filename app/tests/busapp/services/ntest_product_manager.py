import pytest

from busapp.services.inventory_manager import Product

# ------------------------------------------------------
from busapp.apputils.app_logger import applog


# ------------------------------------------------------

def test_product_object_gets_created():
    try:
        test_coke = Product(id = 1, productName="Coke", amountAvailable=10, cost=10)
    except ValueError as ve:
        applog.error(f"Could not create product: {ve=}")
    except Exception as e:
        applog.error(f"Could not create product (other exc): {e=}")

    test_code_dict = {'id': 1, 'productName': 'Coke', 'amountAvailable': 10, 'cost': 10.0}

    assert test_coke.__dict__ == test_code_dict, "OK"

# tests for the cost field
# by checking if raises ValueError
def test_product_cost_must_be_a_multiple_of_5_test_raising_exception():
    with pytest.raises(ValueError, match="Product cost must be a multiple of 5."):
        Product(id=1, productName='ProductWithCostNotMultof5', amountAvailable=10, cost=17)

# or with with xfail 
# @pytest.mark.xfail(reason = "Trying to create a product with cost not a multiple of 5 should fail ")
# def test_product_cost_must_be_a_multiple_of_5_xfail():    
#     test_coke = Product(id = 1, productName="Coke", amountAvailable=10, cost=3)


def test_product_cost_must_be_greater_than_0():    
    with pytest.raises(ValueError, match= "Product cost must be greater than 0."):
        Product(id = 1, productName="Coke", amountAvailable=10, cost=-5)


def test_product_cost_must_be_less_than_10000():    
    with pytest.raises(ValueError, match= "Product cost must be less than greater than 100000."):
        Product(id = 1, productName="Coke", amountAvailable=10, cost=1000000)

def test_product_name_cannot_be_an_empty_string():
    with pytest.raises(ValueError, match= "productName must not be an empty string."):
        Product(id = 1, productName="", amountAvailable=10, cost=1000000)

def test_product_name_with_string_longer_than_128_chars():
    with pytest.raises(ValueError, match="productName must not be longer than 128 characters."):
        long_pepsi_name = "pepsi" * 32  # 4 characters in "pepsi", so 32 * 4 = 128
        test_name = long_pepsi_name + "i"
        Product(id = 1, productName=test_name, amountAvailable=10, cost=10)

# tests for the amountAvailable field
def test_product_amount_cannot_be_negative():
    with pytest.raises(ValueError, match="amountAvailable cannot be negative."):
        Product(id = 1, productName="", amountAvailable=-1, cost=100)

def test_product_amount_cannot_be_more_than_machine_capacity():
    machine_capacity_for_product_amount = 100 # TODO: move to config
    
    with pytest.raises(ValueError, match=f"amountAvailable cannot be more than the machine capacity of {machine_capacity_for_product_amount}"):
        Product(id = 1, productName="", amountAvailable=machine_capacity_for_product_amount+1, cost=100)
