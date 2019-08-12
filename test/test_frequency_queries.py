import unittest

# Can't use from... import directly since the file is into another folder
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from dictionary.frequencyQueries import NewQuery

class TestCase(unittest.TestCase):

    def setUp(self):
        self.my_query = NewQuery()
        self.assertEqual([],self.my_query.queries)
        self.assertEqual([],self.my_query.array)
        self.assertEqual(-1,self.my_query.output)

    def test_read_input(self):
        self.my_query.read_input([(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)])
        self.assertEqual([(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)],self.my_query.queries)

    
