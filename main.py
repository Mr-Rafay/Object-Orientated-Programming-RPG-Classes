# main.py
# ---------------------------------------------------------------------------
# Created By  : Rafay Waqas
# Created Date: 3/19/2024
# version = '4.0'
# ---------------------------------------------------------------------------
"""
Medieval Text-based Map Game
----------------------------------
This program is a simple text-based map game set in a medieval
world. The player navigates through a map, using the commands 'walk' and 'run'.
The game map is represented using a list of lists (array), and location descriptions are
stored in a dictionary.
"""
# ---------------------------------------------------------------------------

# ----IMPORTS AND GLOBAL VARIABLES--------------------------------------------
from player import Player
from game_map import GameMap
from inventory import Inventory
from location import Location
from enemy import Enemy
from item import Item
from combat import Combat


# ----FUNCTIONS--------------------------------------------------------------
def display_main_menu():
    """Display the main menu."""
    print("==== Medieval Adventure Game ====")
    print("1. Start Game")
    print("2. Quit")


# ----MAIN-------------------------------------------------------------------
def main():
    """The main game loop."""
    game_map = GameMap()
    player = Player(game_map)
    inventory = Inventory()

    while True:
        display_main_menu()
        choice = input("> ")

        if choice == '1':
            game_map.play_game(player, inventory)
        elif choice == '2':
            print("Thank you for playing. Farewell!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == '__main__':
    main()