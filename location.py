# location.py
class Location:
    """Represents a location in the game."""

    def __init__(self, name):
        """Initialize the location with a name and description."""
        self.name = name
        self.description = self.get_description()

    def get_description(self):
        """Return the description of the location based on its name."""
        descriptions = {
            'Courtyard': 'You find yourself in the castle courtyard. The adventure begins!',
            'Enchanted Forest': 'You enter an enchanted forest filled with ancient trees and magical creatures.',
            'Misty Mountains': 'You reach the foot of the misty mountains. The peaks disappear into the clouds.',
            'Raging River': 'A raging river blocks your path. The water rushes by with great force.',
            'Damp Dungeon': 'You stumble upon a damp dungeon. The air is heavy with the scent of moss.',
            'Guarded Castle': 'You approach a heavily guarded castle. The drawbridge is raised.',
            'Sandy Shore': 'You arrive at a sandy shore. The waves gently lap against the coastline.',
            'Mysterious Island': 'You discover a mysterious island shrouded in mist.',
            'Throne Room': 'Congratulations! You have reached the Throne Room. Your quest is complete.'
        }
        return descriptions[self.name]

    def display_description(self):
        """Display the description of the location."""
        print(self.description)

    def perform_action(self, player, inventory):
        """Perform a location-specific action."""
        if self.name == 'Enchanted Forest':
            print("You find a magical amulet in the forest. You add it to your inventory.")
            inventory.add_item('Magical Amulet')
        elif self.name == 'Damp Dungeon':
            print("You discover a rusty key in the dungeon. You add it to your inventory.")
            inventory.add_item('Rusty Key')