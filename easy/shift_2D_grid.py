#Questions: Easy
"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.
"""
from typing import List
import logging


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        flatten_matrix = [colounm for row in grid for colounm in row]
        count = 0
        for _ in range(k):
            temp = flatten_matrix.pop()
            flatten_matrix.insert(0, temp)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                grid[r][c] = flatten_matrix[count]
                count +=1
        return grid


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    logging.info(f'Shifted Matrix {result.shiftGrid(grid, k)}')

