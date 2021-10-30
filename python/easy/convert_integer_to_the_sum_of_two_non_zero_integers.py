#Question: Easy
"""
Given an integer n. No-Zero integer is a positive integer which doesn't contain any 0 in its decimal representation.

Return a list of two integers [A, B] where:

A and B are No-Zero integers.
A + B = n
It's guarateed that there is at least one valid solution. If there are many valid solutions you can return any of them.
"""
from typing import List
import logging


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        first = 1
        second = n - first
        if len(str(n)) > 2:
            while '0' in str(second) or '0' in str(first):
                if '0' in str(second):
                    temp = len(str(n)) - list(str(second)).index('0') -1
                    if temp == 1:
                        first += second % 100 + 11
                    elif temp > 0:
                        first += pow(10,temp-1)
                    else:
                        first +=3
                    second = n - first
                elif '0' in str(first):
                    first -=1
                    second +=1
        else:
            while '0' in str(second):
                first +=1
                second -=1

        return [first, second]


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    n = 1010
    n2 = 11
    n3 = 1501
    n4 = 1531
    n5 = 4102
    n6 = 4509
    result = Solution()
    logging.info(f'Non-integer number: {result.getNoZeroIntegers(n5)}')

