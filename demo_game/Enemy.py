class Enemy:
    def __init__(self, type: str, health_points: int = 10, attack_damage: int = 1):
        self.__type = type
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__type

    def talk(self):
        print(f"I am a {self.__type}. Be prepared to fight.")

    def walk_forward(self):
        print(f"{self.__type} moves closer to you.")

    def attack(self):
        print(f"{self.__type} attacks for {self.attack_damage} damage.")

    def special_attack(self):
        print("Enemy has no special attack.")
