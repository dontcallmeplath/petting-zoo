"""Module instantiating a land animal"""
from datetime import date

class Horse:
    """Class representing an animal"""
    def __init__(self, name, species, shift, food, chip):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
        self.chip_number = chip

    def __str__(self):
        return f"{self.name} is a/n {self.species}"

    def feed(self):
        """Method to allow for the feeding of animals"""
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'
    
    @property
    def chip_number(self):
        return self.__chip_number
    
    @chip_number.setter
    def chip_number(self, number):
        pass

    @property # The getter
    def chip_number(self):
        try:
            return self.__chip_number # Note there are 2 underscores here
        except AttributeError:
            return 0

    @chip_number.setter # The setter
    def chip_number(self, new_chip_number):
        if type(new_chip_number) is int:
            self.__chip_number = new_chip_number
        else:
            raise TypeError('Please provide an integer value for the chip number')