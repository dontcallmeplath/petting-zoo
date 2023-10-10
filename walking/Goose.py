"""Module instantiating a land animal"""
from datetime import date

class Goose:
    """Class representing an animal"""
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
sir_honk = Goose("Sir Honk", "common goose", "afternoon")
print(f'{sir_honk.name} the {sir_honk.species} is available to pet during the {sir_honk.shift} shift.')
