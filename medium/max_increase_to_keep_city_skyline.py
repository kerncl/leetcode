"""
You are given an n x n integer matrix grid where grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well.

In the end, the skyline when viewed from all four directions of the grid (i.e., top, bottom, left, and right) must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance.

Return the maximum total sum that the height of the buildings can be increased.

Note that all buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.
"""
import logging
import sys
from typing import List


class Solution:

    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_row = [max(row) for row in grid]
        max_col = [max(grid[row_i][col_i] for row_i in range(len(grid[0]))) for col_i in range(len(grid))]
        diff = 0
        for row_i in range(len(grid[0])):
            for col_i in range(len(grid)):
                min_val = min(max_row[row_i], max_col[col_i])
                if min_val > grid[row_i][col_i]:
                    diff += min_val - grid[row_i][col_i]
        return diff


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)

    format = '%(asctime)s [%(levelname)s]: %(message)s'
    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    test_pattern = [([[3, 0, 8, 4],
                      [2, 4, 5, 7],
                      [9, 2, 6, 3],
                      [0, 3, 1, 0]], 35),
                    ([[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]], 0)]
    for grid, expected_output in test_pattern:
        result = Solution()
        myresult = result.maxIncreaseKeepingSkyline(grid)
        assert myresult  == expected_output, \
            log.error(f'Expected result: {expected_output}, but received {myresult}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
