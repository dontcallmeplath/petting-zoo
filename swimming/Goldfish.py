"""Module instantiating a water animal"""
from datetime import date

class Goldfish:
    """Class representing an animal"""
    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.shift = shift
        self.food = food

    def feed(self):
        """Method to allow for the feeding of animals"""
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'
        
goldilocks = Goldfish("Goldilocks","Ryukin goldfish", "midday", "thawed blood worms")
print(f'{goldilocks.name} the {goldilocks.species} is available to pet during the {goldilocks.shift} shift.')
print(goldilocks.feed())
