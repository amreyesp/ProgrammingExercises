"""Left Rotation"""
"""
A left rotation operation on an array shifts each of the array's elements 1 unit
to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5],
then the array would become [3,4,5,1,2].
Given an array a of n integers and a number, d, perform d left rotations on the
array. Return the updated array to be printed as a single line of space-separated
integers.
Credits: www.hackerrank.com
"""
import random
class NewArray:

    def __init__(self):
        self.array = []
        self.size = 0
        self.distance = 0

    def fillArray(self,size):
        self.array = [element for element in range(size)]
        self.size=len(self.array)

    def rotateLeft(self,distance):
        [self.array.insert(0,self.array.pop()) for i in range(distance)]
        return self.array

    def fastRotation(self,distance):
        left_subarray=self.array[: self.size-distance]
        right_subarray=self.array[self.size-distance :]
        return right_subarray+left_subarray
