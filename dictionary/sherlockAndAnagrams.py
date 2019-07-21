"""sherlock And Anagrams"""
"""
Two strings are anagrams of each other if the letters of one string can be
rearranged to form the other string. Given a string, find the number of pairs of
 substrings of the string that are anagrams of each other.
For example s=mom, the list of all anagrammatic pairs is [m,m],[mo,om] at
positions [0,2],[[0,1],[1,2]] respectively. Function description: Complete the
function sherlockAndAnagrams. It must return an integer that represents the
number of anagrammatic pairs of substrings in s.
Credits: www.hackerrank.com
"""

class NewAnagram:

    def __init__(self):
        self.string = ''
        self.pairs = 0

    def read_input(self,input):
        self.string = input

    def substring_anagrams(self,substring,length):
        for character in substring:
            pass

    def anagrams(self,length):
        for letter in self.string:
            self.substring_anagrams(letter,length)
