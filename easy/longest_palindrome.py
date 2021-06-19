#Questions : Easy
'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
'''
import logging
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_counter = Counter(s)
        if len(s_counter) == 1:
            return len(s)
        for value in s_counter.values():
            if value == 2:
                return len(s)-1


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    s = 'abccccdd'
    result = Solution()
    logging.info(f'longest distance : {result.longestPalindrome(s)}')