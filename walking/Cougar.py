"""Module instantiating a land animal"""
from datetime import date

class Cougar:
    """Class representing an animal"""
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
madam_milf = Cougar("Madam","North American cougar", "midday")
print(f'{madam_milf.name} the {madam_milf.species} is available to pet during the {madam_milf.shift} shift.')
