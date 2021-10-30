"""
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.
"""
import logging
import sys
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # generate empty ans mat
        ans = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]

        def sum_inrange(row_range, col_range):
            sum_val = 0
            for i in row_range:
                for j in col_range:
                    sum_val += mat[i][j]
            return sum_val

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                range_row = range(max(i-k, 0), min(i+k+1, len(mat)))
                range_col = range(max(j-k, 0), min(j+k+1, len(mat[0])))
                ans[i][j] = sum_inrange(range_row, range_col)

        return ans


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    format = '%(asctime)s [%(levelname)s]: %(message)s'

    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    test_pattern = [([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]], 1,
                     [[12, 21, 16],
                      [27, 45, 33],
                      [24, 39, 28]]),
                    ([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]], 2,
                     [[45, 45, 45],
                      [45, 45, 45],
                      [45, 45, 45]])]

    for mat, k, expected in test_pattern:
        solution = Solution()
        myresult = solution.matrixBlockSum(mat, k)
        assert myresult == expected, log.error(f'Expected result: {expected}, but received: {myresult}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
