# Question: Easy
'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
'''
from typing import List
import logging


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    total += self.perimeter(grid, i, j)
        return total

    def perimeter(self, grid: List[List[int]], i: int, j: int) -> int:
        count = 4
        if (i + 1) < len(grid) and grid[i + 1][j] == 1:
            count -= 1
        if (i - 1) >= 0 and grid[i - 1][j] == 1:
            count -= 1
        if (j + 1) < len(grid[i]) and grid[i][j + 1] == 1:
            count -= 1
        if (j - 1) >= 0 and grid[i][j - 1] == 1:
            count -= 1
        return count


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    result = Solution()
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    grid2 = [[1]]
    logging.info(f'Land Perimeter: {result.islandPerimeter(grid)}')
