#Question: Easy
'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
'''
from typing import List
import logging


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # gradient = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        if len(coordinates) == 2:
            return True
        y_diff = coordinates[1][1] - coordinates[0][1]
        x_diff = coordinates[1][0] - coordinates[0][0]
        if not x_diff:
            gradient = 'straight line'
        else:
            gradient = y_diff / x_diff
        for index in range(1, len(coordinates)-1):
            y_diff = (coordinates[index+1][1] - coordinates[index][1])
            x_diff = (coordinates[index + 1][0] - coordinates[index][0])
            if not x_diff:
                if gradient != 'straight line':
                    return False
                continue
            elif gradient != y_diff / x_diff:
                return False
        return True


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    coordinates2= [[0, 0], [0, 1], [0, -1]]
    logging.info(f'Is straight line ? :{result.checkStraightLine(coordinates2)}')