"""
Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
"""
import logging
import sys
from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        t_count = Counter(t)
        s_count = Counter(s)
        tdiff = 0
        for alpha, count in s_count.items():
            temp_count = t_count.get(alpha, 0)
            diff = count - temp_count
            if diff > 0:
                tdiff += diff
        return tdiff


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)

    format = '%(asctime)s [%(levelname)s]: %(message)s'
    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    test_pattern = [("bab", "aba", 1),
                    ("leetcode", "practice", 5),
                    ("anagram", "mangaar", 0),
                    ("xxyyzz", "xxyyzz", 0),
                    ("friend", "family", 4)]

    for s, t, expected in test_pattern:
        solution = Solution()
        myresult = solution.minSteps(s, t)
        assert myresult == expected, log.error(f'Expected result: {expected}, but received: {myresult}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)