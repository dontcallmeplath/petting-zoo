"""Module instantiating a land animal"""
from datetime import date
from animals import Animal
from movements import Walking, Swimming

class Goose(Animal, Walking, Swimming):
    """Child Class representing an animal"""
    def __init__(self, name, species, shift, food, chip):
        super().__init__(name, species, food, chip)
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

    def honk(self):
        """Method to print sound animal makes"""
        print("The goose honks. A lot.")

    def run(self):
        print(f'{self} waddles')

    def __str__(self):
        return f'{self.name} the Goose'
        