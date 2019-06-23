"""Minumum swaps"""
"""
You are given an unordered array consisting of consecutive integers
[1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two
elements. You need to find the minimum number of swaps required to sort the
array in ascending order.
Credits: www.hackerrank.com
"""

import random

class newArray:

    def __init__(self):
        self.array = []
        self.size = 0

    def fillArray(self, size):
        self.array = [element+1 for element in range(size)]
        self.size = len(self.array)

    def unsortArray(self):
        random.shuffle(self.array)
