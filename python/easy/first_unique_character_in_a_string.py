#Question: Easy
'''
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
'''
from collections import Counter
import logging


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count = Counter(s)
        for key,value in s_count.items():
            if value == 1:
                return s.index(key)
        return -1


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    s = 'loveleetcode'
    logging.info(f'Number of repeating character: {result.firstUniqChar(s)}')