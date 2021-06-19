#Question: Easy
'''
An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.
'''
from typing import List
import logging


class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        # check if either rectangle is actually a line
        if (rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]):
            # the line cannot have positive overlap
            return False

        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top


if __name__ == '__main__':
    format ='%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    rec3 = [0, 0, 1, 1]
    rec4 = [1, 0, 2, 1]
    rec5 = [7, 8, 13, 15]
    rec6 = [10, 8, 12, 20]
    logging.info(f'Is rectangle overlap: {result.isRectangleOverlap(rec5, rec6)}')