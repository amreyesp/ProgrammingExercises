import unittest

# Can't use from... import directly since the file is into another folder
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from warmup.jumpingClouds import Game

class TestJumpingClouds(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_createClouds(self):
        self.game.clouding(10)
        self.assertEqual(10,len(self.game.clouds))

    #Clouds values can only be binary
    def test_valueClouds(self):
        self.game.clouding(10)
        value = True
        for cloud in self.game.clouds:
            if cloud != 0 and cloud != 1:
                value = False
                break
        self.assertTrue(value)

    #The set of clouds must be compatible with the jump steps rules (1 or 2 steps)
    def test_proximityThunderheads(self):
        self.game.clouding(100)
        value = True
        self.game.adjustClouding()
        for i in range(len(self.game.clouds)-2):
            if self.game.clouds[i+1] == 1 and self.game.clouds[i+2] == 1:
                value = False
                break
        self.assertTrue(value)
