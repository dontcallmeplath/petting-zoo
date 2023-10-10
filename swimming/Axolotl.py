"""Module instantiating a water animal"""
from datetime import date

class Axolotl:
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

    def __str__(self):
        return f"{self.name} is a/n {self.species}"

    def feed(self):
        """Method to allow for the feeding of animals"""
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'
        
marisol = Axolotl("Marisol","Mosaic axolotl", "morning", "nightcrawlers")
print(marisol)
print(f'{marisol.name} the {marisol.species} is available to view during the {marisol.shift} shift.')
print(marisol.feed())
