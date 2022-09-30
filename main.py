## Jeu Binaire - Gatien G. et Lokendra B.

import pyxel
class App:
    """
    Classe représentant l'application Pyxel.
    """
    def __init__(self):
        pyxel.init(1400, 630, "0b1001", 60)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        pyxel.image(0).load(10, 10, "rsc/icon_large.png")
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        return 0

App()