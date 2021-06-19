#Question: easy
#Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
from typing import List
import time

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        square = [value**2 for value in A]
        square.sort()
        return square

n = [-7,-3,2,3,11]
result = Solution()
start = time.perf_counter_ns()
square_list = result.sortedSquares(n)
time1 = time.perf_counter_ns() - start
print('Square list:', square_list)
print('Total use time {sec} ms' .format(sec=time1/1000))