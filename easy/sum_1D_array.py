# Question: (easy)
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        sum =0
        for value in nums:
            sum += value
            output.append(sum)
        return output


number = [1, 2, 3, 4]
result = Solution()
print(result.runningSum(number))