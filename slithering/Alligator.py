"""Module instantiating a slithering animal"""
from datetime import date

class Alligator:
    """Class representing an animal"""
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.shift = shift
alfred = Alligator("Alfred", "American alligator", "afternoon")
print(f'{alfred.name} the {alfred.species} is available to pet during the {alfred.shift} shift.')
