# Question: Easy
"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
"""
from typing import List
import logging


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            diff = stones.pop() - stones.pop()
            if not diff:
                continue
            else:
                stones.append(diff)
        return stones.pop() if len(stones) else 0


if __name__ == "__main__":
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    stones = [2, 7, 4, 1, 8, 1]
    stones2 = [2, 2]
    result = Solution()
    logging.info(f'Last Stone Weight: {result.lastStoneWeight(stonee2)}')
