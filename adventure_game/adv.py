import sys

from room import Room
from player import Player

# Declare all the rooms
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


# Make a new player object that is currently in the 'outside' room
player = Player(room["outside"])

# Print the current room name
print(player.room.name)

# Print the current description (the textwrap module might be useful here)
print(player.room.description)

# Wait for user input and decide what to do
command = input("Enter direction: ")

# 1. If the user enters a cardinal direction, attempt to move to the room there
# 2. Print an error message if the movement isn't allowed

# 3. If the user enters "q", quit the game
if (command == "q"):
    print("Goodbye!")
    sys.exit()