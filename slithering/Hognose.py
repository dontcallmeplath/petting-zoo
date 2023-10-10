"""Module instantiating a slithering animal"""
from datetime import date

class Hognose:
    """Class representing an animal"""
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.shift = shift
baby_cakes = Hognose("Baby Cakes", "Southern Hognose snake", "midday")
print(f'{baby_cakes.name} the {baby_cakes.species} is available to pet during the {baby_cakes.shift} shift.')
