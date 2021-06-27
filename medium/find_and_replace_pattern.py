"""
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.
"""
import logging
import sys
from typing import List


def getpattern_id(pattern):
    id = 0
    temp_dict = {}
    pattern_id = ''
    for alpha in pattern:
        if alpha not in temp_dict:
            temp_dict[alpha] = id
            id += 1
        pattern_id += str(temp_dict.get(alpha))
    return pattern_id


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        if len(pattern) == 1:
            return [word for word in words if len(word) == 1]
        pattern_id = getpattern_id(pattern)
        return [word for word in words if getpattern_id(word) == pattern_id]


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    format = '%(asctime)s [%(levelname)s]: %(message)s'

    stream = logging.StreamHandler(stream=sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    test_pattern = [(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb", ["mee", "aqq"]),
                    (["a", "b", "c"], "a", ["a", "b", "c"]),
                    (["badc", "abab", "dddd", "dede", "yyxx"], "baba", ["abab", "dede"])]
    for words, pattern, expected_result in test_pattern:
        solution = Solution()
        myresult = solution.findAndReplacePattern(words, pattern)
        assert myresult == expected_result, log.error(f'Expected result: {expected_result}, but received: {myresult}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
