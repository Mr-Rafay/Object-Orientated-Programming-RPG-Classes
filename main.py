# main.py
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