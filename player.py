# player.py
from item import HealingPotion

class Player:
    def __init__(self, game_map):
        self.position = [0, 0]  # Courtyard
        self.game_map = game_map
        self.health = 100
        self.attack_power = 10
        self.inventory = [HealingPotion() for _ in range(5)]  # Add 5 healing potions to the player's inventory

    def update_position(self, direction, steps):
        row_offset, col_offset = self.game_map.valid_directions[direction]
        self.position[0] += row_offset * steps
        self.position[1] += col_offset * steps

    def is_valid_move(self, position):
        row, col = position
        return 0 <= row < len(self.game_map.game_map) and 0 <= col < len(self.game_map.game_map[0])

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Game Over! You have been defeated.")
            exit()

    def use_item(self, item_index):
        if 0 <= item_index < len(self.inventory):
            item = self.inventory[item_index]
            item.use(self)
            self.inventory.remove(item)
        else:
            print("Invalid item index.")