#Question: Easy
'''
Given two binary strings a and b, return their sum as a binary string.
'''
import logging


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A = sum(pow(2, index) for index, digit in enumerate(a[::-1]) if int(digit))
        B = sum(pow(2, index) for index, digit in enumerate(b[::-1]) if int(digit))
        return bin(A+B)[2:]


class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        count = int(a, 2) + int(b, 2)
        return bin(count)[2:]

if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    result2 = Solution2()
    a = "11"
    b = "1"
    a2 = "1010"
    b2 = "1011"
    logging.info(f'sumation of 2 binary result :{result2.addBinary(a2, b2)}')
