# item.py
class Item:
    def __init__(self, name):
        self.name = name

    def use(self, player):
        pass

class HealingPotion(Item):
    def __init__(self):
        super().__init__("Healing Potion")

    def use(self, player):
        heal_amount = 20
        player.health += heal_amount
        print(f"You use a {self.name} and heal for {heal_amount} health points.")