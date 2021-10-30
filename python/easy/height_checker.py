#Question: easy
#Students are asked to stand in non-decreasing order of heights for an annual photo.
#Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.
#Notice that when a group of students is selected they can reorder in any possible way between themselves and the non selected students remain on their seats.
from typing import List
import time


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_height = sorted(heights)
        if sorted_height == heights:
            return 0
        count = 0
        for i in range(len(heights)):
            if heights[i] != sorted_height[i]:
                count += 1
        return count


heights = [1,1,4,2,1,3]
result = Solution()
start = time.perf_counter_ns()
checker = result.heightChecker(heights)
time1 = time.perf_counter_ns() - start
print('Number of student needed to be shifted:', checker)
print('Total use time: {sec} ms' .format(sec=time1/1000))