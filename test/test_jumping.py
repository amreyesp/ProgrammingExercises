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

    def test_jumpBack(self):
        self.game.clouds = [0,0,1,0,0]
        targetCloud = self.game.jumpBack(4)
        self.assertEqual(3,targetCloud)

    def test_jumpAhead(self):
        self.game.clouds = [0,1,0,1,0]
        targetCloud = self.game.jumpAhead(0)
        self.assertEqual(2,targetCloud)

    def test_pathForward(self):
        #self.game.clouds = [0,0,1,0,1,0,0,0,1,0]
        #self.game.searchPath('ahead',0)
        #self.assertEqual([1,3,5,7,9],self.game.path)
        self.game.clouds = [0,0,1,0,0,0,0,0,0]
        self.game.searchPath('ahead',0)
        self.assertEqual([1,3,5,7,8],self.game.path)

    def test_pathBackward(self):
        # self.game.clouds = [0,0,1,0,1,0,0,0,1,0]
        # self.game.searchPath('backward',9)
        # self.assertEqual([7,5,3,1,0],self.game.path)
        self.game.clouds = [0,0,1,0,0,0,0,0,0]
        self.game.searchPath('backward',8)
        self.assertEqual([6,4,3,1,0],self.game.path)
