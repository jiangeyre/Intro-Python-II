from room import Room
from player import Player
from item import Item

# Declare the items

item = {
    'key': Item('Key', 'It is very veryshiny! What will it open up?'),
    'note': Item('Note', 'There is a terribly written poem on here.'),
    'can': Item('Can', 'Why!? It is a can of SPAM!'),
    'sani': Item('Sani', 'Gotta make sure that your hands are clean.'),
    'tp': Item('TP', 'Do not forget to wipe!')
}


# Declare all the rooms
import os

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('Note', 'There is a terribly written poem on here.')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('Key', 'It is very veryshiny! What will it open up?')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('Can', 'Why!? It is a can of SPAM!')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('Sani', 'Gotta make sure that your hands are clean.')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('TP', 'Do not forget to wipe!')]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room. You can input the user name.

new_player = Player(input('\nWhat is your name? '),room['outside'])

os.system("clear")

print(new_player.current_room)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

cmd = ""

print("\nPossible commands:\n>> 'n', 's', 'e', 'w'\n>> 'q' to quit\n>>'search' - to search room\n>>'take' + <item name>\n>>'drop' + <item name>\n>>'inv' - to check inventory")

print(f"You are {new_player.current_room}")

while cmd != ["q"]:
    cmd = str(input("\nType a command or 'q' to quit: ")).lower()

    # Movement
    if cmd == "n":
        if new_player.current_room.n_to != None:
            new_player.current_room = new_player.current_room.n_to
            print(f"\nYou enter the {new_player.current_room}")
        else:
            print("\nYou cannot continue North from here")

    elif cmd == "s":
        if new_player.current_room.s_to != None:
            new_player.current_room = new_player.current_room.s_to
            print(f"\nYou enter the {new_player.current_room}")
        else:
            print("\nYou cannot continue South from here")

    elif cmd == "w":
        if new_player.current_room.w_to != None:
            new_player.current_room = new_player.current_room.w_to
            print(f"\nYou enter the {new_player.current_room}")
        else:
            print("\nYou cannot continue West from here")

    elif cmd == "e":
        if new_player.current_room.e_to != None:
            new_player.current_room = new_player.current_room.e_to
            print(f"\nYou enter the {new_player.current_room}")
        else:
            print("\nYou cannot continue East from here")
    
    if cmd == "q":
        print("Farewell, adventurer.")
        exit()

    elif cmd == 'search':
        new_player.current_room.search()

    # take item(s)
    elif cmd == 'take':
        item_add = input('Please enter the item you wish you take into your inventory: ')
        new_player.take_item(item_add)

    # drop item(s)
    elif cmd == "drop":
        new_player.check_inventory()
        item_rem = input('Which item do you wish to remove? ')
        new_player.drop_item(item_rem)

    elif cmd == "inv":
        new_player.check_inventory()