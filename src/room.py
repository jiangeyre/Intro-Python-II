# Implement a class to hold room information. This should have name and description attributes.

from player import Player

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"{self.name} \n {self.description}"

    def room_inventory(self):
        if self.items is None:
            print('There are no items in this room.')
        else:
            for item in self.items:
                print(f"There is a {item.name} in this room!")