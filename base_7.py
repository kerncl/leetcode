#Question: Easy
'''
Given an integer, return its base 7 string representation.
'''
import logging


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            prefix = '-'
            num = -num
        else:
            prefix = ''
        result = ''
        while True:
            remainder = str(num % 7)
            num = num // 7
            result += remainder
            if not num:
                break
        return prefix + result[::-1]


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    num = 100
    num2 = -7
    logging.info(f'Base num of 7 {result.convertToBase7(num2)}')