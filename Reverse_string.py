# Question: Easy
'''
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.
'''
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        string = ''.join(s)
        return list(string[::-1])


result = Solution()
S = ["h", "e", "l", "l", "o"]
print(f'Output String: {result.reverseString(S)}')
