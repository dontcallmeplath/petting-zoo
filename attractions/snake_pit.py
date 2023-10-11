"""Module to create instance of attraction re snake pit"""
class SnakePit:
    """Class creating instances of snake pits"""
    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute bbs w their bellies on the ground :)"
        self.animals = list()

    def add_animal(self, animal):
        """Method for adding animals to exhibits"""
        return self.animals.append(animal)
