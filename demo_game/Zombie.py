import random
from Enemy import Enemy


class Zombie(Enemy):
    def __init__(self, health_points: int = 10, attack_damage: int = 1):
        super().__init__("Zombie", health_points, attack_damage)

    def talk(self):
        print("*Braaaiiinnnssss......*")

    def spread_disease(self):
        print("The zombie is trying to spread infection.")

    def special_attack(self):
        did_special_attack_work: bool = random.random() < 0.5
        if did_special_attack_work:
            self.health_points += 2
            print("The Zombie regenerated 2 HP!")
