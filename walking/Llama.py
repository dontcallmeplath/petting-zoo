"""Module instantiating a land animal"""
from datetime import date
class Llama:
    """Class representing an animal"""
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
miss_fuzz = Llama("Miss Fuzz","domestic llama")
# attr = vars(miss_fuzz)
# print(attr)
print(miss_fuzz)
