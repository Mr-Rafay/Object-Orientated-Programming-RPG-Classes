# enemy.py
class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"The {self.name} has been defeated!")