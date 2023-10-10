"""Module instantiating a land animal"""
from datetime import date

class Horse:
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
    
fusaichi_pegasus = Horse("Fusaichi Pegasus","American Thoroughbred horse", "morning", "timothy and oat hay")
print(f'{fusaichi_pegasus.name} the {fusaichi_pegasus.species} is available to pet during the {fusaichi_pegasus.shift} shift.')
print(fusaichi_pegasus.feed())
