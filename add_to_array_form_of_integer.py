#Question:Easy
'''
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.
'''
from typing import List
import logging

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        num = ''.join([str(a) for a in A])
        return list(str(int(num)+K))


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    A = [1, 2, 0, 0]
    K = 34
    logging.info(f'Final Output Result :{result.addToArrayForm(A, K)}')