#Question: Easy
"""
Given two strings s and t , write a function to determine if t is an anagram of s.
"""
from typing import List
from collections import Counter
import logging


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = Counter(s)
        t_dict = Counter(t)
        s_dict.subtract(t_dict)
        for k, v in s_dict.items():
            if v != 0:
                return False
        return True


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.INFO)
    result = Solution()
    s = "anagram"
    t = "nagaram"
    s2 = 'ab'
    t2 = 'a'
    logging.info(f'Is Valid Anagram: {result.isAnagram(s,t)}')
