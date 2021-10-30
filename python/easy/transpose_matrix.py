# Question: Easy
"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
"""
from typing import List
import logging


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        B = []
        for _ in range(len(A[0])):
            B.extend([[0]*len(A)])
        logging.info(B)
        for row in range(len(A)):
            for coloumn in range(len(A[0])):
                B[coloumn][row] = A[row][coloumn]
        return [[A[r][c] for r in range(len(A))] for c in range(len(A[0]))]


if __name__ == "__main__":
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    A1 = [[1, 2, 3], [4, 5, 6]]
    result = Solution()
    logging.info(f'Transpose Matrix {result.transpose(A1)}')
