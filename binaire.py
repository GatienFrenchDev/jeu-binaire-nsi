import pyxel, random
from monster import Monster
from player import Player
from coin import Coins

liste = []

class Binaire:
    def __init__(self, x, y, monster : Monster):
        self.x = x
        self.y = y
        self.achatAide = False
        self.aide = False
        self.attendre = 0
        self.aideCost = random.randint(1, monster.lvl)+1
        Binaire.choixConversion(self, monster)

    def choixConversion(self, monster: Monster):
        self.binAnswer = random.randint(0, monster.lvl+1)+1
        self.choix = random.randint(1,3)
        if self.choix == 1: self.conversion = bin(self.binAnswer) #Question Binaire
        elif self.choix == 2: self.conversion = hex(self.binAnswer) #Question Hexa
        elif self.choix == 3: self.conversion = self.binAnswer #Question de Int à Binaire

    def DataButton(self, monster : Monster, player : Player, coin : Coins):
        """Liste des bouttons programmables"""
        global liste
        self.liste = liste
        if self.choix == 3:
            if pyxel.btnp(pyxel.KEY_0):self.liste.append(0)
            elif pyxel.btnp(pyxel.KEY_1):self.liste.append(1)


        elif self.choix == 1 or self.choix == 2:
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

        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.achatAide == False and coin.purse >= self.aideCost:
                self.aideCost = random.randint(1, monster.lvl)+1
                self.achatAide = True
                coin.purse = coin.purse - self.aideCost

        elif pyxel.btnp(pyxel.KEY_BACKSPACE):
            if len(self.liste) == 0:self.liste.append(0),self.liste.pop()
            else:self.liste.pop()

        elif pyxel.btnp(pyxel.KEY_RETURN):
            if self.choix != 3:
                if self.NbrInserer == self.binAnswer:
                    monster.being_hit = 1
                    player.attack(monster, coin)
                    self.liste.clear()
                    Binaire.choixConversion(self, monster)
                else:
                    self.liste.clear()

            elif self.choix == 3: # réponse en binaire
                ReponseBinaire = f"0b{self.NbrInserer}"
                if ReponseBinaire == bin(self.binAnswer):
                    monster.being_hit = 1
                    player.attack(monster, coin)
                    self.liste.clear()
                    Binaire.choixConversion(self, monster)
                else:
                    self.liste.clear()

        self.NbrInserer = sum(d * 10**i for i, d in enumerate(self.liste[::-1])) #transforme la liste en int

    def aideConversion(self):
        pyxel.text(self.x-25, self.y+5, f" AIDE\n {self.aideCost}$ \nESPACE", 15)
        if self.achatAide == True:
            self.attendre += 1
            self.aide = True
            if self.attendre >= 120:
                    self.achatAide = False
                    self.aide = False
                    self.attendre = 0


    def draw(self, monster : Monster, player : Player, coin : Coins):
        Binaire.DataButton(self, monster, player, coin)
        Binaire.aideConversion(self)

        if self.choix == 1:
            pyxel.text(self.x-24, self.y-12, "Binaire en Entier", 9)
            pyxel.text(self.x, self.y, f"{self.conversion}", 7)
            pyxel.text(self.x, self.y+10, f"{self.NbrInserer}", 7)
            if self.aide == True:
                pyxel.text(self.x-18, self.y-3, f"{self.binAnswer}", 10)

        elif self.choix == 2:
            pyxel.text(self.x-24, self.y-12, "Hexa en Entier", 2)
            pyxel.text(self.x, self.y, f"{self.conversion}", 7)
            pyxel.text(self.x, self.y+10, f"{self.NbrInserer}", 7)
            if self.aide == True:
                pyxel.text(self.x-18, self.y-3, f"{self.binAnswer}", 10)

        elif self.choix == 3:
            pyxel.text(self.x-24, self.y-12, "Entier en Binaire", 8)
            pyxel.text(self.x, self.y, f"{self.conversion}", 7)
            pyxel.text(self.x, self.y+10, f"0b{self.NbrInserer}", 7)
            if self.aide == True:
                pyxel.text(self.x-18, self.y-3, f"{bin(self.binAnswer)}", 10)