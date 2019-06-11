import unittest

# Can't use from... import directly since the file is into another folder
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from warmup.repeatedString import NewString

class TestRepeatedString(unittest.TestCase):

    def setUp(self):
        self.myString = NewString()

    def test_randomString(self):
        length=9
        self.myString.randomString(length)
        self.assertEqual(9,len(self.myString.string))
        self.assertTrue('a' in self.myString.string)

    def test_repeatSubstringExact(self):
        n=27
        self.myString.randomString(length=3)
        self.myString.repeatSubstring(n)
        self.assertEqual(n,len(self.myString.substring))

    def test_repeatSubstringModule(self):
        n=89
        self.myString.randomString(length=4)
        self.myString.repeatSubstring(n)
        self.assertEqual(n,len(self.myString.substring))
