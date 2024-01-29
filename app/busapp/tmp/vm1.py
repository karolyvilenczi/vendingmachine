from automat import MethodicalMachine

class HeatingElement:
    def __init__(self, init_temp):
        self.temperature = init_temp

    def turn_on(self):
        print("heating")
        self.temperature += 50



    
    

class CoffeeMachine(object):
    _machine = MethodicalMachine()
    _heating_element = HeatingElement(init_temp = 20)

    @_machine.state(initial=True)
    def dont_have_beans(self):
        "In this state, you don't have any beans."

    @_machine.state()
    def have_beans(self):
        "In this state, you have some beans."

    @_machine.input()
    def put_in_beans(self, beans):
        "The user put in some beans."

    @_machine.output()
    def _save_beans(self, beans):
        "The beans are now in the machine; save them."
        self._beans = beans

    @_machine.input()
    def brew_button(self):
        "The user pressed the 'brew' button."

    @_machine.output()
    def _heat_the_heating_element(self):
        "Heat up the heating element, which should cause coffee to happen."
        self._heating_element.turn_on()

    @_machine.output()
    def _describe_coffee(self):
        return "A cup of coffee made with {}.".format(self._beans)

    dont_have_beans.upon(
        put_in_beans, 
        enter=have_beans, 
        outputs=[_save_beans]
    )
    have_beans.upon(
        brew_button, 
        enter=dont_have_beans,
        outputs=[_heat_the_heating_element, _describe_coffee], 
        collector=lambda iterable: list(iterable)[-1]
    )


coffee_machine = CoffeeMachine()
coffee_machine.put_in_beans("real good beans")
print(coffee_machine.brew_button())

print(coffee_machine)