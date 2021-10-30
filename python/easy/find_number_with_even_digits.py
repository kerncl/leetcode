#Question: easy
#Given an array nums of integers, return how many of them contain an even number of digits.
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        number_even = 0
        for number in nums:
            if number // 10:
                if number % 2 == 0:
                    number_even += 1
        return number_even


nums = [12, 345, 2, 6, 7896]
result = Solution()
Number_ofeven = result.findNumbers(nums)
print('Number of even number:', Number_ofeven)