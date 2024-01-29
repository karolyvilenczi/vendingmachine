import pytest

from busapp.services.inventory_manager import Inventory, Product
from busapp.apputils.app_logger import applog

# ------------------------------------------------------
@pytest.fixture
def empty_inventory():
    return Inventory()

@pytest.fixture
def inventory_with_products():
    p1 = Product(id=1, productName='Product1', amountAvailable=10, cost=20)
    p2 = Product(id=2, productName='Product2', amountAvailable=5, cost=15)
    inventory = Inventory()
    inventory.add_product(p1)
    inventory.add_product(p2)
    return inventory


def test_inventory_create_empty(empty_inventory):
    assert len(empty_inventory.product_list) == 0


def test_inventory_add_product(empty_inventory):
    product = Product(id=1, productName='Product1', amountAvailable=10, cost=20)
    empty_inventory.add_product(product)
    assert len(empty_inventory.product_list) == 1
    assert empty_inventory.product_list[0] == product


def test_inventory_get_product_by_id(inventory_with_products):
    result = inventory_with_products.get_product_by_id(1)
    assert len(result) == 1
    assert result[0].id == 1


def test_inventory_delete_product_by_id(inventory_with_products):
    inventory_with_products.delete_product_by_id(1)
    assert len(inventory_with_products.product_list) == 1
    assert inventory_with_products.get_product_by_id(1) == []


def test_inventory_update_product_by_id(inventory_with_products):
    inventory_with_products.update_product_by_id(1, 'UpdatedProduct', 15, 25)
    updated_product = inventory_with_products.get_product_by_id(1)[0]
    assert updated_product.productName == 'UpdatedProduct'
    assert updated_product.amountAvailable == 15
    assert updated_product.cost == 25
