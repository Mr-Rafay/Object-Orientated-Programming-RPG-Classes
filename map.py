# map.py
#hi guys 
class Tile:
    """Class to represent a single tile on the map."""

    def __init__(self, x, y, content=None):
        self.position = (x, y)
        self.content = content

class GameMap:
    """Class to manage the game map."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[Tile(x, y) for y in range(height)] for x in range(width)]

    def add_content(self, x, y, content):
        """Add content to a specific tile on the map."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.tiles[x][y].content = content