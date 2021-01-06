#Question: Easy
'''
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.
'''
import logging
import string
from collections import deque


class Solution:
    def reformat(self, s: str) -> str:
        alphas = deque()
        digits = deque()
        for _ in s:
            if _.isnumeric():
                digits.append(_)
            else:
                alphas.append(_)

        alphas_len = len(alphas)
        digits_len = len(digits)
        ans = ''
        if abs(alphas_len - digits_len) > 1:
            return ''
        if not alphas_len - digits_len:
            return s

        def alp():
            while alphas:
                yield alphas.popleft()

        def number():
            while digits:
                yield digits.popleft()

        if alphas_len > digits_len:
            num = number()
            for alpha in alphas:
                ans += alpha
                try:
                    ans += next(num)
                except:
                    return ans
        else:
            a = alp()
            for digit in digits:
                ans += digit
                try:
                    ans += next(a)
                except:
                    return ans




if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    s = "covid2019"
    s2 = "a0b1c2"
    logging.info(f'reformat string {result.reformat(s2)}')
