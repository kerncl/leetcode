# Question: Easy
"""
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
"""

import logging
import sys
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(nums[nums[i]])
        return result


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    log = logging.getLogger('mylog')
    stream = logging.StreamHandler(stream=sys.stdout)
    log.addHandler(stream)

    solution = Solution()
    test_patterns = [([0, 2, 1, 5, 3, 4], [0, 1, 2, 4, 5, 3]),
                     ([5, 0, 1, 2, 3, 4], [4, 5, 0, 1, 2, 3])]
    for test, result in test_patterns:
        log.info(f"Test: {test}, Result: {result}")
        myresult = solution.buildArray(test)
        assert result == myresult, log.info(f'Actually Result: {result}, MyResult: {myresult}')

    log.info('Done')

    while log.handlers:
        handler = log.handlers.pop()
        handler.close()
        log.removeHandler(handler)
