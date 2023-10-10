"""Module instantiating a slithering animal"""
from datetime import date

class Gecko:
    """Class representing an animal"""
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.shift = shift
martin = Gecko("Martin", "Crested gecko", "morning")
print(f'{martin.name} the {martin.species} is available to pet during the {martin.shift} shift.')
