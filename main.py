# main.py
# ---------------------------------------------------------------------------
# Created By  : Rafay Waqas
# Created Date: 5/22/2024
# version = '4.0'
# ---------------------------------------------------------------------------
"""
Medieval Text-based Map Game
----------------------------------
This program is a simple text-based map game set in a medieval
world. The player navigates through a map, using the commands 'walk' and 'run'.
The game map is represented using a list of lists (array), and location descriptions are stored in a dictionary.
"""
# ---------------------------------------------------------------------------
from player import Player
from game_map import GameMap
from inventory import Inventory

def display_main_menu():
    print("==== Medieval Adventure Game ====")
    print("1. Start Game")
    print("2. Quit")

def main():
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