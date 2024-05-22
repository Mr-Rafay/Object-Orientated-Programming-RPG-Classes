# player.py

from inventory import Inventory

class Player:
    """Class to represent the player."""

    def __init__(self, name, x, y):
        self.name = name
        self.position = (x, y)
        self.inventory = Inventory()

    def move(self, dx, dy):
        """Move player by (dx, dy)."""
        self.position = (self.position[0] + dx, self.position[1] + dy)

    def collect_object(self, obj):
        """Collect an object and add it to the inventory."""
        self.inventory.add_item(obj)