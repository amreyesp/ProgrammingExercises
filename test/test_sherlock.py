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
        self.assertEqual({},self.my_anagram.anagrams)

    def test_read_input(self):
        self.my_anagram.read_input('mom')
        self.assertEqual('mom',self.my_anagram.string)

    def test_find_substrings_one_letter(self):
        self.my_anagram.read_input('mom')
        self.my_anagram .find_substrings(length=1)
        self.assertEqual({'m':[[0],[2]],'o':[[1]]},self.my_anagram.anagrams)

    def test_find_substrings(self):
        self.my_anagram.read_input('mom')
        self.my_anagram.find_substrings(length=2)
        self.assertEqual({'mo':[[0,1]],'om':[[1,2]]},self.my_anagram.anagrams)

    def test_all_substrings(self):
        self.my_anagram.read_input('mom')
        self.my_anagram.all_substrings()
        self.assertEqual({'m':[[0],[2]],'o':[[1]],'mo':[[0,1]],'om':[[1,2]]},self.my_anagram.anagrams)

    def test_find_anagrams_two_letters(self):
        self.my_anagram.read_input('mom')
        self.my_anagram.all_substrings()
        ans = self.my_anagram.find_anagram('mo')
        self.assertEqual({'m':[[0],[2]],'o':[[1]],'mo':[[0, 1],[1, 2]]},ans)

    def test_find_all_anagrams(self):
        self.my_anagram.read_input('mom')
        self.my_anagram.all_substrings()
        self.my_anagram.find_all_anagrams()
        self.assertEqual({'m':[[0],[2]],'mo':[[0, 1],[1, 2]]},self.my_anagram.anagrams)

    def test_find_all_anagrams_input2(self):
        self.my_anagram.read_input('abba')
        self.my_anagram.all_substrings()
        self.my_anagram.find_all_anagrams()
        self.assertEqual({'a':[[0],[3]],'b':[[1],[2]],'ab':[[0,1],[2,3]],'abb':[[0,1,2],[1,2,3]]},self.my_anagram.anagrams)

    def test_count_pairs(self):
        self.my_anagram.read_input('mom')
        self.my_anagram.all_substrings()
        self.my_anagram.find_all_anagrams()
        pairs = self.my_anagram.count_pairs()
        self.assertEqual(2,pairs)

    def test_count_pairs_input2(self):
        self.my_anagram.read_input('abba')
        self.my_anagram.all_substrings()
        self.my_anagram.find_all_anagrams()
        pairs = self.my_anagram.count_pairs()
        self.assertEqual(4,pairs)

    def test_count_pairs_input2(self):
        self.my_anagram.read_input('abcd')
        self.my_anagram.all_substrings()
        self.my_anagram.find_all_anagrams()
        pairs = self.my_anagram.count_pairs()
        self.assertEqual(0,pairs)

    def test_count_pairs_input3(self):
        self.my_anagram.read_input('ifailuhkqq')
        self.my_anagram.all_substrings()
        self.my_anagram.find_all_anagrams()
        pairs = self.my_anagram.count_pairs()
        self.assertEqual(3,pairs)

    def test_count_pairs_input3(self):
        self.my_anagram.read_input('kkkk')
        self.my_anagram.all_substrings()
        self.my_anagram.find_all_anagrams()
        pairs = self.my_anagram.count_pairs()
        self.assertEqual(10,pairs)

    def test_count_pairs_input4(self):
        self.my_anagram.read_input('cdcd')
        self.my_anagram.all_substrings()
        self.my_anagram.find_all_anagrams()
        pairs = self.my_anagram.count_pairs()
        self.assertEqual(5,pairs)
