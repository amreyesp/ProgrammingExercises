import unittest

# Can't use from... import directly since the file is into another folder
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from array.leftRotation import NewArray

class TestLeftRotation(unittest.TestCase):

    def setUp(self):
        self.myArray = NewArray()

    def test_fillArray(self):
        self.myArray.fillArray(size=9)
        self.assertEqual(9,self.myArray.size)

    def test_rotateLeft(self):
        self.myArray.fillArray(size=9)
        rotated_array = self.myArray.rotateLeft(distance=3)
        self.assertEqual([6,7,8,0,1,2,3,4,5],rotated_array)
