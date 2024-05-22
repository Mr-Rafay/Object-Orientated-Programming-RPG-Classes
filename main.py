# main.py

from player import Player
from enemy import Enemy
from obstacle import Obstacle
from object import GameObject
from map import GameMap

def main():
    # Initialize game components
    player = Player("Hero", 0, 0)
    game_map = GameMap(5, 5)

    # Add objects and obstacles
    game_map.add_content(1, 1, Obstacle("Rock", 1, 1))
    game_map.add_content(2, 2, GameObject("Treasure", 2, 2))
    game_map.add_content(3, 3, Enemy("Goblin", 5, 3, 3))

    # Game loop
    while True:
        print(f"Player position: {player.position}")
        command = input("Enter command (move/view inventory/collect): ").strip().lower()

        if command == "move":
            dx = int(input("Enter dx: "))
            dy = int(input("Enter dy: "))
            new_x = player.position[0] + dx