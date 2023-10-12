"""Module instantiating a water animal"""
from datetime import date
from animals import Animal

class Axolotl(Animal):
    """Child Class representing an animal"""
    def __init__(self, name, species, food, chip):
        super().__init__(name, species, food, chip)
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")} using only my left hand'