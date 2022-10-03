# Jeu Binaire - Gatien G. et Lokendra B.

import pyxel, time


class Coins:
    def __init__(self, x, y, purse=0):
        self.x = x
        self.y = y
        self.purse = purse

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 6, 7)
        pyxel.text(self.x+8, self.y+1, f"{self.purse}", 7)


class Monster:
    def __init__(self, x, y, lvl=0):
        self.x = x
        self.y = y
        self.lvl = lvl
        self.hp = 3*self.lvl+10

    def draw(self):
        pyxel.blt(self.x, self.y, 1, (self.lvl % 4)*16, (self.lvl // 4)*16, 16, 16)

class Player:
    def __init__(self):
        self.strength = 1
        self.multiplier = 1

    def attack(self, monster: Monster):
        monster.hp -= self.strength * self.multiplier

class App:
    """
    Classe représentant l'application Pyxel.
    """
    def __init__(self):
        pyxel.init(108, 72, "0b1001", 60, display_scale=10)
        pyxel.load("rsc/ressources.pyxres")
        pyxel.mouse(True)
        self.player = Player()
        self.coin = Coins(3, 2)
        self.monster = Monster(15, 30, 1)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.player.attack(self.monster)
            print(self.monster.hp)

    def draw(self):
        pyxel.cls(0)
        self.coin.draw()
        self.monster.draw()


App()
