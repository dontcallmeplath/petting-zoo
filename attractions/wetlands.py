"""Module to create instance of attraction re wetlands"""
class WetLands:
    """Class creating instances of wetlands"""
    def __init__(self, name):
        self.attraction_name = name
        self.description = "boggy, cute, and mysterious"
        self.animals = list()

    def add_animal(self, animal):
        """Method for adding animals to exhibits"""
        return self.animals.append(animal)

    @property # The getter
    def last_critter_added(self):
        """Method for returning last animal in list"""
        return f'{self.animals[-1].name} the {self.animals[-1].species}'
    