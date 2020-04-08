# Implement a class to hold room information. This should have name and description attributes.

from player import Player

class Room:
    def __init__(self, name, description, items=[], n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def __str__(self):
        return f"{self.name} \n {self.description}"

    def room_inventory(self):
        if self.items is None:
            print('There are no items in this room.')
        else:
            for item in self.items:
                print(f"There is a {item.name} in this room!")