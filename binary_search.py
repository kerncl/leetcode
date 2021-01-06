#Question: Easy
'''
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.
'''
from typing import List
import logging


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = Solution()
    logging.info(f'Found at index {result.search(nums=nums, target=target)}')