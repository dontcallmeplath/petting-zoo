"""Module instantiating a water animal"""
from datetime import date

class Catfish:
    """Class representing an animal"""
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
icky_thump = Catfish("Icky Thump", "Armored catfish")
print(icky_thump)
