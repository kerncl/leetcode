# Question: Easy
"""
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
"""
from typing import List
import logging
import sys


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums


if __name__ == '__main__':
    format = '%(asctime)s : %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    log = logging.getLogger('mylog')
    stream = logging.StreamHandler(stream=sys.stdout)
    log.addHandler(stream)
    mysolution = Solution()

    test_pattern = [([1, 2, 1], [1, 2, 1, 1, 2, 1]),
                    ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1])]
    for test, result in test_pattern:
        myresult = mysolution.getConcatenation(test)
        assert myresult == result, log.info(f'Expected result: {result}, but received {myresult}')

    log.info('DONE')

    while log.handlers:
        handler = log.handlers.pop()
        handler.close()
        log.removeHandler(handler)
