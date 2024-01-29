"""
Module to implement the actual wending machine logic.
"""

import enum
from typing import List
from pydantic import BaseModel

from transitions import Machine

# from busapp.apputils.app_logger import applog
from . import (
    maintenance,
    inventory_manager as im, 
    money_manager as mm, 
    user_manager as um
)

from busapp.apputils.app_logger import applog
# ------------------------------------------------------


class States(enum.Enum):
    READY = 1
    MAINTENANCE = 2
    SELLING = 3
    DAMAGED = 10

class VendingMachine(Machine):
    def __init__(self):        
        self.machine_initial_setup()   
        
        Machine.__init__(self, states=States, initial=States.MAINTENANCE)
        
        self.add_transition(
            trigger='turn_key_to_ready', 
            source=States.MAINTENANCE, 
            dest = States.READY, 
            before=self.machine_initial_setup, 
            conditions=self.check_if_no_errors_detected
        )

        # from ANY -> MAINTENANCE
        self.add_transition(
            trigger='turn_key_to_maintenance', 
            source='*', 
            dest = States.MAINTENANCE, 
            after=self.activate_maintenance_mode
        )           

        
    def machine_initial_setup(
            self, 
            funds=100, # TODO: add coin management,now this is just funds
            inventory = 20
        ):
        self.funds = funds
        self.inventory = inventory
        applog.success(f"Initial setup: {self.funds=}, {self.inventory=}")
        

    # for conditional state change
    def check_if_no_errors_detected(self):        
        applog.info("Running turn_key_to_ready checks.")
        init_checklist = [
            maintenance.coin_opener_check(),
            maintenance.spring_rotary_motors_check(),
            maintenance.goods_serving_bay_check(),
            maintenance.lights_are_up_check()
        ]
        if all(init_checklist):
            applog.success("All turn_key_to_ready checks passed.")
            return True
        else:
            applog.error("Some checks failed, will not transition to READY state.")
            return False        
        
    
    def activate_maintenance_mode(self):
        # TODO: raise an error log message when any of these fail
        maint_mode_activities = [
            maintenance.open_front_door(),
            maintenance.open_tresor()            
        ]
        # return True if all(init_checklist) else False
        return True


           
    def get_current_funds(self): 
        return f"Current funds: {self.funds}"




        
    
    # def __init__(self):
    #     # TODO:
    #     # Inv is loaded, cannot be empty
    #     # Money is loaded, cannot be empty and should be enough for normal oper
    #     # 
    #     pass

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
