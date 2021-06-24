"""
The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

Each element of nums is in exactly one pair, and
The maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements.
"""
import logging
import sys
from typing import List
from collections import deque


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        nums = deque(nums)
        sum_list = []
        while nums:
            sum_list.append(nums.pop() + nums.popleft())
        return max(sum_list)


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    format = '%(asctime)s [%(levelname)s]: %(meassage)s'

    stream = logging.StreamHandler(stream=sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    test_pattern = [([3, 5, 2, 3], 7),
                    ([3, 5, 4, 2, 4, 6], 8),
                    ([5, 3, 5, 2, 1, 5, 5, 2, 3, 1], 7)]
    for nums, expected_result in test_pattern:
        solution = Solution()
        myresult = solution.minPairSum(nums)
        assert myresult == expected_result, log.error(f'Expected result: {expected_result}, but received: {myresult}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
