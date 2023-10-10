"""Module instantiating a land animal"""
from datetime import date

class Donkey:
    """Class representing an animal"""
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
arsenio = Donkey("Arsenio","regular ol' donkey")
print(arsenio)
