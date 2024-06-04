# inventory.py
class Inventory:
    """Represents the player's inventory."""

    def __init__(self):
        """Initialize an empty inventory."""
        self.items = []

    def add_item(self, item):
        """Add an item to the inventory."""
        self.items.append(item)

    def remove_item(self, item):
        """Remove an item from the inventory."""
        if item in self.items:
            self.items.remove(item)

    def display_inventory(self):
        """Display the items in the inventory."""
        if self.items:
            print("Inventory:")
            for item in self.items:
                print("- " + item.name)
        else:
            print("Your inventory is empty.")

    def use_item(