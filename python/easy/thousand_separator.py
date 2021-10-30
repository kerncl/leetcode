#Question:Easy
"""
Given an integer n, add a dot (".") as the thousands separator and return it in string format.
"""
import logging


class Solution:
    def thousandSeparator(self, n: int) -> str:
        str_n = str(n)
        str_len = len(str_n)
        if str_len <= 3:
            return str_n
        remainder = 0
        start_with = ''
        if str_len % 3:
            remainder = str_len % 3
            start_with = str_n[:remainder] + '.'
        for index in range(remainder,str_len):
            if not (index-remainder) % 3 and (index-remainder) != 0:
                start_with += '.'
            start_with += str_n[index]
        return start_with


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    n = 987
    n2 = 1234
    n3 = 123456789
    logging.info(f'Output string: {result.thousandSeparator(n3)}')