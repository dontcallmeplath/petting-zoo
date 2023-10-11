"""Module to create instance of attraction re petting zoo"""
class PettingZoo:
    """Class creating instances of petting zoos"""
    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute, fuzzy, and cuddly"
        self.animals = list()

    def add_animal(self, animal):
        """Method for adding animals to exhibits"""
        return self.animals.append(animal)
