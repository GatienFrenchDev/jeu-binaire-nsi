## Jeu Binaire - Gatien G. et Lokendra B.

import pyxel
class App:
    """
    Classe représentant l'application Pyxel.
    """
    def __init__(self):
        pyxel.init(160, 120, "Binaire Clicker", 60)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)

App()