# Question: Easy
'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
'''
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix) == 1 or len(matrix[0]) ==1:
            return True
        for i in range (1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True


matrix = [
    [1, 2, 3, 4],
    [5, 1, 2, 3],
    [9, 5, 1, 2]
]
matrix2 = [[18],[66]]
matrix3 = [[11,74,0,93],[40,11,74,7]]
result = Solution()
print(f'ToeplitzMatix {result.isToeplitzMatrix(matrix3)}')