"""Module instantiating a water animal"""
from datetime import date

class Axolotl:
    """Class representing an animal"""
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.shift = shift
marisol = Axolotl("Marisol","Mosaic axolotl", "morning")
print(f'{marisol.name} the {marisol.species} is available to pet during the {marisol.shift} shift.')
