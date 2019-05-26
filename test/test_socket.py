import unittest

# Can't use from... import directly since the file is into another folder
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from warmup.sockMerchant import Sockbag

class TestSockMerchant(unittest.TestCase):

    def set_up(self):
        self.sockbag = Sockbag()

    def test_initial_value(self):
        self.set_up()
        self.assertEqual([], self.sockbag.bag)

    def test_fill_bag(self):
        self.set_up()
        self.sockbag.fill(5,2)
        self.assertEqual(5, len(self.sockbag.bag))

    def test_sort_bag(self):
        self.set_up()
        self.sockbag.bag = [2,3,4,1,2,5,6,7,4,1]
        self.sockbag.sort_bag()
        self.assertEqual([1,1,2,2,3,4,4,5,6,7],self.sockbag.bag)
