# enemy.py

class Enemy:
    """Class to represent an enemy."""

    def __init__(self, name, strength, x, y):
        self.name = name
        self.strength = strength
        self.position = (x, y)

    def move(self, dx, dy):
        """Move enemy by (dx, dy)."""
        self.position = (self.position[0] + dx, self.position[1] + dy)