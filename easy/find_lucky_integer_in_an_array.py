#Question: Easy
"""
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
"""
import logging
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        for value in sorted(set(arr), reverse=True):
            if value == arr.count(value):
                return value
        return -1


if __name__ == "__main__":
    format = "%(asctime)s %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    arr = [2, 2, 3, 4]
    result = Solution()
    logging.info(f'The lucky number is {result.findLucky(arr)}')
