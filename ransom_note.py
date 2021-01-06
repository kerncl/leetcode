#Question: Easy:
'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.
'''
import logging
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = Counter(magazine)
        for char in ransomNote:
            if magazine_counter[char] < ransomNote.count(char):
                return False
        return True


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    ransomNote = 'a'
    magazine = 'b'
    result = Solution()
    logging.info(f'Able found in magzine {result.canConstruct(ransomNote, magazine)}')