## Jeu Binaire - Gatien G. et Lokendra B.

import pyxel

class Coins:
    def __init__(self, x, y, purse=0):
        self.x = x
        self.y = y
        self.purse = purse

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 6, 7)
        pyxel.text(self.x+8, self.y, f"{self.purse}", 7)

class App:
    """
    Classe représentant l'application Pyxel.
    """
    def __init__(self):
        pyxel.init(192, 128, "0b1001", 60, display_scale=6)
        pyxel.load("rsc/ressources.pyxres")
        pyxel.mouse(True)
        self.coin = Coins(3, 2)
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        self.coin.draw()

App()