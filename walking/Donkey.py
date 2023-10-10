"""Module instantiating a land animal"""
from datetime import date

class Donkey:
    """Class representing an animal"""
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
arsenio = Donkey("Arsenio","regular ol' donkey", "morning")
print(f'{arsenio.name} the {arsenio.species} is available to pet during the {arsenio.shift} shift.')
