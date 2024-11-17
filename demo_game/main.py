from Enemy import Enemy
from Hero import Hero
from Ogre import Ogre
from Weapon import Weapon
from Zombie import Zombie


def battle(enemy1: Enemy, enemy2: Enemy):
    enemy1.talk()
    enemy2.talk()
    print("----------------------")

    while enemy1.health_points > 0 and enemy2.health_points > 0:
        enemy1.special_attack()
        enemy2.special_attack()

        print(f"{enemy1.get_type_of_enemy()} HP: {enemy1.health_points}")
        print(f"{enemy2.get_type_of_enemy()} HP: {enemy2.health_points}")

        enemy2.attack()
        enemy1.health_points -= enemy2.attack_damage

        enemy1.attack()
        enemy2.health_points -= enemy1.attack_damage
        print("----------------------")

    if enemy1.health_points > 0:
        print(f"Enemy 1: {enemy1.get_type_of_enemy()} wins!")
    else:
        print(f"Enemy 2: {enemy2.get_type_of_enemy()} wins!")


def hero_battle(hero: Hero, enemy: Enemy):
    enemy.talk()
    print("----------------------")
    while hero.health_points > 0 and enemy.health_points > 0:
        enemy.special_attack()
        print(f"Hero HP: {hero.health_points}")
        print(f"Enemy {enemy.get_type_of_enemy()} HP: {enemy.health_points}")

        hero.attack()
        enemy.health_points -= hero.attack_damage

        enemy.attack()
        hero.health_points -= enemy.attack_damage
        print("----------------------")

    if hero.health_points > 0:
        print("Hero wins!")
    else:
        print(f"Enemy {enemy.get_type_of_enemy()} wins!")


zombie = Zombie(10, 1)
ogre = Ogre(20, 3)
hero = Hero(10, 1)

zombie.talk()
zombie.walk_forward()
zombie.attack()

print(
    f"{zombie.get_type_of_enemy()} has {zombie.health_points} health points and deals {zombie.attack_damage} damage."
)

print(
    f"{ogre.get_type_of_enemy()} has {ogre.health_points} health points and deals {ogre.attack_damage} damage."
)

weapon = Weapon("Sword", 5)
hero.weapon = weapon
hero.equip_weapon()

print()
# battle(zombie, ogre)

print()
hero_battle(hero, ogre)
