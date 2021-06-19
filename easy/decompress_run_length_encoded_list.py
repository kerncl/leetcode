#Question: easy
#We are given a list nums of integers representing a list compressed with run-length encoding.
#Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.
#Return the decompressed list.
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        encoded = []
        for i in range((len(nums))//2):
            freq = nums[2*i]
            val = nums[2*i+1]
            encoded.extend([val]*freq)
        return encoded


class Solution2:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        encoded = []
        for i in range(0,len(nums),2):
            pair = nums[i:i+2]
            encoded.extend([pair[1]]*pair[0])
        return encoded


nums = [1, 2, 3, 4]     #[freq val]
result = Solution()
encoded_list = result.decompressRLElist(nums)
print('Result:', encoded_list)
result2 = Solution2()
encoded_list2 = result2.decompressRLElist(nums)
print('Result:', encoded_list2)
