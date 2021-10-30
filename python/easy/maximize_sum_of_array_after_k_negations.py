# Question: Easy
'''
Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.
'''
from typing import List
import logging


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        sum_A = sum(A)
        temp = 0
        A.sort()
        for _ in range(K):
            if not _:
                if A[_] > 0:
                    sum_A += pow(-1, K) * (A[_] * 2)  # Positive
                    break
            if A[_] < 0:  # Negative
                value = A[_] * 2
                temp = value
            if A[_] > 0:  # Negative --> Positive
                if abs(temp) <= A[_] * 2:
                    value = -temp
                    temp = -temp
                else:
                    if (K - _) % 2:
                        value = A[_] * 2
                        sum_A -= value
                    break
            if not A[_]:  # Zero
                break
            sum_A -= value
        return sum_A


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    A = [4, 2, 3]
    K = 1
    A2 = [3, -1, 0, 2]
    K2 = 3
    A3 = [-2, 9, 9, 8, 4]
    K3 = 5
    A4 = [5, 6, 9, -3, 3]
    K4 = 2
    A5 = [1, 3, 2, 6, 7, 9]
    K5 = 3
    A6 = [8, -7, -3, -9, 1, 9, -6, -9, 3]
    K6 = 8
    A7 = [-2, 5, 0, 2, -2]
    K7 = 3
    A8 = [-2, 9, 9, 8, 4]
    K8 = 5
    A9 = [1, 3, 2, 6, 7, 9]
    K9 = 3
    A10 = [4, 4, -9, 2, 1, 7, 5, 8]
    K10 = 3
    logging.info(f'Max sum {result.largestSumAfterKNegations(A6, K6)}')
