# Question: Easy
'''
Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.

A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
'''
from typing import List
import logging


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        final_list = 0
        for row in mat:
            if row.count(1) > 1:
                pass
            else:
                for row_index, row_value in enumerate(row):
                    count = 0
                    if row_value:
                        for colunm_index in range(len(mat)):
                            if mat[colunm_index][row_index] == 1:
                                count += 1
                        if count == 1:
                            final_list += 1
        return final_list


if __name__ == "__main__":
    format = "%(asctime)s:  %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)
    mat = [[1, 0, 0],
           [0, 0, 1],
           [1, 0, 0]]
    mat2 = [[0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0]]
    result = Solution()
    print(f'Special Position: {result.numSpecial(mat2)}')
