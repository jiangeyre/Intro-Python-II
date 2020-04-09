from room import Room
from player import Player

# Declare all the rooms
import os

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# Make a new player object that is currently in the 'outside' room.

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

print("\nPossible commands:\n>> 'n', 's', 'e', 'w'\n>> 'q' to quit")

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