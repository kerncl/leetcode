#Question: Easy
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''
from typing import List
import logging


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        for value in set(nums):
            if nums.count(value) / length >= 0.5:
                return value
        return None


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    logging.info(f'{result.majorityElement(nums)} has repeated the most number')