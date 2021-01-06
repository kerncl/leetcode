#Question:
#On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.
#You can move according to the next rules:
#In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
#You have to visit the points in the same order as they appear in the array.
from typing import List


class Solution:
    def modulus(self, num):
        if num < 0:
            return int(-num)
        return num

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        distance = 0
        for i in range(1, len(points)):
            x_distance = points[i][0] - points[i-1][0]
            y_distance = points[i][1] - points[i-1][1]
            x_distance = self.modulus(x_distance)
            y_distance = self.modulus(y_distance)
            if x_distance > y_distance:
                temp_distance = x_distance
            else:
                temp_distance = y_distance
            distance = distance + temp_distance
        return distance



points = [[1,1],[3,4],[-1,0]]
result = Solution()
total_distance = result.minTimeToVisitAllPoints(points)
print('Total distance travel:', total_distance)