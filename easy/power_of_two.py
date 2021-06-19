#Question: Easy
'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
'''
import logging


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 :
            return True
        if n % 2 or n<1 :
            return False

        binary = bin(n)
        if binary[2:].count('1') > 1:
            return False
        return True


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    n = 16
    logging.info(f'is Power of two: {result.isPowerOfTwo(n)}')