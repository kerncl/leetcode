#Question: Easy
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
from typing import List
from collections import Counter
import logging


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_nums = Counter(nums)
        for index, num in enumerate(nums):
            diff = target - num
            set_nums[num] = set_nums[num] - 1
            if diff in set_nums.keys() and set_nums[diff] > 0:
                nums[index] = None
                return [index, nums.index(diff)]


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    nums = [3, 2, 4]
    target = 6
    nums2 = [2, 7, 11, 15]
    target2 = 9
    nums3 = [3, 3]
    target3 = 6
    result = Solution()
    logging.info(f'Two number of sum: {result.twoSum(nums3, target3)}')