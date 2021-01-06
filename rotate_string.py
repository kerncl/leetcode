#Question: Easy
'''
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.
'''
import logging


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if B in A+A:
            return True
        return False


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    result = Solution()
    A = 'abcde'
    B = 'cdeab'
    A2 = ''
    B2 = ''
    result = Solution()
    logging.info(f'Rotate String ? : {result.rotateString(A2, B2)}')