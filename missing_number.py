# Question: Easy
'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''
from typing import List
import logging


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for index in range(len(nums)+1):
            if index not in nums_set:
                return index



if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    nums = [3, 0, 1]
    result = Solution()
    logging.info(f'Missing value: {result.missingNumber(nums)}')
