"""
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
"""
import logging
import sys
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        max_col = len(mat[0])
        max_row = len(mat)
        # col
        for _ in range(max_row-2, 0, -1):
            i = _
            j = 0
            diag_list = []
            while j < max_col and i < max_row:
                diag_list.append(mat[i][j])
                j += 1; i +=1;
            diag_list.sort(reverse=True)
            i = _
            j = 0
            while j < max_col and i < max_row:
                mat[i][j] = diag_list.pop()
                j += 1; i +=1;

        # row
        for _ in range(max_col-1):
            j = _
            i = 0
            diag_list = []
            while j < max_col and i < max_row:
                diag_list.append(mat[i][j])
                j += 1; i +=1;
            diag_list.sort(reverse=True)
            j = _
            i = 0
            while j < max_col and i < max_row:
                mat[i][j] = diag_list.pop()
                j += 1; i +=1;

        return mat


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)

    format = '%(asctime)s [%(levelname)s]: %(message)s'
    stream = logging.StreamHandler(stream=sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    test_pattern = [([[3, 3, 1, 1],
                      [2, 2, 1, 2],
                      [1, 1, 1, 2]],
                     [[1, 1, 1, 1],
                      [1, 2, 2, 2],
                      [1, 2, 3, 3]]),
                    ([[11, 25, 66, 1, 69, 7],
                      [23, 55, 17, 45, 15, 52],
                      [75, 31, 36, 44, 58, 8],
                      [22, 27, 33, 25, 68, 4],
                     [84, 28, 14, 11, 5, 50]],
                    [[5, 17, 4, 1, 52, 7],
                     [11, 11, 25, 45, 8, 69],
                     [14, 23, 25, 44, 58, 15],
                     [22, 27, 31, 36, 50, 66],
                     [84, 28, 75, 33, 55, 68]])]

    for mat, expected_result in test_pattern:
        solution = Solution()
        myresult = solution.diagonalSort(mat)
        assert myresult == expected_result,\
            log.error(f'Expected result: {expected_result}, but received {myresult}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
