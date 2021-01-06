# Question: Easy
'''
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])
'''
from typing import List
import logging


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum_A = sum(A)
        expected = sum_A // 3
        if sum_A % 3:
            return False
        total = 0
        array = 0
        for digit in A:
            total += digit
            if total == expected:
                array += 1
                total = 0
        return True if array >= 3 else False


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    result = Solution()
    A = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
    A2 = [10, -10, 10, -10, 10, -10, 10, -10]
    logging.info(f'Able to partition into 3 array ? {result.canThreePartsEqualSum(A2)}')
