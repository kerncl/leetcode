#Question: Easy
'''
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.
'''
import logging


class Solution:
    def isHappy(self, n: int) -> bool:
        defult = n
        while True:
            sum = 0
            num_str = str(n)
            for digit in num_str:
                sum += pow(int(digit), 2)
            n = sum
            if n < 5:
                break
        return True if n == 1 else False


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    n = 19
    n2 = 7
    n3 = 1111111
    n4 = 2
    result = Solution()
    logging.info(f'Is it the happy number {result.isHappy(n4)}')