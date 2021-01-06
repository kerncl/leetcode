#Question: Easy
'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:
'''
from typing import List
import logging


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        rm = nums.count(val)
        for i in range(rm):
            nums.remove(val)
        return len(nums)


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    nums = [3, 2, 2, 3]
    val = 3
    result = Solution()
    logging.info(f'Final len of array {result.removeElement(nums, val)}')