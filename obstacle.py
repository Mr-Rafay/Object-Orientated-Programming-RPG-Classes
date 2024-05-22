# obstacle.py

class Obstacle:
    """Class to represent an obstacle."""

    def __init__(self, name, x, y):
        self.name = name
        self.position = (x, y)