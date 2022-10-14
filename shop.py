import pyxel

class Shop:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, player):
        pyxel.text(self.x, self.y, f"force:\n{player.strength}\nup:\n{player.strength**2}$", 7)
    
    def buy_strength(self, player, coins):
        if coins.purse - player.strength**2 >= 0:
            player.strength += 1
            coins.purse -= player.strength**2