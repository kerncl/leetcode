#Question: easy
#Given an integer n, return any array containing n unique integers such that they add up to 0.
from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        out_list = ['']*n
        if n % 2:
            out_list[n//2] = 0
        for i in range(n//2):
            out_list[i] = -i-1
            out_list[n-1-i] = i+1
        return out_list


n = 5
result = Solution()
out = result.sumZero(n)
print('List of unique integer:', out)