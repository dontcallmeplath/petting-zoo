"""Module instantiating a land animal"""
from datetime import date
from animals import Animal

class Goose(Animal):
    """Child Class representing an animal"""
    def __init__(self, name, species, shift, food, chip):
        super().__init__(name, species, food, chip)
        self.shift = shift
        self.walking = True
        self.date_added = date.today()
        