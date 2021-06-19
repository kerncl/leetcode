#Question: Easy
"""
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
"""
from typing import List
import logging


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sort_arr = sorted(set(arr))
        d = dict(zip(sort_arr, range(1,len(sort_arr)+1)))

        return [d[value] for value in arr]

    def __repr__(self):
        return f'{self.__class__.__name__}({arr!r})'


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    arr = [40, 10, 20, 30]
    logging.info(f'Rank array: {result.arrayRankTransform(arr)}')