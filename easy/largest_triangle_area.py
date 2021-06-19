# Question: Easy
"""
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.
"""
from typing import List
import logging
import math
from itertools import combinations


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p1, p2, p3):
            one = p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1]
            two = p1[1]*p2[0]+p2[1]*p3[0]+p3[1]*p1[0]
            return abs(one -two)/2
        ans = 0

        for p1, p2, p3 in combinations(points,3):
            ans = max(ans, area(p1,p2,p3))
        return ans


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    points2 = [[4, 6], [6, 5], [3, 1]]
    logging.info(f'Area of the triangle: {result.largestTriangleArea(points)}')
