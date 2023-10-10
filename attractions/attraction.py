"""Module instantiating an exhibit attraction"""
class Attraction:
    "Class creating different exhibits"
    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = []
