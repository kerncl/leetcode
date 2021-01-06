# Question: Easy
'''
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
'''
from typing import List
from string import ascii_lowercase
import logging


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = ascii_lowercase.find(target)
        for alpha in ascii_lowercase[index + 1:]:
            if alpha in letters:
                return alpha
        return letters[0]


class Solution2:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        l = 0
        r = len(letters) - 1
        while (l <= r):
            mid = (l + r) // 2
            if letters[mid] > target:
                ans = letters[mid]
                r = mid - 1
            else:
                l = mid + 1
        return ans


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    letters = ["c", "f", "j"]
    target = "a"
    logging.info(f'the next alpha is :{result.nextGreatestLetter(letters, target)}')
