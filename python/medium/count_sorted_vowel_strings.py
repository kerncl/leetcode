"""
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.
"""
import logging
import sys
import itertools


class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowel = ('a', 'e', 'i', 'o', 'u')
        if n == 1:
            return 5
        result = []
        # result = [_ for _ in itertools.combinations(vowel, n)]
        for _ in itertools.combinations_with_replacement(vowel, n):
            for i in range(n-1):
                if _[i] > _[i+1]:
                    break
            else:
                result.append(_)
        return len(result)


class Solution2:
    def countVowelStrings(self, n: int) -> int:
        return (n+1)*(n+2)*(n+3)*(n+4)//24


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    format = '%(asctime)s [%(levelname)s]: %(message)s'

    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    test_pattern = [(1, 5),
                    (2, 15),
                    (33, 66045)]

    for n, expected in test_pattern:
        solution = Solution2()
        myresult = solution.countVowelStrings(n)
        assert myresult == expected, log.error(f'Expected result: {expected}, but received: {myresult}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
