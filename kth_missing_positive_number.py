#Question:Easy
'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.
'''
from typing import List
import logging


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        index = 1
        while True:
            if index not in arr:
                count +=1
                if count == k:
                    return index
            index +=1


if __name__ == '__main__':
    format = '%(asctime)s :%(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    arr = [2, 3, 4, 7, 11]
    k = 5
    result = Solution()
    logging.info(f'THe missing positive integer is {result.findKthPositive(arr,k)}')