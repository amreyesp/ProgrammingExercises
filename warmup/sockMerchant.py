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
        self.colours = []
        self.socks = []
        self.pairs = []
        self.odds = []

    def count_socks(self):
        for colour in self.colours:
            self.socks.append(self.bag.count(colour))

    def count_pairs(self):
        for sock in self.socks:
            self.pairs.append(int(sock/2))
            self.odds.append(sock % 2)

    def id_colours(self):
        for sock in self.bag:
            if sock not in self.colours:
                self.colours.append(sock)

    def fill(self,size,colour):
        for sock in range(size):
            self.bag.append(random.randint(1,colour))

    def sort_bag(self):
        self.bag.sort()


"""Main"""

mybag=Sockbag()
mybag.bag = [10,20,20,10,10,30,50,10,20]
mybag.sort_bag()
mybag.id_colours()
mybag.count_socks()
mybag.count_pairs()
print(mybag.bag)
print(mybag.pairs)
print(mybag.odds)
