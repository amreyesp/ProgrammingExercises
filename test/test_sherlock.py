import unittest

# Can't use from... import directly since the file is into another folder
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from dictionary.sherlockAndAnagrams import NewAnagram

class TestSherlock(unittest.TestCase):

    def setUp(self):
        self.my_anagram = NewAnagram()
        self.assertEqual('',self.my_anagram.string)
        self.assertEqual(0,self.my_anagram.pairs)

    def test_read_input(self):
        self.my_anagram.read_input('mom')
        self.assertEqual('mom',self.my_anagram.string)

    def test_anagrams_length1(self):
        self.my_anagram.read_input('momo')
        pairs = self.my_anagram.anagrams(length=1)
        self.assertEqual(2,self.my_anagram.pairs)
