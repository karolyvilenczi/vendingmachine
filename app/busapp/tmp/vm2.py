from transitions import Machine
import random

class NarcolepticSuperhero(object):

    states = ['ASLEEP', 'HANGING OUT', 'HUNGRY', 'SWEATY', 'SAVING THE WORLD']

    def __init__(self, name):
        self.name = name

        self.kittens_rescued = 0

        self.machine = Machine(model=self, states=NarcolepticSuperhero.states, initial='ASLEEP')

        # Add some transitions. We could also define these using a static list of
        # dictionaries, as we did with states above, and then pass the list to
        # the Machine initializer as the transitions= argument.

        
        self.machine.add_transition(trigger='wake_up', source='ASLEEP', dest='HANGING OUT')
        self.machine.add_transition(trigger='work_out', source='HANGING OUT', dest='HUNGRY')
        self.machine.add_transition(trigger='eat', source='HUNGRY', dest='HANGING OUT')

        # Superheroes are always on call. ALWAYS. But they're not always
        # dressed in work-appropriate clothing.
        self.machine.add_transition(trigger='distress_call', source='*', dest='SAVING THE WORLD',
                         before='change_into_super_secret_costume')

        self.machine.add_transition('complete_mission', 'SAVING THE WORLD', 'SWEATY',
                         after='update_journal')

        # Sweat is a disorder that can be remedied with water.
        # Unless you've had a particularly long day, in which case... bed time!
        self.machine.add_transition('clean_up', 'SWEATY', 'ASLEEP', conditions=['is_exhausted'])
        self.machine.add_transition('clean_up', 'SWEATY', 'HANGING OUT')

        # Our NarcolepticSuperhero can fall ASLEEP at pretty much any time.
        self.machine.add_transition('nap', '*', 'ASLEEP')

    def update_journal(self):
        """ Dear Diary, today I saved Mr. Whiskers. Again. """
        self.kittens_rescued += 1

    @property
    def is_exhausted(self):
        """ Basically a coin toss. """
        return random.random() < 0.5

    def change_into_super_secret_costume(self):
        print("Beauty, eh?")


bm = NarcolepticSuperhero("Batman")