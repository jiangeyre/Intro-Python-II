# Write a class to hold player information, e.g. what room they are in currently.

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return (f"{self.name} is in {self.current_room}.")

    def travel(self, direction):
        if hasattr(self.current_room, f'{direction}_to'):
            current_room = getattr(self.current_room, f'{direction}_to')
            self.current_room = current_room
            print(f"You entered the {current_room}.")
        else:
            print("Wrong way!!!")

    def add_item(self, item):
        i = None
        for x in self.current_room.items:
            if x.name == item:
                i = x
            if i is None:
                print('This item is not in the current room.')
            else:
                self.inventory.append(i)
                print(f"You have obtained {item}!")