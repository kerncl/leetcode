#Questions: easy
#Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.
from typing import List
import time


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(arr))!=len(arr)


arr = [3,5,-2,-3,-6,-6]
result = Solution()
start = time.perf_counter_ns()
unq = result.uniqueOccurrences(arr)
time1 = time.perf_counter_ns() - start
print('Is unquie:', unq)
print('Total time used: {sec} ms' .format(sec=time1/1000))