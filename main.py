# Jeu Binaire - Gatien G. et Lokendra B.

import pyxel, time, random
 
nb_lignes_sprites = 3

class App:
    """
    Classe représentant l'application Pyxel.
    """
    def __init__(self):
        pyxel.init(108, 72, "0b1001", 60, display_scale=10)
        pyxel.load("rsc/ressources.pyxres")
        pyxel.mouse(True)
        self.hp_bar = HealthBar(9, 55)
        self.player = Player()
        self.coin = Coins(3, 2)
        self.monster = Monster(15, 20)
        self.shop = Shop(65, 12)
        self.binaire = Binaire(65, 45, self.monster.lvl)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 64 < pyxel.mouse_x < 102 and 8 < pyxel.mouse_y < 30:
                self.shop.buy_strength(self.player, self.coin)
            # self.monster.being_hit = 1
            # self.player.attack(self.monster, self.coin)

    def draw(self):
        pyxel.camera()
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 108, 72)
        self.coin.draw()
        self.hp_bar.draw(self.monster)
        self.monster.draw()
        self.binaire.draw()
        self.shop.draw(self.player)


class Coins:
    def __init__(self, x, y, purse=0):
        self.x = x
        self.y = y
        self.purse = purse

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 6, 7, 0)
        pyxel.text(self.x+8, self.y+1, f"{self.purse+1}", 7)


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
        if self.lvl < 10:
            pyxel.text(88, 2, f"lvl {self.lvl}", 7)
        else :
            pyxel.text(84, 2, f"lvl {self.lvl}", 7)
        if self.being_hit > 0:
            self.being_hit += 1
            pyxel.blt(self.x+1, self.y+2, 1, self.index*16, ((self.lvl // 4) % nb_lignes_sprites)*16, 16, 16, 0)
            if self.being_hit > 5: # durée de l'animation (ici 5 frames soit environ 0.08s)
                self.being_hit = 0
        else:
            pyxel.blt(self.x, self.y, 1, self.index*16, ((self.lvl // 4) % nb_lignes_sprites)*16, 16, 16, 0)
    
    def reset_hp(self):
        self.hp = 3*self.lvl+10+random.randint(0, 5)
        self.initial_hp = self.hp
    
    def set_new_index(self):
        self.index = random.randint(0, 3)


class HealthBar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, monster: Monster):
        if monster.hp < 10:
            pyxel.text(self.x+8, self.y-7, f"{monster.hp} hp", 7)
        else:
            pyxel.text(self.x+6, self.y-7, f"{monster.hp} hp", 7)
        pyxel.rect(self.x, self.y, 30, 4, 13)
        pyxel.rect(self.x, self.y, (monster.hp/monster.initial_hp)*30, 4, 8)
        

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
            coins.purse += (monster.lvl ** 2 + 1)*self.coin_multiplier+random.randint(0, 5)


class Binaire:
    def __init__(self, x, y, lvl):
        self.x = x
        self.y = y
        self.bin = random.randint(0, lvl+1)+1

    def draw(self):
        pyxel.text(self.x, self.y, f"{bin(self.bin)}", 7)

class Shop:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, player: Player):
        pyxel.text(self.x, self.y, f"Force : {player.strength}\n\nUP : {player.strength**2}$", 7)
    
    def buy_strength(self, player: Player, coins : Coins):
        if coins.purse - player.strength**2 >= 0:
            pyxel.play(0, 1)
            player.strength += 1
            coins.purse -= player.strength**2

App()
