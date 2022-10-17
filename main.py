# Jeu Binaire - Gatien G. et Lokendra B.

# importation des modules de python
import pyxel, time, random

# importation des classes local
from coin import Coins
from monster import Monster
from healthbar import HealthBar
from player import Player
from music import Music
from binaire import Binaire
from shop import Shop

class App:
    """
    Classe représentant l'application Pyxel.
    """
    def __init__(self):
        pyxel.init(108, 72, "Projet 0b1001", 60, display_scale=10)
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
    
App()
