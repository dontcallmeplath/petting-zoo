"""Module instantiating a water animal"""
from datetime import date
from animals import Animal

class Octopus(Animal):
    """Child Class representing an animal"""
    def __init__(self, name, species, food, chip):
        super().__init__(name, species, food, chip)
        self.swimming = True
        self.date_added = date.today()