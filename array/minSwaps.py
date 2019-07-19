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
        self.sorted_array = []
        self.size = 0
        self.swaps = 0
        self.algorithmcalls = 0

    def fillArray(self, size):
        self.array = [element+1 for element in range(size)]
        self.size = len(self.array)

    def unsortArray(self):
        random.shuffle(self.array)

    def mergeSort(self,list):
        self.algorithmcalls += 1
        if len(list) < 2:
            return list
        else:
            middle = len(list)//2
            right = self.mergeSort(list[:middle])
            left = self.mergeSort(list[middle:])
            return self.merge(right,left)

    def merge(self,list1,list2):
        self.sorted_array = []
        i,j = 0,0
        while (i < len(list1) and j < len(list2)):
            if (list1[i] < list2[j]):
                self.sorted_array.append(list1[i])
                i += 1
            else:
                self.sorted_array.append(list2[j])
                j += 1

        self.sorted_array += list1[i:]
        self.sorted_array += list2[j:]
        return self.sorted_array

    def position_distance(self,array):
        position_array = []
        for element in array:
            position_array.append(array.index(element)+1-element)
        return position_array

    def swap(self,array):
        position_array = self.position_distance(array)
        pos1, pos2  = position_array.index(min(position_array)), position_array.index(max(position_array))
        array[pos2], array[pos1] = array[pos1], array[pos2]
        return array

    def minSwaps(self):
        final_array = self.array.copy()
        final_array.sort()
        self.sorted_array = self.array.copy()
        while self.sorted_array != final_array:
            self.sorted_array = self.swap(self.sorted_array)
            self.swaps += 1
        return self.sorted_array
