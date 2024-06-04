# item.py
class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def use(self, player):
        print(f"You use the {self.name}.")
        if self.effect == 'heal':
            player.health += 20
            print("You heal yourself for 20 health points.")
        elif self.effect == 'attack_boost':
            player.attack_power += 5
            print("Your attack power increases by 5.")