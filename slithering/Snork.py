"""Module instantiating a slithering animal"""
from datetime import date

class Snork:
    """Class representing an animal"""
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.shift = shift
squish_pls = Snork("Squish", "Ball python", "afternoon")
print(f'{squish_pls.name} the {squish_pls.species} is available to pet during the {squish_pls.shift} shift.')
