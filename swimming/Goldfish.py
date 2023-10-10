"""Module instantiating a water animal"""
from datetime import date

class Goldfish:
    """Class representing an animal"""
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.shift = shift
goldilocks = Goldfish("Goldilocks","Ryukin goldfish", "midday")
print(f'{goldilocks.name} the {goldilocks.species} is available to pet during the {goldilocks.shift} shift.')
