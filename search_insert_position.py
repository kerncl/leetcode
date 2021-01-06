#Question: Easy
'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
'''
from typing import List
import logging


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        set_num = set(nums)
        if target in set_num:
            return nums.index(target)
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        if target > sum(set_num) // len(set_num):
            for _ in range(len(set_num)//2, len(set_num)):
                if target < nums[_]:
                    return _
        for _ in range(len(set_num)//2+1):
            if target <= nums[_]:
                return _


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    nums = [1, 3, 5, 6]
    target = 5
    nums2 = [1, 3, 5, 6]
    target2 = 2
    nums3 = [1, 3]
    target3 = 2
    result = Solution()
    logging.info(f'Index: {result.searchInsert(nums3, target3)}')