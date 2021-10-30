#Question: easy
#Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
#A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
from typing import List
import time


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        column_max = None
        for row in matrix:
            row_min = None
            for val in row:
                if row_min == None:
                    row_min =val
                if row_min > val:
                    row_min = val
            if column_max == None:
                column_max = row_min
            if column_max < row_min:
                column_max = row_min
        return column_max


matrix = [[3,7,8],[9,11,13],[15,16,17]]
result = Solution()
start = time.perf_counter_ns()
lucky_number = result.luckyNumbers(matrix)
print('Lucky Number:', lucky_number)
print('Total use time {sec} ms' .format(sec=lucky_number/1000))