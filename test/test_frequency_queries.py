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
        self.assertEqual([],self.my_query.output)

    def test_read_input(self):
        self.my_query.read_input([(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)])
        self.assertEqual([(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)],self.my_query.queries)

    def test_process_query_case1x(self):
        self.my_query.process_query([1,1])
        self.assertEqual([1],self.my_query.array)

    def test_process_query_case2x_present(self):
        self.my_query.array = [1,1,1]
        self.my_query.process_query([2,1])
        self.assertEqual([1,1],self.my_query.array)

    def test_process_query_case2x_notpresent(self):
        self.my_query.array = [0,2,3]
        self.my_query.process_query([2,1])
        self.assertEqual([0,2,3],self.my_query.array)

    def test_process_query_case3x_freq2_notpresent(self):
        self.my_query.array = [0,2,3,1,4]
        self.my_query.process_query([3,2])
        self.assertEqual(0,self.my_query.output)

    def test_process_query_case3x_freq2_present(self):
        self.my_query.array = [1,2,2,1,4]
        self.my_query.process_query([3,2])
        self.assertEqual([1],self.my_query.output)

    def test_process_query_case3x_freq2_notpresent(self):
        self.my_query.array = [1,2,2,2,4]
        self.my_query.process_query([3,2])
        self.assertEqual([0],self.my_query.output)

    def test_frequency_queries(self):
        self.my_query.read_input([(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)])
        self.my_query.frequency_queries()
        self.assertEqual([1,1],self.my_query.array)
        self.assertEqual([0,1],self.my_query.output)

    def test_frequency_queries_input0(self):
        self.my_query.read_input([(1,5),(1,6),(3,2),(1,10),(1,10),(1,6),(2,5),(3,2)])
        self.my_query.frequency_queries()
        self.assertEqual([0,1],self.my_query.output)

    def test_frequency_queries_input1(self):
        self.my_query.read_input([(3,4),(2,1003),(1,16),(3,1)])
        self.my_query.frequency_queries()
        self.assertEqual([0,1],self.my_query.output)

    def test_frequency_queries_input2(self):
        self.my_query.read_input([(1,3),(2,3),(3,2),(1,4),(1,5),(1,5),(1,4),(3,2),(2,4),(3,2)])
        self.my_query.frequency_queries()
        self.assertEqual([0,1,1],self.my_query.output)
