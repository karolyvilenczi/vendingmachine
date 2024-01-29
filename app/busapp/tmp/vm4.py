from transitions import Machine

class Matter(Machine):
    def say_hello(self): print("hello, new state!")
    def say_goodbye(self): print("goodbye, old state!")

    def __init__(self):
        self.melting_temp = 100
        self.set_current_environment()   

        states=['solid', 'liquid', 'gas', 'plasma']
        
        Machine.__init__(self, states=states, initial='solid')
        self.add_transition(trigger='melt', source='solid', dest = 'liquid', before=self.set_current_environment, conditions=self.is_hot_enough_to_melt)

        # transitions = [
        #     { 'trigger': 'melt', 'source': 'solid', 'dest': 'liquid', 'before': 'set_current_environment', 'conditions': 'is_hot_enough_to_melt'},
        #     { 'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas', 'after': 'disappear' },
        #     { 'trigger': 'burn', 'source': 'solid', 'dest': 'gas', 'conditions':'is_flammable'},
        #     { 'trigger': 'sublimate', 'source': 'solid', 'dest': 'gas' },
        #     { 'trigger': 'ionize', 'source': 'gas', 'dest': 'plasma' }
        # ]
        

        # Machine.__init__(self, states=states, transitions=transitions, initial='solid')


    
    def set_current_environment(self, temp=0, pressure=101.325):
        print(f"Setting {temp=} & {pressure=}")                
        self.temp = temp
        self.pressure = pressure

    # for conditional state change
    def is_hot_enough_to_melt(self, temp):        
        return True if temp > self.melting_temp else False
        
    def is_flammable(self): 
        return True
    
    def is_really_hot(self): 
        return True
    
    # before / after callbacks
    # def make_hissing_noises(self): print("HISSSSSSSSSSSSSSSS")
    def disappear(self): print("where'd all the liquid go?")

    
    def print_temperature(self): 
        print("Current temperature is %d degrees celsius." % self.temp)
    
    def print_pressure(self): 
        print("Current pressure is %.2f kPa." % self.pressure)

        
