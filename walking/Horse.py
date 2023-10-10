"""Module instantiating a land animal"""
from datetime import date

class Horse:
    """Class representing an animal"""
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
galapagos = Horse("Galapagos","Fusaichi Pegasus horse")
print(galapagos)
