"""Sock Merchant"""

"""
John works at a clothing store. He has a large pile of socks that he must pair
by color for sale. Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are. For example,
there are 7 socks with ar=[1,2,1,2,1,3,2] colors . There is one pair of color 1
and one of color 2. There are three odd socks left, one of each color.
The number of pairs is 2.
Credits: www.hackerrank.com
"""
import random

class Sockbag:

    def __init__(self):
        self.bag = []

    def fill(self,size,colour):
        for i in range(size):
            self.bag.append(random.randint(1,colour))

    def sort_bag(self):
        self.bag.sort()
