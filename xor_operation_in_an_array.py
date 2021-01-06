#Question: Easy
"""
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
"""
import logging
import math

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        if n == 1:
            return start
        list_num = [start + 2*_ for _ in range(n)]
        ans = 0
        for value in list_num:
            ans ^= value
        return ans


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    n = 5
    start = 0
    result = Solution()
    logging.info(f'XOR resut: {result.xorOperation(n, start)}')
