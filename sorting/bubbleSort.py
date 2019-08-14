"""Sorting: Bubble Sort"""
"""
Considering the Bubble sort algorithm, given an array of integers, sort the array
in ascending order using it. Once sorted, print the following three lines:
1.Array is sorted in numSwaps swaps., where  numSwaps is the number of swaps that took place.
2.First Element: firstElement, where firstElement is the first element in the sorted array.
3.Last Element: lastElement, where lastElement is the last element in the sorted array.
Credits: www.hackerrank.com
"""

class NewSort:

    def __init__(self):
        self.array = []
        self.minswaps = 0

    def bubble_algorithm(self,array):
        n = len(array)
        for i in range(n):
            for j in range(n-1):
                if (array[j] > array[j + 1]):
                    a1 = array[j]
                    a2 = array[j + 1]
                    array[j] = a2
                    array[j+1] = a1
        self.array = array

    def calc_minswaps(self,array):
        n = len(array)
        for i in range(n):
            for j in range(n-1):
                if (array[j] > array[j + 1]):
                    a1 = array[j]
                    a2 = array[j + 1]
                    array[j] = a2
                    array[j+1] = a1
                    self.minswaps += 1
        self.array = array

    def print_result(self):
        first = self.array[0]
        last = self.array[-1]
        return [first,last]
