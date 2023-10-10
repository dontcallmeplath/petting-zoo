"""Module instantiating a slithering animal"""
from datetime import date

class Alligator:
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

    def __str__(self):
        return f"{self.name} is a/n {self.species}"
    
    def feed(self):
        """Method to allow for the feeding of animals"""
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

alfred = Alligator("Alfred", "American alligator", "afternoon", "fish")
print(alfred)
print(f'{alfred.name} the {alfred.species} is available to pet during the {alfred.shift} shift.')
print(alfred.feed())
