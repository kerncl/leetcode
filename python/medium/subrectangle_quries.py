"""
Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in the constructor and supports two methods:

1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)

Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and bottom right coordinate is (row2,col2).
2. getValue(int row, int col)

Returns the current value of the coordinate (row,col) from the rectangle.
"""
from typing import List
from pprint import pprint
import logging
import sys


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for x in range(row1, row2 + 1):
            for y in range(col1, col2 + 1):
                self.rect[x][y] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rect[row][col]

    def __str__(self):
        return str(self.rect)


class SubrectangleQueries2:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle
        self.new_format = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.new_format.append([row1, col1, row2, col2, newValue])

    def getValue(self, row: int, col: int) -> int:
        for format in self.new_format[::-1]:
            row1, col1, row2, col2, newValue = format
            if row1 <= row <= row2 and col1 <= col <= col2:
                return newValue
        return self.rect[row][col]

    # def __str__(self):
    #     return str(self.rect)


if __name__ == '__main__':
    format = '%(asctime)s [%(levelname)s]: %(message)s'
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(logging.Formatter(format))

    log.addHandler(stream)
    result = SubrectangleQueries2([[1, 2, 1],
                                  [4, 3, 4],
                                  [3, 2, 1],
                                  [1, 1, 1]]
                                 )
    assert result.getValue(0, 2) == 1, log.error('Invalid return value expected value 1')
    result.updateSubrectangle(0, 0, 3, 2, 5)
    # log.info(result)
    assert result.getValue(0, 2) == 5, log.error('Invalid return value expected value 5')
    assert result.getValue(3, 1) == 5, log.error('Invalid return value expected value 5')
    result.updateSubrectangle(3, 0, 3, 2, 10)
    # log.info(result)
    assert result.getValue(3, 1) == 10, log.error('Invalid return value expected value 10')
    assert result.getValue(0, 2) == 5, log.error('Invalid return value expected value 5')

    while log.handlers:
        handler = log.handlers[0]
        log.removeHandler(handler)