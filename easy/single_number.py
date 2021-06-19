#Question: Easy
'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for value in set(nums):
            if nums.count(value) == 1:
                return value


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        diff = 0
        for num in nums:
            diff ^=num
        return diff

nums = [4, 1, 2, 1, 2]
result = Solution()
print(f'Single Number {result.singleNumber(nums)}')
result2 = Solution2()
print(f'Single Number {result2.singleNumber(nums)}')