"""Parent Module instantiating animal types"""
from datetime import date

class Animal:
    "Class for passing attributes to child animals"
    def __init__(self, name, species, food, chip):
        self.name = name
        self.species = species
        self.food = food
        self.__chip_number = chip
        self.date_added = date.today()

    def __str__(self):
        return f"{self.name} is a/n {self.species}"

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, num):
        pass
    