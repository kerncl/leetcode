"""
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.
"""
import logging
import sys
from typing import List
from operator import itemgetter


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=itemgetter(0))
        return max(points[i+1][0] - points[i][0] for i in range(len(points)-1))


class Solution2:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_points = sorted(set([x for x, _ in points]))
        if len(x_points) == 1:
            return 0
        return max(x_points[i+1] - x_points[i] for i in range(len(x_points)-1))


class Solution3:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_points = sorted([x for x, _ in points])
        return max(x_points[i+1] - x_points[i] for i in range(len(x_points)-1))


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)

    format = '%(asctime)s [%(levelname)s]: %(message)s'
    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    test_pattern = [([[8, 7], [9, 9], [7, 4], [9, 7]], 1),
                    ([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]], 3)]
    for point, expected_result in test_pattern:
        solution = Solution2()
        myresult = solution.maxWidthOfVerticalArea(points=point)
        assert myresult == expected_result,\
            log.error(f'Expected result: {expected_result}, but received : {expected_result}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
