# game_map.py
from location import Location
from enemy import Enemy
from item import Item


class GameMap:
    """Represents the game map."""

    def __init__(self):
        """Initialize the game map and valid actions/directions."""
        self.game_map = [
            [Location('Courtyard', None), Location('Enchanted Forest', Enemy('Goblin', 50, 5)), Location('Misty Mountains', None)],
            [Location('Raging River', None), Location('Damp Dungeon', Enemy('Skeleton', 30, 8)), Location('Guarded Castle', Enemy('Knight', 80, 12))],
            [Location('Sandy Shore', None), Location('Mysterious Island', None), Location('Throne Room', None)]
        ]
        self.valid_actions = ['walk', 'run']
        self.valid_directions = {'north': (-1, 0), 'south': (1, 0), 'east': (0, 1), 'west': (0, -1)}

    def play_game(self, player, inventory):
        """Start the game."""
        while True:
            current_location = self.game_map[player.position[0]][player.position[1]]
            current_location.display_description()

            if current_location.name == 'Throne Room':
                print("Congratulations! You have reached the Throne Room and completed your quest.")
                break

            if current_location.enemy:
                print(f"You encounter a {current_location.enemy.name}!")
                combat = Combat(player, current_location.enemy)
                combat.start_combat()

            print(f"What do you want to do? (Valid actions: {', '.join(self.valid_actions)})")
            action = input("> ").lower()

            if action in self.valid_actions:
                steps = 1 if action == 'walk' else 2
                print(f"Which direction do you want to go? (Valid directions: {', '.join(self.valid_directions)})")
                direction = input("> ").lower()

                if direction in self.valid_directions:
                    new_position = player.position.copy()
                    player.update_position(direction, steps)

                    if player.is_valid_move(player.position):
                        current_location.perform_action(player, inventory)
                    else:
                        player.position = new_position
                        print("You cannot go that way. An invisible force stops you!")
                else:
                    print("Invalid direction. Please choose a valid direction.")
            elif action == 'inventory':
                inventory.display_inventory()
            elif action == 'quit':
                print("Thank you for playing. Farewell, brave adventurer!")
                break
            else:
                print("Invalid action. Please choose a valid action.")