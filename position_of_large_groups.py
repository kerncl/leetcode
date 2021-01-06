#Question: Easy
'''
In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.
'''
from typing import List
import logging


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        count = 1
        temp = None
        ans = []
        s += ' '
        for index, alpha in enumerate(s):
            if temp != alpha:
                temp = alpha
                if count >= 3:
                    ans.append([index-count, index-1])
                count = 1
            else:
                count += 1

        return ans


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    s = "abbxxxxzzy"
    s2 = 'abbc'
    s3 = "abcdddeeeeaabbbcd"
    s4 = 'aaa'
    result = Solution()
    logging.info(f' Repeating alpha: {result.largeGroupPositions(s4)}')