import unittest

# Can't use from... import directly since the file is into another folder
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from dictionary.ransomNote import NewNote

class TestRansomNote(unittest.TestCase):

    def setUp(self):
        self.my_note = NewNote()
        self.assertEqual(0,self.my_note.magazine_size)
        self.assertEqual(0,self.my_note.note_size)
        self.assertEqual([],self.my_note.magazine)
        self.assertEqual([],self.my_note.note)

    def test_read_input(self):
        self.my_note.read_input(6,4,'give me one grand today night','give one grand today')
        self.assertEqual(6,self.my_note.magazine_size)
        self.assertEqual(4,self.my_note.note_size)
        self.assertEqual(['give','me','one','grand','today','night'],self.my_note.magazine)
        self.assertEqual(['give','one','grand','today'],self.my_note.note)

    def test_check_magazine(self):
        self.my_note.read_input(6,4,'give me one grand today night','give one grand today')
        ans = self.my_note.check_magazine()
        self.assertEqual('Yes',ans)

    def test_input1(self):
        self.my_note.read_input(6,5,'two times three is not four','two times two is four')
        ans = self.my_note.check_magazine()
        self.assertEqual('No',ans)

    def test_input2(self):
        self.my_note.read_input(7,4,'ive got a lovely bunch of coconuts','ive got some coconuts')
        ans = self.my_note.check_magazine()
        self.assertEqual('No',ans)
