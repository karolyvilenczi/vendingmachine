"""
Module to implement the actual wending machine logic.
"""

from pydantic import BaseModel
from typing import List

from busapp.apputils import app_logger

import inventory_manager as im
import money_manager as mm
import user_manager as um

# ------------------------------------------------------
applog = app_logger.make_logger("SRV:WENDING MACHINE")


class VendingMachine:
    def __init__(self):
        # TODO:
        # Inv is loaded, cannot be empty
        # Money is loaded, cannot be empty and should be enough for normal oper
        # 
        pass

    # what states can be for the machine?
    # BASE STATE - ready to accept coins &

    # what states can be for the items?
    # out on display: 'ONDISPLAY'
    # out on display and enough money is given: 'READYTOSELL'
    
    # - set all items on display as ONDISPLAY

    # - accepting coins - someone wants to buy smt
    # -- show (use some stack based model to keep track of the coins) the current sum 
    # --- light up (also set to READYTOSELL) those items that are less than eq. the total entered
    
    # the user picks the item
    # - set all other back to 'ONDISPLAY'
    # - add the sum I keep to my money:
    # -- incrase my sales account by that sum # TODO: add accounting & reporting to money_manager
    # -- add the coins (according to their type to the stack)
    # - give back the difference
    # - turn the spring
    # - go back to BASE state



# ===============================================================
if __name__ == "__main__":
    applog.info("Started directly")
else:
    applog.info("Started as module")
