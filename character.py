from weapon import fists
from healthbar import HealthBar

class Character:

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print (f"{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}")

class Player(Character):
        def __init__(self, name: str = "Player", health: int = 100) -> None:
            super().__init__(name=name, health=health)          
            self.default_weapon = self.weapon
            self.health_bar = HealthBar(self, color="blue")
            self.pos = [0,0]
            self.marker = player_marker
            self.movement_options: dict [str, bool]

        def equip(self, weapon) -> None:
            self.weapon = weapon
            print(f"{self.name} equipped a(n) {self.weapon.name}")

        def drop (self) -> None:
            print(f"{self.name} dropped {self.weapon.name}!")
            self.weapon = self.default_weapon

class Enemy(Character):
        def __init__(self, name: str, health: int, weapon= None) -> None:
            super().__init__(name=name, health=health)
            self.weapon = weapon
            self.health_bar = HealthBar(self, color = "red")

            enemies.append(self)

enemies = []
slime = Enemy("Slime", 10, jaws)
goblin = Enemy("Goblin", 20, short_bow)
spider = Enemy("Spuder", 15, jaws)
rat = Enemy("Rat", 6, claws)