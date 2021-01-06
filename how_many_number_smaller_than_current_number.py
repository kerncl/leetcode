#Question: easy
#Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #sortedNumber = sorted(list(set(nums)))
        sortedNumber = sorted(nums)
        repeater_list = []
        for currentvalue in nums:
            repeater = sortedNumber.index(currentvalue)
            repeater_list.append(repeater)
        return repeater_list


nums = [8,1,2,2,3]
result = Solution()
smallertncurrent = result.smallerNumbersThanCurrent(nums)
print('Smaller numbes than current:', smallertncurrent)
