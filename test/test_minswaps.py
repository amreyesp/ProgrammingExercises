import unittest

# Can't use from... import directly since the file is into another folder
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from array.minSwaps import newArray

class TestMinimumSwaps(unittest.TestCase):

    def setUp(self):
        self.myArray = newArray()

    def test_fillArray(self):
        self.myArray.fillArray(size=4)
        self.assertEqual([1,2,3,4],self.myArray.array)
        self.assertEqual(4,self.myArray.size)

    def test_unsortArray(self):
        self.myArray.array = [1,2,3,4]
        self.myArray.unsortArray()
        self.assertTrue([1,2,3,4] != self.myArray.array)

    def test_mergeSort(self):
        self.myArray.array = [4,3,1,2]
        self.myArray.size = len(self.myArray.array)
        self.myArray.mergeSort(self.myArray.array)
        #print('The sorted array is: ',self.myArray.sorted_array)
        #print('The solution required ',self.myArray.algorithmcalls,' Merge Sort function calls.')
        self.assertEqual([1,2,3,4],self.myArray.sorted_array)

    def test_position_distance(self):
        self.myArray.array = [4,3,1,2]
        self.myArray.size = len(self.myArray.array)
        aux_array= self.myArray.position_distance(self.myArray.array)
        self.assertEqual([-3,-1,2,2],aux_array)

    def test_first_iter_minSwaps(self):
        self.myArray.array = [4,3,1,2]
        self.myArray.size = len(self.myArray.array)
        aux_array = self.myArray.swap(self.myArray.array)
        self.assertEqual([1,3,4,2],aux_array)

    def test_minSwaps(self):
        self.myArray.array = [4,3,1,2]
        self.myArray.size = len(self.myArray.array)
        self.myArray.minSwaps()
        self.assertEqual(3,self.myArray.swaps)
        print('The sorted array is: ',self.myArray.sorted_array)
        print('The solution required ',self.myArray.swaps,'swaps.')

    def test_minSwaps_input1(self):
        self.myArray.array = [2,3,4,1,5]
        self.myArray.size = len(self.myArray.array)
        self.myArray.minSwaps()
        self.assertEqual(3,self.myArray.swaps)
        print('The sorted array is: ',self.myArray.sorted_array)
        print('The solution required ',self.myArray.swaps,'swaps.')

    def test_minSwaps_input2(self):
        self.myArray.array = [1,3,5,2,4,6,7]
        self.myArray.size = len(self.myArray.array)
        self.myArray.minSwaps()
        self.assertEqual(3,self.myArray.swaps)
        print('The sorted array is: ',self.myArray.sorted_array)
        print('The solution required ',self.myArray.swaps,'swaps.')
