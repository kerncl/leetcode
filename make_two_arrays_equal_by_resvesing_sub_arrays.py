#Question: easy
#Given two integer arrays of equal length target and arr.
#In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.
#Return True if you can make arr equal to target, or False otherwise.
from typing import List
import time

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if set(target) != set(arr):
            return False
        else:
            for value in target:
                if target.count(value) != arr.count(value):
                    return False
                return True

class Solution2:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        if target == arr:
            return True
        else:
            return False


target = [1, 2, 2, 3]
arr = [1, 1, 2, 3]
result = Solution()
start = time.perf_counter_ns()
match = result.canBeEqual( target=target, arr=arr)
time1 = time.perf_counter_ns() - start
print('Targer match with arr:', match)
print('Total use time {sec} ns' .format(sec=time1))
result2 = Solution2()
start = time.perf_counter_ns()
match2 = result2.canBeEqual( target=target, arr=arr)
time2 = time.perf_counter_ns() - start
print('Targer match with arr:', match2)
print('Total use time: {sec} ns' .format(sec=time2))