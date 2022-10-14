import pyxel

class HealthBar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, monster):
        if monster.hp < 10:
            pyxel.text(self.x+8, self.y-7, f"{monster.hp} hp", 7)
        else:
            pyxel.text(self.x+6, self.y-7, f"{monster.hp} hp", 7)
        pyxel.rect(self.x, self.y, 30, 4, 13)
        pyxel.rect(self.x, self.y, (monster.hp/monster.initial_hp)*30, 4, 8)