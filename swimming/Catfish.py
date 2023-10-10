"""Module instantiating a water animal"""
from datetime import date

class Catfish:
    """Class representing an animal"""
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.shift = shift
icky_thump = Catfish("Icky Thump", "Armored catfish", "midday")
print(f'{icky_thump.name} the {icky_thump.species} is available to pet during the {icky_thump.shift} shift.')
