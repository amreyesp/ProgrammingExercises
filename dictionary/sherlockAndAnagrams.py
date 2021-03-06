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
from math import factorial

class NewAnagram:

    def __init__(self):
        self.string = ''
        self.anagrams = {}

    def read_input(self,input):
        self.string = input

    def find_substrings(self,length):
        aux_anagram = ''
        aux_index = []
        for index, letter in enumerate(self.string):
            if index <= len(self.string) - length:
                aux_anagram = self.string[index:index+length]
                for i in range(length):
                    aux_index.append(index+i)
                if aux_anagram not in self.anagrams:
                    self.anagrams[aux_anagram] = [aux_index]
                else:
                    self.anagrams[aux_anagram].append(aux_index)
                aux_anagram = ''
                aux_index = []

    def all_substrings(self):
        length = len(self.string)
        for index in range(length-1):
            self.find_substrings(index+1)

    def find_anagram(self,mykey):
        for key in self.anagrams.copy():
            if key != mykey:
                aux_anagram = ''.join(sorted(key))
                if aux_anagram == ''.join(sorted(mykey)):
                    self.anagrams[mykey]=self.anagrams[mykey]+self.anagrams[key]
                    self.anagrams.pop(key)
        return self.anagrams

    def find_all_anagrams(self):
        for key in self.anagrams.copy():
            if key in self.anagrams:
                self.find_anagram(key)
            #delete key if it doesnt have a pair
                if len(self.anagrams[key]) < 2:
                    self.anagrams.pop(key)

    def count_pairs(self):
        pairs = 0
        for key in self.anagrams:
            number_of_elements = len(self.anagrams[key])
            if number_of_elements == 2:
                pairs += 1
            else:
                #estimate number of pairs through a combination
                combination = factorial(number_of_elements) / (factorial(number_of_elements - 2) * factorial(2))
                pairs += combination
        return pairs

def main():
    my_anagram = NewAnagram()
    my_anagram.read_input('cdcd')
    my_anagram.all_substrings()
    my_anagram.find_all_anagrams()
    pairs = my_anagram.count_pairs()
    print('The number of anagrams pairs for',my_anagram.string,'is:',pairs)

if __name__=='__main__':
    main()
