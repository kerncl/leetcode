# Question: Easy
'''
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
'''
from typing import List
from itertools import accumulate
import logging


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_front = [i for i in accumulate(nums)]
        sum_end = [j for j in accumulate(nums[::-1])]
        logging.info(f'sum_front:{sum_front}\n \t \tsum_end:{sum_end} ')
        for index, value in enumerate(sum_front):
            if value in sum_end:
                index_end = sum_end[::-1].index(value)
                if (index + 1) + 1 + (len(nums) - index_end) == len(nums):
                    logging.info(f'matches index:{index}; index_end:{index_end}; sum value:{value}')
                    return index + 1
        return -1


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    nums2 = [1, 2, 3]
    nums3 = [-1, -1, -1, 0, -1, -1]
    nums4 = [-1, -1, -1, 0, 1, 1]
    logging.info(f'{result.pivotIndex(nums4)}')
