# Question: Easy
'''
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.
'''
from typing import List
import logging


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        if all(m >= 2*x for x in nums if x != m):
            return nums.index(m)
        return -1


if __name__ == '__main__':
    format = '%(asctime)s : %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    nums = [3, 6, 1, 0]
    nums2 = [0, 0, 0, 1]
    logging.info(f'{result.dominantIndex(nums2)}')
