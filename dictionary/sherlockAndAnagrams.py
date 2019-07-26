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
        self.anagrams = {}

    def read_input(self,input):
        self.string = input

    def anagrams_one_letter(self,length):
        for index, letter in enumerate(self.string):
            #add key
            if letter not in self.anagrams:
                self.anagrams[letter] = [[index]]
            #add value if key already exists
            else:
                self.anagrams[letter].append([index])

    def id_anagrams(self,length):
        #id potential anagrams: step over each character and create substring
        #in this functions substrings can be set joining not consecutively characters
        for pivot in range(len(self.string)):
            aux_anagram = self.string[pivot]
            aux_index = [pivot]
            for index, character in enumerate(self.string[pivot+1:]):
                if len(aux_anagram) < length:
                    if index+pivot+1 not in aux_index:
                        aux_anagram = aux_anagram + character
                        aux_index.append(index+pivot+1)
                if len(aux_anagram) == length:
                    if aux_anagram not in self.anagrams:
                        self.anagrams[aux_anagram] = [aux_index]
                    else:
                        self.anagrams[aux_anagram].append(aux_index)
                    aux_anagram = self.string[pivot]
                    aux_index = [pivot]


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

    def pair_anagrams(self):
        self.anagrams_one_letter(length=1)
        for key in self.anagrams.copy():
            if len(self.anagrams[key]) < 2:
                self.anagrams.pop(key)
        length = len(self.string)
        for index in range(length-2):
            self.find_substrings(index+2)

    def count_pairs(self,mykey):
        for key in self.anagrams.copy():
            aux_anagram = ''.join(sorted(key))
            print(aux_anagram)
            print(key)
            #for right_key in self.anagrams.copy():
        return 0
