# inventory.py
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def display_inventory(self):
        if self.items:
            print("Inventory:")
            for item in self.items:
                print("- " + item.name)
        else:
            print("Your inventory is empty.")

    def use_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                item.use(self.player)
                self.remove_item(item)
                break
        else:
            print(f"You don't have a {item_name} in your inventory.")