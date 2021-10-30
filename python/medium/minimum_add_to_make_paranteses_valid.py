"""
Given a string s of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
"""
import logging
import sys


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        while s:
            if '()' in s:
                s = s.replace('()','')
            else:
                return len(s)
        return 0


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)

    format = '%(asctime)s [%(levelname)s]: %(message)s'
    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    log.addHandler(stream)

    test_pattern = [("())", 1),
                    ("(((", 3),
                    ("()", 0),
                    ("()))((", 4)]

    for s, expected in test_pattern:
        solution = Solution()
        myresult = solution.minAddToMakeValid(s)
        assert myresult == expected, log.error(f'Expected result: {expected}, but received: {myresult}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)