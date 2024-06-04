# game_map.py
from location import Location


class GameMap:
    """Represents the game map."""

    def __init__(self):
        """Initialize the game map and valid actions/directions."""
        self.game_map = [
            [Location('Courtyard'), Location('Enchanted Forest'), Location('Misty Mountains')],
            [Location('Raging River'), Location('Damp Dungeon'), Location('Guarded Castle')],
            [Location('Sandy Shore'), Location('Mysterious Island'), Location('Throne Room')]
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