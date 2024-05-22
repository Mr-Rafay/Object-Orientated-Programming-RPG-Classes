# inventory.py

class Inventory:
    """Class to manage the player's inventory."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the inventory."""
        self.items.append(item)

    def view_inventory(self):
        """Return the list of items in the inventory."""
        return self.items