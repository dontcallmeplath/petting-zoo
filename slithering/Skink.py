"""Module instantiating a slithering animal"""
from datetime import date

class Skink:
    """Class representing an animal"""
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
stink = Skink("Stink", "Blue-tongued skink")
print(stink)
