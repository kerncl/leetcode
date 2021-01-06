# Question: Easy
'''
Given a binary array, find the maximum number of consecutive 1s in this array
'''
from typing import List
import logging


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = []
        count = 0
        nums.append(0)
        for digit in nums:
            if not digit:
                ones.append(count)
                count = 0
            else:
                count += 1
        return max(ones)


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    nums = [1, 1, 0, 1, 1, 1]
    result = Solution()
    logging.info(f'Max number of 1 {result.findMaxConsecutiveOnes(nums)}')
