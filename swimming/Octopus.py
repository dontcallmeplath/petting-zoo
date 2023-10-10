"""Module instantiating a water animal"""
from datetime import date

class Octopus:
    """Class representing an animal"""
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.shift = shift
ronald = Octopus("Ronald","Umbrella octopus", "afternoon")
print(f'{ronald.name} the {ronald.species} is available to pet during the {ronald.shift} shift.')
