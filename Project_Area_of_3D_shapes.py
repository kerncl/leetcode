# Question: Easy
'''
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
Now we view the projection of these cubes onto the xy, yz, and zx planes.
A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.
Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
Return the total area of all three projections.
'''
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xz_view = 0
        reverse_grid = []
        for _ in range(len(grid)):
            reverse_grid.append(['']*len(grid))
        for row in grid:
            xz_view += max(row)
            for column in row:
                if column != 0:
                    xz_view += 1
        for x in range(len(grid)):
            for y in range(len(grid)):
                reverse_grid[x][y] = grid[y][x]
        for _ in reverse_grid:
            xz_view += max(_)
        return xz_view


grid = [[1, 2], [3, 4]]
result = Solution()
print(f'Total Area: {result.projectionArea(grid)}')
