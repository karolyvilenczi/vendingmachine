import os
import sys
import inspect

import pytest

# from busapp.apputils import app_logger
from busapp.services import vending_machine as vm

# ------------------------------------------------------
from busapp.apputils.app_logger import applog


@pytest.fixture(scope="session")
def fixt_wm():
    test_vm = vm.VendingMachine()
    applog.debug(f"{test_vm} fixt created for test session.")
    yield test_vm

    applog.debug(f"deleting {test_vm} after test session.")
    del test_vm


# def test_vm_is_empty_at_beginning(fixt_wm):
#     assert fixt_wm.items == []


# def test_items_length_incr_by_1_after_adding_an_item_to_the_vm(fixt_wm):
#     len_before = fixt_wm.get_items_length()

#     apple = Item(id=1, name="apple", price=10)
#     fixt_wm.add_item(apple)
#     len_after = fixt_wm.get_items_length()

#     assert (len_after - len_before) == 1


# ------------------------------------------------------
# @pytest.mark.asyncio
# async def test_get_items():
#     result = await wending_machine.get_items()
#     assert result == {"items": ["a", "b", "c"]}
