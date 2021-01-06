#Question: Easy
"""
You have n candies, the ith candy is of type candies[i].

You want to distribute the candies equally between a sister and a brother so that each of them gets n / 2 candies (n is even). The sister loves to collect different types of candies, so you want to give her the maximum number of different types of candies.

Return the maximum number of different types of candies you can give to the sister.
"""
from typing import List
import logging


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(candies)//2, len(set(candies)))


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    candies = [1, 1, 2, 3]
    logging.info(f'Number of candies distribute : {result.distributeCandies(candies)}')
