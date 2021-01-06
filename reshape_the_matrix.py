#Question: Easy
"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""
from typing import List
import logging


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r*c:
            return nums
        flatten_matrix = [nums[row][coloumn] for row in range(len(nums)) for coloumn in range(len(nums[0]))]
        count = 0
        reshape_matrix = []
        for r_ in range(r):
            row_list = []
            for c_ in range(c):
                row_list.append(flatten_matrix[count])
                count += 1
            reshape_matrix.extend([row_list])
        return reshape_matrix


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    nums =[[1, 2], [3, 4]]
    r = 1
    c = 4
    r2 = 2
    c2 = 4
    logging.info(f'Reshape matrix: {result.matrixReshape(nums, r, c)}')