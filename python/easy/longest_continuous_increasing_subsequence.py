# Question: Easy
'''
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
'''
from typing import List
import logging


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        max_count = 0
        if nums:
            temp_digit = nums.pop(0)
        else:
            return 0
        for digit in nums:
            if temp_digit < digit:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
            temp_digit = digit
        return max(max_count, count)


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    nums = [1, 3, 5, 4, 7]
    nums2 = [1, 3, 5, 7]
    result = Solution()
    logging.info(f'Is continuous: {result.findLengthOfLCIS(nums2)}')
