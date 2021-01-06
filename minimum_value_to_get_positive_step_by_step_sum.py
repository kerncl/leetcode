# Question: Easy
'''
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.
'''
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        num_list = []
        for index in range(len(nums)):
            if not index:
                diff = nums[index]
            else:
                diff += nums[index]
            num_list.append(diff)
        min_value = min(num_list)
        if min_value < 1:
            return abs(min_value)+1
        else:
            return 1


nums = [-3, 2, -3, 4, 2]
nums2 = [1, -2, -3]
nums3 = [2, 3, 5, -5, -1]
result = Solution()
print(f'Minimum Positive: {result.minStartValue(nums)}')
