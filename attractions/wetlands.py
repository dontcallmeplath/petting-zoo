"""Module to create instance of attraction re wetlands"""
from .attraction import Attraction

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
    