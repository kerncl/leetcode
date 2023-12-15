"""
There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have.
"""
import logging
import sys
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        count = len(piles)
        dup = count // 3
        piles.sort()
        higher, lower = piles[dup:], piles[:dup]

        if count == 3:
            return piles[1]

        return sum([higher[2*i] for i in range(dup)])


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    format = '%(asctime)s [%(levelname)s]: %(message)s'

    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter((logging.Formatter(format)))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    test_pattern = [([2,4,1,2,7,8], 9),
                    ([2,4,5], 4),
                    ([9,8,7,6,5,1,2,3,4], 18)]

    for piles, expected in test_pattern:
        solutions = Solution()
        result = solutions.maxCoins(piles)
        assert result == expected, log.error(f'Expected result: {expected}, but received: {result}')


    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)