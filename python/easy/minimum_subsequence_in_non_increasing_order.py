#Question: (Easy)
'''
Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence.
#If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.
#Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.
'''
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        nums.sort(reverse=True)
        for i in range(len(nums)):
            sum_front = sum(x for x in nums[:i+1])
            sum_end = sum(x for x in nums[i+1:len(nums)])
            if sum_front > sum_end:
                return nums[:i+1]




nums = [4,4,7,6,7]
result = Solution()
print(result.minSubsequence(nums=nums))




