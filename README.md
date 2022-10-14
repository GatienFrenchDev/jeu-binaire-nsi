# Jeu binaire NSI [0b1001]

Ce jeu est un projet de nsi de terminale. Il a pour but d'apprendre à **convertir** un nombre dans différentes bases (binaire, hexadecimal) et s'entrainer sur le calcul mental.

Il est codé en Python et utilise la librairie **[pyxel](https://github.com/kitao/pyxel)**.

Ce jeu a permis d'acquérir de l'expérience avec cette librairie pour pouvoir par la suite participer à la Nuit du Code.

![image](https://user-images.githubusercontent.com/80203026/195835842-c56325e0-6900-4321-ac66-6dd366d669aa.png)

![image](https://user-images.githubusercontent.com/80203026/195836140-b179ca5b-78c5-4c96-96af-fe4fdae85880.png)


### Comment lancer le jeu ?
Pour jouer au jeu rien de compliquer :
- tout d'abord, télécharger le repo :
```bash
git clone https://github.com/GatienFrenchDev/jeu-binaire-nsi.git
```
 - puis télécharger la dernière version de la librairie pyxel à l'aide de pip :
 ```bash
 pip install pyxel
 ```

 - et finalement, executer avec python3 le fichier `main.py`
 ```
 python3 main.py
 ```

### Fonctionnement du jeu
- Avec les touches **0 à 9** du clavier vous pouvez répondre à la conversion.

- Pour supprimer un caractère appuyez sur la touche **retour arrière**.

- Pour valider la conversion appuyez sur la touche **entrée**.

- La touche **espace** vous permettera en l'échange d'un certain nombre de Coins de pouvoir acheter la solution pendant un court instant.

**Système de coins :** Lorsque vous réalisez une conversion le monstre subit un certain nombre de dégâts (en fonction de votre force), lorsque le monstre meurt vous gagnez des coins et vous montez en niveau. 

Plus votre niveau est haut, plus les P.V. du monstre, son nombre de coins attribué et le niveau des conversions augmentent.

Avec les Coins gagnés vous pouvez acheter de la force pour augmenter vos dégâts.
