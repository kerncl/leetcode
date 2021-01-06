#Question: Easy
'''
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].
'''
from typing import List
from collections import Counter
import logging


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        match = Counter()
        for i,pair in enumerate(dominoes):
            match.update([str(pair)])
            pair.reverse()
            match.update([str(pair)])
        del match['None']
        return max(match.values())


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
    dominoes2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]
    result = Solution()
    logging.info(f'How many equivalent: {result.numEquivDominoPairs(dominoes)}')