#Question: easy
#Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
from typing import List
import time


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([nums[i] for i in range(0, len(nums), 2)])


nums = [1, 4, 3, 2]
result = Solution()
start = time.perf_counter_ns()
array_min = result.arrayPairSum(nums)
time1 = time.perf_counter_ns() - start
print('array:', array_min)
print('Total use time: {sec} ms' .format(sec=time1/1000))