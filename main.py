# Jeu Binaire - Gatien G. et Lokendra B.

import pyxel, time, random
 
nb_lignes_grilles = 1


class Coins:
    def __init__(self, x, y, purse=0):
        self.x = x
        self.y = y
        self.purse = purse

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 6, 7, 0)
        pyxel.text(self.x+8, self.y+1, f"{self.purse+1}", 7)


class Monster:
    def __init__(self, x, y, lvl=0):
        self.x = x
        self.y = y
        self.lvl = lvl
        self.index = random.randint(0, 3)
        self.hp = 3*self.lvl+10

    def draw(self):
        pyxel.text(70, 3, f"lvl {self.lvl}", 7)
        pyxel.blt(self.x, self.y, 1, self.index*16, (self.lvl // 4)*16, 16, 16, 0)
    
    def reset_hp(self):
        self.hp = self.get_default_hp()
    
    def set_new_index(self):
        self.index = random.randint(0, 3)

    def get_default_hp(self)->int:
        return 3*self.lvl+10

class HealthBar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, monster: Monster):
        pyxel.text(self.x+5, self.y-7, f"{monster.hp} hp", 7)
        pyxel.rect(self.x, self.y, 30, 4, 13)
        pyxel.rect(self.x, self.y, (monster.hp/monster.get_default_hp())*30, 4, 8)
        

class Player:
    def __init__(self):
        self.strength = 1
        self.multiplier = 1
        self.coin_multiplier = 1

    def attack(self, monster: Monster, coins: Coins):
        monster.hp -= self.strength * self.multiplier
        if monster.hp < 1:
            monster.lvl += 1
            monster.reset_hp()
            monster.set_new_index()
            coins.purse += (monster.lvl // 5 + 1)*self.coin_multiplier


class App:
    """
    Classe représentant l'application Pyxel.
    """
    def __init__(self):
        pyxel.init(108, 72, "0b1001", 60, display_scale=10)
        pyxel.load("rsc/ressources.pyxres")
        pyxel.mouse(True)
        pyxel.tilemap(0)
        self.hp_bar = HealthBar(9, 50)
        self.player = Player()
        self.coin = Coins(3, 2)
        self.monster = Monster(15, 20)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnp(pyxel.KEY_SPACE):
            self.player.attack(self.monster, self.coin)

    def draw(self):
        pyxel.cls(0)
        self.coin.draw()
        self.hp_bar.draw(self.monster)
        self.monster.draw()


App()
