# Jeu Binaire - Gatien G. et Lokendra B.

import pyxel, time, random
 
nb_lignes_sprites = 5

liste = []

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
        self.coin = Coins(3, 6)
        self.monster = Monster(15, 20)
        self.shop = Shop(65, 8)
        self.binaire = Binaire(65, 45, self.monster)
        Music.musika(self)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 64 < pyxel.mouse_x < 102 and 8 < pyxel.mouse_y < 30:
                self.shop.buy_strength(self.player, self.coin)
            #self.monster.being_hit = 1
            #self.player.attack(self.monster, self.coin)

    def draw(self):
        pyxel.camera()
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 108, 72)
        self.coin.draw()
        self.hp_bar.draw(self.monster)
        self.monster.draw()
        self.binaire.draw(self.monster, self.player, self.coin)
        self.shop.draw(self.player)


class Coins:
    def __init__(self, x, y, purse=0):
        self.x = x
        self.y = y
        self.purse = purse

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 6, 7, 0)
        pyxel.text(self.x+8, self.y+1, f"{self.purse+1}", 10)


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
    def __init__(self, x, y, monster : Monster):
        self.x = x
        self.y = y
        Binaire.binaire(self, monster)

    def binaire(self, monster: Monster):
        self.bin = random.randint(0, monster.lvl+1)+1

    def DataButton(self):
        global liste
        self.liste = liste 
        if pyxel.btnp(pyxel.KEY_0):self.liste.append(0)
        elif pyxel.btnp(pyxel.KEY_1):self.liste.append(1)
        elif pyxel.btnp(pyxel.KEY_2):self.liste.append(2)
        elif pyxel.btnp(pyxel.KEY_3):self.liste.append(3)
        elif pyxel.btnp(pyxel.KEY_4):self.liste.append(4)
        elif pyxel.btnp(pyxel.KEY_5):self.liste.append(5)
        elif pyxel.btnp(pyxel.KEY_6):self.liste.append(6)
        elif pyxel.btnp(pyxel.KEY_7):self.liste.append(7)
        elif pyxel.btnp(pyxel.KEY_8):self.liste.append(8)
        elif pyxel.btnp(pyxel.KEY_9):self.liste.append(9)
        elif pyxel.btnp(pyxel.KEY_BACKSPACE):
            if len(self.liste) == 0:self.liste.append(0),self.liste.pop()
            else:self.liste.pop()
        
    
    def draw(self, monster : Monster, player : Player, coin : Coins):
        Binaire.DataButton(self)
        pyxel.text(self.x, self.y, f"{bin(self.bin)}", 7)
        RespBin = sum(d * 10**i for i, d in enumerate(self.liste[::-1])) #transforme la liste en int

        if pyxel.btnp(pyxel.KEY_RETURN):
            if self.bin == RespBin:
                monster.being_hit = 1
                player.attack(monster, coin)
                self.liste.clear()
                Binaire.binaire(self, monster)
            else:
                self.liste.clear()

        pyxel.text(self.x, self.y+10, f"{RespBin}", 7)
    

class Shop:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, player: Player):
        pyxel.text(self.x, self.y, f"force:\n{player.strength}\nup:\n{player.strength**2}$", 7)
    
    def buy_strength(self, player: Player, coins : Coins):
        if coins.purse - player.strength**2 >= 0:
            player.strength += 1
            coins.purse -= player.strength**2

class Music: # bout de code venant d'un exemple du module pyxel https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/04_sound_api.py
    def musika(self):
        pyxel.sound(0).set(
            "e2e2c2g1 g1g1c2e2 d2d2d2g2 g2g2rr" "c2c2a1e1 e1e1a1c2 b1b1b1e2 e2e2rr",
            "p",
            "3", 
            "vffn fnff vffs vfnn",
            25,
        )
        pyxel.sound(1).set(
            "r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2" "f2f2f2e2 f2e2d2c2 d2d2d2d2 g2g2r r ",
            "s",
            "3",
            "nnff vfff vvvv vfff svff vfff vvvv svnn",
            25,
        )
        pyxel.sound(2).set(
            "c1g1c1g1 c1g1c1g1 b0g1b0g1 b0g1b0g1" "a0e1a0e1 a0e1a0e1 g0d1g0d1 g0d1g0d1",
            "t",
            "4",
            "n",
            25,
        )
        pyxel.sound(3).set(
            "f0c1f0c1 g0d1g0d1 c1g1c1g1 a0e1a0e1" "f0c1f0c1 f0c1f0c1 g0d1g0d1 g0d1g0d1",
            "t",
            "2",
            "n",
            25,
        )
        Music.play_music(True, True, True)
    
    def play_music(self, ch0, ch1):
        pyxel.play(1, [0, 1], loop=True)
        pyxel.play(2, [2, 3], loop=True)


App()
