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

    def search(self):
        if len(self.items) > 0:
            output = f"You have discovered: "
            for i in self.items:
                output += f"\n {i.name}"
            print(output)
        else:
            print("Ah, alas! There is nothing in this dreaded room.")

    def get_items(self):
        output = []
        for i in self.items:
            output.append(f"{i.name}".lower())
        return output
    
    def remove_item(self, item):
        for i, o in enumerate(self.items):
            if o.name.lower() == item:
                del self.items[i]
                break

    def add_item(self, item):
        self.items.append(item)

    # def room_inventory(self):
    #     if self.items is None:
    #         print('There are no items in this room.')
    #     else:
    #         for item in self.items:
    #             print(f"There is a {item.name} in this room!")