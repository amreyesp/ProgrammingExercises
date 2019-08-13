import unittest

# Can't use from... import directly since the file is into another folder
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from sorting.bubbleSort import NewSort

class TestCase(unittest.TestCase):

    def setUp(self):
        self.my_sort = NewSort()
        self.assertEqual([],self.my_sort.array)
        self.assertEqual(0,self.my_sort.minswaps)

    def test_bubble_algorithm(self):
        self.my_sort.bubble_algorithm([6,4,1])
        self.assertEqual([1,4,6],self.my_sort.array)
