from transitions import Machine
import enum

# from busapp.apputils.app_logger import applog
import busapp.services.maintenance as maintenance

class States(enum.Enum):
    READY = 1
    MAINTENANCE = 2
    SELLING = 3
    DAMAGED = 10

class VM(Machine):
    # def say_hello(self): print("hello, new state!")
    # def say_goodbye(self): print("goodbye, old state!")

    def __init__(self):        
        self.set_current_environment()   
        
        Machine.__init__(self, states=States, initial=States.MAINTENANCE)
        
        self.add_transition(
            trigger='turn_key_to_ready', 
            source=States.MAINTENANCE, 
            dest = States.READY, 
            before=self.setup_machine, 
            conditions=self.check_if_no_errors_detected
        )

        # from ANY -> MAINTENANCE
        self.add_transition(
            trigger='turn_key_to_maintenance', 
            source='*', 
            dest = States.MAINTENANCE, 
            after=self.activate_maintenance_mode
        )           

        
    def setup_machine(
            self, 
            funds=100, # TODO: add coin management,now this is just funds
            inventory = 20
        ):
        print(f"Setting {funds=}, {inventory=}")
        self.funds = funds
        self.inventory = inventory
        

    # for conditional state change
    def check_if_no_errors_detected(self):        
        # TODO: Fix this
        init_checklist = [
            maintenance.coin_opener_check(),
            maintenance.spring_rotary_motors_check(),
            maintenance.goods_serving_bay_check(),
            maintenance.lights_are_up_check()
        ]

        # applog.debug(init_checklist)
        print(init_checklist)
        
        
        # return True if all(init_checklist) else False
        # TODO: raise an error log message when False
        # return False
        return True
    
    def activate_maintenance_mode(self):
        # TODO: raise an error log message when any of these fail
        maint_mode_activities = [
            maintenance.open_front_door(),
            maintenance.open_tresor()            
        ]
        # return True if all(init_checklist) else False
        return True


           
    def print_current_funds(self): 
        print(f"Current funds: {self.funds}")
    
         



 # transitions = [
        #     { 'trigger': 'melt', 'source': 'solid', 'dest': 'liquid', 'before': 'set_current_environment', 'conditions': 'is_hot_enough_to_melt'},
        #     { 'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas', 'after': 'disappear' },
        #     { 'trigger': 'burn', 'source': 'solid', 'dest': 'gas', 'conditions':'is_flammable'},
        #     { 'trigger': 'sublimate', 'source': 'solid', 'dest': 'gas' },
        #     { 'trigger': 'ionize', 'source': 'gas', 'dest': 'plasma' }
        # ]