import unittest

# Can't use from... import directly since the file is into another folder
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from array.leftRotation import NewArray

class TestLeftRotation(unittest.TestCase):

    def test_setUp(self):
        self.myArray = NewArray()
        self.assertEqual([],self.myArray.array)
        self.assertEqual(0,self.myArray.size)
        self.assertEqual(0,self.myArray.distance)
