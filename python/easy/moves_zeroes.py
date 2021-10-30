#Questions: Easy
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""
from typing import List
import logging


class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        no_zeros = nums.count(0)
        for _ in range(no_zeros):
            nums.remove(0)
            nums.append(0)
        return nums

if __name__ == '__main__':
    format = '%(asctime)s: %(mesaages)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    nums = [0, 1, 0, 3, 12]
    result = Solution()
    logging.info(f'After moves zeros: {result.moveZeroes(nums)}')
