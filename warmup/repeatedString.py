"""Repeated String"""

"""
Lilah has a string, s, of lowercase English letters that she repeated infinitely
many times. Given an integer, n, find and print the number of letter a's in the
first n letters of Lilah's infinite string.
For example, if the string s='abcac' and n=10, the substring we consider is
abcacabcac, the first 10 characters of her infinite string. There are 4
occurrences of a in the substring.
Credits: www.hackerrank.com
"""

import random, string

class NewString:

    def __init__(self):
        self.string = ''
        self.substring = ''
        self.n = 0
        self.a = 0

    def randomString(self,length):
        letters = string.ascii_lowercase
        self.string='a'+''.join(random.choice(letters) for i in range(length-1))

    def repeatSubstring(self,n):
        self.substring=self.string.join(self.string for i in range(len(self.string)-1))
        print(self.string)
        print(self.substring)
