#Question: Easy
'''
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
'''
import logging


class Solution:
    def tribonacci(self, n: int) -> int:

        first, second, third = 0,1,1
        for _ in range(n):
            first, second, third = second, third, first + second + third
        return first

if __name__ == '__main__':
    format ='%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    n =4
    logging.info(f'Output result {result.tribonacci(4)}')