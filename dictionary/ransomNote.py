"""Ransom Note"""
"""
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be
traced back to him through his handwriting. He found a magazine and wants to
know if he can cut out whole words from it and use them to create an untraceable
replica of his ransom note. The words in his note are case-sensitive and he must
use only whole words available in the magazine. He cannot use substrings or
concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if
he can replicate his ransom note exactly using whole words from the magazine;
otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only
"attack at dawn". The magazine has all the right words, but there's a case
mismatch. The answer is No.
Credits: www.hackerrank.com
"""

class NewNote:

    def __init__(self):
        self.magazine_size = 0
        self.note_size = 0
        self.magazine = []
        self.note = []

    def read_input(self,size_mag,size_note,mag_words,note_words):
        self.magazine_size = size_mag
        self.note_size = size_note

        words = mag_words.split()
        for word in words:
            self.magazine.append(word)

        words = note_words.split()
        for word in words:
            self.note.append(word)

    def check_magazine(self):
        for word_note in self.note:
            if word_note in self.magazine:
                self.magazine.remove(word_note)
            else:
                return 'No'
        return 'Yes'
