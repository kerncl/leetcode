#Question:Easy
'''Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.'''
from typing import List
import logging


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row_number in range(numRows):
            row = [None for _ in range(row_number+1)]
            row[0], row[-1] = 1, 1
            for coloumn in range(1,len(row)-1):
                row[coloumn] = triangle[row_number-1][coloumn-1] + triangle[row_number-1][coloumn]
            triangle.append(row)
        return triangle

if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    numRows = 5
    result = Solution()
    logging.info(f'Output triangle : {result.generate(numRows)}')