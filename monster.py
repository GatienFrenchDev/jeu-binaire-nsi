import pyxel, random

nb_lignes_sprites = 5

class Monster:
    def __init__(self, x, y, lvl=1):
        self.x = x
        self.y = y
        self.lvl = lvl
        self.being_hit = 0
        self.index = random.randint(0, 3)
        self.hp = 3*self.lvl+10+random.randint(0, 5)
        self.initial_hp = self.hp
    
    def draw(self):
        pyxel.text(30, 2, f"LEVEL {self.lvl}", 7)
        if self.being_hit > 0:
            self.being_hit += 1
            pyxel.blt(self.x+2, self.y+1, 1, self.index*16, ((self.lvl // 4) % nb_lignes_sprites)*16, 16, 16, 0)
            pyxel.fill(self.x, self.y, 4)
            
            if self.being_hit > 5: # durée de l'animation (ici 5 frames soit environ 0.08s)
                pyxel.blt(self.x-2, self.y+1, 1, self.index*16, ((self.lvl // 4) % nb_lignes_sprites)*16, 16, 16, 0)
                self.being_hit = 0
        else:
            pyxel.blt(self.x, self.y, 1, self.index*16, ((self.lvl // 4) % nb_lignes_sprites)*16, 16, 16, 0)
    
    def reset_hp(self):
        self.hp = 3*self.lvl+10+random.randint(0, 5)
        self.initial_hp = self.hp
    
    def set_new_index(self):
        self.index = random.randint(0, 3)