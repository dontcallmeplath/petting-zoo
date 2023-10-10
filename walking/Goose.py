"""Module instantiating a land animal"""
from datetime import date

class Goose:
    """Class representing an animal"""
    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food 

    def feed(self):
        """Method to allow for the feeding of animals"""
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'
        
sir_honk = Goose("Sir Honk", "common goose", "afternoon", "orchard and timothy hay")
print(f'{sir_honk.name} the {sir_honk.species} is available to pet during the {sir_honk.shift} shift.')
print(sir_honk.feed())
