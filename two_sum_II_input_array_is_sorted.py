# Question: Easy
'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
'''
from typing import List
import logging


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        number_set = sorted(list(set(numbers)))
        for a in number_set:
            for b in number_set:
                if a+b == target:
                    index1 = numbers.index(a)
                    index2 = numbers.index(b)
                    if index1 == index2:
                        index2 +=1
                    return [index1 + 1, index2 + 1]



if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    result = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    numbers2 = [0, 0, 3, 4]
    target2 = 0
    logging.info(f'Number of list sum out with the target number: {result.twoSum(numbers2, target2)}')