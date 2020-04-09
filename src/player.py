# Write a class to hold player information, e.g. what room they are in currently.

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return (f"{self.name} is in {self.current_room}.")

    def check_inventory(self):
        if len(self.inventory) > 0:
            output = f"\nInventory:\n"
            for item in self.inventory:
                output += f"{item.name}"
            print(output)
        else:
            print("\nYour inventory is currently empty.")

    def take_item(self, item):
        self.inventory.append(item)
        print(f"\nYou take the {item.name}") 

    def drop_item(self, item):
        self.inventory.remove(item)
        print(f"\nYou drop the {item.name}") 


    # def add_item(self, item):
    #     i = None
    #     for x in self.current_room.items:
    #         if x.name == item:
    #             i = x
    #         if i is None:
    #             print('This item is not in the current room.')
    #         else:
    #             self.inventory.append(i)
    #             print(f"You have obtained {item}!")