# Question: Easy
"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""
from typing import List
import logging


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.INFO)
    result = Solution()
    nums = [1, 2, 3, 1]
    logging.info(f'Is Duplicate {result.containsDuplicate(nums)}')
