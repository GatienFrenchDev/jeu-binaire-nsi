import pyxel

class Coins:
    def __init__(self, x, y, purse=0):
        self.x = x
        self.y = y
        self.purse = purse

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 6, 7, 0)
        pyxel.text(self.x+8, self.y+1, f"{self.purse+1}", 10)