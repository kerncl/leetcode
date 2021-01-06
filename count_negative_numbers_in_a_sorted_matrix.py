#Question: easy
#Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
#Return the number of negative numbers in grid.
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        for row in grid:
            for num in row:
                if num < 0:
                    neg +=1
        return  neg


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
result = Solution()
number_neg = result.countNegatives(grid)
print('Number of negative value:', number_neg)