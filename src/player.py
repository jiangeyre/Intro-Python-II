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
                output += f"{item.name}\n"
            print(output)
        else:
            print("\nYour inventory is currently empty.")

    def take_item(self, item):
        i = None
        for it in self.current_room.items:
            if it.name == item:
                i = it
        if i is None:
            print('The item you are looking for is not in the room.')   
        else:         
            self.inventory.append(i)
            print(f'{item} is yours now!')
            self.current_room.items.remove(i)
            print(f'{i.name} has been removed from the {self.current_room}.')

    def drop_item(self, item):
        i = None
        for it in self.inventory:
            if it.name == item:
                i = it
        if i is None:
            print('Item is not in inventory.')  
        else:          
            self.inventory.remove(i)
            self.current_room.items.append(i)
            print('{i.item} has been removed! Good day.')