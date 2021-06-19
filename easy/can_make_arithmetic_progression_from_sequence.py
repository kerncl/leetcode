#Question: easy
#Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
#Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.
from typing import List
import time

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort(reverse=True)
        r = arr[0] - arr[1]
        for i in range(1,len(arr)):
            if arr[i-1] - arr[i] != r:
                return False
        return True


arr = [1, 2, 4]
result = Solution()
start = time.perf_counter_ns()
ap = result.canMakeArithmeticProgression(arr)
time1 = time.perf_counter_ns() - start
print('is AP ?', ap)
print('Total Use time: {sec} ms' .format(sec=time1/1000))
