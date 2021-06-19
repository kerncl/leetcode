#Question: Easy
"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
"""
import logging


class Solution:
    def addDigits(self, num: int) -> int:
        digit = 0
        while num:
            digit += num%10
            num //= 10
            if not num:
                num = digit
                digit =0
                if not num // 10:
                    return num
        return 0

class Solution2:
    def addDigits(self, num: int) -> int:
        return 1 + (num -1) % 9 if num else 0


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:M:%S')
    logging.getLogger().setLevel(logging.INFO)
    result = Solution()
    num = 38
    logging.info(f'Ans: {result.addDigits(num)}')