"""Module instantiating a slithering animal"""
from datetime import date

class Hognose:
    """Class representing an animal"""
    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.shift = shift
        self.food = food

    def feed(self):
        """Method to allow for the feeding of animals"""
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'
        
baby_cakes = Hognose("Baby Cakes", "Southern Hognose snake", "midday", "a feeder mouse")
print(f'{baby_cakes.name} the {baby_cakes.species} is available to pet during the {baby_cakes.shift} shift.')
print(baby_cakes.feed())