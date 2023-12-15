"""
Given a string s, find the length of the longest substring without repeating characters.
"""
import logging
import sys
import numpy as np


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uni = np.unique(list(s))
        len_uni = len(uni)
        len_s = len(s)
        if len_uni == 1:
            return 1

        if len_uni == len_s:
            return len_uni

        for i, size in enumerate(range(len_uni, 0, -1)):
            for j in range(len_s - len_uni + 1 + i):
                current_s = s[j:j+size]
                if size == len(np.unique(list(current_s))):
                    return size


        # eg: len(s) = 8, len(uni) = 3
        # [0:3], 3
        # [1:4], 3
        # [2:5], 3
        # [3:6], 3
        # [4:7], 3
        # [5:8], 3
        # [0:2], 2


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s < 2:
            return len_s

        restart = 0
        start = 0
        found = {}  # record the index
        for i in range(len_s):
            char = s[i]
            if char in found:
                start = max(found[char] + 1, start)
            found[char] = i
            restart = max(restart, i - start)

        return restart + 1


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    format = '%(asctime)s [%(levelname)s]: %(message)s'

    stream = logging.StreamHandler(sys.stdout)
    stream.setLevel(logging.INFO)
    stream.setFormatter(logging.Formatter(format))
    log.addHandler(stream)

    test_pattern = [('abcabcbb', 3),
                    ("bbbbb", 1),
                    ("pwwkew", 3),
                    ("ohvhjdml", 6),
                    ('loddktdji', 5)]

    solution = Solution2()
    for s, expected in test_pattern:
        result = solution.lengthOfLongestSubstring(s)
        assert result == expected, log.error(f'Expected result: {expected}, but received: {result} on {s}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
