#Question: Easy
'''
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
'''
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for value in arr:
            if value % 2:
                #odd
                count += 1
                if count == 3:
                    return True
            else:
                #even
                count = 0
        return False


arr = [2,6,4,1]
result = Solution()
print(f'Odd Number repeated three time: {result.threeConsecutiveOdds(arr)}')