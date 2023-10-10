"""Module instantiating a land animal"""
from datetime import date

class Horse:
    """Class representing an animal"""
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
galapagos = Horse("Galapagos","Fusaichi Pegasus horse", "morning")
print(f'{galapagos.name} the {galapagos.species} is available to pet during the {galapagos.shift} shift.')
