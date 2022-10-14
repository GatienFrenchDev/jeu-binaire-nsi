import pyxel, random

class Player:
    def __init__(self):
        self.strength = 1
        self.multiplier = 1
        self.coin_multiplier = 1

    def attack(self, monster, coins):
        monster.hp -= self.strength * self.multiplier
        if monster.hp < 1:
            monster.lvl += 1
            monster.reset_hp()
            monster.set_new_index()
            coins.purse += (monster.lvl ** 2 + 1)*self.coin_multiplier+random.randint(0, 5)