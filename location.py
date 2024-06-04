# location.py
class Location:
    def __init__(self, name, enemy=None, item=None):
        self.name = name
        self.description = self.get_description()
        self.enemy = enemy
        self.item = item

    def get_description(self):
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
        print(self.description)

    def perform_action(self, player, inventory):
        if self.item:
            print(f"You find a {self.item.name}. You add it to your inventory.")
            inventory.add_item(self.item)
            self.item = None