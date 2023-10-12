"""Module instantiating a land animal"""
from datetime import date
from animals import Animal

class Llama(Animal):
    """Child Class representing an animal"""
    def __init__(self, name, species, shift, food, chip):
        super().__init__(name, species, food, chip)
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        return f'On {date.today().strftime("%m/%d/%Y")} we sang "RockyTop" to {self.name} so she would eat her {self.food}'