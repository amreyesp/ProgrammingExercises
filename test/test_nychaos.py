import unittest

# Can't use from... import directly since the file is into another folder
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from array.newYearChaos import Queue

class TestNewYearChaos(unittest.TestCase):

    def setUp(self):
        self.myQueue = Queue()

    def test_initialQueue(self):
        self.myQueue.initialize(size=8)
        self.assertEqual([1,2,3,4,5,6,7,8],self.myQueue.queue)