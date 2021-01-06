# Question: Easy
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''
from typing import List
import logging


class Solution:
    def rob(self, nums: List[int]) -> int:
        money1 = sum(nums[i] for i in range(0, len(nums), 2))
        money2 = sum(nums[i] for i in range(1, len(nums), 2))
        return max(money1, money2)


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    nums = [1, 2, 3, 1]
    nums2 = [2, 1, 1, 2]
    logging.info(f'max amount of money to rob {result.rob(nums2)}')
