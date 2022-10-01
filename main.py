## Jeu Binaire - Gatien G. et Lokendra B.

import pyxel

class Bird:
    """
    Classe représentant un oiseau.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 8
        self.height = 8

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 0, self.width, self.height)

class Box:
    """
    Classe représentant une boite.
    """
    def __init__(self, x, y, side=1):
        """
        :param x: position x ou spawn l'objet
        :param y : position y ou spawn l'objet
        :param side: 0 pour côté gauche, 1 pour sans contour, 2 pour côté droit
        """
        self.x = x
        self.y = y
        self.side = side
        self.width = 8
        self.height = 8
    def draw(self):
        match self.side:
            case 0:
                pyxel.blt(self.x, self.y, 0, 0, 0, self.width, self.height)
            case 1:
                pyxel.blt(self.x, self.y, 0, 0, 8, self.width, self.height)
            case 2:
                pyxel.blt(self.x, self.y, 0, 8, 0, self.width, self.height)

class Coins:
    def __init__(self, x, y, purse=0):
        self.x = x
        self.y = y
        self.purse = purse

    def draw(self):
        pyxel.text(self.x, self.y, f"{self.purse}", 7)
        pyxel.blt(self.x+4, self.y, 0, 24, 0, 5, 6)

class App:
    """
    Classe représentant l'application Pyxel.
    """
    def __init__(self):
        pyxel.init(192, 128, "0b1001", 60, display_scale=6)
        pyxel.load("rsc/ressources.pyxres")
        pyxel.mouse(True)
        self.bird = Bird(64, 32)
        self.box_coins = [Box(0, 0, 0), Box(8, 0, 2)]
        self.coin = Coins(3, 1)
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        for box in self.box_coins:
            box.draw()
        self.coin.draw()

App()