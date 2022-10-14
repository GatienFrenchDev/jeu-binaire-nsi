import pyxel

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