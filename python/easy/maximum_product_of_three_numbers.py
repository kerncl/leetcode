#Question: Easy
'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
'''
import logging
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums.pop() * nums.pop() * nums.pop()
        nums.sort()
        if nums[0]*nums[1] > nums[len(nums)-2]*nums[len(nums)-1] or nums[len(nums)-3] < 0:
            return nums[0]*nums[1]*nums.pop()
        else:
            return nums.pop() * nums.pop() * nums.pop()

class Solution2:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) - 3], nums[0] * nums[1] * nums[2],
                   nums[0] * nums[1] * nums[len(nums) - 1])

if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    nums = [1,2,3]
    nums2 = [-100,-98,-1,2,3,4]
    nums3 = [-8, -7, -2, 10, 20]
    logging.info(f'Max of 3 product: {result.maximumProduct(nums3)}')