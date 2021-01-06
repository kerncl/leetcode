#Question: Easy
'''
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.
'''
from typing import List
import logging


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)
        for value in set(arr):
            if arr.count(value) / length > 0.25:
                return value


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    result = Solution()
    logging.info(f'{result.findSpecialInteger(arr)} appear more than 25% in the list')