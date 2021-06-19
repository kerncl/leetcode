#Question: easy
#Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sorted_list = sorted(nums)
        max = (sorted_list[len(sorted_list)-2]-1)*(sorted_list[len(sorted_list)-1]-1)
        return max

nums = [3,4,5,2]
result = Solution()
max = result.maxProduct(nums)
print('Product of two maximum integer in array:', max)