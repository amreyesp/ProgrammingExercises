import unittest

# Can't use from... import directly since the file is into another folder
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from array.newYearChaos import Queue

class TestNewYearChaos(unittest.TestCase):

    def setUp(self):
        self.myQueue = Queue()

    def test_initialState(self):
        self.myQueue.initialState(size=8)
        self.assertEqual([1,2,3,4,5,6,7,8],self.myQueue.queue)

    def test_finalState(self):
        self.myQueue.initialState(size=8)
        self.myQueue.finalState()
        self.assertFalse([1,2,3,4,5,6,7,8] == self.myQueue.queue)

    def test_invalidState(self):
        self.myQueue.queue = [2,1,5,3,4]
        self.assertFalse(self.myQueue.invalidState())
        self.myQueue.queue = [2,5,1,3,4]
        self.assertTrue(self.myQueue.invalidState())

    # def test_countBribes(self):
    #     self.myQueue.queue = [2,1,5,3,4]
    #     self.myQueue.countBribes()
    #     self.assertEqual(3,self.myQueue.bribes)
