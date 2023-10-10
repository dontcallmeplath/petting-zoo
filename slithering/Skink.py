"""Module instantiating a slithering animal"""
from datetime import date

class Skink:
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
        
stink = Skink("Stink", "Blue-tongued skink", "morning", "leafy greens")
print(f'{stink.name} the {stink.species} is available to pet during the {stink.shift} shift.')
print(stink.feed())