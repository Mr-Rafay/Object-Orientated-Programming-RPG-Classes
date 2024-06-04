# combat.py
class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_combat(self):
        while True:
            print(f"Player Health: {self.player.health}")
            print(f"Enemy Health: {self.enemy.health}")
            print("What do you want to do?")
            print("1. Attack")
            print("2. Use Item")
            print("3. Flee")

            choice = input("> ")

            if choice == '1':
                self.player_attack()
            elif choice == '2':
                self.use_item()
            elif choice == '3':
                self.flee()
                break
            else:
                print("Invalid choice. Please try again.")

            if self.enemy.health <= 0:
                print(f"You have defeated the {self.enemy.name}!")
                break

            self.enemy_attack()

            if self.player.health <= 0:
                print("Game Over! You have been defeated.")
                exit()

    def player_attack(self):
        damage = self.player.attack_power
        self.enemy.take_damage(damage)
        print(f"You attack the {self.enemy.name} for {damage} damage.")

    def enemy_attack(self):
        damage = self.enemy.attack_power
        self.player.take_damage(damage)
        print(f"The {self.enemy.name} attacks you for {damage} damage.")

    def use_item(self):
        print("Inventory:")
        for index, item in enumerate(self.player.inventory, start=1):
            print(f"{index}. {item.name}")

        if not self.player.inventory:
            print("Your inventory is empty.")
            return

        item_index = int(input("Enter the item number to use: ")) - 1
        self.player.use_item(item_index)

    def flee(self):
        print("You flee from the battle.")