import random
from Enemy import Enemy


class Ogre(Enemy):
    def __init__(self, health_points: int = 10, attack_damage: int = 1):
        super().__init__("Ogre", health_points, attack_damage)

    def talk(self):
        print("Ogre says: 'Me smash you!'")

    def special_attack(self):
        did_special_attack_work: bool = random.random() < 0.20
        if did_special_attack_work:
            self.attack_damage += 4
            print("Ogre gets angry and Ogre's attack damage increased by 4!")