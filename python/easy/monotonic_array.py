# Question: Easy
"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.
"""
from typing import List
import logging


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        IsAsending = False
        IsDesending = False
        temp = None
        for index in range(1, len(A)):
            if A[index - 1] == A[index]:
                continue
            if temp == None:
                temp = A[index]
                if temp < A[index - 1]:
                    IsDesending = True
                else:
                    IsAsending = True
                continue
            if IsDesending:
                if A[index - 1] < A[index]:
                    return False
            if IsAsending:
                if A[index - 1] > A[index]:
                    return False
        return True


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    A = [1, 2, 2, 3]
    A2 = [6, 5, 4, 4]
    A3 = [1, 3, 2]
    A4 = [1, 1, 1]
    A5 = [1, 0, 3]
    result = Solution()
    logging.info(f' Is monotone: {result.isMonotonic(A5)}')
