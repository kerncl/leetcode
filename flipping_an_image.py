#Question: easy
#Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
#To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
#To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        reversed_row = []
        for row in A:
            reversed_row.append(list(reversed(row)))
        for row in range(len(reversed_row)):
            for digit in range(len(reversed_row)):
                if reversed_row[row][digit] == 1:
                    reversed_row[row][digit] = 0
                elif reversed_row[row][digit] == 0:
                    reversed_row[row][digit] = 1
        return reversed_row

Img = [[1,1,0],[1,0,1],[0,0,0]]
result = Solution()
flip_image = result.flipAndInvertImage(Img)
print('fliped image:', flip_image)