# Question: Easy
"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.
"""
from typing import List
import logging
from itertools import combinations


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        n = len(A)
        for i in range(n-2):
            if A[i] < A[i+1] + A[i+2]:
                return  A[i] + A[i+1] + A[i+2]
        return 0


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    A = [3, 6, 2, 3]
    logging.info(f'Perimeter: {result.largestPerimeter(A)}')
