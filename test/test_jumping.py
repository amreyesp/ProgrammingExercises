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

    def test_valueClouds(self):
        self.game.clouding(10)
        value = True
        for cloud in self.game.clouds:
            if cloud != 0 and cloud != 1:
                value = False
                break
        self.assertTrue(value)
