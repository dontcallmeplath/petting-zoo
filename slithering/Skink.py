"""Module instantiating a slithering animal"""
from datetime import date

class Skink:
    """Class representing an animal"""
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.shift = shift
stink = Skink("Stink", "Blue-tongued skink", "morning")
print(f'{stink.name} the {stink.species} is available to pet during the {stink.shift} shift.')
