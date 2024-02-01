"""
Module to implement the actual wending machine logic.
"""

import enum
from typing import List

from transitions import Machine

# from busapp.apputils.app_logger import applog
from . import  maintenance

from busapp.apputils.app_logger import applog
# ------------------------------------------------------



class States(enum.Enum):
    READY = "ready"
    MAINTENANCE = "maintenance"
    SELLING = "selling"
    DAMAGED = "damaged"

class VendingMachine(Machine):
    
    # Impl. a singleton pattern
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(VendingMachine, cls).__new__(cls)
        return cls._instance


    def __init__(
            self, 
            # value
            ):

        if not hasattr(self, 'initialized'):            
            # self.value = value
            self.initialized = True        
        
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

        # from READY -> SELLING
        self.add_transition(
            trigger='coin_inserted', 
            source=[States.READY,States.SELLING],
            dest = States.SELLING,
            after=self.check_if_coin_is_valid
        )         

        # from SELLING -> READY
        self.add_transition(
            trigger='move_coins_to_tresor',
            source=States.SELLING,
            dest = States.READY,
            after=self.check_if_coins_saved_to_tresor
        )

        # from SELLING -> READY
        self.add_transition(
            trigger='press_reset',
            source=States.SELLING,
            dest = States.READY,
            after=self.return_all_coins_to_return_bay
        )
        

        
    def machine_initial_setup(
            self, 
            funds=100, # TODO: add coin management,now this is just funds
            inventory = 20 #TODO get this from inventory mgmt
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
        return True if all(maint_mode_activities) else False
        
    
    def check_if_coin_is_valid(self):
        return maintenance.coin_is_valid()
    
    def check_if_coins_saved_to_tresor(self):
        saving_money_to_tresor_activities = [
            maintenance.open_tresor_bay(),
            maintenance.save_coins_to_tresor_bay(),
            maintenance.close_tresor_bay()
        ]
    
        return True if all(saving_money_to_tresor_activities) else False


         
    def get_current_funds(self): 
        return f"Current funds: {self.funds}"


    def  return_all_coins_to_return_bay(self):
        return maintenance.return_all_coins_to_return_bay()


    # def get_current_state(self): 
    #     return self.get_model_state()


# ===============================================================
if __name__ == "__main__":
    applog.info("Started directly")
else:
    applog.info("Started as module")
