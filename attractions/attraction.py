"""Module instantiating an exhibit attraction"""
class Attraction:
    "Class creating different exhibits"
    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __srt__(self):
        return f'{self.attraction_name} ({len(self)} animals)'

    def __len__(self):
        return len(self.animals)
