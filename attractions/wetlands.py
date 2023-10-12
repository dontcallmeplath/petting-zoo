"""Module to create instance of attraction re wetlands"""
from .attraction import Attraction
from movements import Swimming

class WetLands(Attraction):
    """Class creating instances of wetlands"""
    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal(self, animal):
        """Method for adding animals to exhibits"""
        return self.animals.append(animal)

    @property # The getter
    def last_critter_added(self):
        """Method for returning last animal in list"""
        return f'{self.animals[-1].name} the {self.animals[-1].species}'
    
    def add_animal_pythonic(self, animal):
        try:
            if animal.swimming:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f'{animal} doesn\'t like to be petted, so please do not put it in the {self.attraction_name} attraction.')

    # Number 2: Actual typing check
    def add_animal_type_check(self, animal):
        if isinstance(animal, Swimming):
            self.animals.append(animal)
            print(f"{animal} now lives in {self.attraction_name}")
        else:
            print(f'{animal} doesn\'t like to be petted, so please do not try to put it in the {self.attraction_name} attraction.')
    