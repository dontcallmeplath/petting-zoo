"""Module to create instance of attraction re petting zoo"""
from .attraction import Attraction
from movements import Walking

class PettingZoo(Attraction):
    """Class creating instances of petting zoos"""
    def __init__(self, name, description):
        super().__init__(name, description)
        
                
    def add_animal(self, animal):
        """Method for adding animals to exhibits"""
        return self.animals.append(animal)
    
    @property # The getter
    def last_critter_added(self):
        """Method for returning last animal in list"""
        return f'{self.animals[-1].name} the {self.animals[-1].species}'
    
    # Number 1: Duck typing check
    def add_animal_pythonic(self, animal):
        try:
            if animal.walking:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f'{animal} doesn\'t like to be petted, so please do not put it in the {self.attraction_name} attraction.')

    # Number 2: Actual typing check
    def add_animal_type_check(self, animal):
        if isinstance(animal, Walking):
            self.animals.append(animal)
            print(f"{animal} now lives in {self.attraction_name}")
        else:
            print(f'{animal} doesn\'t like to be petted, so please do not try to put it in the {self.attraction_name} attraction.')
    