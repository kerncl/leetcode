#Question: Easy
'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))
'''
from typing import List
from itertools import accumulate
import logging


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])

class NumArray2:

    def __init__(self, nums: List[int]):
        self.nums =[0] + [num for num in accumulate(nums)]  #join 2 list together

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j+1] - self.nums[i]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    nums = [-2, 0, 3, -5, 2, -1]
    sumRange = [0, 2]
    sumRange2 = [2, 5]
    sumRange3 = [0, 5]
    numArray = NumArray2(nums=nums)
    logging.info(f'{numArray.sumRange(sumRange[0], sumRange[-1])}')
    logging.info(f'{numArray.sumRange(sumRange2[0], sumRange2[-1])}')
    logging.info(f'{numArray.sumRange(sumRange3[0], sumRange3[-1])}')