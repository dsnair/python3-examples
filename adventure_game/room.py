# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    # instantiate objects
    # allows calling Room.name & Room.description
    def __init__(self, name, description):
        self.name = name
        self.description = description