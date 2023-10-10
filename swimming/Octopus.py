"""Module instantiating a water animal"""
from datetime import date

class Octopus:
    """Class representing an animal"""
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
ronald = Octopus("Ronald","Umbrella octopus")
print(ronald)
