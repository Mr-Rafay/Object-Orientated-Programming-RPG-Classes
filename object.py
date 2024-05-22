# object.py

class GameObject:
    """Class to represent an object that can be collected."""

    def __init__(self, name, x, y):
        self.name = name
        self.position = (x, y)