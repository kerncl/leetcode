#Question :Easy
'''
Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.
'''
from typing import List
import logging


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for row_num in range(rowIndex+1):
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1
            for column_num in range(1,len(row)-1):
                row[column_num] = triangle[row_num-1][column_num-1] + triangle[row_num-1][column_num]
            triangle.append(row)
        return triangle[-1]



if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    rowIndex = 3
    rowIndex2 = 0
    result = Solution()
    logging.info(f'Row index number : {result.getRow(rowIndex)}')