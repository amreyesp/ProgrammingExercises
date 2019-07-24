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



    def substring_anagrams(self,substring,length):
        for character in substring:
            pass

    def anagrams(self,length):
        for letter in self.string:
            self.substring_anagrams(letter,length)
