"""Module instantiating a slithering animal"""
from datetime import date

class Gecko:
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

martin = Gecko("Martin", "Crested gecko", "morning", "crickets")
print(f'{martin.name} the {martin.species} is available to pet during the {martin.shift} shift.')
print(martin.feed())
